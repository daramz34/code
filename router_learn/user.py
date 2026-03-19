from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["User Management"])


@router.get("/")
def get_all_users():
    return {
        "Message": "Listing all users from the user.py file"
    }


@router.get("/{id}")
def get_user_by_id(id:int):
    return {
        "message": f"Fetching user with ID: {id}"
    } 