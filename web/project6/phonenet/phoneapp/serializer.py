from rest_framework import serializers
from .models import *


class GoodImgsSer(serializers.Serializer):
    img = serializers.ImageField()
    good = serializers.CharField(source='good.name')
    id = serializers.IntegerField(read_only=True)

    def validate_good(self, good):
        try:
            Good.objects.get(name=good)
        except:
            raise serializers.ValidationError('商品名不存在')
        return good

    def validate(self, attrs):
        g = Good.objects.get(name=attrs['good']['name'])
        attrs['good'] = g
        return attrs

    def create(self, validated_data):
        print(validated_data, '888888888')
        instance = GoodImg.objects.create(**validated_data)
        return instance


class ToolImgSer(serializers.Serializer):
    name = serializers.CharField()
    img = serializers.ImageField()
    tool = serializers.CharField(source='tool.title')

    def validate_tool(self, tool):
        try:
            Tool.objects.get(title=tool)
        except:
            raise serializers.ValidationError('标题名不存在')
        return tool

    def validate(self, attrs):
        t = Tool.objects.get(title=attrs['tool']['title'])
        attrs['tool'] = t
        return attrs

    def create(self, validated_data):
        instance = Toolimg.objects.create(**validated_data)
        return instance


class SgoodSer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField(max_length=15, min_length=2, error_messages={
        'min_length': '最少2',
        'max_length': '最多15'
    })

    good = serializers.CharField(max_length=10)
    img = serializers.ImageField()
    desc = serializers.CharField()
    price = serializers.IntegerField()
    view = serializers.IntegerField()

    def validate_good(self, good):
        try:
            Good.objects.get(name=good)
        except:
            raise serializers.ValidationError('分类名不存在')
        return good

    def validate(self, attrs):
        c = Good.objects.get(name=attrs['good'])
        attrs['good'] = c
        return attrs

    def create(self, validated_data):
        instance = Sgood.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.category = validated_data.get('good', instance.category)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class GoodSeRelCate(serializers.Serializer):
    name = serializers.CharField(max_length=15, min_length=2, error_messages={
        'min_length': '最少2',
        'max_length': '最多15'
    })
    id = serializers.IntegerField(read_only=True)
    category = serializers.CharField(max_length=10)
    imgs = GoodImgsSer(label='图片', many=True, read_only=True)
    sgoods = SgoodSer(label='图片', many=True, read_only=True)


class CategorySer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    id = serializers.IntegerField(read_only=True)
    goods = GoodSeRelCate(label='图片', many=True, read_only=True)

    def create(self, validated_data):
        instance = Category.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance


class AdvantageSer(serializers.Serializer):
    img = serializers.ImageField()

    def create(self, validated_data):
        instance = Advantage.objects.create(**validated_data)
        return instance


class ToolSer(serializers.Serializer):
    title = serializers.CharField()
    toolimg = ToolImgSer(label='标题', many=True, read_only=True)

    def create(self, validated_data):
        instance = Tool.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.save()
        return instance


class GoodSer(serializers.Serializer):
    # 返回数据字段
    name = serializers.CharField(max_length=15, min_length=2, error_messages={
        'min_length': '最少2',
        'max_length': '最多15'
    })

    category = serializers.CharField(max_length=10)
    imgs = GoodImgsSer(label='图片', many=True, read_only=True)
    sgoods = SgoodSer(label='图片', many=True, read_only=True)

    def validate_category(self, category):
        try:
            Category.objects.get(name=category)
        except:
            raise serializers.ValidationError('分类名不存在')
        return category

    def validate(self, attrs):
        c = Category.objects.get(name=attrs['category'])
        attrs['category'] = c
        return attrs

    def create(self, validated_data):
        instance = Good.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class UserRegisterSer(serializers.Serializer):
    username = serializers.CharField(max_length=10, error_messages={
        'required': '用户名必填'
    })
    password = serializers.CharField(max_length=10, write_only=True)
    password2 = serializers.CharField(max_length=10, write_only=True)

    def validated_password2(self, data):
        if data != self.initial_data['password']:
            raise serializers.ValidationError('密码输入不一致')
        else:
            return data

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data.get('username'), email=validated_data.get('email'),
                                        password=validated_data.get('password'))


class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'user_permissions', 'groups']

    # 如果修改了密码对密码进行哈希加密
    def validate(self, attrs):
        from django.contrib.auth import hashers
        if attrs.get('password'):
            attrs['password'] = hashers.make_password(attrs['password'])
        return attrs


class OrderSer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class LabelSer(serializers.Serializer):
    name = serializers.CharField(max_length=5)

    def create(self, validated_data):
        instance = Label.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance


class PersonalySer(serializers.Serializer):
    name = serializers.CharField()
    num = serializers.IntegerField()

    def create(self, validated_data):
        instance = Personaly.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance
