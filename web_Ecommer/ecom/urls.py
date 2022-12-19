from django.urls import path, include
from . import  views
from rest_framework import routers
router = routers.DefaultRouter()

router.register("user", views.UserIdView,'user')

urlpatterns=[
    path('',include(router.urls)),
    path('category/',views.CategoriesView.as_view()),#danh muc
    path('category/<int:pk>',views.CategoryIdView.as_view()),
    path('producer/',views.ProducerView.as_view()),#nha san xuat
    path('producer/<int:pk>',views.ProducerIdView.as_view()),
    path('laptop/', views.LaptopView.as_view()),#laptop
    path('laptop/<int:pk>', views.LaptopIdView.as_view()),
    path('book/', views.BookView.as_view()),#sach
    path('book/<int:pk>', views.BookIdView.as_view()),
    path('author/', views.AuthorView.as_view()),#tac gia
    path('author/<int:pk>', views.AuthorIdView.as_view()),
    path('brand/', views.BrandView.as_view()),#nhan hieu
    path('brand/<int:pk>', views.BrandIdView.as_view()),
    path('publisher/', views.PublisherView.as_view()),#nha xuat ban
    path('publisher/<int:pk>', views.PublisherIdView.as_view()),
    path('shoe/', views.ShoeView.as_view()),#giay
    path('shoe/<int:pk>', views.ShoeIdView.as_view()),
    path('user/', views.UserView.as_view()),#giay
    path('cart/', views.CartView.as_view()),  # giay
    path('cart/<int:pk>', views.CartIdView.as_view()),
    path('cartitem/', views.CartItemView.as_view()),  # giay
    path('cartitem/<int:pk>', views.CartItemIdView.as_view()),
    path('product/', views.ProductView.as_view()),  # giay
    path('product/<int:pk>', views.ProductIdView.as_view()),
    path('order/', views.OrderView.as_view()),  # giay
    path('order/<int:pk>', views.OrderIdView.as_view()),
    path('orderitem/', views.OrderItemView.as_view()),  # giay
    path('orderitem/<int:pk>', views.OrderItemIdView.as_view()),

]