# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class MedicalTestCatagoryDict(models.Model):
    seqid = models.BigIntegerField(primary_key=True)
    test_cata_id = models.BigIntegerField(blank=True, null=True)
    test_cata_name = models.CharField(max_length=255, blank=True, null=True)
    test_cat1_id = models.BigIntegerField(blank=True, null=True)
    test_cat1_name = models.CharField(max_length=255, blank=True, null=True)
    test_cat2_id = models.BigIntegerField(blank=True, null=True)
    test_cat2_name = models.CharField(max_length=255, blank=True, null=True)
    test_cat3_id = models.BigIntegerField(blank=True, null=True)
    test_cat3_name = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_test_catagory_dict'


class MedicalTestIndexAliasDict(models.Model):
    seqid = models.BigIntegerField(primary_key=True)
    test_idx_id = models.BigIntegerField(blank=True, null=True)
    test_idx_name = models.CharField(max_length=500, blank=True, null=True)
    test_idx_alias = models.CharField(max_length=500, blank=True, null=True)
    test_cata_id = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_test_index_alias_dict'


class MedicalTestIndexDict(models.Model):
    seqid = models.BigIntegerField(primary_key=True)
    test_idx_id = models.BigIntegerField(blank=True, null=True)
    test_idx_name = models.CharField(max_length=500, blank=True, null=True)
    test_idx_name_en = models.CharField(max_length=500, blank=True, null=True)
    test_cata_id = models.BigIntegerField(blank=True, null=True)
    relation_test = models.TextField(db_column='Relation_Test', blank=True, null=True)  # Field name made lowercase.
    relation_question = models.TextField(db_column='Relation_Question', blank=True, null=True)  # Field name made lowercase.
    testwhys = models.TextField(db_column='TestWhys', blank=True, null=True)  # Field name made lowercase.
    testwhen = models.TextField(db_column='TestWhen', blank=True, null=True)  # Field name made lowercase.
    suffererprepare = models.TextField(db_column='SuffererPrepare', blank=True, null=True)  # Field name made lowercase.
    swatchgather = models.TextField(db_column='SwatchGather', blank=True, null=True)  # Field name made lowercase.
    testprinciple = models.TextField(db_column='TestPrinciple', blank=True, null=True)  # Field name made lowercase.
    normalvaluedescription = models.TextField(db_column='NormalValueDescription', blank=True, null=True)  # Field name made lowercase.
    diseaserelated = models.TextField(db_column='DiseaseRelated', blank=True, null=True)  # Field name made lowercase.
    summary = models.TextField(db_column='Summary', blank=True, null=True)  # Field name made lowercase.
    testdescription = models.TextField(db_column='TestDescription', blank=True, null=True)  # Field name made lowercase.
    resulteffectreason = models.TextField(db_column='ResultEffectReason', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_test_index_dict'
