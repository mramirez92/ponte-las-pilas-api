from .models import Dicho
# restfw
from rest_framework import generics
from .serializers import DichoSerializer
from .permissions import IsOwnerOrReadOnly


class DichoList(generics.ListCreateAPIView):
    queryset = Dicho.objects.all()
    serializer_class = DichoSerializer
    # permission_classes = (IsOwnerOrReadOnly,)


class DichoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dicho.objects.all()
    serializer_class = DichoSerializer
    permission_classes = (IsOwnerOrReadOnly,)


