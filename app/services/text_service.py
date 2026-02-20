from app.logger import logger

def process_text_logic(text: str)->int:
    """
    Contiene la lógica de negocio.
    No depende de FastAPI.
    """
    """if text == "error":
      raise ValueError("Error forzado")"""

    length = len(text)

    logger.info(
        "text_processed",
        text_length=length
    )

    return length