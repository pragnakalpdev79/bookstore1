from django.urls import path
from . import views
app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/',views.booklist,name='books'),
    path('books/<int:pk>',views.book_detail,name='book_detail'),
    path('authors/',views.authorlist,name='authors'),
    path('authors/<int:pk>',views.author_detail,name='author-detail'),

]