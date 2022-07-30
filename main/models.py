from typing import Iterable, Optional
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class SocialMedia(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    logo = models.ImageField(upload_to=f'uploads/socialmedia/{name}')

    def __str__(self):
        return self.name
    
class ProjectTag(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    short_title = models.CharField(max_length=50, default="loremp")
    project_link = models.URLField(blank=True)
    description = RichTextUploadingField()
    short_description = models.CharField(default="lorem ipsum dolor sit amet, consectetur adipiscing", max_length=200)
    where_is_projects_on_website = models.CharField(max_length=100)
    
    list_tags = models.ManyToManyField(ProjectTag)
    
    def save(self) -> None:
        print(str(self.description).find("<img"))
        description = str(self.description)
        new_description = description.replace("<img", "<img class='responsive-img'")
        self.description = new_description
        return super().save()

    def __str__(self):
        return self.short_title
    
class CVCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    priority = models.IntegerField()
    
    def __str__(self):
        return self.name


"""class CVLevel(models.Model):
    name = models.CharField(max_length=20, unique=True, default="High School")
    color = models.CharField(max_length=20, default="white")
    
    def __str__(self):
        return self.name"""

class CVItem(models.Model):
    category = models.ForeignKey(CVCategory, to_field="name", default="Uncategorized", on_delete=models.SET_DEFAULT)
    title = RichTextUploadingField()
    start_month = models.IntegerField(default = -1)
    start_year = models.IntegerField(default = -1)
    end_month = models.IntegerField(default = -1)
    end_year = models.IntegerField(default = -1)
    
    def __str__(self):
        return self.title


class CVItemListExpandible(models.Model):
    category = models.ForeignKey(CVCategory, to_field="name", default="Uncategorized", on_delete=models.SET_DEFAULT)
    title = models.CharField(max_length=100)
    expand = models.JSONField(default=None, blank=True, null=True)
    
    def __str__(self):
        return self.title
    

class ContactItem(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=200, blank=True, null=True, default=None)
    sender_email = models.EmailField(blank=True, null=True, default=None)
    subject = models.CharField(max_length=500)
    message = models.TextField()
    contact_time = models.DateTimeField()
    send_status = models.BooleanField(default=0)