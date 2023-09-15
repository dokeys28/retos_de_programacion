from fastapi import APIRouter

router = APIRouter(prefix='/dias', tags=['dias'])



@router.get("/")
def index():
    return 'Api de Dias'