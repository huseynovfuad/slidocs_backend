from rest_framework import generics, permissions
from .serializers import BasketSerializer
from .models import Basket
from .permissions import IsOwnerOrReadOnly



class BasketListView(generics.ListAPIView):
    serializer_class = BasketSerializer

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user).order_by("-id")



class BasketCreateView(generics.CreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)



class BasketDeleteView(generics.DestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    lookup_field = "id"
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)


class BasketDecreaseView(generics.UpdateAPIView):
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()
    lookup_field = "id"
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)