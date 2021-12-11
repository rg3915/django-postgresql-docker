from django.urls import path

from backend.core import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('articles/', v.article_list, name='article_list'),
]
