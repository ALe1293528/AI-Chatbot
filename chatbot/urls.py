"""
URL configuration for chatbot project.
"""
from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),  # 包含聊天应用的 URL
] 