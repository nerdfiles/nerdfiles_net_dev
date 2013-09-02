from app.models import *
from app.serializers import *

from rest_framework import generics
from rest_framework import permissions

from django.contrib.auth.models import User


def render_response(request, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(request)
    return render_to_response(*args, **kwargs)


class UserList(generics.ListCreateAPIView):
    """List all users or create a new User"""
    permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """Retrieve, update or delete a User instance."""
    permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer


class AddressList(generics.ListCreateAPIView):
    """List all addresses or create a new Address"""
    permission_classes = (permissions.IsAuthenticated,)
    model = Address
    serializer_class = AddressSerializer


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete an Address."""
    permission_classes = (permissions.IsAuthenticated,)
    model = Address
    serializer_class = AddressSerializer


def HomeView(request):
    '''
        Landing page view.
    '''
    context = {'CONTEXT': True}
    return render_response(request, 'base.tmpl.haml', context)
