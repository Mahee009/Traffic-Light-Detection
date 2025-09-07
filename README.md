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

## 🚀 How to Run
```bash
pip install -r requirements.txt
python traffic_light_detection.py --source 0  # For webcam
python traffic_light_detection.py --source sample_video.mp4  # For sample video
