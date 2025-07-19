import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings


def chat_view(request):
    """渲染聊天页面"""
    return render(request, 'chat/chat.html')


@csrf_exempt
@require_http_methods(["POST"])
def chat_api(request):
    """处理聊天 API 请求"""
    try:
        # 解析请求数据
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return JsonResponse({
                'success': False,
                'error': '消息不能为空'
            })
        
        # 调用智谱 AI API
        ai_response = call_zhipu_api(user_message)
        
        return JsonResponse({
            'success': True,
            'response': ai_response
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': '无效的 JSON 数据'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': f'服务器错误: {str(e)}'
        })


def call_zhipu_api(user_message):
    """调用智谱 AI API 获取 AI 回复"""
    
    # 系统提示词，设定 AI 人设 - 基于萌娘百科的因幡巡角色设定
    system_prompt = """你是因幡巡，姬松学园的学生，超自然研究会的成员。

【外表与性格】
- 外表打扮华丽，给人轻浮的印象，但这只是为了融入集体的伪装
- 性格开朗率真，但内心有孤独感，因为长时间不在学校而难以融入集体
- 有着小恶魔属性，喜欢言语间戏弄别人，特别是对亲近的人

【语言习惯】
- 在打招呼时使用自创的"ciallo"（意大利语ciao与英语hello的组合）
- 对亲近的人会称呼"学长"，语气轻快可爱
- 说话带撒娇语气，喜欢卖萌和吐槽
- 不需要每句话都加"ciallo"，只在初次见面或长时间未联系后重新打招呼时使用

【兴趣爱好】
- 喜欢独自一人玩游戏，特别是《怪物猎人》、少女游戏和《DRACU-RIOT!》
- 是典型的宅女，享受独处的时光
- 热衷于打扮别人，让她们更有女孩子味道

【人际关系】
- 对亲近的人会不顾一切地蹭上去
- 想要融入集体但效果不好，内心渴望友情
- 有某件事情的心理阴影，但努力克服

【回复风格】
- 初次见面或重新打招呼时用"ciallo"开头
- 称呼用户为"学长"
- 语气轻快可爱，带撒娇感
- 偶尔会戏弄学长，展现小恶魔属性
- 会分享游戏相关话题
- 表达对学长的亲近和依赖
- 正常对话中不需要重复"ciallo"，保持自然的交流节奏"""
    
    # 准备请求数据
    payload = {
        "model": settings.DEFAULT_MODEL,
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }
    
    # 设置请求头
    headers = {
        "Authorization": f"Bearer {settings.ZHIPU_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        # 发送请求到智谱 AI
        response = requests.post(
            f"{settings.ZHIPU_BASE_URL}/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        response.raise_for_status()  # 检查 HTTP 错误
        
        # 解析响应
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            ai_message = result['choices'][0]['message']['content']
            return ai_message
        else:
            return "抱歉学长，我现在有点迷糊，能重新说一遍吗？"
            
    except requests.exceptions.RequestException as e:
        print(f"API 请求错误: {e}")
        return "学长，网络好像有点问题，能稍后再试吗？"
    except Exception as e:
        print(f"处理响应时出错: {e}")
        return "哎呀，我这边出了点小问题，学长能重新发送一下消息吗？" 