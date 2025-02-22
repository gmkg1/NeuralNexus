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
          "I am so frustrated right now, and I can’t calm down",

"Nothing ever goes my way, and I’m sick of it",

"I hate how people always take advantage of me",

"I can't believe they did that to me, it's completely unfair",

"I'm tired of being disrespected and treated like I don’t matter",

"I just want to scream because everything is going wrong",

"Why does no one ever listen to what I have to say?",

"I’m done being nice to people who don’t appreciate me",

"I have had enough of people taking me for granted",

"It makes me so angry when people lie to me",

"I can't stand it when people interrupt me and don’t let me speak",

"Every little thing is irritating me right now",

"I’m tired of pretending that everything is fine when it’s not",

"I feel like I’m about to explode from all this frustration",

"I’m so mad at myself for making the same mistakes again",

"People always let me down, and I’m getting sick of it",

"I don’t understand why people can’t just be honest with me",

"It’s infuriating when people don’t respect my time",

"I hate when people make decisions for me without asking",

"I’m so fed up with dealing with the same problems over and over again",

"Why do people always test my patience?",

"I can't believe they think they can just walk all over me",

"I'm losing my patience, and I don’t care anymore",

"It’s exhausting to always have to explain myself to people who don’t listen",

"I wish people would stop trying to control my life",

"I can’t tolerate being ignored when I’m clearly speaking",

"I hate being blamed for things that aren’t my fault",

"I'm so irritated by how unfair everything feels",

"I don’t care what anyone thinks—I’m going to do what I want",

"Every time I try to be nice, someone takes advantage of it",

"I'm tired of people assuming they know what’s best for me",

"I hate being told to calm down when I have every right to be upset",

"I can’t take this anymore, I just need to get away",

"I get so annoyed when people don’t take me seriously",

"I feel like no one respects my boundaries, and it makes me furious",

"I hate when people pretend to care but don’t actually listen",

"I don’t understand why people always have to make things difficult",

"I’m beyond frustrated with how unfairly I’m being treated",

"I feel like I have to fight for everything, and I’m exhausted",

"I can’t believe how selfish some people can be",

"I'm so irritated that people think they can get away with anything",

"I hate when people assume they know what I’m feeling",

"I am so angry that I don’t even want to talk about it",

"I can’t stand when people waste my time",

"I’m furious that I keep getting blamed for things I didn’t do",

"I feel completely disrespected, and I won’t tolerate it anymore",

"I hate when people don’t take responsibility for their actions",

"I can’t believe they would betray my trust like that",

"It makes me so mad when people try to manipulate me",

"I don’t want to hear excuses, I just want things to be fair",

        
        # **Joy (500)**
        *["I love this!", "This makes me so happy!", "I feel amazing!", "I am so excited!", 
          "You are the best!", "I love spending time with you!", "I feel so grateful!", 
          "This is the best day ever!", "I can't stop smiling!", "Life is beautiful!", 
          "I enjoy every moment!", "I am in a great mood!", "i like her", 
          "This is wonderful!", "I feel cheerful!"] * 33 + ["Happiness is the best feeling!",],"I feel so happy right now, everything is going great",

"This is the best day I’ve had in a long time",

"I can’t stop smiling because I’m so excited",

"I’m really proud of myself for achieving this",

"I feel so grateful for everything in my life",

"Everything is finally falling into place, and I couldn’t be happier",

"I love spending time with people who make me feel good",

"I feel so energetic and full of life today",

"I’m enjoying every moment of this experience",

"This is exactly what I needed to feel better",

"I feel completely at peace with where I am in life",

"I can’t believe how lucky I am to have such amazing people around me",

"I’m overwhelmed with happiness, and it feels amazing",

"I love the feeling of accomplishing something I worked hard for",

"I’m having such a great time, and I don’t want it to end",

"I feel so refreshed and positive about everything",

"I can’t help but laugh because I’m just so happy",

"This moment is absolutely perfect, and I’m so grateful for it",

"I feel like nothing can bring me down today",

"I woke up feeling so good about everything",

"I love seeing the people around me happy too",

"Life feels so beautiful when you appreciate the little things",

"I finally feel like I’m exactly where I’m supposed to be",

"I’m so excited about the future and what’s coming next",

"I can’t stop thinking about how great things are right now",

"I love the sense of freedom and happiness I feel today",

