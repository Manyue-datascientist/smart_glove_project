from ultralytics import YOLO

class ParentModel:
    def __init__(self):
        """Load the parent YOLO v11 L model."""
        self.model = YOLO("models/yolo11l.pt")  # Load YOLO v11 L

    def train(self, data_yaml="coco8.yaml", epochs=100):
        """Train the parent model on a dataset."""
        results = self.model.train(data=data_yaml, epochs=epochs, imgsz=640)
        return results

    def infer(self, image_path):
        """Run inference with the parent model."""
        results = self.model(image_path)
        return results

# Example Usage
if __name__ == "__main__":
    parent = ParentModel()
    results = parent.infer("data/Test_M.jpg")
    print(results)
