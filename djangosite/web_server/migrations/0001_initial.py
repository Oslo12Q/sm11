# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MedicalTestCatagoryDict',
            fields=[
                ('seqid', models.BigIntegerField(serialize=False, primary_key=True)),
                ('test_cata_id', models.BigIntegerField(null=True, blank=True)),
                ('test_cata_name', models.CharField(max_length=255, null=True, blank=True)),
                ('test_cat1_id', models.BigIntegerField(null=True, blank=True)),
                ('test_cat1_name', models.CharField(max_length=255, null=True, blank=True)),
                ('test_cat2_id', models.BigIntegerField(null=True, blank=True)),
                ('test_cat2_name', models.CharField(max_length=255, null=True, blank=True)),
                ('test_cat3_id', models.BigIntegerField(null=True, blank=True)),
                ('test_cat3_name', models.CharField(max_length=255, null=True, blank=True)),
                ('create_time', models.DateTimeField(null=True, blank=True)),
                ('update_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'medical_test_catagory_dict',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MedicalTestIndexAliasDict',
            fields=[
                ('seqid', models.BigIntegerField(serialize=False, primary_key=True)),
                ('test_idx_id', models.BigIntegerField(null=True, blank=True)),
                ('test_idx_name', models.CharField(max_length=500, null=True, blank=True)),
                ('test_idx_alias', models.CharField(max_length=500, null=True, blank=True)),
                ('test_cata_id', models.BigIntegerField(null=True, blank=True)),
                ('create_time', models.DateTimeField(null=True, blank=True)),
                ('update_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'medical_test_index_alias_dict',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MedicalTestIndexDict',
            fields=[
                ('seqid', models.BigIntegerField(serialize=False, primary_key=True)),
                ('test_idx_id', models.BigIntegerField(null=True, blank=True)),
                ('test_idx_name', models.CharField(max_length=500, null=True, blank=True)),
                ('test_idx_name_en', models.CharField(max_length=500, null=True, blank=True)),
                ('test_cata_id', models.BigIntegerField(null=True, blank=True)),
                ('relation_test', models.TextField(null=True, db_column='Relation_Test', blank=True)),
                ('relation_question', models.TextField(null=True, db_column='Relation_Question', blank=True)),
                ('testwhys', models.TextField(null=True, db_column='TestWhys', blank=True)),
                ('testwhen', models.TextField(null=True, db_column='TestWhen', blank=True)),
                ('suffererprepare', models.TextField(null=True, db_column='SuffererPrepare', blank=True)),
                ('swatchgather', models.TextField(null=True, db_column='SwatchGather', blank=True)),
                ('testprinciple', models.TextField(null=True, db_column='TestPrinciple', blank=True)),
                ('normalvaluedescription', models.TextField(null=True, db_column='NormalValueDescription', blank=True)),
                ('diseaserelated', models.TextField(null=True, db_column='DiseaseRelated', blank=True)),
                ('summary', models.TextField(null=True, db_column='Summary', blank=True)),
                ('testdescription', models.TextField(null=True, db_column='TestDescription', blank=True)),
                ('resulteffectreason', models.TextField(null=True, db_column='ResultEffectReason', blank=True)),
                ('create_time', models.DateTimeField(null=True, blank=True)),
                ('update_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'medical_test_index_dict',
                'managed': False,
            },
        ),
    ]
