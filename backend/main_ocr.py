from typing import Dict, Any
import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import tempfile
import shutil
from pathlib import Path

# Import OCR service
try:
    from services.ocr import ocr_service
    from services.parser import ParserService
    OCR_AVAILABLE = True
except ImportError as e:
    print(f"OCR services not available: {e}")
    OCR_AVAILABLE = False

# Import health router
from api.health import router as health_router

load_dotenv()

APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")

app = FastAPI(title="CompliCopilot API", version=APP_VERSION)

# CORS for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3000", 
        "http://127.0.0.1:3001",
        "http://127.0.0.1:5500",
        "http://127.0.0.1:5501",
        "http://localhost:5500",
        "http://localhost:5501",
        "http://127.0.0.1:8000",
        "http://localhost:8000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create uploads directory
uploads_dir = Path(UPLOAD_DIR)
uploads_dir.mkdir(exist_ok=True)

@app.get("/", tags=["root"])
def root() -> Dict[str, Any]:
    return {
        "message": "CompliCopilot API is running!",
        "status": "ok",
        "service": "backend", 
        "version": APP_VERSION,
        "ocr_available": OCR_AVAILABLE,
        "docs": "/docs",
        "endpoints": {
            "health": "/api/v1/health",
            "upload": "/upload" if OCR_AVAILABLE else "disabled",
            "docs": "/docs",
            "redoc": "/redoc"
        }
    }

# Simple OCR endpoint for testing
@app.post("/upload", tags=["receipts"])
async def upload_receipt(file: UploadFile = File(...)):
    """
    Upload a receipt image and extract text using OCR.
    """
    if not OCR_AVAILABLE:
        raise HTTPException(status_code=503, detail="OCR service is not available")
    
    # Validate file type
    if not file.content_type or not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(file.filename).suffix) as temp_file:
            shutil.copyfileobj(file.file, temp_file)
            temp_path = temp_file.name
        
        # Run OCR
        extracted_text = ocr_service.extract_text_from_image(temp_path)
        
        # Parse the extracted text
        parser = ParserService()
        parsed_data = parser.parse_receipt_text(extracted_text)
        
        # Clean up temp file
        os.unlink(temp_path)
        
        return {
            "status": "success",
            "filename": file.filename,
            "extracted_text": extracted_text,
            "parsed_data": parsed_data
        }
        
    except Exception as e:
        # Clean up temp file if it exists
        if 'temp_path' in locals():
            try:
                os.unlink(temp_path)
            except:
                pass
        raise HTTPException(status_code=500, detail=f"OCR processing failed: {str(e)}")

# Include health router
app.include_router(health_router)