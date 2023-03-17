from fastapi import APIRouter

router = APIRouter(prefix="/users",
                   tags=["users"] 
                    )

@router.get("/")
async def root():
    return {"message": "Hola estamos en users"}