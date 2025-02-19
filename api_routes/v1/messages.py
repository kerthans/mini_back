from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Message
from database import get_db

router = APIRouter()

@router.post("/messages/")
def create_message(sender_id: int, receiver_id: int, content: str, db: Session = Depends(get_db)):
    new_message = Message(sender_id=sender_id, receiver_id=receiver_id, content=content, timestamp=datetime.utcnow())
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return {"message": "Message created", "data": new_message}

@router.get("/messages/{message_id}")
def get_message(message_id: int, db: Session = Depends(get_db)):
    message = db.query(Message).filter(Message.id == message_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"data": message}

@router.put("/messages/{message_id}")
def update_message_status(message_id: int, status: str, db: Session = Depends(get_db)):
    message = db.query(Message).filter(Message.id == message_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    message.status = status
    db.commit()
    return {"message": "Message status updated", "data": message}

@router.delete("/messages/{message_id}")
def delete_message(message_id: int, db: Session = Depends(get_db)):
    message = db.query(Message).filter(Message.id == message_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    db.delete(message)
    db.commit()
    return {"message": "Message deleted"}