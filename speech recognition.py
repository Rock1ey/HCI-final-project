import tkinter as tk

# import threading
# import speech_recognition as sr

# # 创建识别器对象
# recognizer = sr.Recognizer()
# is_listening = False

def start_voice_recognition():
    # 在这里添加开始语音识别逻辑
    # global is_listening # 全局变量，多个函数共享
    # is_listening = True # 设置为开始录音
    # threading.Thread(target=listen_in_background).start() # 开启线程
    pass

def stop_voice_recognition():
    # 在这里添加停止语音识别的逻辑
    # global is_listening
    # is_listening = False # 设置为停止录音
    # print("Listening stopped:", is_listening)
    pass

# def listen_in_background():
#     # 线程：语音输入过程
#     global is_listening
#     with sr.Microphone() as source:
#         if is_listening:
#             print("请说话...")
#             recognizer.adjust_for_ambient_noise(source)
#             try:
#                 audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=5)
#                 text = recognizer.recognize_sphinx(audio_data, language='zh-CN')
#                 is_listening = True
#                 print("你说的是: " + text)
#             except sr.UnknownValueError:
#                 print("无法识别音频")
#             except sr.RequestError as e:
#                 print("无法请求结果；{0}".format(e))
#             except sr.WaitTimeoutError:
#                 print("等待超时，没有检测到语音输入")

#创建主窗口
root = tk.Tk()
root.title("语音识别应用")
root.configure(background='lightblue')  # 设置背景颜色

#创建提示标签
tip_label = tk.Label(root, text="点击按钮开始语音识别", bg='lightblue',font=("华文行楷",20,"normal"))
tip_label.pack(pady=10)
tip_label = tk.Label(root, text="1.天气预报", bg='lightblue',font=("华文行楷",15,"normal"))
tip_label.pack(pady=10)
tip_label = tk.Label(root, text="2.日程安排", bg='lightblue',font=("华文行楷",15,"normal"))
tip_label.pack(pady=10)
tip_label = tk.Label(root, text="3.播放音乐", bg='lightblue',font=("华文行楷",15,"normal"))
tip_label.pack(pady=10)

#创建开始语音识别按钮
start_button = tk.Button(root, text="开始录音", command=start_voice_recognition, bg='lightgreen', width=15)
start_button.pack(pady=5)

#创建停止语音识别按钮
stop_button = tk.Button(root, text="停止录音", command=stop_voice_recognition, bg='salmon', width=15)
stop_button.pack(pady=5)

#运行主循环
root.mainloop()