"I feel completely content with everything in my life",

"This achievement means so much to me, and I couldn’t be prouder",

"I feel so confident and capable of doing anything",

"I’m surrounded by so much positivity, and it’s amazing",

"I love how everything is working out just the way I hoped",

"I feel so lighthearted and carefree right now",

"I can’t believe how wonderful today has been",

"I feel truly happy in this moment, and I want to hold onto it",

"I love how simple things can bring so much joy",

"This is one of those days I will always remember",

"I finally feel like all my hard work has paid off",

"I feel so loved and appreciated, and it means the world to me",

"I’m so proud of how far I’ve come in life",

"I love this feeling of excitement and possibility",

"I feel like I’m on top of the world right now",

"I can’t wait to share this happiness with everyone around me",

"I feel so lucky to be experiencing this moment",

"This is exactly what I needed to brighten my day",

"I’m so thankful for everything I have in my life",

"I feel like dancing because I’m so happy",

"Everything feels so perfect right now, and I’m loving it",

"I finally feel like I’m truly enjoying life to the fullest",

"This happiness feels so pure and real, and I never want it to end",

"I can’t wait to wake up tomorrow and keep this joy going",
          
        
        # **Sadness (500)**
        *["I feel so sad.", "Nothing is going right.", "I just want to cry.", "I miss you so much.", 
          "Life is so hard.", "I feel heartbroken.", "I feel empty inside.", 
          "I can't stop feeling sad.", "This is so painful.", "Everything hurts.", 
          "I feel lost and hopeless.", "I feel like crying.", "No one understands me.", 
          "I feel so weak.", "Tears keep coming to my eyes."] * 33 + ["Everything makes me sad."],
          "I feel empty inside, and nothing seems to help",

"Today has been really hard, and I don't know how to cope",

"I just want to be alone and not talk to anyone",

"Nothing excites me anymore, and I have no motivation",

"I keep thinking about everything that has gone wrong in my life",

"It hurts to know that I am not important to the people I care about",

"I feel like crying, but I don’t even have the energy for that",

"No matter what I do, I feel like I’m not good enough",

"I feel disconnected from everything and everyone",

"The things that used to make me happy don’t matter to me anymore",

"I feel like I’m stuck in a cycle of disappointment and pain",

"Everything around me feels dull and meaningless",

"I wish things were different, but I don’t know how to change them",

"I keep replaying bad memories in my head and can’t move forward",

"I feel like I’ve lost something important, but I don’t even know what",

"I'm constantly exhausted, even though I haven't done much",

"I feel like I have failed in everything I set out to do",

"Even when I’m with people, I still feel alone",

"I don’t think anyone truly understands how I feel",

"I don’t see the point in trying anymore",

"Sometimes, I just want to disappear so I don't have to feel this way",

"I feel like I’ve been carrying this sadness for so long that I don’t know any other way to feel",

"Even when something good happens, I can’t enjoy it",

"I wake up every day feeling like nothing will ever change",

"I feel like I'm drowning in my own thoughts and emotions",

"I want to talk about my feelings, but I don’t think anyone would care",

"People tell me to move on, but I don’t know how",

"My heart feels heavy all the time, and I don’t know why",

"I try to pretend I’m okay, but inside, I feel completely broken",

"I miss the person I used to be before all of this",

"Every time I try to be happy, something brings me back down",

"I don’t think I will ever be truly happy again",

"I feel like I’m constantly disappointing the people around me",

"No matter how hard I try, nothing ever works out for me",

"I feel like my life is passing by, and I have no control over it",

"I can’t stop thinking about all the mistakes I’ve made",

"I feel trapped in my own mind, and I just want a break",

"I don’t know how to ask for help, even though I need it",

"I hate feeling this way, but I can’t stop it",

"Nothing ever goes the way I want it to, and I’m tired of trying",

"I feel like my emotions are too much for anyone to handle",

"I wish I could go back to a time when I wasn’t feeling like this",

"I feel invisible, like nobody really notices me",

"I want to feel better, but I don’t know where to start",

"I feel like I have lost myself and don’t know how to find me again",

"It’s exhausting to pretend that I’m okay when I’m really not",

"I feel like I’m waiting for something to change, but nothing ever does",

"I have so many things I want to say, but I can’t find the right words",

"I don’t even know why I feel sad, but I can’t shake this feeling",

