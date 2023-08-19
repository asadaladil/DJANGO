from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name="Home Page"),
    path('show_page/',views.showData,name="Show data Page")
]
