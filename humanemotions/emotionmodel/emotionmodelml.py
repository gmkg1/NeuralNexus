import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

data ={ 
    "text":["i love you","i am happy","i am sad","i am angry","thank you","i hate you"],
    "emotions":["happy","happy","sad","anger","happy","anger"]
}
df = pd.DataFrame(data)

vectorizer = CountVectorizer()
x=vectorizer(df["text"])
y=df["emotions"]
model = LogisticRegression()
model.fit(x,y)
pickle.dump(model,open("emotion_model.pkl","wb"))
pickle.dump(vectorizer,open("vectorizer.pkl","wb"))
print("model saved")


