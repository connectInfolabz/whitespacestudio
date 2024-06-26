# Generated by Django 5.0.4 on 2024-04-11 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CATEGORY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATNAME', models.CharField(max_length=70)),
                ('CATIMAGE', models.ImageField(null=True, upload_to='catimg')),
            ],
        ),
        migrations.CreateModel(
            name='CONTACT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=60)),
                ('EMAIL', models.EmailField(max_length=254)),
                ('PHONE', models.BigIntegerField()),
                ('MESSAGE', models.TextField()),
                ('TIMESTAMP', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LOGIN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=60)),
                ('EMAIL', models.EmailField(max_length=254)),
                ('PHONE', models.BigIntegerField()),
                ('PASSWORD', models.CharField(max_length=50)),
                ('dp', models.ImageField(null=True, upload_to='upic')),
                ('TIMESTAMP', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PRODUCT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=100)),
                ('MATERIAL_TYPE', models.CharField(max_length=100)),
                ('COLOR', models.CharField(max_length=50)),
                ('PRICE', models.FloatField()),
                ('DESCRIPTION', models.TextField()),
                ('QUANTITY', models.IntegerField()),
                ('IMAGE', models.ImageField(null=True, upload_to='proimg')),
                ('STATUS', models.CharField(choices=[('1', 'Available'), ('0', 'Not Available')], max_length=60)),
                ('CATID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('message', models.TextField()),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='PRODUCTIMAGE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IMAGE', models.ImageField(null=True, upload_to='proimg')),
                ('PRODUCTID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='PRODUCTINQUIRY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QUANTITY', models.IntegerField()),
                ('BUDGET', models.FloatField()),
                ('MESSAGE', models.TextField()),
                ('INQUIRYSTATUS', models.CharField(max_length=100)),
                ('TIMESTAMP', models.DateTimeField(auto_now=True)),
                ('PRODUCTID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.product')),
                ('USERID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.login')),
            ],
        ),
    ]
