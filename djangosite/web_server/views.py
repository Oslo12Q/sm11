#!/usr/bin/python
#-*- coding: UTF-8 -*- 
#coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from sm.data_cleaning.data_clear import *

from django.http import HttpResponse
from django.db import connection
from datetime import date,datetime
from sm.djangosite.web_server.models import *
import os
import json
import random
import MySQLdb

class MyEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj,date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONDecoder.default(self,obj)

def index(request):
    return render(request,'index.html')

def web_data_clear(request):
    
    filedir = 'F:\\sm\\data_cleaning\\testdata'
    #列出文件夹下所有的elsx文件
    list = os.listdir(filedir) 
    #生产随机数
    ran_list = random.randint(0,len(list))
    ran_file = list[ran_list] 
    full_path = filedir +'\\' + ran_file
    rest_data_json = data_clear(full_path)
    data = json.dumps(rest_data_json,ensure_ascii=False)

    return render(request, 'data_clear.html',{'data': data})

def list_mtcd(request):
    
    mtcd_list = []
    medical_test_catagory_dict = MedicalTestCatagoryDict.objects.all()
    for i in medical_test_catagory_dict:
        seqid = i.seqid
        test_cata_id = i.test_cata_id
        test_cata_name = i.test_cata_name
        test_cat1_id = i.test_cat1_id
        test_cat1_name = i.test_cat1_name
        test_cat2_id = i.test_cat2_id
        test_cat2_name = i.test_cat2_name
        test_cat3_id = i.test_cat3_id
        test_cat3_name = i.test_cat3_name
        create_time = i.create_time
        update_time = i.update_time
        mtcd_data = {
            'seqid':seqid,
            'test_cata_id':test_cata_id,
            'test_cata_name':test_cata_name,
            'test_cat1_id':test_cat1_id,
            'test_cat1_name':test_cat1_name,
            'test_cat2_id':test_cat2_id,
            'test_cat2_name':test_cat2_name,
            'test_cat3_id':test_cat3_id,
            'test_cat3_name':test_cat3_name,
            'create_time':create_time,
            'update_time':update_time
        }
        mtcd_list.append(mtcd_data)
    rst_data = {
        "data":mtcd_list
    }
    data = json.dumps(rst_data,cls=MyEncoder,ensure_ascii=False)
    return HttpResponse(data)

def list_mtid(request):
    
    test_cata_id = request.GET.get('test_cata_id',None)
    print test_cata_id
    if test_cata_id:
        mtid_list = []
        medical_test_index_dict = MedicalTestIndexDict.objects.filter(test_cata_id = test_cata_id)
        for i in medical_test_index_dict:
            seqid = i.seqid
            test_idx_id = i.test_idx_id
            test_idx_name = i.test_idx_name
            test_idx_name_en = i.test_idx_name_en
            test_cata_id = i.test_cata_id
            relation_test = i.relation_test
            relation_question = i.relation_question
            testWhys = i.testwhys
            testWhen = i.testwhen
            suffererprepare = i.suffererprepare
            swatchGather = i.swatchgather
            TestPrinciple = i.testprinciple
            normalValueDescription = i.normalvaluedescription
            diseaseRelated = i.diseaserelated
            summary = i.summary
            testDescription = i.testdescription
            resultEffectReason = i.resulteffectreason
            create_time = i.create_time
            update_time = i.update_time
            mtid_data = {
                'seqid':seqid,
                'test_idx_id':test_idx_id,
                'test_idx_name':test_idx_name,
                'test_idx_name_en':test_idx_name_en,
                'test_cata_id':test_cata_id,
                'relation_test':relation_test,
                'relation_question':relation_question,
                'testWhys':testWhys,
                'TestWhen':testWhen,
                'SuffererPrepare':suffererprepare,
                'SwatchGather':swatchGather,
                'TestPrinciple':TestPrinciple,
                'NormalValueDescription':normalValueDescription,
                'DiseaseRelated':diseaseRelated,
                'Summary':summary,
                'TestDescription':testDescription,
                'ResultEffectReason':resultEffectReason,
                'create_time':create_time,
                'update_time':update_time
            }
            mtid_list.append(mtid_data)
        rst_data = {
            "data":mtid_list
        }
        data = json.dumps(rst_data,cls=MyEncoder,ensure_ascii=False)
        return HttpResponse(data)
    else:
        return HttpResponse('test_cata_id is None') 

def list_index_dict(request):
    
    test_idx_id = request.GET.get('test_idx_id',None)
    print test_idx_id
    if test_idx_id:
        mtIa_list = []
        medical_test_index_alias_dicts = MedicalTestIndexAliasDict.objects.filter(test_idx_id = test_idx_id)
        for i in medical_test_index_alias_dicts:
            seqid = i.seqid
            test_idx_id = i.test_idx_id
            test_idx_name = i.test_idx_name
            test_idx_alias = i.test_idx_alias
            test_cata_id = i.test_cata_id
            create_time = i.create_time
            update_time = i.update_time
            mtia_data = {
                'seqid':seqid,
                'test_idx_id':test_idx_id,
                'test_idx_name':test_idx_name,
                'test_idx_alias':test_idx_alias,
                'test_cata_id':test_cata_id,
                'create_time':create_time,
                'update_time':update_time
            }
            mtIa_list.append(mtia_data)
        rst_data = {
            "data":mtIa_list
        }
        data = json.dumps(rst_data,cls=MyEncoder,ensure_ascii=False)
        return HttpResponse(data)
    else:
        return HttpResponse('test_idx_id is None')

def update_dict(request):
    pass

def increase_dict(request):
    pass


    
    