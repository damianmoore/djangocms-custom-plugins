from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from easy_thumbnails.files import get_thumbnailer

from .models import EmbeddedContentPluginModel, ImagePluginModel, FilePluginModel, PlainTextPluginModel


class EmbeddedContentPlugin(CMSPluginBase):
    model = EmbeddedContentPluginModel
    name = "Embedded Content"
    render_template = "custom_plugins/embedded_content.html"

plugin_pool.register_plugin(EmbeddedContentPlugin)


class ImagePlugin(CMSPluginBase):
    model = ImagePluginModel
    name = "Image"
    render_template = "custom_plugins/image.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        width = 1000
        height = 1000
        crop = False
        if instance.width:
            width = instance.width
        if instance.height:
            height = instance.height
        if instance.crop == 'on':
            crop = True

        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'dimensions': '{}x{}'.format(width, height),
            'crop': crop,
        })
        return context

    def icon_src(self, instance):
        thumbnailer = get_thumbnailer(instance.image)
        thumbnail_options = {
            'crop': True,
            'size': (50, 50),
        }
        thumbnail = thumbnailer.get_thumbnail(thumbnail_options)
        return thumbnail.url

plugin_pool.register_plugin(ImagePlugin)


class FilePlugin(CMSPluginBase):
    model = FilePluginModel
    name = "File"
    render_template = "custom_plugins/file.html"

    def render(self, context, instance, placeholder):
        num = instance.file.size
        for x in ['bytes','KB','MB','GB','TB']:
            if num < 1024.0:
                file_size = "%3.1f %s" % (num, x)
                break
            num /= 1024.0

        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'file_size': file_size,
        })
        return context

plugin_pool.register_plugin(FilePlugin)


class PlainTextPlugin(CMSPluginBase):
    model = PlainTextPluginModel
    name = "Plain Text"
    render_template = "custom_plugins/plain_text.html"

plugin_pool.register_plugin(PlainTextPlugin)
