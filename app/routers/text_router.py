from fastapi import APIRouter, HTTPException
from app.models.request_models import TextRequest
from app.services.text_service import process_text_logic
from app.logger import logger



router = APIRouter()


@router.post("/process")
def process_text(request: TextRequest):
    try:
        
        result = process_text_logic(request.text)
        return {"length": result}

    except Exception as e:
        logger.error(
            "processing_error",
            error=str(e)
        )

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )