# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookLikeBox',
            fields=[
                ('cmsplugin_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False,
                                      to='cms.CMSPlugin', on_delete=models.CASCADE)),
                ('pageurl',
                 models.URLField(help_text="If blank, the page where it's displayed will be used.", null=True,
                                 verbose_name='URL to like', blank=True)),
                ('width',
                 models.PositiveSmallIntegerField(default=None, help_text='Leave empty for auto scaling.', null=True,
                                                  verbose_name='Width', blank=True)),
                ('height', models.PositiveSmallIntegerField(default=587, verbose_name='Height')),
                ('connections', models.PositiveSmallIntegerField(default=10, verbose_name='Amount of Users')),
                ('transparent', models.BooleanField(default=True, verbose_name='Transparent')),
                ('stream', models.BooleanField(default=True, verbose_name='Show stream')),
                ('header', models.BooleanField(default=True, verbose_name='Show header')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FacebookLikeButton',
            fields=[
                ('cmsplugin_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False,
                                      to='cms.CMSPlugin', on_delete=models.CASCADE)),
                ('pageurl',
                 models.URLField(help_text="If blank, the page where it's displayed will be used.", null=True,
                                 verbose_name='URL to like', blank=True)),
                ('layout', models.CharField(default=b'standard', max_length=50, verbose_name='Layout Style',
                                            choices=[(b'standard', 'standard'), (b'button_count', 'button count')])),
                ('show_faces',
                 models.BooleanField(default=True, help_text='Show profile pictures below the like button.',
                                     verbose_name='Show Faces')),
                ('width',
                 models.PositiveSmallIntegerField(default=None, help_text='Leave empty for auto scaling.', null=True,
                                                  verbose_name='Width', blank=True)),
                ('height', models.PositiveSmallIntegerField(default=80, verbose_name='Height')),
                ('verb', models.CharField(default=b'like', max_length=50, verbose_name='Verb to display',
                                          choices=[(b'like', 'like'), (b'recommend', 'recommend')])),
                ('font', models.CharField(default=b'verdana', max_length=50, verbose_name='Font',
                                          choices=[(b'arial', 'Arial'), (b'lucida+grande', 'lucida grande'),
                                                   (b'segoe+ui', 'segoe ui'), (b'tahoma', 'tahoma'),
                                                   (b'trebuchet+ms', 'trebuchet ms'), (b'verdana', 'verdana')])),
                ('color_scheme', models.CharField(default=b'light', max_length=50, verbose_name='Color Scheme',
                                                  choices=[(b'light', 'light'), (b'dark', 'dark')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
