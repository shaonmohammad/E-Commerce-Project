from rest_framework import serializers
from .models import Product,Category,Stock
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','username','email','password','password2')
        extra_kwargs = {'password':{'write_only':True}}
    
    def validate(self, data):
        if data['password'] == ['password2']:
            raise serializers.ValidationError({"password":"Passwords do not match."})
        return data
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
  
class ProductSerializer(serializers.ModelSerializer):
    stock_quantity = serializers.IntegerField(write_only=True)
    class Meta:
        model = Product
        fields = '__all__'
    
    def create(self, validated_data):
        stock_quantity = validated_data.pop('stock_quantity')
        product = Product.objects.create(**validated_data)
        Stock.objects.create(product=product,quantity=stock_quantity)
        return product

    def update(self,instance,validate_data):
        stock_quantity = validate_data.pop('stock_quantity',None)

        for attr,value in validate_data.items():
            setattr(instance,attr,value)
        instance.save()

        if stock_quantity is not None:
            instance.stock.quantity = stock_quantity
            instance.stock.save()
        return instance
        
  
class ProductListSerializer(serializers.ModelSerializer):
    stock_quantity = serializers.SerializerMethodField()
    category_name = serializers.CharField(source='category.name',read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'category_name', 'description', 'price','image','stock_quantity') 
  
    def get_stock_quantity(self,obj):
        return obj.stock.quantity if obj.stock else 0
    

class StockSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name') 
    class Meta:
        model = Stock
        fields = ('id','product_name','quantity')
        