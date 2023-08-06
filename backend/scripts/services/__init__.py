from fastapi import APIRouter
from scripts.core.handlers.student_handler import StudentHandler
from scripts.schemas import Student, UpdateStudent
from fastapi import HTTPException, status


router = APIRouter(prefix="/api")

@router.get("/students")
def get_students():
    try:
        student_handler = StudentHandler()
        return student_handler.get_students()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        ) from e
    

@router.get("/students/{student_id}")
def get_student_by_id(student_id: str):
    try:
        student_handler = StudentHandler()
        return student_handler.get_student_by_id(student_id=student_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        ) from e
        
        
@router.post("/students")
def add_student(student: Student):
    try:
        student_handler = StudentHandler()
        return student_handler.add_student(student=student.dict())
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        ) from e


@router.put("/students")
def update_student(student: UpdateStudent):
    try:
        student_handler = StudentHandler()
        return student_handler.update_student(student=student.dict())
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        ) from e

@router.delete("/students/{student_id}")
def delete_student(student_id: str):
    try:
        student_handler = StudentHandler()
        return student_handler.delete_student(student_id=student_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        ) from e