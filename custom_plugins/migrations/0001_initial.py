# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmbeddedContentPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('content', embed_video.fields.EmbedVideoField(help_text='Insert the URL of a YouTube video or SoundCloud track/playlist.')),
                ('height', models.CharField(blank=True, help_text="Optionally set a height, e.g. '500px' for 500 pixels.", max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FilePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(blank=True, help_text='Optionally set a title to display instead of the file name.', max_length=100)),
                ('file', filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.CASCADE, to='filer.File')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ImagePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('width', models.IntegerField(blank=True, help_text='Optional width in pixels', null=True)),
                ('height', models.IntegerField(blank=True, help_text='Optional height in pixels', null=True)),
                ('crop', models.CharField(choices=[('off', 'off'), ('on', 'on')], default='off', help_text='Whether the image should be cropped to the exact dimensions set in width and height or just scaled to fit.', max_length=3)),
                ('alt', models.CharField(blank=True, help_text='Specifies an alternate text for an image, if the image cannot be displayed.<br />Is also used by search engines to classify the image.', max_length=255, null=True, verbose_name='alternate text')),
                ('float', models.CharField(blank=True, choices=[('left', 'left'), ('right', 'right'), ('center', 'center')], help_text='Move image left, right or center.', max_length=10, null=True, verbose_name='side')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PlainTextPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('body', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
