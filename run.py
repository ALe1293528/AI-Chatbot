#!/usr/bin/env python3
"""
因幡巡 AI 聊天系统启动脚本
"""

import os
import sys
import subprocess

def run_command(command, description):
    """运行命令并显示结果"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} 完成")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} 失败")
        print(f"错误信息: {e.stderr}")
        return False

def main():
    print("🎀 欢迎使用因幡巡 AI 聊天系统！")
    print("=" * 50)
    
    # 检查 Python 版本
    if sys.version_info < (3, 8):
        print("❌ 需要 Python 3.8 或更高版本")
        sys.exit(1)
    
    print(f"✅ Python 版本: {sys.version}")
    
    # 安装依赖
    if not run_command("pip install -r requirements.txt", "安装项目依赖"):
        print("❌ 依赖安装失败，请检查网络连接或手动安装")
        sys.exit(1)
    
    # 运行数据库迁移
    if not run_command("python manage.py migrate", "运行数据库迁移"):
        print("❌ 数据库迁移失败")
        sys.exit(1)
    
    print("\n🎉 项目初始化完成！")
    print("=" * 50)
    print("🚀 启动开发服务器...")
    print("📱 访问地址: http://localhost:8000")
    print("🛑 按 Ctrl+C 停止服务器")
    print("=" * 50)
    
    # 启动开发服务器
    try:
        subprocess.run("python manage.py runserver", shell=True)
    except KeyboardInterrupt:
        print("\n👋 感谢使用因幡巡 AI 聊天系统！")

if __name__ == "__main__":
    main() 