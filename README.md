# 基于语音识别的虚拟助理

## 简介
本项目是一个基于语音识别技术的虚拟助理程序，能够通过语音指令执行各种任务，如查询天气、查看日程、打开浏览器、启动记事本和播放音乐等。项目使用了讯飞的语音识别API和spaCy的自然语言处理技术，并使用Tkinter实现了用户界面。

## 环境配置
本项目在Anaconda虚拟环境下运行，以下是安装和运行程序的步骤：

### 1. 创建并激活Conda虚拟环境

    conda create -n speech_recognition python=3.10
    conda activate speech_recognition

### 2. 安装依赖库
在激活的Conda虚拟环境中，运行以下命令安装所需的依赖库：

    conda install spacy websocket-client pyaudio tkinter

### 3. 下载spaCy中文模型

    python -m spacy download zh_core_web_sm

### 4.项目目录结构

```
speech_recognition/
│
├── intent_and_actions.py
├── XunfeiASRClient.py
├── ChatApplication.py
├── image/
│   ├── robot.png
│   ├── record.png
│   ├── stop.png
└── README.md
```

### 5.配置讯飞API
在XunfeiASRClient.py文件中，替换以下部分的app_id和api_key为你在讯飞官网申请的真实值：

    # 应用的app_id和api_key
    app_id = "your_app_id"  
    api_key = "your_api_key"  

## How To Run?

### 1.cmd usage
在项目根目录下，进入cmd，运行以下命令启动虚拟助理程序：

     python ChatApplication.py


### 2.vscode usage
在vscode中打开项目文件夹，打开ChatApplication.py文件，点击右上角的运行代码按钮，即可运行程序

## 使用说明
1.启动程序后，将显示一个聊天窗口。\
2.点击录音按钮开始录音，再次点击停止录音。\
3.语音识别结果将显示在聊天窗口中，并根据识别的意图执行相应的任务。

## 注意事项
1.语音识别功能依赖网络连接，请确保运行时网络连接正常。\
2.由于使用了外部API，语音识别的准确性可能会受到环境噪音和用户发音等因素的影响。