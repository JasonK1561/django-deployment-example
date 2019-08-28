from django.urls import path, include
from basic_app import views


#TEMPLATE TAGGING
app_name = 'basic_app' #This is the appname it is looking for in the html page
urlpatterns = [
    path('other', views.other, name= 'other'), #name=other is what the template tagging is looking for in the html page.
    path('relative_url_templates', views.relative_url_templates, name= 'relative_url_templates'),
]
