# Generated by Django 3.1 on 2020-11-02 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20201031_1439'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Principles',
            new_name='Principle',
        ),
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.service')),
            ],
        ),
        migrations.CreateModel(
            name='Certificat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('school', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('services', models.ManyToManyField(blank=True, through='portfolio.CertCat', to='portfolio.Service')),
            ],
        ),
        migrations.AlterField(
            model_name='certcat',
            name='certificats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.certificat'),
        ),
        migrations.AlterField(
            model_name='langcat',
            name='certificats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.language'),
        ),
        migrations.AlterField(
            model_name='service',
            name='certificats',
            field=models.ManyToManyField(blank=True, through='portfolio.CertCat', to='portfolio.Certificat'),
        ),
        migrations.AlterField(
            model_name='service',
            name='languages',
            field=models.ManyToManyField(blank=True, through='portfolio.LangCat', to='portfolio.Language'),
        ),
        migrations.DeleteModel(
            name='Certificats',
        ),
        migrations.DeleteModel(
            name='Languages',
        ),
    ]
