from django.db.models import Max
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class booksapi(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        books_obj=books.objects.all()
        seriallizer=bookseriallizer(books_obj,many=True)
        return Response({'status':200,'payload':seriallizer.data})

    def post(self,request):
        serializer=bookseriallizer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':400,'payload':serializer.data,'message':'Something Went Wrong'})
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':'Saved Successfully'})

    def patch(self,request):
        try:
            obj=books.objects.get(book_name=request.data['book_name'])
            serializer=bookseriallizer(obj,data=request.data,partial=True)
            if not serializer.is_valid():
                return Response({'status':400,'errors':serializer.errors})
            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':'Update Successfully'})
        except Exception as e:
            return Response({'status':401,'message':'Invalid Id'})

    def delete(self,request):
        try:
            obj=books.objects.get(book_name=request.data['book_name'])
            obj.delete()
            return Response({'status':200,'msg':'Delete Successfully'})
        except:
            return Response({'status':400,'message':'invalid name'})

class userapi(APIView):
    
    def get(self,request):
        obj=User.objects.all()
        serializer=userseriallizer(obj,many=True)
        return Response({'status':200,'payload':serializer.data})
    
    def post(self,request):
        serializer=userseriallizer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':400,'payload':serializer.data,'message':'Something Went Wrong'})
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':'Saved Successfully'})

    def patch(self,request):
        try:
            obj=User.objects.get(username=request.data['username'])
            serializer=userseriallizer(obj,data=request.data,partial=True)
            if not serializer.is_valid():
                return Response({'status':400,'errors':serializer.errors})
            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':'Update Successfully'})
        except Exception as e:
            return Response({'status':401,'message':'Invalid name'})

    def delete(self,request):
        try:
            obj=User.objects.get(username=request.data['username'])
            obj.delete()
            return Response({'status':200,'msg':'Delete Successfully'})
        except:
            return Response({'status':400,'message':'invalid name'})


class orderbook(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        obj=order_book.objects.all()
        serializer=orderserializer(obj,many=True)
        return Response({'status':200,'payload':serializer.data})

    def post(self,request):
        serializer=orderserializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':400,'errors':serializer.errors})
        serializer.save()
        return Response({'status':200,'msg':'order placed.'})