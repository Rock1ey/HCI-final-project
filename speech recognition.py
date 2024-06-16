import tkinter as tk
from tkinter import scrolledtext
import subprocess
import webbrowser 

from intent_recognition import extract_intent_and_entities
from intent_recognition import get_random_weather_and_tips
from intent_recognition import get_random_schedule

import threading
import speech_recognition as sr

# 创建识别器对象
recognizer = sr.Recognizer()

class ChatApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("语音助手")

        # Configure background color for chat history
        self.background_color = "#f0f0f0"  # Light gray background color

        self.chat_history = scrolledtext.ScrolledText(root, width=60, height=20, bg=self.background_color)
        self.chat_history.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # 用户和机器人头像（假设在未来的逻辑中仍然使用）
        # self.user_avatar = tk.PhotoImage(file="user.png")  # 替换为您的用户头像图像
        self.robot_avatar = tk.PhotoImage(file="robot.png")  # 替换为您的机器人头像图像

        # 将 'robot' 改为 ''（空字符串）以删除机器人头像上方的标签
        self.robot_name = ''

        # 创建录音按钮
        self.record_button = tk.Button(root, text="录音", command=self.record_voice)
        self.record_button.grid(row=2, column=1, pady=20, padx=20, sticky='s')  # 根据需要调整行、列、内边距和粘性属性

        # 模拟聊天会话（可以根据实际使用情况删除或修改）
        self.add_message(self.robot_name, "请问您需要什么帮助？")

    def handle_recognized_text(self, text):
        intent, entities = extract_intent_and_entities(text)
        print(f"Intent: {intent}, Entities: {entities}")
        result = self.perform_action(intent)
        self.add_message(self.robot_name, result)

    def listen_in_background(self):
        with sr.Microphone() as source:
            print("请说话...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio_data = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                text = recognizer.recognize_sphinx(audio_data, language='zh-CN')
                print("你说的是: " + text)
                self.handle_recognized_text(text)
            except sr.UnknownValueError:
                print("无法识别音频")
            except sr.RequestError as e:
                print("无法请求结果；{0}".format(e))
            except sr.WaitTimeoutError:
                print("等待超时，没有检测到语音输入")

    def record_voice(self):
        # 录音功能的占位函数；替换为实际逻辑
        #在这里添加开始语音识别逻辑
        threading.Thread(target=self.listen_in_background).start()

    def add_message(self, sender, message):
        self.chat_history.configure(state='normal')

        if sender == "You":
            self.chat_history.image_create(tk.END, image=self.user_avatar)
            self.chat_history.insert(tk.END, " ")
            self.chat_history.insert(tk.END, f"You: {message}\n", 'user')
        elif sender == self.robot_name:
            self.chat_history.image_create(tk.END, image=self.robot_avatar)
            self.chat_history.insert(tk.END, "Robot: ")
            self.chat_history.insert(tk.END, f"{message}\n", 'robot_message')

        self.chat_history.configure(state='disabled')
        self.chat_history.see(tk.END)

    def run(self):
        self.root.mainloop()


    def perform_action(self, intent):
        if intent == "天气":
            weather, tips = get_random_weather_and_tips()
            result = f"天气情况：{weather}\n{tips}"
        elif intent == "日程":
            result = "您有一个日程安排：" + get_random_schedule()
        elif intent == "浏览器": 
            webbrowser.open("http://www.google.com") 
            # 可以根据需求更改默认打开的网址 
            result = "浏览器已打开。" 
        elif intent == "记事本": 
            subprocess.Popen(['notepad.exe']) 
            result = "记事本已打开。"
        else:
            result = "抱歉，我不明白您的意图。"
        return result


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApplication(root)

    app.chat_history.tag_config('user', foreground='#007bff')  # 绿色文本
    app.chat_history.tag_config('robot_message', foreground='#28a745')  

    app.run()
