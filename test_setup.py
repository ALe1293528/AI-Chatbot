#!/usr/bin/env python3
"""
项目设置测试脚本
"""

import os
import sys
import django
from pathlib import Path

def test_django_setup():
    """测试 Django 设置"""
    print("🔍 测试 Django 设置...")
    
    # 添加项目路径到 Python 路径
    project_root = Path(__file__).parent
    sys.path.insert(0, str(project_root))
    
    # 设置 Django 环境
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot.settings')
    
    try:
        django.setup()
        print("✅ Django 设置成功")
        return True
    except Exception as e:
        print(f"❌ Django 设置失败: {e}")
        return False

def test_imports():
    """测试关键模块导入"""
    print("🔍 测试模块导入...")
    
    try:
        from chat.views import chat_view, chat_api, call_zhipu_api
        from django.conf import settings
        print("✅ 关键模块导入成功")
        return True
    except Exception as e:
        print(f"❌ 模块导入失败: {e}")
        return False

def test_settings():
    """测试设置配置"""
    print("🔍 测试设置配置...")
    
    try:
        from django.conf import settings
        
        # 检查关键设置
        required_settings = [
            'ZHIPU_API_KEY',
            'ZHIPU_BASE_URL', 
            'DEFAULT_MODEL'
        ]
        
        for setting in required_settings:
            if hasattr(settings, setting):
                value = getattr(settings, setting)
                if setting == 'ZHIPU_API_KEY':
                    # 隐藏 API Key 的完整内容
                    display_value = value[:10] + "..." if len(value) > 10 else value
                else:
                    display_value = value
                print(f"  ✅ {setting}: {display_value}")
            else:
                print(f"  ❌ 缺少设置: {setting}")
                return False
        
        print("✅ 设置配置正确")
        return True
    except Exception as e:
        print(f"❌ 设置配置测试失败: {e}")
        return False

def test_urls():
    """测试 URL 配置"""
    print("🔍 测试 URL 配置...")
    
    try:
        from django.urls import reverse
        from django.test import RequestFactory
        
        # 测试 URL 解析
        factory = RequestFactory()
        
        # 测试聊天页面 URL
        try:
            chat_url = reverse('chat:chat_view')
            print(f"  ✅ 聊天页面 URL: {chat_url}")
        except Exception as e:
            print(f"  ❌ 聊天页面 URL 解析失败: {e}")
            return False
        
        # 测试 API URL
        try:
            api_url = reverse('chat:chat_api')
            print(f"  ✅ API URL: {api_url}")
        except Exception as e:
            print(f"  ❌ API URL 解析失败: {e}")
            return False
        
        print("✅ URL 配置正确")
        return True
    except Exception as e:
        print(f"❌ URL 配置测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("🎀 因幡巡 AI 聊天系统 - 项目设置测试")
    print("=" * 50)
    
    tests = [
        test_django_setup,
        test_imports,
        test_settings,
        test_urls
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！项目设置正确。")
        print("🚀 可以运行 'python run.py' 启动项目")
    else:
        print("⚠️  部分测试失败，请检查项目配置")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 