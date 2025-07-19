// 聊天功能 JavaScript
class ChatApp {
    constructor() {
        this.messageInput = document.getElementById('messageInput');
        this.sendButton = document.getElementById('sendButton');
        this.chatMessages = document.getElementById('chatMessages');
        this.typingIndicator = document.getElementById('typingIndicator');
        
        this.isLoading = false;
        
        this.init();
    }
    
    init() {
        // 绑定事件
        this.messageInput.addEventListener('input', () => this.handleInputChange());
        this.messageInput.addEventListener('keydown', (e) => this.handleKeyDown(e));
        this.sendButton.addEventListener('click', () => this.sendMessage());
        
        // 自动调整输入框高度
        this.messageInput.addEventListener('input', () => this.adjustTextareaHeight());
        
        // 初始状态
        this.updateSendButton();
    }
    
    handleInputChange() {
        this.updateSendButton();
    }
    
    handleKeyDown(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            this.sendMessage();
        }
    }
    
    updateSendButton() {
        const hasText = this.messageInput.value.trim().length > 0;
        this.sendButton.disabled = !hasText || this.isLoading;
    }
    
    adjustTextareaHeight() {
        this.messageInput.style.height = 'auto';
        this.messageInput.style.height = Math.min(this.messageInput.scrollHeight, 120) + 'px';
    }
    
    async sendMessage() {
        const message = this.messageInput.value.trim();
        if (!message || this.isLoading) return;
        
        // 添加用户消息到界面
        this.addMessage(message, 'user');
        
        // 清空输入框
        this.messageInput.value = '';
        this.messageInput.style.height = 'auto';
        
        // 更新按钮状态
        this.updateSendButton();
        
        // 显示加载状态
        this.showTypingIndicator();
        this.isLoading = true;
        
        try {
            // 发送请求到后端
            const response = await axios.post('/api/chat/', {
                message: message
            });
            
            if (response.data.success) {
                // 添加 AI 回复
                this.addMessage(response.data.response, 'ai');
            } else {
                // 显示错误消息
                this.addMessage(`错误: ${response.data.error}`, 'ai');
            }
        } catch (error) {
            console.error('发送消息失败:', error);
            this.addMessage('抱歉学长，网络连接出现了问题，请稍后再试～', 'ai');
        } finally {
            // 隐藏加载状态
            this.hideTypingIndicator();
            this.isLoading = false;
            this.updateSendButton();
        }
    }
    
    addMessage(content, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'flex items-start space-x-3';
        
        if (sender === 'user') {
            // 用户消息 - 右侧显示
            messageDiv.innerHTML = `
                <div class="flex-1"></div>
                <div class="message-bubble rounded-lg p-3 max-w-xs lg:max-w-md">
                    <p class="text-gray-800">${this.escapeHtml(content)}</p>
                </div>
                <div class="w-8 h-8 bg-gradient-to-r from-blue-400 to-blue-600 rounded-full flex items-center justify-center flex-shrink-0">
                    <span class="text-white text-sm font-bold">你</span>
                </div>
            `;
        } else {
            // AI 消息 - 左侧显示
            messageDiv.innerHTML = `
                <img src="/static/头像.jpeg" alt="因幡巡" class="w-8 h-8 rounded-full flex-shrink-0 object-cover">
                <div class="ai-message-bubble rounded-lg p-3 max-w-xs lg:max-w-md">
                    <p class="text-gray-800">${this.escapeHtml(content)}</p>
                </div>
            `;
        }
        
        this.chatMessages.appendChild(messageDiv);
        this.scrollToBottom();
    }
    
    showTypingIndicator() {
        this.typingIndicator.classList.add('show');
        this.scrollToBottom();
    }
    
    hideTypingIndicator() {
        this.typingIndicator.classList.remove('show');
    }
    
    scrollToBottom() {
        setTimeout(() => {
            this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
        }, 100);
    }
    
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// 页面加载完成后初始化应用
document.addEventListener('DOMContentLoaded', () => {
    new ChatApp();
}); 