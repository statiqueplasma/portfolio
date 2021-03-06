# Generated by Django 3.1 on 2020-10-31 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='certificats',
            field=models.ManyToManyField(blank=True, through='portfolio.CertCat', to='portfolio.Certificats'),
        ),
        migrations.AlterField(
            model_name='services',
            name='languages',
            field=models.ManyToManyField(blank=True, through='portfolio.LangCat', to='portfolio.Languages'),
        ),
        migrations.AlterField(
            model_name='services',
            name='principles',
            field=models.ManyToManyField(blank=True, through='portfolio.PrinCat', to='portfolio.Principles'),
        ),
        migrations.AlterField(
            model_name='services',
            name='softwars',
            field=models.ManyToManyField(blank=True, through='portfolio.SofCat', to='portfolio.Softwars'),
        ),
    ]
