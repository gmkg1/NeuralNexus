import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from collections import defaultdict

import random

data = {
    "text": [
        # **Anger (500)**
        *["I hate this.", "I am so mad.", "I can't stand this.", "You always make me angry.", 
          "This makes me furious!", "I feel so betrayed!", "I can't forgive this!", 
          "You are making me crazy!", "I hate being ignored!", "You lied to me again!", 
          "This is so frustrating!", "I feel like screaming!", "This is the worst day!", 
          "Why do you never listen?", "I am about to explode!"] * 33 + ["I feel angry!"],
        
        # **Joy (500)**
        *["I love this!", "This makes me so happy!", "I feel amazing!", "I am so excited!", 
          "You are the best!", "I love spending time with you!", "I feel so grateful!", 
          "This is the best day ever!", "I can't stop smiling!", "Life is beautiful!", 
          "I enjoy every moment!", "I am in a great mood!", "i like her", 
          "This is wonderful!", "I feel cheerful!"] * 33 + ["Happiness is the best feeling!"],
        
        # **Sadness (500)**
        *["I feel so sad.", "Nothing is going right.", "I just want to cry.", "I miss you so much.", 
          "Life is so hard.", "I feel heartbroken.", "I feel empty inside.", 
          "I can't stop feeling sad.", "This is so painful.", "Everything hurts.", 
          "I feel lost and hopeless.", "I feel like crying.", "No one understands me.", 
          "I feel so weak.", "Tears keep coming to my eyes."] * 33 + ["Everything makes me sad."],
        
        # **Fear (500)**
        *["I am so scared.", "I feel afraid.", "I don't know what will happen next.", 
          "I can't stop shaking.", "This is terrifying.", "I feel unsafe.", 
          "I don't want to be alone.", "I am so nervous!", "I feel trapped.", 
          "This is making me anxious.", "I can't sleep, I'm too scared.", 
          "I feel frozen in fear.", "I feel panic inside me.", "I want to run away!", 
          "I feel like something bad is coming."] * 33 + ["My stomach hurts from fear."],
        
        # **Disgust (500)**
        *["This is so disgusting.", "I feel sick looking at this.", "This is so gross!", 
          "I can't stand this smell!", "This is the worst thing ever.", "I want to throw up.", 
          "This makes me feel so uncomfortable.", "This is nasty!", "I want to leave now.", 
          "This is making my stomach turn.", "I can't even look at it!", "This is horrible!", 
          "I don't want to touch that!", "I feel dirty just being here.", "I feel bad seeing this."] * 33 + ["I am completely disgusted."],
        
        # **Love (500)**
        *["I love you.", "You mean everything to me.", "I care about you so much.", 
          "You make my heart happy.", "I enjoy every moment with you.", "I can't imagine life without you.", 
          "You are the most important person to me.", "I feel safe with you.", 
          "You bring light into my life.", "I feel lucky to have you.", "You make my life better.", 
          "You are my world.", "I feel complete with you.", "You make my heart race.", 
          "I want to be with you forever."] * 33 + ["I will always be by your side."]
    ],
    "emotions": (
        ["Anger"] * 500 + 
        ["Joy"] * 500 + 
        ["Sadness"] * 500 + 
        ["Fear"] * 500 + 
        ["Disgust"] * 500 + 
        ["Love"] * 500
    )
}

# Shuffle the data for randomness
combined = list(zip(data["text"], data["emotions"]))
random.shuffle(combined)
data["text"], data["emotions"] = zip(*combined)

min_length = min(len(data["text"]), len(data["emotions"]))
train_data = {
    "text": data["text"][:min_length],
    "emotions": data["emotions"][:min_length]
}
df = pd.DataFrame(train_data)

vectorizer = CountVectorizer()
x=vectorizer.fit_transform(df["text"])
y=df["emotions"]
model = LogisticRegression()
model.fit(x,y)
pickle.dump(model,open("emotion_model.pkl","wb"))
pickle.dump(vectorizer,open("vectorizer.pkl","wb"))
print("model saved")


