# coding=utf-8
""""QGIS News Feed Entry model definition

.. note:: This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

"""

__author__ = 'elpaso@itopen.it'
__date__ = '2019-05-07'
__copyright__ = 'Copyright 2019, ItOpen'


from django.contrib.gis.db import models
from django.db.models import Q
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from tinymce import models as tinymce_models
from datetime import datetime


class QgisLanguageField(models.CharField):
    """
    A language field for Django models.
    """
    def __init__(self, *args, **kwargs):
        # Local import so the languages aren't loaded unless they are needed.
        from .languages import LANGUAGES
        kwargs.setdefault('max_length', 3)
        kwargs.setdefault('choices', LANGUAGES)
        super().__init__(*args, **kwargs)


class PublishedManager(models.Manager):
    """Returns published entries, considering the publication
    dates and the published flag"""

    def get_queryset(self):
        return super().get_queryset().filter(Q(publication_start__isnull=True) | (Q(publication_start__lte=datetime.now())), Q(publication_end__isnull=True) | (Q(publication_end__gte=datetime.now())) , published=True )


class QgisFeedEntry(models.Model):
    """A feed entry for QGIS welcome page
    """

    title = models.CharField(_('Title'), max_length=255)
    image = models.ImageField(_('Image'), upload_to='feedimages', height_field='image_height', width_field='image_width', max_length=None, blank=True, null=True)
    content = tinymce_models.HTMLField()
    url = models.URLField(_('URL'), max_length=200, blank=True, null=True, help_text=_('URL for more information link'))

    # Auto fields
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, editable=False)
    image_height = models.IntegerField(_('Image height'), blank=True, null=True, editable=False)
    image_width = models.IntegerField(_('Image width'), blank=True, null=True, editable=False)
    created = models.DateField(_('Creation date'), auto_now=False, auto_now_add=True, editable=False)
    modified = models.DateField(_('Modification date'), auto_now=True, editable=False)

    # Options
    published = models.BooleanField(_('Published'), default=False, db_index=True)
    sticky = models.BooleanField(_('Sticky entry'), default=False, help_text=_('Check this option to keep this entry on top'))
    sorting = models.PositiveIntegerField(blank=False,
                                          null=False,
                                          default=0,
                                          verbose_name=_('Sorting order'),
                                          help_text=_('Increase to show at top of the list'),
                                          db_index=True
                                          )

    # Filters
    language_filter = QgisLanguageField(_('Language filter'), blank=True, null=True, help_text=_('The entry will be hidden to users who have not set a matching language filter'), db_index=True)
    spatial_filter = models.PolygonField(_('Spatial filter'), blank=True, null=True, help_text=_('The entry will be hidden to users who have set a location that does not match'))

    # Dates
    publication_start = models.DateField(_('Publication start'), auto_now=False, auto_now_add=False, blank=True, null=True, db_index=True)
    publication_end = models.DateField(_('Publication end'), auto_now=False, auto_now_add=False, blank=True, null=True, db_index=True)

    # Managers
    objects = models.Manager()
    published_entries = PublishedManager()


    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = _('QGIS Feed Entry')
        verbose_name_plural = _('QGIS Feed Entries')
        ordering = ('-sticky', '-sorting', '-created')