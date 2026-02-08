from django.urls import path
from . import views

urlpatterns = [
    
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:id>/', views.task_detail, name='task_detail'),
    path('tasks/update/<int:id>/', views.update_task, name='update_task'),
    path('', views.home, name='home'),
]
