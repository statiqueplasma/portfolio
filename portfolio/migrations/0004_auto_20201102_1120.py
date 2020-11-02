# Generated by Django 3.1 on 2020-11-02 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20201102_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='principle',
            name='services',
            field=models.ManyToManyField(blank=True, through='portfolio.PrinCat', to='portfolio.Service'),
        ),
        migrations.RemoveField(
            model_name='language',
            name='services',
        ),
        migrations.AddField(
            model_name='language',
            name='services',
            field=models.ManyToManyField(blank=True, through='portfolio.LangCat', to='portfolio.Service'),
        ),
        migrations.CreateModel(
            name='Softwar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('services', models.ManyToManyField(blank=True, through='portfolio.SofCat', to='portfolio.Service')),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='softwars',
            field=models.ManyToManyField(blank=True, through='portfolio.SofCat', to='portfolio.Softwar'),
        ),
        migrations.AlterField(
            model_name='sofcat',
            name='certificats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.softwar'),
        ),
        migrations.DeleteModel(
            name='Softwars',
        ),
    ]