"I feel like no matter what I do, I’ll never be truly happy",
        
        # **Fear (500)**
        *["I am so scared.", "I feel afraid.", "I don't know what will happen next.", 
          "I can't stop shaking.", "This is terrifying.", "I feel unsafe.", 
          "I don't want to be alone.", "I am so nervous!", "I feel trapped.", 
          "This is making me anxious.", "I can't sleep, I'm too scared.", 
          "I feel frozen in fear.", "I feel panic inside me.", "I want to run away!", 
          "I feel like something bad is coming."] * 33 + ["My stomach hurts from fear."],"I feel like something bad is about to happen",

"My heart is racing, and I can’t seem to calm down",

"I don’t know what to do, and it’s making me panic",

"I feel so uneasy, like I’m being watched",

"I’m too scared to move or say anything",

"I feel trapped, and I don’t know how to get out of this situation",

"My hands are shaking, and I can barely think straight",

"I feel completely powerless and out of control",

"I don’t want to be alone right now, it’s making me nervous",

"I feel like running away, but I don’t know where to go",

"I keep thinking about the worst possible outcome",

"My stomach is in knots, and I can’t stop worrying",

"I feel frozen in place, unable to react",

"I can’t stop imagining everything that could go wrong",

"I feel like something is lurking in the shadows",

"My mind won’t stop racing with anxious thoughts",

"I don’t feel safe here, and I need to leave",

"I feel like I’m suffocating under all this pressure",

"I don’t know who to trust, and that terrifies me",

"I’m scared of making a mistake that I can’t fix",

"I feel like I’m walking on thin ice, and it could break at any moment",

"My body is tense, and I can’t relax no matter what I do",

"I feel like everyone is staring at me, judging me",

"I can’t shake this overwhelming sense of dread",

"I keep hearing noises, and I don’t know where they’re coming from",

"My mind keeps playing out terrifying scenarios",

"I feel like I’m being followed, and it won’t go away",

"I don’t want to close my eyes because I’m afraid of what I’ll see",

"My breath is getting shallow, and I feel dizzy with fear",

"I feel like I’m in danger, but I don’t know why",

"I want to scream, but I feel completely paralyzed",

"My thoughts are spiraling out of control, and I can’t stop them",

"I feel like something terrible is waiting just around the corner",

"I don’t want to be here anymore, it’s making me anxious",

"I feel a deep sense of unease that I can’t explain",

"My instincts are telling me to run, but I don’t know where to go",

"I’m afraid to speak up because I don’t know how people will react",

"I can’t stop my hands from trembling",

"I feel like I’m being pulled into a situation I can’t escape from",

"My chest feels tight, and I can’t seem to catch my breath",

"I don’t want to answer the phone because I’m afraid of what I’ll hear",

"I feel like I’m in way over my head, and there’s no way out",

"I keep having nightmares, and I wake up in a panic",

"I feel like I have no control over what’s happening to me",

"I’m scared of failing and disappointing everyone around me",

"I don’t want to take another step forward because I don’t know what’s ahead",

"My whole body feels tense, and I can’t shake this anxiety",

"I’m afraid that if I let my guard down, something bad will happen",

"I don’t know how to stop feeling this overwhelming sense of fear",

"I feel like I need to hide because I’m not safe",


        
        # **Disgust (500)**
        *["This is so disgusting.", "I feel sick looking at this.", "This is so gross!", 
          "I can't stand this smell!", "This is the worst thing ever.", "I want to throw up.", 
          "This makes me feel so uncomfortable.", "This is nasty!", "I want to leave now.", 
          "This is making my stomach turn.", "I can't even look at it!", "This is horrible!", 
          "I don't want to touch that!", "I feel dirty just being here.", "I feel bad seeing this."] * 33 + ["I am completely disgusted."],
          "I feel completely repulsed by this situation",

"This smell is making me want to gag",

"I can’t even look at it without feeling sick",

"The thought of touching that makes my skin crawl",

"I feel so grossed out right now",

"I can't believe people actually enjoy this",

"The way they behave is absolutely disgusting",

"This place is filthy, and I don’t want to be here",

"I feel nauseous just thinking about it",

"I hate how slimy and dirty this feels",

"This is the most revolting thing I’ve ever seen",

"I feel sick to my stomach just being around this",

"The way they chew with their mouth open is unbearable",

