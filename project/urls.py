from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from accounts.views import UserRegistrationView
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
urlpatterns = [
    url(r'^logout/$', logout, {'next_page': '/login/'}, name='logout'),
    url(r'^login/$',login,{'template_name':'login.html'},name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^new-user/$', UserRegistrationView.as_view(), name='user_registration'),
]
