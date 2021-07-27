# Generated by Django 3.1.13 on 2021-07-27 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='myproject_blog', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(default='Title', max_length=50)),
                ('description', models.CharField(default='Title', max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
