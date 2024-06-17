import tkinter as tk
from tkinter import scrolledtext
from tkinter.font import Font

from intent_and_actions import extract_intent_and_entities
from intent_and_actions import perform_action

import threading

from XunfeiASRClient import XunfeiASRClient
from XunfeiASRClient import app_id
from XunfeiASRClient import api_key

# 聊天界面类，UI的实现
class ChatApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("语音助手")

        self.background_color = "#f0f0f0"  # 聊天背景颜色

        # 创建一个大字体对象
        self.large_font = Font(family="Helvetica", size=14)

        self.chat_history = scrolledtext.ScrolledText(root, width=60, height=20, bg=self.background_color,font=self.large_font)
        self.chat_history.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # 用户和机器人头像（假设在未来的逻辑中仍然使用）
        # self.user_avatar = tk.PhotoImage(file="user.png")  # 替换为您的用户头像图像
        self.robot_avatar = tk.PhotoImage(file="image/robot.png")  # 替换为您的机器人头像图像

        # 将 'robot' 改为 ''（空字符串）以删除机器人头像上方的标签
        self.robot_name = ''

        # 创建开始录音按钮，并将图像设置为按钮背景
        self.record_button_image = tk.PhotoImage(file="image/record.png")
        self.stop_button_image = tk.PhotoImage(file="image/stop.png")
        self.record_button = tk.Button(root, image=self.record_button_image, command=self.toggle_recording)
        self.record_button.grid(row=2, column=1, pady=20, padx=20, sticky='s')  # 根据需要调整行、列、内边距和粘性属性

        # 模拟聊天会话（可以根据实际使用情况删除或修改）
        self.add_message(self.robot_name, "请问您需要什么帮助？(1.查询日志 2.查询天气 3.上网 4.记笔记 5.播放音乐)")

        # 讯飞语音识别客户端
        self.xunfei_client = None
        self.recording = False  # 记录当前是否正在录音

    def handle_recognized_text(self, text):
        '''
        处理识别到的文本，识别意图并执行相应的操作
        '''
        intent, entities = extract_intent_and_entities(text)
        print(f"Intent: {intent}, Entities: {entities}")
        result = perform_action(intent)
        # 聊天框显示信息
        self.add_message(self.robot_name, result)

    def toggle_recording(self):
        '''
        按钮状态转化
        '''
        if not self.recording:
            # 开始录音
            self.record_voice()
            self.record_button.config(image=self.stop_button_image)
        else:
            # 结束录音
            self.stop_recording()
            self.record_button.config(image=self.record_button_image)

        self.recording = not self.recording

    def record_voice(self):
        '''
        开始录音，创建一个新的连接
        '''
        if self.xunfei_client is None or not self.xunfei_client.ws.connected:
            self.xunfei_client = XunfeiASRClient(app_id=app_id, api_key=api_key, \
                                                 result_callback=self.handle_recognized_text)
        threading.Thread(target=self.xunfei_client.send_audio_stream).start()

    def stop_recording(self):
        '''
        结束录音，关闭连接
        '''
        if self.xunfei_client:
            self.xunfei_client.close()

    def add_message(self, sender, message):
        '''
        往文本框中添加一条信息，用于显示回应
        '''
        self.chat_history.configure(state='normal')

        if sender == "You":
            self.chat_history.image_create(tk.END, image=self.user_avatar)
            self.chat_history.insert(tk.END, " ")
            self.chat_history.insert(tk.END, f"You: {message}\n", 'user')
        elif sender == self.robot_name:
            self.chat_history.image_create(tk.END, image=self.robot_avatar)
            # self.chat_history.insert(tk.END, "Robot: ")
            self.chat_history.insert(tk.END, " : ")
            self.chat_history.insert(tk.END, f"{message}\n", 'robot_message')

        self.chat_history.configure(state='disabled')
        self.chat_history.see(tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApplication(root)

    app.chat_history.tag_config('user', foreground='#007bff')  # 绿色文本
    app.chat_history.tag_config('robot_message', foreground='#28a745')  

    app.run()
