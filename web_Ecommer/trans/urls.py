from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    # path('login/',views.SiteLoginView.as_view(), name='Login'),
    path('login/', views.login_user),
    path('register/', views.Register, name='Register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('home/', views.get_home, name="home"),
    path('category/', views.get_category, name='category'),
    path('producer/', views.get_Producer, name='producer'),
    path('brand/', views.get_Brand, name='brand'),
    path('order/', views.get_Order, name='order'),
    path('publisher/', views.get_Publisher, name='publisher'),
    path('author/', views.get_Author, name='author'),
    path('laptop/', views.get_Laptop, name='laptop'),
    path('book/', views.get_Book, name='book'),
    path('shoe/', views.get_Shoe, name='shoe'),
    path("", views.gethomeclient, name="homeclient"),
    path("product/<int:id>", views.getProductDetail),
    path('cart/', views.getListCartItem, name="cart"),
    path('orderAdd/', views.getOrderadd, name="order"),
    path('deletecart/', views.deletecard, name="deletecard"),
    path('listorder/', views.getOrderlist, name="listorder"),
    path('listbook/', views.getListBook, name="listbook"),
    path('listlaptop/', views.getListLaptop, name="listlaptop"),
    path('listshoe/', views.getListShoe, name="listshoe"),
    path('user/', views.get_User, name="user"),
    path('updategiao/<int:id>', views.getupdateDanggiao, name="updategiao"),
    path('updatetc/<int:id>', views.getupdatetc, name="updatetc"),
    path('search/', views.getProductsearch, name="productsearch"),

]
