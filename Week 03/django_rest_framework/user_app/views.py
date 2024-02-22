from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from rest_framework.authtoken.models import Token
from . import signals

# Create your views here.
class RegistrationView(APIView):
    def post(self,request):
        data = {}
        serializer =serializers.RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration Successfull'
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        
        return Response(data)

class LogoutView(APIView):
    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    