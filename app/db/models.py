from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id                 = Column(Integer, primary_key=True, index=True)
    model_used         = Column(String, nullable=True)
    budget             = Column(Float, nullable=True)
    runtime            = Column(Float, nullable=True)
    popularity         = Column(Float, nullable=True)
    vote_average       = Column(Float, nullable=True)
    language_count     = Column(Integer, nullable=True)
    season             = Column(String, nullable=True)
    language           = Column(String, nullable=True)
    genres             = Column(String, nullable=True)
    predicted_revenue  = Column(Float, nullable=True)
    created_at         = Column(DateTime(timezone=True), server_default=func.now())