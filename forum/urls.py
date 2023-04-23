from django.urls import path
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('create/', create_forum_ajax, name='create_forum'),
    path('delete/<int:id>', delete_forum, name='delete_forum'),
    path('json-post/', get_post_json, name='json-post'),
]