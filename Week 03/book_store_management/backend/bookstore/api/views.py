from django.shortcuts import render
from .models import BookStoreModel
from .serializers import BookStoreSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets


# Create your views here.


# ------------API View-----------#
#------------------------------------Start---------------------------------------#
class BookListAPI(APIView):
    def get(self, request, format=None): #GET request
        model = BookStoreModel.objects.all()
        serializer = BookStoreSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request, format=None): #POST request
        serializer = BookStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BookDetailAPI(APIView):
    def get_object(self, pk):
        try:
            return BookStoreModel.objects.get(pk=pk)
        except BookStoreModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None): #GET request for retrive single data
        model = self.get_object(pk)
        serializer = BookStoreSerializer(model)
        return Response(serializer.data)

    def put(self, request, pk, format=None): #UPDATE retuest
        model = self.get_object(pk)
        serializer = BookStoreSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None): #DELETE request
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#-----------------------------------End---------------------------------------#


#--------Generic Class View----------#
#------------------------------------Start--------------------------------------#
class BookListGeneric(generics.ListCreateAPIView): #GET,POST request
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer


class BookDetailGeneric(generics.RetrieveUpdateDestroyAPIView): #DELETE,UPDATE,GET for single data request
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer
#------------------------------------End----------------------------------------#



#--------Model View Set----------#
#------------------------------------Start--------------------------------------#
class BookViewSet(viewsets.ModelViewSet): #All request
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer
#------------------------------------End----------------------------------------#

    
    