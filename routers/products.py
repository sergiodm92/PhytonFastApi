from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["users"] 
                    )

@router.get("/")
async def root():
    return {"message": "Hola estamos en products"}