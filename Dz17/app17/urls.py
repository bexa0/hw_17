from django.urls import path
from app17.views import *

urlpatterns = [
    path('', task_list_view, name='task_list'),
    path('create/', task_create_view, name='task_create'),
    path('task_update/<int:pk>', task_update_view, name='task_update'),
    path('task_detail/<int:pk>', task_detail_view, name='task_detail'),
    path('task_history/', task_history_view, name='task_history'),
    path('action_history', action_history_view, name='action_history'),
    path('delete/<int:pk>', task_delete_view, name='task_delete'),
    path('completed/<int:pk>', button_completed, name='completed' ),
    path('in_process/<int:pk>', button_completed, name='in_process' ),
    path('task_history/', task_history_view, name='task_history'),
    path('settings/', settings, name='settings')
]
