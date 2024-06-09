import spacy
from spacy.matcher import Matcher
import random

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
    ]
}

matcher = Matcher(nlp.vocab)

# 添加匹配规则到matcher
for intent, patterns in intents.items():
    matcher.add(intent, patterns)

def extract_intent_and_entities(text):
    doc = nlp(text)
    matches = matcher(doc)
    print(f"Matches: {matches}")  # 调试信息，打印匹配结果
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

def recommend_food(weather):
    if "下雨" in weather:
        return "下雨天可以考虑点外卖，吃一些温暖的食物，比如热汤、热面、炖菜等。"
    elif "下雪" in weather:
        return "下雪天可以考虑吃火锅、涮肉等火热的食物，也可以吃一些热气腾腾的麻辣烫。"
    elif "晴天" in weather:
        return "晴天可以考虑野餐，可以准备一些沙拉、水果、三明治等清爽的食物，也可以烧烤。"
    elif "多云" in weather:
        return "多云天气适合吃一些清淡的食物，比如清炒、凉拌等，也可以选择去餐馆品尝不同的菜肴。"
    elif "阴天" in weather:
        return "阴天可以考虑吃一些滋补的食物，比如排骨汤、炖鸡汤等，也可以做一些温暖的家常菜。"
    elif "雾霾" in weather:
        return "雾霾天气不宜外出，可以在家里做一些清淡易消化的食物，避免油腻和辛辣的食物。"
    elif "台风" in weather:
        return "台风天气应该注意安全，不宜外出，可以准备一些方便食品和干粮，确保食物的新鲜和安全。"
    elif "雷阵雨" in weather:
        return "雷阵雨天气变化较快，可以准备一些方便快捷的食物，比如快餐、速食等，以备不时之需。"
    elif "冰雹" in weather:
        return "冰雹天气不宜外出，可以在家里做一些暖心的美食，比如热乎乎的汤羹、炖品等，保持身体暖和。"
    else:
        return "当前天气情况下，暂时无法提供推荐。"

# 根据意图执行相应的操作
def perform_action(intent):
    if intent == "天气":
        weather = get_random_weather()
        return f"天气情况：{weather}\n{recommend_food(weather)}"
    elif intent == "日程":
        return "您有一个日程安排：" + get_random_schedule()
    else:
        return "抱歉，我不明白您的意图。"

# 测试函数
texts = [
    "明天天气怎么样？",
    "今天有什么安排？",
    "晴天应该吃什么？",
    "下雨天有什么安排？"
]

for text in texts:
    intent, entities = extract_intent_and_entities(text)
    print(f"Text: {text}")
    print(f"Intent: {intent}, Entities: {entities}")
    print(perform_action(intent))
    print()
