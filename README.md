# 🕳️ Hole Lotta Problems

> **AI-powered crowdsourced pothole detection and civic accountability platform — built on AMD ROCm**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-orange?style=flat-square&logo=pytorch)
![AMD ROCm](https://img.shields.io/badge/AMD-ROCm-red?style=flat-square)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-purple?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=flat-square&logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

---

## The Problem

Every day, millions of Indians navigate roads riddled with potholes — absorbing vehicle damage, risking accidents, and filing complaints that go nowhere.

Municipalities react only when pressure builds, not when damage occurs. **There is no intelligent system that continuously detects road damage, prioritizes it by severity, and tells authorities where to act — before it becomes a crisis.**

---

## Our Solution

Hole Lotta Problems is an AI-powered Urban Road Intelligence Platform that:

- 📸 **Detects** potholes from citizen photos using YOLOv8 computer vision
- 📍 **Maps** damage in real-time via GPS-tagged heatmaps
- 🧠 **Clusters** forum reports using LLaMA 7B to extract hotspots
- 📊 **Scores** road health city-wide with a dynamic Road Health Index
- 🐦 **Escalates** unresolved hotspots via an automated Twitter bot that publicly tags municipalities

---

## Architecture

![Architecture Diagram](docs/architecture_diagram.png)

| Layer | Component | AMD ROCm Library |
|---|---|---|
| Image Decoding | rocJPEG + rocDecode | `rocJPEG`, `rocDecode` |
| CV Pipeline | YOLOv8 + MIVisionX | `MIVisionX`, `MIOpen` |
| LLM Inference | LLaMA 7B | `MIOpen`, `RCCL` |
| Heatmap Rendering | deck.gl | GPU-accelerated |

---

## Tech Stack

**AI/ML**
- YOLOv8 (Ultralytics) — pothole detection & severity classification
- LLaMA 7B (4-bit quantized) — NLP clustering & tweet generation
- Sentence Transformers — complaint similarity
- ONNX Runtime — on-device mobile inference

**Backend**
- FastAPI — REST API
- PostgreSQL + PostGIS — geospatial data
- Firebase — real-time sync
- Celery + Redis — async task queue

**Frontend / Mobile**
- React Native — cross-platform mobile app
- deck.gl + OpenStreetMap — GPU-accelerated heatmap
- Tweepy — Twitter bot

**AMD ROCm Ecosystem**
- ROCm, MIOpen, MIVisionX, rocJPEG, rocDecode, RCCL

---

## Project Structure

```
hole-lotta-problems/
├── model/
│   ├── train/          # YOLOv8 training scripts
│   ├── inference/      # Inference pipeline
│   └── utils/          # Preprocessing, augmentation
├── backend/
│   ├── api/            # FastAPI routes
│   ├── services/       # Business logic (detection, clustering, bot)
│   └── utils/          # Helpers
├── mobile/             # React Native app
├── bot/                # Twitter bot scripts
├── notebooks/          # Experimentation & EDA
├── docs/               # Architecture diagrams, assets
├── data/
│   ├── raw/            # Raw image datasets
│   └── processed/      # Preprocessed data
├── requirements.txt
├── .env.example
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- CUDA 11.8+ (local dev) or AMD ROCm 5.7+ (deployment)
- Node.js 18+ (mobile)
- PostgreSQL with PostGIS extension
- Redis

### Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/hole-lotta-problems.git
cd hole-lotta-problems

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Fill in your API keys in .env

# Start the backend
cd backend
uvicorn main:app --reload
```

### Mobile Setup

```bash
cd mobile
npm install
npx expo start
```

---

## Environment Variables

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/holalotta

# Firebase
FIREBASE_API_KEY=
FIREBASE_PROJECT_ID=

# Twitter Bot
TWITTER_API_KEY=
TWITTER_API_SECRET=
TWITTER_ACCESS_TOKEN=
TWITTER_ACCESS_SECRET=

# Groq (LLaMA fallback)
GROQ_API_KEY=

# AMD / Model
MODEL_PATH=model/weights/yolov8_pothole.pt
DEVICE=cuda  # or rocm for AMD deployment
```

---

## Team

**Hole Lotta Problems** — Built at [Hackathon Name]

| Name | Role |
|------|------|
| Aviraj Sinha , Abhinandan Singh | Backend + ML |
| Aviraj Sinha | Mobile (React Native) |
| Abhinandan Singh | CV Model + AMD ROCm |
| Abhinav Bisht | Frontend Design, PowerPoint Presentation, Product Refinement |

---

## License

MIT License — see [LICENSE](LICENSE) for details.
