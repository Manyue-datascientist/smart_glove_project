from ultralytics import YOLO
import os

# Directory where we save models
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

# Define models to download
model_files = {
    "yolo11l": "yolo11l.pt",  # YOLO v11l (Parent Model)
    "yolov8n": "yolov8n.pt",  # YOLO v8n (Child Model)
    "yolov8n-seg": "yolov8n-seg.pt"  # YOLO v8n-seg (Child Model for segmentation)
}

def download_model(model_name):
    """Downloads a YOLO model if not already present."""
    model_path = os.path.join(MODEL_DIR, model_files[model_name])

    if os.path.exists(model_path):
        print(f"✅ {model_name} already downloaded: {model_path}")
    else:
        print(f"⬇️ Downloading {model_name}...")
        model = YOLO(model_files[model_name])  # This automatically downloads from Ultralytics
        model.export(format="torch")  # Save the model in `.pt` format
        print(f"✅ {model_name} downloaded and saved.")

if __name__ == "__main__":
    # Download all required models
    for model in model_files.keys():
        download_model(model)
