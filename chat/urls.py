from django.urls import path
from . import views

app_name = 'chat'
 
urlpatterns = [
    path('', views.chat_view, name='chat_view'),  # 聊天页面
    path('api/chat/', views.chat_api, name='chat_api'),  # 聊天 API 接口
] 