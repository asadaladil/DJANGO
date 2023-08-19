from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="Home Page"),
    path('delete/<int:roll>',views.delete_student,name="Delete_Student"),
]
