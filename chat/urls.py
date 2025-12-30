from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('send/', views.send_message, name='send'),
    path('<str:username>/', views.conversation, name='conversation'),
]
