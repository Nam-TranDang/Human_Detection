from ultralytics import YOLO
from pathlib import Path



model_path = Path(r"F:\working_people_detection\runs\detect\train\weights\best.pt")  
video_path = Path(r"") #import video path

model = YOLO(model_path)

result = model(video_path, save=True, show=True, device=0)