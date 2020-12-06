from django.urls import path
from market import views


app_name = 'market'

urlpatterns = [
    # path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name= 'contact'),
    path('about-detail.html', views.aboutDetail, name= 'aboutDetail'),
    path('product-detail.html', views.productDetail, name= 'productDetail'),
    path('product-list1.html', views.productList1, name= 'productList1'),
    path('product-list2.html', views.productList2, name= 'productList2'),

]