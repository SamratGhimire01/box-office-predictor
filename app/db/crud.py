from sqlalchemy.orm import Session
from app.db.models import Prediction

def save_prediction(db:Session,data:dict):
    prediction = Prediction(**data)
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction

def get_all_predictions(db:Session):
    return db.query(Prediction).order_by(Prediction.created_at.desc()).all()
