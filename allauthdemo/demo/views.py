from django.shortcuts import render


from django.contrib import messages
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.edit import FormView, ContextMixin, FormMixin, UpdateView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

from .forms import NewUpload, ConfigUpload, ContactForm

# Create your views here.
def contact(request):
    form_class = ContactForm
    
    return render(request, 'contact.html', {
        'form': form_class,
    })


class MyModelInstanceMixin(FormMixin):
    def get_model_instance(self):
        return None

    def get_form_kwargs(self):
        kwargs = super(MyModelInstanceMixin, self).get_form_kwargs()
        instance = self.get_model_instance()
        if instance:
            kwargs.update({'instance': instance})
        return instance


class Slic3rUpload(FormView):

    form_class = ConfigUpload
    template_name = "visitor/configupload.html"
    #success_url = '/email-sent/'
    view_name = 'up_config'
    success_url = reverse_lazy(view_name)


    def form_valid(self, form):
        # TODO: not sure how to enforce *minimum* length of a field.
        #print "form valid..."
        #print "save to user:", self.request.user, form.cleaned_data
        form.save()
        messages.add_message(self.request, messages.INFO, 'Slic3r config added')
        return super(Slic3rUpload, self).form_valid(form)


config_upload = Slic3rUpload.as_view()

class DemoUserEditView(FormView):


    form_class = NewUpload
    template_name = "member/member-action.html"
    #success_url = '/email-sent/'
    view_name = 'user_action'
    success_url = reverse_lazy(view_name)

    def post(self, request, *args, **kwargs):
        # Set up the FileUploadHandler
        '''
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        '''
        form = self.form_class(request.POST, request.FILES)
        # Process the POST data by loading the ModelForm
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        # TODO: not sure how to enforce *minimum* length of a field.
        #print "form valid..."
        #print "save to user:", self.request.user, form.cleaned_data
        form.save()
        messages.add_message(self.request, messages.INFO, 'User profile updated')
        return super(DemoUserEditView, self).form_valid(form)


upload_form = login_required(DemoUserEditView.as_view())
