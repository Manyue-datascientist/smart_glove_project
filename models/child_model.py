from ultralytics import YOLO

class ChildModel:
    def __init__(self, model_type="detection"):
        """Load the child model - either YOLO v8n or YOLO v8n-seg."""
        if model_type == "detection":
            self.model = YOLO("models/yolov8n.pt")  # YOLO v8n for detection
        elif model_type == "segmentation":
            self.model = YOLO("models/yolov8n-seg.pt")  # YOLO v8n-seg for segmentation

    def infer(self, image_path):
        """Run inference with the child model."""
        results = self.model(image_path,save=True)
        return results

# Example Usage
if __name__ == "__main__":
    child = ChildModel("detection")
    results = child.infer("data/Test_M.jpg")
    print(results)
