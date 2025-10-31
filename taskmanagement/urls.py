from django.urls import path
from.import views
from django.contrib.auth.views import LoginView

urlpatterns  = [
    # path('hello',views.hello),
    
    path('',views.home_view),
    # path('login',views.login_view,name='login_view'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login_view'),
    path('signin',views.signin_view,name='signin_view'),
    path('accounts/profile/',views.desktop_view,name='desktop_view'),
    path('add',views.addtask_view,name='addtask_view'),
    path('', views.task_list_view, name='task_list'),
    path('update/<int:pk>',views.update_task_view,name='update'),
    path('delete/<int:pk>',views.delete_task_view,name='delete'),
    
]