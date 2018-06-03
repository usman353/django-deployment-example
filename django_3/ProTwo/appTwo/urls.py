from django.conf.urls import url
from appTwo import views

app_name='apptwo'
urlpatterns = [
    url(r'^$',views.users,name='users'),
    url(r'^form/',views.form_view,name='form'),
    url(r'^relative/$',views.relative,name='relative')
]
