# from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from shop.models import Product
from shop.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().select_related('category')
    serializer_class = ProductSerializer


# class ProductListView(ListCreateAPIView):
#     queryset = Product.objects.all().select_related('category')
#     serializer_class = ProductSerializer
    

# class ProductRetrieveAPIView(RetrieveAPIView):
#     queryset = Product.objects.all().select_related('category')
#     serializer_class = ProductSerializer


# class ProductDestroyAPIView(DestroyAPIView):
#     queryset = Product.objects.all().select_related('category')
#     serializer_class = ProductSerializer
