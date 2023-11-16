from rest_framework import generics
from rest_framework import parsers
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from user_app.models import Customer
from user_app.serializers import RegisterSerializer, CustomerSerializer, LoginSerializer


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)


class LoginAPIView(generics.CreateAPIView):
    permission_classes = ()
    throttle_classes = ()
    parser_classes = (parsers.JSONParser,)
    serializer_class = LoginSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=kwargs.get('pk'))
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass

    def options(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass
