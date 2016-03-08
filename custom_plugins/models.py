from cms.models import CMSPlugin
from django.db import models
from embed_video.fields import EmbedVideoField
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField


class EmbeddedContentPluginModel(CMSPlugin):
    content = EmbedVideoField(help_text='Insert the URL of a YouTube video or SoundCloud track/playlist.')
    height = models.CharField(max_length=10, blank=True, help_text='Optionally set a height, e.g. \'500px\' for 500 pixels.')


class ImagePluginModel(CMSPlugin):
    CROP_CHOICES = (
        ('off', 'off'),
        ('on', 'on'),
    )
    FLOAT_CHOICES = (
        ('left', 'left'),
        ('right', 'right'),
        ('center', 'center'),
    )

    image = FilerImageField()
    width = models.IntegerField(blank=True, null=True, help_text='Optional width in pixels')
    height = models.IntegerField(blank=True, null=True, help_text='Optional height in pixels')
    crop = models.CharField(max_length=3, choices=CROP_CHOICES, default='off',
        help_text='Whether the image should be cropped to the exact dimensions set in width and height or just scaled to fit.')
    alt = models.CharField('alternate text', max_length=255, blank=True, null=True,
        help_text='Specifies an alternate text for an image, if the image cannot be displayed.<br />Is also used by search engines to classify the image.')
    float = models.CharField('side', max_length=10, blank=True, null=True, choices=FLOAT_CHOICES,
        help_text='Move image left, right or center.')


class FilePluginModel(CMSPlugin):
    file = FilerFileField()
    title = models.CharField(max_length=100, blank=True, help_text='Optionally set a title to display instead of the file name.')


class PlainTextPluginModel(CMSPlugin):
    body = models.TextField()


class RawHtmlPluginModel(CMSPlugin):
    body = models.TextField()
