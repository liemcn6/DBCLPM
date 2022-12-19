from django.shortcuts import render

from thayque import settings
from .models import Category, Laptop, Book, Shoe, User, Author, Brand, Publisher, Producer,Cart,CartItem,Product,OrderItem,Order
# Create your views here.
from rest_framework import filters
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import status,viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView
from .serializer import CategorySerializer, ProducerSerializer, LaptopSerializer, BrandSerializer, BookSerializer,\
    ShoeSerializer, AuthorSerializer, PublisherSerializer,UserSerializer,CartSerializer,CartItemSerializer,ProductSerializer,OrderSerializer,OrderItemSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CategoriesView(ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.all()

    # tao moi category
    def create(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Category successful'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Category unsuccessful'
        }, status=status.HTTP_400_BAD_REQUEST)


class CategoryIdView(RetrieveUpdateDestroyAPIView):
    model = Category
    serializer_class = CategorySerializer

    def get_queryset(self):
        category_tmp = Category.objects.filter(pk=self.kwargs.get('pk'))
        return category_tmp

    # cap nhat san pham
    def put(self, request, *args, **kwargs):
        category_tmp = get_object_or_404(Category, id=kwargs.get('pk'))
        serializer = CategorySerializer(category_tmp, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Update category successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update category unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    # xoa category
    def delete(self, request, *args, **kwargs):
        category_tmp = get_object_or_404(Category, id=kwargs.get('pk'))
        category_tmp.delete()

        return JsonResponse({
            'message': 'Delete category successful!'
        }, status=status.HTTP_200_OK)


class ProducerView(ListCreateAPIView):
    model = Producer
    serializer_class = ProducerSerializer

    # get danh sach danh muc
    def get_queryset(self):
        return Producer.objects.all()

    # tao moi category
    def create(self, request, *args, **kwargs):
        serializer = ProducerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Producer successful'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Producer unsuccessful'
        }, status=status.HTTP_400_BAD_REQUEST)


class ProducerIdView(RetrieveUpdateDestroyAPIView):
    model = Producer
    serializer_class = ProducerSerializer

    # lay chi tiet danh muc
    def get_queryset(self):
        Producer_tmp = Producer.objects.filter(pk=self.kwargs.get('pk'))
        return Producer_tmp

        # cap nhat san pham

    def put(self, request, *args, **kwargs):
        Producer_tmp = get_object_or_404(Producer, id=kwargs.get('pk'))
        serializer = ProducerSerializer(Producer_tmp, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Producer successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Producer unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

        # xoa category

    def delete(self, request, *args, **kwargs):
        Producer_tmp = get_object_or_404(Producer, id=kwargs.get('pk'))
        Producer_tmp.delete()

        return JsonResponse({
            'message': 'Delete Producer successful!'
        }, status=status.HTTP_200_OK)


class LaptopView(ListCreateAPIView):
    model = Laptop
    serializer_class = LaptopSerializer

    # get danh sach danh muc
    def get_queryset(self):
        return Laptop.objects.all()

        # tao moi category

    def create(self, request, *args, **kwargs):
        serializer = LaptopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Laptop successful'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Laptop unsuccessful'
        }, status=status.HTTP_400_BAD_REQUEST)


class LaptopIdView(RetrieveUpdateDestroyAPIView):
    model = Laptop
    serializer_class = LaptopSerializer

    # lay chi tiet danh muc
    def get_queryset(self):
        Laptop_tmp = Laptop.objects.filter(pk=self.kwargs.get('pk'))
        return Laptop_tmp

        # cap nhat san pham

    def put(self, request, *args, **kwargs):
        Laptop_tmp = get_object_or_404(Laptop, id=kwargs.get('pk'))
        serializer = LaptopSerializer(Laptop_tmp, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Laptop successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Laptop unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

        # xoa category

    def delete(self, request, *args, **kwargs):
        Laptop_tmp = get_object_or_404(Laptop, id=kwargs.get('pk'))
        Laptop_tmp.delete()

        return JsonResponse({
            'message': 'Delete Laptop successful!'
        }, status=status.HTTP_200_OK)


class BookView(ListCreateAPIView):
    model = Book
    serializer_class = BookSerializer

    # get danh sach danh muc
    def get_queryset(self):
        return Book.objects.all()

        # tao moi category

    def create(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Book successful'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Book unsuccessful'
        }, status=status.HTTP_400_BAD_REQUEST)


