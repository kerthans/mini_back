
# models/message.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    receiver_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    content = Column(String(1000), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    status = Column(String(20), default='unread')

    sender = relationship('User', foreign_keys=[sender_id])
    receiver = relationship('User', foreign_keys=[receiver_id])












# models/message.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String)
    timestamp = Column(DateTime)
    status = Column(String, default='unread')

    sender = relationship('User', foreign_keys=[sender_id])
    receiver = relationship('User', foreign_keys=[receiver_id])
>>>>>>> 3165d80654ce0ef4397cf5fc1618f4323d7c4000
