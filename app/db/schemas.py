from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MovieInput(BaseModel):
    model_type      : str = "random_forest"
    budget          : float
    runtime         : float
    popularity      : float
    vote_average    : float
    language_count  : int = 1
    season          : str = "Summer"
    language        : str = "en"
    action          : int = 0
    adventure       : int = 0
    animation       : int = 0
    comedy          : int = 0
    crime           : int = 0
    documentary     : int = 0
    drama           : int = 0
    family          : int = 0
    fantasy         : int = 0
    horror          : int = 0
    romance         : int = 0
    science_fiction : int = 0


class PredictionOut(BaseModel):
    id : int
    model_used : str
    budget              : float
    runtime             : float
    popularity          : float
    vote_average        : float
    predicted_revenue   : float
    created_at          : datetime

    class Config:
        from_attributes = True