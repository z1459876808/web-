"""phonenet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from phoneapp.views import *
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

router = routers.DefaultRouter()
router.register('categorys', CategoryViewSets)
router.register('goods', GoodViewSets)
router.register('goodImgs', GoodImgViewSets)
router.register('sgood', SgoodViewSets)

router.register('advanImgs', AdvanImgViewSets)
router.register('tool', MytoolViewSets)
router.register('toolimg', ToolimgViewSets)
router.register('user', userViewSets)
router.register('order', OrderViewSets)
router.register('label', LabelViewSets)
router.register('personal', PersonalViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # 右上角出现登录功能
    path('', include('rest_framework.urls')),
    url(r'^login1/$', token_obtain_pair, name='login'),
    url(r'^refresh/$', token_refresh, name='refresh'),
    url(r'^getuserinfo/$', getuserinfo),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    path('api/v1/docs/', include_docs_urls(title="RestFulAPI", description="RestFulAPI v1")),

]