class BookIdView(RetrieveUpdateDestroyAPIView):
    model = Book
    serializer_class = BookSerializer

    # lay chi tiet danh muc
    def get_queryset(self):
        Book_tmp = Book.objects.filter(pk=self.kwargs.get('pk'))
        return Book_tmp

        # cap nhat san pham

    def put(self, request, *args, **kwargs):
        Book_tmp = get_object_or_404(Book, id=kwargs.get('pk'))
        serializer = BookSerializer(Book_tmp, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Book successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Book unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

        # xoa category

    def delete(self, request, *args, **kwargs):
        Book_tmp = get_object_or_404(Book, id=kwargs.get('pk'))
        Book_tmp.delete()

        return JsonResponse({
            'message': 'Delete Book successful!'
        }, status=status.HTTP_200_OK)


class BrandView(ListCreateAPIView):
    model = Brand
    serializer_class = BrandSerializer

    # get danh sach danh muc
    def get_queryset(self):
        return Brand.objects.all()

        # tao moi category

    def create(self, request, *args, **kwargs):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Brand successful'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Brand unsuccessful'
        }, status=status.HTTP_400_BAD_REQUEST)


class BrandIdView(RetrieveUpdateDestroyAPIView):
    model = Brand
    serializer_class = BrandSerializer

    # lay chi tiet danh muc
    def get_queryset(self):
        Brand_tmp = Brand.objects.filter(pk=self.kwargs.get('pk'))
        return Brand_tmp

        # cap nhat san pham

    def put(self, request, *args, **kwargs):
        Brand_tmp = get_object_or_404(Brand, id=kwargs.get('pk'))
        serializer = BrandSerializer(Brand_tmp, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Brand successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Brand unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

        # xoa category

    def delete(self, request, *args, **kwargs):
        Brand_tmp = get_object_or_404(Brand, id=kwargs.get('pk'))
        Brand_tmp.delete()

        return JsonResponse({
            'message': 'Delete Brand successful!'
        }, status=status.HTTP_200_OK)


class AuthorView(ListCreateAPIView):
    model = Author
    serializer_class = AuthorSerializer

    # get danh sach danh muc
    def get_queryset(self):
        return Author.objects.all()

        # tao moi category

    def create(self, request, *args, **kwargs):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Author successful'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Author unsuccessful'
        }, status=status.HTTP_400_BAD_REQUEST)


class AuthorIdView(RetrieveUpdateDestroyAPIView):
    model = Author
    serializer_class = AuthorSerializer

    # lay chi tiet danh muc
    def get_queryset(self):
        Author_tmp = Author.objects.filter(pk=self.kwargs.get('pk'))
        return Author_tmp

        # cap nhat san pham

    def put(self, request, *args, **kwargs):
        Author_tmp = get_object_or_404(Author, id=kwargs.get('pk'))
        serializer = AuthorSerializer(Author_tmp, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Author successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Author unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

        # xoa category

    def delete(self, request, *args, **kwargs):
        Author_tmp = get_object_or_404(Author, id=kwargs.get('pk'))
        Author_tmp.delete()

        return JsonResponse({
            'message': 'Delete Author successful!'
        }, status=status.HTTP_200_OK)


class PublisherView(ListCreateAPIView):
    model = Publisher
    serializer_class = PublisherSerializer

    # get danh sach danh muc
    def get_queryset(self):
        return Publisher.objects.all()

        # tao moi category

    def create(self, request, *args, **kwargs):
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Publisher successful'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Publisher unsuccessful'
        }, status=status.HTTP_400_BAD_REQUEST)


class PublisherIdView(RetrieveUpdateDestroyAPIView):
    model = Publisher
    serializer_class = PublisherSerializer

    # lay chi tiet danh muc
    def get_queryset(self):
        Publisher_tmp = Publisher.objects.filter(pk=self.kwargs.get('pk'))
        return Publisher_tmp

        # cap nhat san pham

    def put(self, request, *args, **kwargs):
        Publisher_tmp = get_object_or_404(Publisher, id=kwargs.get('pk'))
        serializer = PublisherSerializer(Publisher_tmp, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Publisher successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Publisher unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

        # xoa category

    def delete(self, request, *args, **kwargs):
        Publisher_tmp = get_object_or_404(Publisher, id=kwargs.get('pk'))
        Publisher_tmp.delete()

        return JsonResponse({
            'message': 'Delete Publisher successful!'
        }, status=status.HTTP_200_OK)


class ShoeView(ListCreateAPIView):
    model = Shoe
    serializer_class = ShoeSerializer

    # get danh sach danh muc
    def get_queryset(self):
        return Shoe.objects.all()

        # tao moi category

    def create(self, request, *args, **kwargs):
        serializer = ShoeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Shoe successful'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Shoe unsuccessful'
        }, status=status.HTTP_400_BAD_REQUEST)


