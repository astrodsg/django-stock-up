# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfoilo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(help_text='Portfolio Name', max_length=100)),
                ('description', models.CharField(help_text='Describe Portfolio', max_length=200, default=True)),
                ('creation_date', models.DateTimeField(verbose_name='created', default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(verbose_name='updated', default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['stock_up_user_id', 'name', 'creation_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('symbol', models.CharField(help_text='Stock Symbol', max_length=10)),
                ('name', models.CharField(help_text='Stock Name', max_length=100)),
                ('unit_price', models.FloatField()),
                ('nstocks', models.IntegerField()),
                ('creation_date', models.DateTimeField(verbose_name='created', default=django.utils.timezone.now)),
                ('portfolio_id', models.ForeignKey(to='stock_manager.Portfoilo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StockUpUser',
            fields=[
                ('user_ptr', models.OneToOneField(serialize=False, to=settings.AUTH_USER_MODEL, auto_created=True, primary_key=True, parent_link=True)),
                ('display_name', models.CharField(help_text='Display Name', max_length=80)),
                ('cash', models.FloatField(default=10000)),
                ('init_cash', models.FloatField(default=10000)),
            ],
            options={
                'ordering': ['username'],
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='portfoilo',
            name='stock_up_user_id',
            field=models.ForeignKey(to='stock_manager.StockUpUser'),
            preserve_default=True,
        ),
    ]
