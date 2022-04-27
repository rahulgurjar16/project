from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import BookSerializer
from .models import Book

class BookList(GenericAPIView, ListModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get(self, request,*args, **kwargs):
        return self.list(request, *args, **kwargs)

class BookCreate(GenericAPIView, CreateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class BookRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class BookUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class BookDestroy(GenericAPIView, DestroyModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)