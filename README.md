# 🚀 CompliCopilot — Intelligent Expense Management System

[![FastAPI](https://img.shields.io/badge/FastAPI-0.112.1-009639.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.13+-3776ab.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Tesseract](https://img.shields.io/badge/Tesseract-OCR-brightgreen.svg?style=flat)](https://github.com/tesseract-ocr/tesseract)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com)

**CompliCopilot** is a fully functional Progressive Web Application (PWA) that revolutionizes expense management for small businesses through **AI-powered OCR** and **intelligent data extraction**.

## ✨ **Current Status: FULLY OPERATIONAL** ✨

CompliCopilot is now a **working production-ready application** with the following implemented features:
- ✅ **Google OAuth Authentication** via Firebase
- ✅ **Real-time OCR Processing** using Tesseract 5.5.0
- ✅ **Intelligent Data Extraction** (vendor, date, amount)
- ✅ **File Upload & Processing** with image preprocessing
- ✅ **CSV Export Functionality** for expense records
- ✅ **Dockerized Deployment** with FastAPI backend
- ✅ **Firebase Integration** for secure authentication

---

## 🌟 Project Overview

### **The Idea**
CompliCopilot simplifies expense management for small businesses by automating the tedious process of receipt handling. Our advanced OCR system extracts vendor names, dates, and amounts with high precision, while AI categorizes expenses automatically.

### **Problem Statement**
Small businesses often struggle with:
- Manual receipt handling and data entry errors
- Time-consuming expense categorization
- Lack of compliance with tax regulations
- Difficulty in organizing financial records

### **Innovation & Implementation**
- **Advanced OCR Pipeline**: Multi-stage image preprocessing with Tesseract OCR
- **Smart Data Extraction**: Regex-based parsing with confidence scoring
- **Seamless Authentication**: Google OAuth integration via Firebase
- **Real-time Processing**: Instant receipt analysis and form population
- **Export Capabilities**: One-click CSV generation for accounting software

### **Market Potential**
The global market for expense management software is projected to reach **$10 billion** by 2030. CompliCopilot aims to capture a significant share by targeting small and medium-sized businesses.

---

## 🏗️ Project Architecture

### **Production Architecture**
- **frontend/**: Static PWA with Google OAuth, file upload, and real-time OCR integration
- **backend/**: FastAPI application with Firebase authentication and Tesseract OCR processing
- **services/**: Modular services for OCR, parsing, compliance, and storage
- **database/**: PostgreSQL with SQLAlchemy ORM for data persistence
- **docker/**: Production-ready containerization with optimized images

### **Tech Stack**
- **Frontend**: Vanilla JavaScript, HTML5, CSS3, Firebase Auth SDK
- **Backend**: FastAPI, Python 3.11, SQLAlchemy, PostgreSQL
- **OCR Engine**: Tesseract 5.5.0 with advanced image preprocessing
- **Authentication**: Firebase Admin SDK, Google OAuth 2.0
- **AI/ML**: Pattern recognition for vendor/amount/date extraction
- **Deployment**: Docker containers, Vercel integration ready
- **Storage**: Firebase Storage for receipt images

### **Key Features Implemented**
- **Smart OCR Processing**: Multiple PSM modes for optimal text extraction
- **Intelligent Parsing**: Advanced regex patterns for data extraction
- **Real-time Form Population**: Automatic field filling from OCR results
- **CSV Export**: Professional expense reports for accounting integration
- **Secure Authentication**: Firebase-based user management
- **Image Preprocessing**: Noise reduction, contrast enhancement, deskewing

---

## 🛠️ Implementation Highlights

### **OCR & AI Processing**
1. **Advanced Image Preprocessing**: Grayscale conversion, noise reduction, contrast enhancement
2. **Multi-Mode OCR**: Tesseract PSM modes for different document layouts
3. **Intelligent Text Extraction**: Confidence scoring and quality validation
4. **Smart Data Parsing**: Regex patterns for vendor names, dates, and monetary amounts
5. **Real-time Processing**: Instant feedback and form population

### **Authentication & Security**
1. **Google OAuth Integration**: Seamless login via Firebase Auth
2. **Token-based Security**: JWT authentication for API endpoints
3. **Development Mode**: Flexible authentication for testing environments
4. **Session Management**: Secure user state persistence

### **User Experience**
1. **Drag & Drop Upload**: Intuitive file selection and processing
2. **Real-time Feedback**: Progress indicators and status updates
3. **Form Auto-population**: OCR results automatically fill expense forms
4. **One-click Export**: CSV generation for accounting software integration
5. **Responsive Design**: Works seamlessly on desktop and mobile devices

---

## 🚀 Quick Start Guide

### **Method 1: Docker Compose (Recommended)**
```bash
# Clone the repository
git clone https://github.com/siyajha919-o/CompliCopilot.git
cd CompliCopilot

# Start all services
cd docker
docker-compose up --build
```
Access: Frontend at `http://127.0.0.1:3000`, Backend at `http://127.0.0.1:8000`

### **Method 2: Manual Setup**

#### **Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Start OCR-enabled version
python -m uvicorn main_ocr:app --host 127.0.0.1 --port 8000 --reload
```

#### **Frontend Setup**
```bash
cd frontend
npm install
npm start
```

### **Method 3: Quick Testing**
```bash
cd backend
python -m uvicorn main_simple:app --host 127.0.0.1 --port 8000 --reload
```

### **🔧 Available Deployment Options**

| File | Purpose | Features | Database |
|------|---------|----------|----------|
| `main_ocr.py` | **Full OCR System** | Complete OCR + Parsing | None |
| `main_simple.py` | **Basic API** | Health checks only | None | 
| `main_full.py` | **SQLite Version** | All features + Database | SQLite |
| `main.py` | **Production** | Complete system | PostgreSQL |

### **📊 API Endpoints**
- `GET /` - Service status and information
- `GET /api/v1/health` - Health check
- `GET /docs` - Interactive API documentation  
- `POST /upload` - Receipt OCR processing *(OCR versions)*

### **🧪 Testing the Application**

1. **Upload Receipt**: Visit `http://127.0.0.1:3000/upload.html`
2. **API Testing**: Use `http://127.0.0.1:8000/docs` for interactive testing
3. **Health Check**: `curl http://127.0.0.1:8000/api/v1/health`

---

## 👨‍💻 Developer

**CompliCopilot** is developed and maintained by:

- **siyajha919-o** 🚀  
  *Full-Stack Developer & Project Creator*  
  Complete system architecture, OCR implementation, backend development, frontend design, Firebase integration, and project management

---

## 🌟 Features in Action

1. **📸 Receipt Upload**: Drag-and-drop interface with instant feedback
2. **🔍 OCR Processing**: Advanced Tesseract integration with image preprocessing
3. **📝 Data Extraction**: Automatic parsing of vendor, date, and amount
4. **📋 Form Population**: Real-time filling of expense forms
5. **📊 CSV Export**: One-click download for accounting software
6. **🔐 Secure Login**: Google OAuth via Firebase authentication
7. **📱 Responsive Design**: Works on desktop and mobile devices

---

## 🎯 Future Enhancements

- **AI Categorization**: Automatic expense category detection
- **Multi-language OCR**: Support for international receipts
- **Mobile App**: Native iOS and Android applications
- **Accounting Integration**: Direct QuickBooks/Xero sync
- **Advanced Analytics**: Spending patterns and insights
- **Team Collaboration**: Multi-user business accounts

---

## 📜 License

MIT License - Feel free to use this project for educational and commercial purposes.

---

**CompliCopilot** | *Transforming expense management, one receipt at a time*