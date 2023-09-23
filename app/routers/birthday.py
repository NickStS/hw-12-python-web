from fastapi import APIRouter, Depends
from datetime import date, timedelta
from sqlalchemy.orm import Session
from typing import List
from ..crud import get_contacts
from ..database import database
from ..models import Contact
from ..schemas import Contact

router = APIRouter()

@router.get("/contacts/birthday/", response_model=List[Contact])
async def list_contacts_with_upcoming_birthdays(db: Session = Depends(database.get_db)):
    today = date.today()
    next_week = today + timedelta(days=7)
    
    contacts = get_contacts(db)
    
    upcoming_birthday_contacts = [
        contact for contact in contacts if contact.birthday and today <= contact.birthday <= next_week
    ]
    
    return upcoming_birthday_contacts
