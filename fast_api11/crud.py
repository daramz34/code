from sqlalchemy.orm import Session
from fast_api12.models import URL
from schema import UserCreate
import random, string





def gen_short_code(length=6):
    chars= string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def create_url(db:Session, url:UserCreate):
    short_code = gen_short_code()
    db_url = URL(
        url=url.url,
        short_code=short_code
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


def get_url(db: Session, url_id: int):
    db_url = db.query(URL).filter(URL.id == url_id).first()

    return db_url

def get_all_urls(db:Session):
    db_url = db.query(URL).all()
    return db_url



def delete_url(db:Session, url_id:int):
    db_url = db.query(URL).filter(URL.id == url_id).first()

    if db_url:
        db.delete(db_url)
        db.commit()
        return True
    return False