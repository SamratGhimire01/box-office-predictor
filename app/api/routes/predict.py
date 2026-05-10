from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.schemas import MovieInput,PredictionOut
from app.db import crud
from ml.predict import predict_linear_regression,predict_random_forest
import json

router = APIRouter()

def build_features(movie: MovieInput):
    # Base features
    features={
        'budget'         : movie.budget,
        'runtime'        : movie.runtime,
        'popularity'     : movie.popularity,
        'vote_average'   : movie.vote_average,
        'Language_count' : movie.language_count,
    }
    
    # Season one-hot
    for s in ['Summer','Winter','Fall']:
        features[f'season_{s}'] = 1 if movie.season == s else 0

    # Language one-hot  
    for l in ['en', 'es', 'fr', 'hi', 'pt', 'ru', 'tr']:
        features[f"lang_{l}"] = 1 if movie.language == l else 0 
        
    features['lang_other'] = 1 if movie.language not in ['en', 'es', 'fr', 'hi', 'pt', 'ru', 'tr'] else 0
    
    # Genres
    features['Action']          = movie.action
    features['Adventure']       = movie.adventure
    features['Animation']       = movie.animation
    features['Comedy']          = movie.comedy
    features['Crime']           = movie.crime
    features['Documentary']     = movie.documentary
    features['Drama']           = movie.drama
    features['Family']          = movie.family
    features['Fantasy']         = movie.fantasy
    features['Horror']          = movie.horror
    features['Romance']         = movie.romance
    features['Science Fiction'] = movie.science_fiction
    
    return features

@router.post("/predict")
def predict(movie:MovieInput, db:Session = Depends(get_db)):
    features = build_features(movie)
    
    if movie.model_type == "linear_regression":
        revenue = predict_linear_regression(features)
    else:
        revenue = predict_random_forest(features)
    
    # Saving in database
    genres_selected = []
    for g in ['action','adventure','animation','comedy','crime',
              'documentary','drama','family','fantasy','horror',
              'romance','science_fiction']:
        if getattr(movie, g)==1:
            genres_selected.append(g.replace("_"," ").title())
            
    crud.save_prediction(db,{
        'model_used' : movie.model_type,
        "budget"            : movie.budget,
        "runtime"           : movie.runtime,
        "popularity"        : movie.popularity,
        "vote_average"      : movie.vote_average,
        "language_count"    : movie.language_count,
        "season"            : movie.season,
        "language"          : movie.language,
        "genres"            : ", ".join(genres_selected),
        "predicted_revenue" : revenue,
    })
    
    return {
        "model_used" : movie.model_type,
        "predicted_revenue_usd" : round(revenue,2),
        "predicted_revenue_fmt" : f"${revenue:,.2f}"
    }
    
@router.get("/history")
def get_history(db:Session = Depends(get_db)):
    predictions = crud.get_all_predictions(db)
    return predictions