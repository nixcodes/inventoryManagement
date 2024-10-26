from . import views
from django.urls import path

urlpatterns = [
    path('', views.productsView, name="productsview"),
    path('modify', views.productsModify, name="productsmodify"),
    path('create', views.productsCreate, name="productscreate"),
    path('calculator', views.productsDiscountCalc, name="productsdiscountcalc"),
    path('desc/<productSeq>', views.productDescription, name="productsdesc"),
    path('modify/<productSeq>', views.productsModify, name="productmodify"),
    path('updateSuccess', views.updateSuccess , name="update_product"),
    path('deleteSuccess', views.deleteSuccess , name="delete_product"),
]