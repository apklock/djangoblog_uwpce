from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',
    url(r'^', include('myblog.urls')),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'login.html'},
        name="login"),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/'},
        name="logout"),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
     url('^register/', CreateView.as_view(
            template_name='register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
    #url('^accounts/', include('django.contrib.auth.urls')),
)
