from django.urls import path
from .import views
from .views import UserLogoutView
urlpatterns = [
    path('',views.home,name='homepage'),
    path('complete/<int:id>/',views.complete_task,name='completepage'),
    path('completed/',views.completed_tasks,name='completedpage'),
    path('incomplete/',views.incomplete_tasks,name='incompletepage'),
    path('edit_task/<int:id>/',views.edit_task,name='editpage'),
    path('delete_task/<int:id>/',views.delete_task,name='deletepage'),
    path('add_task/',views.add_tasks,name='addpage'),
   path('logout/', UserLogoutView.as_view(), name='logout'),
]
