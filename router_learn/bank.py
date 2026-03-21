from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/bank", tags=["Banking"])


accounts = {
    "101": 500.0,
    "102": 1200.50
}


@router.post("/withdraw/{acc_id}")
def withdraw(acc_id: str, amount:float):
    if acc_id not in accounts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Account {acc_id} does not exist"
        )
    
    if amount <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You cannot withdraw zero or negatuve money"
        )
    

    if amount > accounts[acc_id]:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail="Insufficient Funds"
        )
    


    accounts[acc_id] -= amount
    return{
        "account_id": acc_id,
        "withdrawn": amount,
        "remaining_balance": accounts[acc_id]
    }