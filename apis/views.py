from rest_framework import generics, permissions, views
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions
from books.models import Book
#from .serializers import BookSerializer, LoginSerializer
from . import serializers #imports all


# Create your views here.
class BookAPIList( generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    name = "book-api-list"

class BookAPIDetail( generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    name = "book-api-detail"

"""
class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)        
        return Response(None, status=status.HTTP_202_ACCEPTED)    
"""