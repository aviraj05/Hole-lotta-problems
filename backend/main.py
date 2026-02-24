from fastapi import FastAPI, UploadFile, File, Form, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel
import time

# Import AMD placeholders
from ai_pipeline import (
    amd_rocjpeg_decode,
    yolov8_severity_classification,
    spacy_extract_location,
    llama_generate_civic_report
)

app = FastAPI(
    title="Road Intelligence Prototype API",
    description="FastAPI Backend powered by AMD ROCm Mock Pipeline",
    version="1.0.0"
)

# Allow cross-origin for mobile app / frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalysisResponse(BaseModel):
    message: str
    severity: str
    confidence: float
    report_text: str
    processing_time_ms: float

def background_process_and_tweet(severity: str, report_text: str):
    """
    Placeholder for Celery + Redis + Tweepy task.
    In production, this streams into Postgres + PostGIS and triggers Twitter bot
    """
    print(f"[BACKGROUND TASK] Logging severe pothole to PostGIS Database...")
    if severity == "Critical":
        print(f"[BACKGROUND TASK] Auto-tweeting: {report_text}")

@app.get("/")
def read_root():
    return {"status": "Hardware Accelerated API Engine is Running"}

@app.post("/api/reports/submit")
async def analyze_road(
    background_tasks: BackgroundTasks,
    image: UploadFile = File(...),
    lat: float = Form(...),
    lng: float = Form(...),
):
    start_time = time.time()
    
    # 1. Hardware Decode Validation
    image_bytes = await image.read()
    decode_info = amd_rocjpeg_decode(image_bytes)
    
    # 2. CV Pipeline: YOLOv8 Inference
    cv_results = yolov8_severity_classification(decode_info)
    
    # 3. NLP Pipeline
    location_tags = spacy_extract_location(lat, lng)
    generated_report = llama_generate_civic_report(cv_results["severity"], location_tags)
    
    # Calculate performance metrics
    end_time = time.time()
    processing_ms = round((end_time - start_time) * 1000, 2)
    
    # Append backend tasks (mock Celery/Redis)
    background_tasks.add_task(background_process_and_tweet, cv_results["severity"], generated_report)
    
    import uuid
    report_id = str(uuid.uuid4())
    
    return JSONResponse(status_code=200, content={
        "report_id": report_id,
        "message": "Image analyzed successfully via AMD ROCm Pipeline",
        "severity": cv_results["severity"].capitalize(),
        "confidence": cv_results["confidence"],
        "report_text": generated_report,
        "processing_time_ms": processing_ms,
        "decode_engine": decode_info["status"]
    })

@app.get("/api/heatmap/data")
async def get_heatmap():
    return JSONResponse(status_code=200, content={
        "hotspots": [
            { "id": "1", "coordinate": { "latitude": 18.5204, "longitude": 73.8567 }, "severity": "Critical" },
            { "id": "2", "coordinate": { "latitude": 18.5224, "longitude": 73.8587 }, "severity": "Medium" },
            { "id": "3", "coordinate": { "latitude": 18.5184, "longitude": 73.8547 }, "severity": "Low" },
        ]
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
