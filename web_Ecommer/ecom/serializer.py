from rest_framework import serializers
from .models import Category, Laptop, Book, Shoe, User, Author, Brand, Publisher, Producer,Cart,CartItem,Product,Order,OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ('id', 'name')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'address')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'dob')

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'quantity', 'Cart_id','Product_id')

class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = ('id', 'name', 'description', 'price', 'image', 'quantity', 'Category', 'cpu', 'ram', 'producer','Rating','NumReview')

    def to_representation(self, instance):
        rep = super(LaptopSerializer, self).to_representation(instance)
        rep['Category'] = instance.Category.name
        rep['producer'] = instance.producer.name
        return rep


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields ='__all__'

    def to_representation(self, instance):
        rep = super(BookSerializer, self).to_representation(instance)
        rep['Category'] = instance.Category.name
        rep['author'] = instance.author.name
        rep['publisher'] = instance.publisher.name
        return rep


class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = ('id', 'name', 'description', 'price', 'image', 'quantity', 'Category', 'material', 'Brand', 'size','Rating','NumReview')

    def to_representation(self, instance):
        rep = super(ShoeSerializer, self).to_representation(instance)
        rep['Category'] = instance.Category.name
        rep['Brand'] = instance.Brand.name
        return rep
class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = User
        fields=('id','first_name','last_name','username','password','email','date_joined','is_superuser','avatar')
        extra_kwargs = {
            # 'password':{'write_only': 'true'},
            'email':{'required':'true'}
        }
    def create(self, validated_data):
        user = User.objects.create(

            username=validated_data['username'],
            email= validated_data['email'],
            first_name = validated_data['first_name'],
            last_name= validated_data['last_name'],
            avatar=validated_data['avatar'],
            is_superuser=validated_data['is_superuser']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields= ('id', 'User','total',"name")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields='__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields= ('id','Cart','Product','quantity')
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['Product'] = ProductSerializer(instance.Product).data
        return rep

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields= ('id', 'User','total','status','username','address','phone','content','code','date')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields= ('id','Product','quantity','code')
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['Product'] = ProductSerializer(instance.Product).data
        return rep
