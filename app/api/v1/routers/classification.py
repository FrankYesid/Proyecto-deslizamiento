from fastapi import APIRouter, File, UploadFile, Depends
from typing import Optional
from app.api.v1.controllers.classification import handle_image_classification

router = APIRouter()

@router.post("/classify")
async def classify_image(
    file: UploadFile = File(...),
    model_name: Optional[str] = None
):
    return await handle_image_classification(file, model_name)
