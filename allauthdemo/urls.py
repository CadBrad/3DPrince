from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

import allauthdemo.views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='visitor/landing-index.html'), name='landing_index'),
    url(r'^about$', TemplateView.as_view(template_name='visitor/landing-about.html'), name='landing_about'),
    url(r'^terms/$', TemplateView.as_view(template_name='visitor/terms.html'), name='website_terms'),
    url(r'^contact$', TemplateView.as_view(template_name='visitor/contact.html'), name='website_contact'),

    
    url(r'^infinity-box$', TemplateView.as_view(template_name='visitor/boxinfo.html'), name='infinity_box'),
    url(r'^compatible-printers$', TemplateView.as_view(template_name='visitor/allprinters.html'), name='printer_config'),

    (r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', 'allauthdemo.auth.views.account_profile', name='account_profile'),
 
    url(r'^member/$', allauthdemo.views.member_index, name='user_home'),
    url(r'^member/action$', 'allauthdemo.demo.views.upload_form', name='user_action'),
    url(r'^member/uploadconfig$', 'allauthdemo.demo.views.config_upload', name='up_config'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)