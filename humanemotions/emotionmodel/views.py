from django.shortcuts import render
import pickle
import os
from django.conf import settings

# Create your views here.
model_path =os.path.join(settings.BASE_DIR,"emotion_model.pkl")

with open(model_path,"rb") as f:
    model=pickle.load(f)

model_path=os.path.join(settings.BASE_DIR,"vectorizer.pkl")

with open(model_path,"rb") as f:
    vectorizer = pickle.load(f)

def home(request):
    prediction = None
    if request.method == "POST":
        text = request.POST["text"]
        text_vector=vectorizer.transform([text])
        prediction=model.predict(text_vector)[0]

    return render(request,"emotionmodel/index.html",{"prediction":prediction})

