from django.urls import path
from .import views
urlpatterns = [
    path('<int:roll>/',views.MytemplateView.as_view(),name='homepage'),
    #path('store_new_book/',views.store_book,name='store_book'),
    #path('show_books/',views.show_books,name='show_book'),
    path('show_book/',views.BooklistView.as_view(),name='show_book'),
    path('book_details/<int:id>',views.BookDetailsView.as_view(),name='book_details'),
    path('store_new_book/',views.BookFormView.as_view(),name='store_book'),
    #path('edit_book/<int:id>',views.edit_book,name='edit_book'),
    path('edit_book/<int:pk>',views.BookUpdateView.as_view(),name='edit_book'),
    #path('delete_book/<int:id>',views.delete_book,name='delete_book'),
    path('delete_book/<int:pk>',views.DeleteBookView.as_view(),name='delete_book'),
]
