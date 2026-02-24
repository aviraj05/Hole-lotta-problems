from ultralytics import YOLO
import torch

def train():
    print(f"Training on: {'CUDA' if torch.cuda.is_available() else 'CPU'}")
    print(f"GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}")

    model = YOLO("yolov8n.pt")  # start from pretrained nano — swap to yolov8m for better accuracy

    results = model.train(
        data="data/pothole_dataset.yaml",
        epochs=50,
        imgsz=640,
        batch=16,
        device=0,                    # GPU 0 (CUDA or ROCm)
        project="model/weights",
        name="yolov8_pothole",
        patience=10,                 # early stopping
        augment=True,
        verbose=True
    )

    print(f"Training complete. Weights saved to: model/weights/yolov8_pothole/weights/best.pt")


if __name__ == "__main__":
    train()
