from shop import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='ShopHome'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='ContactUs'),
    path('tracker/',views.tracker,name='TrackingStatus'),
    path('search/',views.search,name='Search'),
    path('products/<int:product_id>',views.productview,name='productview'),
    path('checkout/',views.checkout,name='Checkout'),
    path('handlerequest/',views.handlerequest,name='HandleRequest'),

]
