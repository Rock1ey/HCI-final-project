import speech_recognition as sr

# 创建识别器对象
recognizer = sr.Recognizer()

# 使用麦克风作为音频源
with sr.Microphone() as source:
    print("请说话...")
    # 调整环境噪声以提高识别的准确性
    recognizer.adjust_for_ambient_noise(source)

    try:
        # 录制音频，设置最大等待时间和最长录音时间
        audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=5)
        
        # 使用CMU Sphinx将音频转换为文本
        result = recognizer.recognize_sphinx(audio_data, language='zh-CN')
        print("你说的是: " + result)
    except sr.UnknownValueError:
        print("无法识别音频")
    except sr.RequestError as e:
        print("无法请求结果；{0}".format(e))
    except sr.WaitTimeoutError:
        print("等待超时，没有检测到语音输入")