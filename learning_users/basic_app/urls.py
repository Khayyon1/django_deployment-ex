from django.conf.urls import url, include
from .views import register, user_login

# TEMPLATE URLS
app_name = 'basic_app'

urlpatterns =[
    url('^register/$', register, name='register'),
    url('^user_login/$', user_login, name='user_login'),
]