"I don’t even want to be near them, it’s so unpleasant",

"This food looks spoiled, and I can’t eat it",

"I feel like I need to wash my hands immediately",

"The texture of this is making me incredibly uncomfortable",

"The way they treat people is completely repulsive",

"I can't believe I ever liked this, it’s disgusting",

"This tastes horrible, and I want to spit it out",

"I don’t even want to breathe near this, it smells awful",

"Watching that made me feel so uncomfortable",

"This is beyond gross, I need to leave",

"I feel like I need a shower after touching that",

"The way they act makes my skin crawl",

"I feel like vomiting just thinking about it",

"I can't stand the sight of this, it makes me feel sick",

"This room is so dirty, I don’t want to touch anything",

"I feel completely revolted by what just happened",

"The way they treated that person was absolutely vile",

"I can’t believe how unhygienic this is",

"This situation is making my stomach turn",

"I don’t even want to imagine what that must feel like",

"This is the most unhygienic thing I’ve ever seen",

"I feel like I need to scrub my hands after this",

"The way that smells is making me lightheaded",

"I hate the feeling of something sticky on my skin",

"This place is infested with bugs, and I can't stand it",

"The way they talk about others makes me sick",

"This combination of flavors is absolutely repulsive",

"I can’t believe people actually enjoy this, it’s disgusting",

"This feels so unclean, I don’t want to touch it",

"The way they left this place is completely unsanitary",

"This sight is making me physically uncomfortable",

"I feel like my whole body is covered in something dirty",

"I can’t even force myself to deal with this",

"This is so unsettling that I need to look away",

"I feel completely grossed out just being here",

"I can't stand the smell of this, it’s unbearable",

"I need to get away from this before I get sick",
        
        # **Love (500)**
        *["I love you.", "You mean everything to me.", "I care about you so much.", 
          "You make my heart happy.", "I enjoy every moment with you.", "I can't imagine life without you.", 
          "You are the most important person to me.", "I feel safe with you.", 
          "You bring light into my life.", "I feel lucky to have you.", "You make my life better.", 
          "You are my world.", "I feel complete with you.", "You make my heart race.", 
          "I want to be with you forever."] * 33 + ["I will always be by your side."],"I feel so deeply connected to you",

"I can’t imagine my life without you in it",

"I care about you more than I can express",

"Every moment with you feels special",

"I feel completely safe and understood when I’m with you",

"I love the way you make me feel",

"I feel an unbreakable bond between us",

"You mean more to me than words can say",

"I appreciate everything you do for me",

"I feel like I can be myself when I’m with you",

"I trust you with all my heart",

"I just want to see you happy",

"You are the best thing that has ever happened to me",

"I love the way you understand me without even trying",

"I feel so lucky to have you in my life",

"My heart feels full when I’m around you",

"I want to support you no matter what happens",

"I love spending time with you, no matter what we’re doing",

"I feel like we are meant to be together",

"I will always be here for you",

"Every time I see you, I feel a sense of warmth and happiness",

"I respect and admire you more than you know",

"You make even the hardest days feel easier",

"I feel completely at peace when I’m with you",

"I can’t stop thinking about you",

"Just knowing that you’re in my life makes everything better",

"I love the way you make me laugh",

"I want to grow and experience life with you",

"You inspire me to be a better person",

"I feel like I can talk to you about anything",

"I cherish every moment we spend together",

"I feel so close to you, even when we’re apart",

"I love the way you look at me",

"I feel so happy just knowing you exist",

"I never want to take you for granted",

"You are my favorite person in the world",

"I feel so proud of you and everything you do",

"I want to be there for you in every way I can",

"I love the way you make me feel special",

"You make my life brighter just by being in it",

"I appreciate every little thing you do for me",

"You are the first person I think of when something good happens",

"I love how comfortable and natural it feels to be with you",

"I want to make you as happy as you make me",

"I feel like we are a perfect match",

"You make even ordinary moments feel magical",

"I can’t wait to see what the future holds for us",

"I feel so grateful to have someone like you in my life",

"You are the reason I believe in love",

"I want to be by your side forever",
    ],
    "emotions": (
        ["Anger"] * 550 + 
        ["Joy"] * 550 + 
        ["Sadness"] * 550 + 
        ["Fear"] * 550 + 
        ["Disgust"] * 550 + 
        ["Love"] * 550
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


