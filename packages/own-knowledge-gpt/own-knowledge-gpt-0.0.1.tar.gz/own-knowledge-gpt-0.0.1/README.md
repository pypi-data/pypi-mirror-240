---
title: Own Knowledge GPT
emoji: 🚀
colorFrom: indigo
colorTo: red
sdk: gradio
sdk_version: 4.2.0
app_file: app.py
pinned: false
license: mit
---

# Own-Knowledge-GPT 
## Introduction 
Welcome to the Own-Knowledge-GPT, this is a demo project that allow you want your Chat bot can learn anything you want 

This project is built by Python and integration with OpenAI API which use GPT-3.5-turbo model 

## Getting Started 
### 1. Environment Setup
The project is built in python 3.9+. You need to install python 3.9 or later
```commandline
  git clone git@hf.co:spaces/myn0908/Own-Knowledge-GPT
```
For install dependencies:
```commandline
 pip install -r requirements.txt
```
### How to use 
This project use Gradio to build User Interface, please use: 
```commandline
 python app.py
```
Enjoy project with step by step follow this: 

Bot Learning with URL 
![Screenshot 2023-11-13 at 19.56.40.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fzc%2Fcsmhsgrd0bz3bbkycljwdk2c0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_zJFx9p%2FScreenshot%202023-11-13%20at%2019.56.40.png)

Please input URL and your file format and then press Training button, when the training process is finished, it's will notice you Training Completed 

After that, you can starting chat with your custom bot about the topic in your URL
![Screenshot 2023-11-13 at 20.00.10.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fzc%2Fcsmhsgrd0bz3bbkycljwdk2c0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_xDIQGv%2FScreenshot%202023-11-13%20at%2020.00.10.png)

The vector index storage by this structure: 

![Screenshot 2023-11-13 at 20.03.04.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fzc%2Fcsmhsgrd0bz3bbkycljwdk2c0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_ZTP7r9%2FScreenshot%202023-11-13%20at%2020.03.04.png)