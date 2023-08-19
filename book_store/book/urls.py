from django.urls import path
from .import views
urlpatterns = [
    path('<int:roll>/',views.MytemplateView.as_view(),name='homepage'),
    path('store_new_book/',views.store_book,name='store_book'),
    path('show_books/',views.show_books,name='show_book'),
    path('edit_book/<int:id>',views.edit_book,name='edit_book'),
    path('delete_book/<int:id>',views.delete_book,name='delete_book'),
]
