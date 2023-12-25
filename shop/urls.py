# from django.urls import path 
# # from shop.views import ProductListView, ProductRetrieveAPIView, ProductDestroyAPIView
# from shop.views import ProductViewSet


# urlpatterns = [
#     path("products/", ProductViewSet.as_view(), name='list'),
# ]


from rest_framework.routers import DefaultRouter

from shop.views import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')


urlpatterns = router.urls
