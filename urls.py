from django.urls import path
from app1 import views

urlpatterns = [
    path('list/',views.BookList.as_view()),
    path('create/',views.BookCreate.as_view()),
    path('retrieve/<int:pk>/',views.BookRetrieve.as_view()),
    path('update/<int:pk>/',views.BookUpdate.as_view()),
    path('destroy/<int:pk>/',views.BookDestroy.as_view())
]
