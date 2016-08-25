from django import forms
from django.core.validators import MinLengthValidator

from .models import UploadedFiles, ConfigFiles



class NewUpload(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # TODO: this doesn't seem to work. Need to get to the bottom of it.
        #self.base_fields["display_name"].min_length = 2
        #self.base_fields["display_name"].validators.append(MinLengthValidator)
        #print self.base_fields['display_name'].validators
        super(forms.ModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UploadedFiles
        fields = ('Title', 'STL','Photo', 'Category', 'SubCategory')
 
class ConfigUpload(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # TODO: this doesn't seem to work. Need to get to the bottom of it.
        #self.base_fields["display_name"].min_length = 2
        #self.base_fields["display_name"].validators.append(MinLengthValidator)
        #print self.base_fields['display_name'].validators
        super(forms.ModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ConfigFiles
        fields = ('Printer', 'Plastic', 'HDConfig', 'LDConfig')
 