class ShoeIdView(RetrieveUpdateDestroyAPIView):
    model = Shoe
    serializer_class = ShoeSerializer

    # lay chi tiet danh muc
    def get_queryset(self):
        Shoe_tmp = Shoe.objects.filter(pk=self.kwargs.get('pk'))
        return Shoe_tmp

        # cap nhat san pham

    def put(self, request, *args, **kwargs):
        Shoe_tmp = get_object_or_404(Shoe, id=kwargs.get('pk'))
        serializer = ShoeSerializer(Shoe_tmp, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Shoe successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Shoe unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

        # xoa category

    def delete(self, request, *args, **kwargs):
        Shoe_tmp = get_object_or_404(Shoe, id=kwargs.get('pk'))
        Shoe_tmp.delete()

        return JsonResponse({
            'message': 'Delete Shoe successful!'
        }, status=status.HTTP_200_OK)

class UserView(ListCreateAPIView):
    model = User
    serializer_class = UserSerializer


    # get danh sach danh muc
    def get_queryset(self):
        user = User.objects.filter(is_active=True)
        q=self.request.query_params.get('q')
        if q is not None:
            user = user.filter(username = q)
        return user

    # tao moi category
    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new User successful'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({

        }, status=status.HTTP_400_BAD_REQUEST)

class get_User_register(APIView):
    User= User.objects.filter()

class UserIdView(viewsets.ViewSet):

    serializer_class = UserSerializer

    # def get_permissions(self):
    #     # if self.action == 'get_current_user':
    #     #     return [permissions.IsAuthenticated()]
    #     return None
    #     # return [permissions.AllowAny()]

    @action(methods=['get'],detail= False , url_path='current')
    def get_current_user(self, request):
        return JsonResponse(self.serializer_class(request.user).data, status=status.HTTP_200_OK)


class CartView(ListCreateAPIView):
    model = Cart
    serializer_class = CartSerializer
    def get_queryset(self):
        cart = Cart.objects.filter()
        q = self.request.query_params.get('q')
        if q is not None:
            cart = cart.filter(name=q)
        return cart

    # tao moi category
    def create(self, request, *args, **kwargs):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new cart successful'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new cart unsuccessful'
        }, status=status.HTTP_400_BAD_REQUEST)


class CartIdView(RetrieveUpdateDestroyAPIView):
    model = Cart
    serializer_class = CartSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # lay chi tiet danh muc
    def get_queryset(self):
        cart_tmp = Cart.objects.filter(pk=self.kwargs.get('pk'))
        return cart_tmp

    # cap nhat san pham
    def put(self, request, *args, **kwargs):
        cart_tmp = get_object_or_404(Cart, id=kwargs.get('pk'))
        serializer = CartSerializer(cart_tmp, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Update cart successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update cart unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    # xoa category
    def delete(self, request, *args, **kwargs):
        cart_tmp = get_object_or_404(Cart, id=kwargs.get('pk'))
        cart_tmp.delete()

        return JsonResponse({
            'message': 'Delete cart successful!'
        }, status=status.HTTP_200_OK)

class CartItemView(ListCreateAPIView):
    model = CartItem
    serializer_class = CartItemSerializer
    def get_queryset(self):
        cartitem = CartItem.objects.filter()
        q = self.request.query_params.get('q')
        if q is not None:
            cartitem = cartitem.filter(Cart=q)
        return cartitem

    # tao moi category
    def create(self, request, *args, **kwargs):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new cart successful'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new cart unsuccessful'
        }, status=status.HTTP_400_BAD_REQUEST)

