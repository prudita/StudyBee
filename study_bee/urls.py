from django.urls import path
from study_bee.views import show_tracker
from study_bee.views import create_transaction
from study_bee.views import register #sesuaikan dengan nama fungsi yang dibuat
from study_bee.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from study_bee.views import logout_user #sesuaikan dengan nama fungsi yang dibuat



app_name = 'study_bee'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('create', create_transaction, name='create_transaction'),
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat

]
