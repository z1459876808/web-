from rest_framework import viewsets

from .serializer import *
from rest_framework import permissions
from .permissions import Orderpermission, Catepermission
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def getuserinfo(request):
    user = JWTAuthentication().authenticate(request)
    seria = UserSer(instance=user[0])
    return Response(seria.data, status=status.HTTP_200_OK)


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySer
    # 创建更新删除需要管里员权限
    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destory':
            return [permissions.IsAdminUser()]
        else:
            return []


class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSer


class GoodImgViewSets(viewsets.ModelViewSet):
    queryset = GoodImg.objects.all()
    serializer_class = GoodImgsSer


class AdvanImgViewSets(viewsets.ModelViewSet):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSer


class MytoolViewSets(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSer


class ToolimgViewSets(viewsets.ModelViewSet):
    queryset = Toolimg.objects.all()
    serializer_class = ToolImgSer


class userViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSer
        return UserSer


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'retrieve' or self.action == 'destory':
            return [Orderpermission()]
        else:
            return [permissions.IsAdminUser()]


class LabelViewSets(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSer

class PersonalViewSets(viewsets.ModelViewSet):
    queryset = Personaly.objects.all()
    serializer_class = PersonalySer

class SgoodViewSets(viewsets.ModelViewSet):
    queryset = Sgood.objects.all()
    serializer_class = SgoodSer