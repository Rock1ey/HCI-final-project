# Speech recognition-based virtual assistant

## Brief introduction
This project is a virtual assistant program based on voice recognition technology, which can perform various tasks through voice commands, such as checking the weather, checking schedules, opening browsers, launching notepads, and playing music. The project uses iFLYTEK's speech recognition API and spaCy's natural language processing technology, and uses Tkinter to implement the user interface.

## Environment configuration
The project runs in the Anaconda virtual environment, and here are the steps to install and run the program:

### 1. Create and activate a Conda virtual environment

    conda create -n speech_recognition python=3.10
    conda activate speech_recognition

### 2. Install dependencies
In the activated Conda virtual environment, run the following command to install the required dependencies:

    conda install spacy websocket-client pyaudio tkinter

### 3. Download spaCy Chinese model

    python -m spacy download zh_core_web_sm

### 4.Project directory structure

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

### 5.Configure the iFLYTEK API
In the XunfeiASRClient.py file, replace the app_id and api_key in the following parts with the real value you applied for on the official website of iFLYTEK:

    # The app_id and api_key of your app
    app_id = "your_app_id"  
    api_key = "your_api_key"  

## How To Run?

### 1.cmd usage
In the root directory of the project, go to cmd and run the following command to start the Virtual Assistant:

     python ChatApplication.py


### 2.VScode usage
Open the project folder in VScode, open the ChatApplication.py file, and click the Run Code button in the upper right corner to run the program

## Directions for use
1.Once you launch the program, a chat window will be displayed.\
2.Tap the record button to start recording, and tap again to stop recording.\
3.The speech recognition results are displayed in the chat window, and the corresponding task is performed according to the recognized intent.

## Precautions
1.The voice recognition feature relies on a network connection, so make sure that the network connection is working properly when you are running.\
2.Due to the use of external APIs, the accuracy of speech recognition can be affected by factors such as ambient noise and user pronunciation.