class CartItemIdView(RetrieveUpdateDestroyAPIView):
    model = CartItem
    serializer_class = CartItemSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # lay chi tiet danh muc
    def get_queryset(self):
        CartItem_tmp = CartItem.objects.filter(pk=self.kwargs.get('pk'))
        return CartItem_tmp

    # cap nhat san pham
    def put(self, request, *args, **kwargs):
        CartItem_tmp = get_object_or_404(CartItem, id=kwargs.get('pk'))
        serializer = CartItemSerializer(CartItem_tmp, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Update CartItem successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update CartItem unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    # xoa category
    def delete(self, request, *args, **kwargs):
        CartItem_tmp = get_object_or_404(CartItem, id=kwargs.get('pk'))
        CartItem_tmp.delete()

        return JsonResponse({
            'message': 'Delete CartItem successful!'
        }, status=status.HTTP_200_OK)

class ProductView(ListCreateAPIView):
    model = Product
    serializer_class = ProductSerializer
    def get_queryset(self):
        product = Product.objects.filter()
        q = self.request.query_params.get('q')
        if q is not None:
           product = product.filter(name__contains=q)
        return product

    # tao moi category
    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Product successful'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Product unsuccessful'
        }, status=status.HTTP_400_BAD_REQUEST)


class ProductIdView(RetrieveUpdateDestroyAPIView):
    model = Product
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # lay chi tiet danh muc
    def get_queryset(self):
        Product_tmp = Product.objects.filter(pk=self.kwargs.get('pk'))
        return Product_tmp

    # cap nhat san pham
    def put(self, request, *args, **kwargs):
        Product_tmp = get_object_or_404(Cart, id=kwargs.get('pk'))
        serializer = ProductSerializer(Product_tmp, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Update Product successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Product unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    # xoa category
    def delete(self, request, *args, **kwargs):
        Product_tmp = get_object_or_404(Product, id=kwargs.get('pk'))
        Product_tmp.delete()

        return JsonResponse({
            'message': 'Delete Product successful!'
        }, status=status.HTTP_200_OK)

class OrderView(ListCreateAPIView):
    model = Order
    serializer_class = OrderSerializer
    def get_queryset(self):
        order = Order.objects.filter()
        q = self.request.query_params.get('q')
        if q is not None:
            order = order.filter(User=q)
        return order

    # tao moi category
    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new Order successful'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Order unsuccessful'
        }, status=status.HTTP_400_BAD_REQUEST)


class OrderIdView(RetrieveUpdateDestroyAPIView):
    model = Order
    serializer_class = OrderSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # lay chi tiet danh muc
    def get_queryset(self):
        order_tmp = Order.objects.filter(pk=self.kwargs.get('pk'))
        return order_tmp

    # cap nhat san pham
    def put(self, request, *args, **kwargs):
        order_tmp = get_object_or_404(Order, id=kwargs.get('pk'))
        serializer = OrderSerializer(order_tmp, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Update Order successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Order unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    # xoa category
    def delete(self, request, *args, **kwargs):
        order_tmp = get_object_or_404(Order, id=kwargs.get('pk'))
        order_tmp.delete()

        return JsonResponse({
            'message': 'Delete Order successful!'
        }, status=status.HTTP_200_OK)


class OrderItemView(ListCreateAPIView):
    model = OrderItem
    serializer_class = OrderItemSerializer
    def get_queryset(self):
        orderItem = OrderItem.objects.filter()
        q = self.request.query_params.get('q')
        if q is not None:
            orderItem = orderItem.filter(code=q)
        return orderItem

    # tao moi category
    def create(self, request, *args, **kwargs):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new OrderItem successful'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new OrderItem unsuccessful'
        }, status=status.HTTP_400_BAD_REQUEST)


class OrderItemIdView(RetrieveUpdateDestroyAPIView):
    model = OrderItem
    serializer_class = OrderItemSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # lay chi tiet danh muc
    def get_queryset(self):
        orderItem_tmp = OrderItem.objects.filter(pk=self.kwargs.get('pk'))
        return orderItem_tmp

    # cap nhat san pham
    def put(self, request, *args, **kwargs):
        orderItem_tmp = get_object_or_404(OrderItem, id=kwargs.get('pk'))
        serializer = OrderItemSerializer(orderItem_tmp, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Update OrderItem successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update OrderItem unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    # xoa category
    def delete(self, request, *args, **kwargs):
        orderItem_tmp = get_object_or_404(OrderItem, id=kwargs.get('pk'))
        orderItem_tmp.delete()

        return JsonResponse({
            'message': 'Delete OrderItem successful!'
        }, status=status.HTTP_200_OK)


