from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('scrape', views.perform_scrapping ,name='perform_scrapping')
]
