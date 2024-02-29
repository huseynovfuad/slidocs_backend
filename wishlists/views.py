from rest_framework import generics
from .serializers import WishlistSerializer
from .models import Wishlist
from rest_framework.response import Response
from rest_framework import status


class WishlistListView(generics.ListAPIView):
    serializer_class = WishlistSerializer

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user).order_by("-id")



class WishlistCreateView(generics.CreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)



class WishlistDeleteView(generics.DestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)