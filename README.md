# 🚦 Real-Time Traffic Light Detection System

## 📌 Overview
This project detects traffic light states (Red, Yellow, Green) in real-time using **Python, OpenCV, and HSV color segmentation**.

## ⚡ Features
- Real-time detection via webcam.
- Video file input support.
- Bounding boxes and labels for detected signals.
- Screenshot saving for results.

## 🛠️ Tech Stack
- Python
- OpenCV
- NumPy
- HSV Color Space

## Demo Video  
[Click here to watch the demo]
  https://drive.google.com/file/d/19gtP7dX0hRSxCv3w7oAWq9x55WGiZZed/view?usp=sharing

## 🚀 Live Demo
Check out the deployed app here: 
 https://traffic-light-detection-djahavfku7yhnntmaqgsxj.streamlit.app/

## 🚀 How to Run
```bash
pip install -r requirements.txt
python traffic_light_detection.py --source 0  # For webcam
python traffic_light_detection.py --source sample_video.mp4  # For sample video
