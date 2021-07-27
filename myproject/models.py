from cms.models.pluginmodel import CMSPlugin

from django.db import models

class Blog(CMSPlugin):
    title = models.CharField(max_length=50, default="Title")
    description = models.CharField(max_length=50, default="Description")