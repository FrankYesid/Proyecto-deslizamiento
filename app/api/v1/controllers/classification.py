from fastapi import UploadFile, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
import io
from PIL import Image
from app.services.ml_inference import MLInferenceService
from app.config.settings import settings

def handle_image_classification(
    file: UploadFile,
    model_name: Optional[str] = None
):
    try:
        # Validate file type
        if not file.filename.lower().endswith(tuple(settings.SUPPORTED_IMAGE_FORMATS)):
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported file format. Supported formats: {', '.join(settings.SUPPORTED_IMAGE_FORMATS)}"
            )

        # Read and process image
        contents = file.read()
        if len(contents) > settings.MAX_IMAGE_SIZE:
            raise HTTPException(
                status_code=413,
                detail=f"File size exceeds maximum allowed size of {settings.MAX_IMAGE_SIZE} bytes"
            )

        image = Image.open(io.BytesIO(contents))
        
        # Get model name
        model_name = model_name or settings.DEFAULT_MODEL
        
        # Process with ML service
        inference_service = MLInferenceService()
        result = inference_service.classify_image(image, model_name)
        
        return JSONResponse(content=result)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
