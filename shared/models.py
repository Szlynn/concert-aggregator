from sqlalchemy import Column, Integer, String, Date, Time, Text, DateTime
from datetime import datetime
from .database import Base

class ConcertEvent(Base):
    __tablename__ = "concert_events"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    event_date = Column(Date, nullable=False)
    venue = Column(String(255), nullable=False)
    source = Column(String(100), nullable=False)
    event_url = Column(Text, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

