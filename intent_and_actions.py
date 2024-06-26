import spacy
from spacy.matcher import Matcher
import random

import subprocess
import webbrowser 

# 加载预训练的spaCy中文模型
nlp = spacy.load('zh_core_web_sm')

# 定义意图和匹配规则
intents = {
    "天气": [
        [{"TEXT": "天气"}],
        [{"TEXT": "气温"}],
        [{"TEXT": "天气"}, {"TEXT": "今天"}],
        [{"TEXT": "天气"}, {"TEXT": "明天"}],
        [{"TEXT": "天气"}, {"TEXT": "周末"}],
    ],
    "日程": [
        [{"TEXT": "日程"}],
        [{"TEXT": "日历"}],
        [{"TEXT": "安排"}],
        [{"TEXT": "日程"}, {"TEXT": "今天"}],
        [{"TEXT": "日程"}, {"TEXT": "明天"}],
        [{"TEXT": "日程"}, {"TEXT": "周末"}],
    ],
    "浏览器": [ 
        [{"TEXT": "打开"}, {"TEXT": "浏览器"}], 
        [{"TEXT": "启动"}, {"TEXT": "浏览器"}], 
        [{"TEXT": "上网"}], 
        [{"TEXT": "打开"}, {"TEXT": "网页"}], 
        [{"TEXT": "浏览"}], 
    ],
    "记事本": [ 
        [{"TEXT": "打开"}, {"TEXT": "记事本"}], 
        [{"TEXT": "启动"}, {"TEXT": "记事本"}], 
        [{"TEXT": "记笔记"}], 
        [{"TEXT": "写笔记"}], 
        [{"TEXT": "记事"}],
        [{"TEXT": "笔记"}], 
    ],
    "音乐": [
        [{"TEXT": "播放"}, {"TEXT": "音乐"}],
        [{"TEXT": "打开"}, {"TEXT": "音乐"}],
        [{"TEXT": "听"}, {"TEXT": "音乐"}],
        [{"TEXT": "播放"}],
        [{"TEXT": "音乐"}],
    ]
}

matcher = Matcher(nlp.vocab)

# 添加匹配规则到matcher
for intent, patterns in intents.items():
    matcher.add(intent, patterns)

def extract_intent_and_entities(text):
    '''
    从文本中提取意图和实体
    '''
    doc = nlp(text)
    matches = matcher(doc)
    # print(f"Matches: {matches}")  # 调试信息，打印匹配结果
    if matches:
        intent = nlp.vocab.strings[matches[0][0]]
        entities = {ent.label_: ent.text for ent in doc.ents}
        return intent, entities
    return None, {}

def get_random_weather():
    weather_conditions = [
        "晴天",
        "多云",
        "阴天",
        "下雨",
        "暴雨",
        "下雪",
        "大雪",
        "雾霾",
        "台风",
        "雷阵雨",
        "冰雹"
    ]
    return random.choice(weather_conditions)

def get_random_schedule():
    schedules = [
        "会议",
        "约会",
        "生日聚会",
        "讲座",
        "派对",
        "运动活动",
        "旅行",
        "学习",
        "家庭聚餐",
        "社交活动"
    ]
    return random.choice(schedules)


weather_conditions_and_tips = {
    "晴天": "天气很好，适合户外活动，但记得防晒。",
    "多云": "天气较好，适合外出，但可能会有短暂的阴云。",
    "阴天": "天气阴沉，注意保暖。",
    "下雨": "请携带雨具，注意防滑。",
    "暴雨": "尽量减少外出，注意安全。",
    "下雪": "穿暖和点，注意路滑。",
    "大雪": "尽量减少外出，注意保暖和路滑。",
    "雾霾": "减少外出，必要时戴口罩。",
    "台风": "尽量避免外出，注意安全。",
    "雷阵雨": "携带雨具，注意雷电天气。",
    "冰雹": "避免外出，注意安全。"
}

def get_random_weather_and_tips():
    weather = random.choice(list(weather_conditions_and_tips.keys()))
    tips = weather_conditions_and_tips[weather]
    return weather, tips

def weather_query():
    weather, tips = get_random_weather_and_tips()
    return f"天气情况：{weather}。注意事项：{tips}"


def perform_action(intent):
    '''
    根据意图执行相应的动作
    '''
    if intent == "天气":
        weather, tips = get_random_weather_and_tips()
        result = f"天气情况：{weather} {tips}"
    elif intent == "日程":
        result = "您有一个日程安排：" + get_random_schedule()
    elif intent == "浏览器": 
        webbrowser.open("http://www.google.com") 
        # 可以根据需求更改默认打开的网址 
        result = "浏览器已打开。" 
    elif intent == "记事本": 
        subprocess.Popen(['notepad.exe']) 
        result = "记事本已打开。"
    elif intent == "音乐":
        # 打开音乐流媒体网站
        webbrowser.open("https://music.163.com/")  # 可以根据需求更改默认打开的音乐网站
        result = "音乐网站已打开。"
    else:
        result = "抱歉，我不明白您的意图。"
    return result
