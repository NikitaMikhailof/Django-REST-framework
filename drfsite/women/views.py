from rest_framework import generics, viewsets
from .models import Women
from .serializers import WomenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication



class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer  
    permission_classes = (IsAdminOrReadOnly, ) 


