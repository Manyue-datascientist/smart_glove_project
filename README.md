 🛍️Smart Glove for Visually Impaired Shopping Assistance
📌 Project Overview
This project is designed to assist visually impaired individuals in navigating stores and locating products using AI-powered object detection and hand guidance.

✔ Uses YOLOv8 Nano for real-time object detection & segmentation.
✔ Tracks hand movement using MediaPipe & IMU sensors.
✔ Provides audio guidance & will integrate haptic feedback via a soft robotic glove.
✔ Designed for real-world deployment on Raspberry Pi & Jetson Nano.

🎯 Features
✅ Object Detection: Identify and locate store products (e.g., eggs, milk, etc.).
✅ Hand Tracking: Estimate hand position relative to the detected object.
✅ Real-Time Guidance: Assist users via audio feedback (voice commands).
✅ Future Expansion: Integrate haptic glove for direct hand guidance.

🛠️ Tech Stack
🔹 Software
Computer Vision: YOLOv8 Nano (Ultralytics)
Hand Tracking: MediaPipe, OpenCV, IMU Sensors (MPU6050)
Voice Feedback: TTS (Text-to-Speech) for real-time guidance
Model Deployment: ONNX, TensorRT (for Raspberry Pi)
API Interface: Flask (for future expansion)
🔹 Hardware (Upcoming)
Processing Unit: Raspberry Pi 5 + AI HAT (13 TOPS NPU)
Camera: OAK-D or Orbbec Astra+
Actuators: Soft Pneumatic Actuators for Glove Feedback
Microcontroller: Arduino Nano 33 BLE for controlling actuators
Sensors: IMU (MPU6050) for hand movement detection

🚀 Project Structure
 
smart_glove_project/
├── src/                # Main source code
│   ├── detection/      # Object detection & segmentation
│   ├── hand_tracking/  # Hand tracking system
│   ├── guidance/       # Audio & haptic feedback
│   ├── hardware/       # Raspberry Pi / Arduino interface
│   ├── utils/          # Common utilities
│   ├── api/            # API Interface (future expansion)
├── models/             # Trained YOLO models
├── data/               # Datasets & annotations
├── configs/            # Config files
├── tests/              # Unit tests
├── scripts/            # Training & deployment scripts
├── README.md           # Project documentation
├── requirements.txt    # Dependencies
├── main.py             # Entry point for the system

📌 Setup Instructions
1️⃣ Clone the Repository
 
git clone https://github.com/Manyue-datascientist/smart_glove_project
cd smart_glove_project
2️⃣ Create & Activate Virtual Environment
 
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
3️⃣ Install Dependencies
 
pip install -r requirements.txt
4️⃣ Run Object Detection
 
python src/detection/yolo_detector.py
👥 Contributors
[Manyu Javvadi](https://www.linkedin.com/in/manyue-javvadi-datascientist/) – Project Lead

📌 Future Plans
✅ Implement object detection & voice-based navigation.
🔜 Integrate haptic feedback via soft robotics.
🔜 Deploy on Raspberry Pi & Jetson Nano for real-world testing.