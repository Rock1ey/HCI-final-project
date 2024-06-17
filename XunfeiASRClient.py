# -*- encoding:utf-8 -*-
import hashlib
import hmac
import base64
import json
import time
import threading
import websocket
from urllib.parse import quote
import logging
import pyaudio

# 应用的app_id和api_key
app_id = "14ff183b"  
api_key = "c7e014dd116610bdebd2427259dd1005"  

# 讯飞代理类，用于一次语音识别的实现
class XunfeiASRClient:
    def __init__(self, app_id, api_key, result_callback):
        """
        初始化讯飞ASR客户端
        :param app_id: 应用ID
        :param api_key: 应用API密钥
        :param result_callback: 识别结果回调函数
        """
        # 设置app_id和api_key
        self.app_id = app_id
        self.api_key = api_key

        # 在识别结果接收完成后调用该回调函数传递结果
        self.result_callback = result_callback

        # 建立连接
        self.ws = self.create_connection()
        self.is_recording = False
        self.audio = pyaudio.PyAudio()
        self.stream = None
        if self.ws:
            # 启动一个线程接收WebSocket消息
            self.trecv = threading.Thread(target=self.recv)
            self.trecv.start()

    def create_connection(self):
        """
        建立WebSocket连接的方法
        :return: WebSocket对象
        """
        base_url = "ws://rtasr.xfyun.cn/v1/ws"
        ts = str(int(time.time()))
        signa = self.generate_signa(ts)
        try:
            return websocket.create_connection(f"{base_url}?appid={self.app_id}&ts={ts}&signa={quote(signa)}")
        except Exception as e:
            print(f"Error creating connection: {e}")
            return None

    def generate_signa(self, ts):
        """
        生成签名的方法
        :param ts: 时间戳
        :return: 签名字符串
        """
        # 拼接 app_id 和 ts
        data = (self.app_id + ts).encode('utf-8')
        
        # 计算 MD5
        md5 = hashlib.md5()
        md5.update(data)
        md5_data = md5.hexdigest().encode('utf-8')
        
        # 使用 API Key 进行 HMAC-SHA1 加密
        api_key_bytes = self.api_key.encode('utf-8')
        hmac_sha1 = hmac.new(api_key_bytes, md5_data, hashlib.sha1).digest()
        
        # 将加密结果进行 Base64 编码
        signa = base64.b64encode(hmac_sha1).decode('utf-8')
        
        return signa

    def send_audio_stream(self):
        """
        录音并发送音频流的方法
        """
        if self.ws is None:
            print("WebSocket connection failed.")
            return

        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        CHUNK = 1280

        self.stream = self.audio.open(format=FORMAT,
                                      channels=CHANNELS,
                                      rate=RATE,
                                      input=True,
                                      frames_per_buffer=CHUNK)

        self.is_recording = True
        print("录音开始...")
        while self.is_recording:
            data = self.stream.read(CHUNK)
            self.ws.send(data)
            time.sleep(0.04)
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        if self.ws and self.ws.connected:
            self.ws.send(bytes(json.dumps({"end": True}).encode('utf-8')))
            print("send end tag success")

    def recv(self):
        """
        接收WebSocket消息的方法
        """
        try:
            full_result = ""
            while self.ws and self.ws.connected:
                result = self.ws.recv()
                if not result:
                    # print("receive result end")
                    break
                result_dict = json.loads(result)
                if result_dict["action"] == "started":
                    # print("handshake success, result: " + result)
                    pass
                elif result_dict["action"] == "result":
                    data = result_dict["data"]
                    result_data = json.loads(data)
                    if "cn" in result_data:
                        st = result_data["cn"]["st"]
                        rt = st["rt"]
                        for item in rt:
                            ws = item["ws"]
                            for w in ws:
                                cw = w["cw"]
                                for c in cw:
                                    word = c["w"]
                                    full_result += word
                elif result_dict["action"] == "error":
                    print("rtasr error: " + result)
                    self.ws.close()
                    return
            print("Recognized text: " + full_result)
            self.result_callback(full_result) # 调用结果回调函数
        except websocket.WebSocketConnectionClosedException:
            print("receive result end")
        except Exception as e:
            print(f"Error receiving data: {e}")

    def close(self):
        """
        关闭连接的方法
        """
        self.is_recording = False
        if self.ws:
            self.ws.close()
        # print("connection closed")

if __name__ == '__main__':
    logging.basicConfig()

    client = XunfeiASRClient(app_id, api_key)
    try:
        client.send_audio_stream()
    except KeyboardInterrupt:
        client.close()


