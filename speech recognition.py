import tkinter as tk

def start_voice_recognition():
# 在这里添加语音识别逻辑
  pass

def stop_voice_recognition():
# 在这里添加停止语音识别的逻辑
  pass

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