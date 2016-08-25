import os
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings


from django.contrib.auth.models import User
from allauthdemo.auth.models import DemoUser
from allauthdemo.auth.models import UserProfile


# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    
    return os.path.join('uploads', str(instance.id), filename)
    '''
    return 'user_{0}/{1}'.format(instance.user.id, Title)
    '''


def UploadedConfigPath(instance, filename):

    return os.path.join('uploadedconfigs', str(instance.id), filename)
    '''
    return 'user_{0}/{1}'.format(instance.user.id, Title)
    '''

    
class ConfigFiles(models.Model):

    
    HDConfig = models.FileField(_('High Detail'), 
    upload_to=UploadedConfigPath)
    LDConfig = models.FileField(_('Low Detail'), 
    upload_to=UploadedConfigPath)
    Printer = models.CharField(_('Printer Model'),
    max_length=100, blank=True, null=True, unique=False)
    Plastic = models.CharField(_('Plastic'),    
    max_length=40, blank=True, null=True, unique=False)
    creator = models.CharField(_('Creator'),
    max_length=40, blank=True, null=True, unique=False)

    pub_date = models.DateTimeField(_('date_joined'), 
    default=timezone.now)




class UploadedFiles(models.Model):

    STL = models.FileField(_('STL Upload'), 
        upload_to=user_directory_path)
    Photo = models.ImageField(_('Photo'),
     upload_to=user_directory_path)

    Title = models.CharField(_('Title of object'),
     max_length=40, blank=True, null=True, unique=False)
    Category = models.CharField(_('Category'),
     max_length=40, blank=True, null=True, unique=False)
    SubCategory = models.CharField(_('SubCategory'),
     max_length=40, blank=True, null=True, unique=False)
    SubSubCategory = models.CharField(_('SubSubCategory_field'),
     max_length=40, blank=True, null=True, unique=False)
    
    FileType = models.BooleanField(_('Global_or_Local'),
    default=0, unique=False)
    LicenseType = models.BooleanField(_('Previous License?'),
    default=0, unique=False)
    LicenseTag = models.CharField(_('License'),
     max_length=200, blank=True, null=True, unique=False)
 

    pub_date = models.DateTimeField(_('date_joined'), default=timezone.now)

