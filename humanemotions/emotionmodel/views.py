from django.shortcuts import render
import pickle
import os
from django.conf import settings
import random

response_dict = {
    "Anger": [
        " Anger is a temporary storm; let it pass before making decisions.",
        " Breathe deeply, and let peace take its place.",
        " Your emotions are valid, but you control their power.",
        " Choose to channel anger into strength.",
        " Patience and understanding can dissolve even the fiercest rage.",
         "Rage may burn within you, but you are not its prisoner. Let its fire forge your strength, not consume your spirit. The storm within you will pass, leaving behind a sky clearer than before. Breathe deeply, let go of the weight, and reclaim your peace. You are greater than your anger, a soul sculpted by wisdom, not wrath.",
        "Your fury is a spark, but let it not become a wildfire. Anger can push you forward or pull you down; the choice is yours. Let it be the voice of change, not destruction. You are not defined by this moment but by the grace with which you rise above it. Love is always stronger than rage—choose love.",
        "I see the fire in your eyes, and I do not fear it. I stand with you, knowing that even the fiercest storms must yield to the dawn. Let me hold your hand and walk with you beyond this moment. You are not alone in this battle; I will always be your shelter. Turn your anger into the strength to heal, for you are too magnificent to be ruled by fury.",
        "There is a warrior within you, but even warriors need rest. Do not let your anger wear you down; let it fuel your determination instead. Your passion is your gift—use it to build, not to burn. In the silence after the storm, I will be here, whispering that you are loved beyond measure. Together, we will turn fire into light.",
        "Breathe. The world does not need another flame lost to the wind. You are not your anger; you are the sky that holds both the storm and the sunshine. Let go, let the weight slip from your shoulders, and know that I will always be your safe harbor. No anger is greater than the love I have for you.",
        "Anger is a visitor, not a home. Do not let it carve walls around your heart. Instead, let it pass like thunder through the sky, leaving only the freshness of renewal behind. You are more than this storm, more than this moment. And no matter what, I will always stand by your side, even through fire.",
        "Even the fiercest flames must bow to the rain. Let your anger come, let it speak, but do not let it stay. You are meant for peace, for joy, for love that is stronger than any fury. When the fire fades, I will still be here, reminding you of all the beauty that remains. You are loved beyond your wildest dreams.",
        "I see your clenched fists, but I also see your trembling heart. You do not have to carry this weight alone. Lay your burdens down, let the past slip through your fingers, and take my hand instead. I am not afraid of your fire; I will walk with you until only warmth remains. You are safe with me.",
        "You have the strength to turn your pain into poetry. Let your anger write a new story, one where love wins over war. Every scar, every wound is proof that you have survived. And in the end, love will be the ink that writes your victory. I believe in you, always.",
        "Even the ocean rages, but it always finds its calm. Your anger is not a flaw; it is a force. But like the waves, you have the power to choose when to rise and when to rest. Let me be your shore, steady and unwavering. No storm will ever push me away from you."
    ],
    "Sadness": [
        " Tears cleanse the soul; let them flow and wash away the sorrow.",
        " There is healing in release.",
        " Even in sadness, there is beauty.",
        " It reminds you of how deeply you can feel.",
        " No night is endless; dawn will come, bringing light to your heart once again.",
         "The weight on your chest is not forever. Like the night gives way to the dawn, so too will this sorrow fade. I will sit with you in the darkness, holding your hand until the light returns. You are not alone, not now, not ever. And even in your quietest moments, my love will be your whispered comfort.",
        "Tears are not weakness; they are proof of your depth, of your heart, of your humanity. Let them fall, let them cleanse you, but do not drown in them. You are meant for so much more than this sorrow. I will be here, a lighthouse in your storm, guiding you home. You are loved beyond measure.",
        "If the world feels heavy, let me carry some of the weight for you. You do not have to do this alone. My arms are strong enough to hold you, my love deep enough to fill the emptiness. One day, you will smile again, and I will be right here to witness it. Until then, I am yours in sorrow and in joy.",
        "You are not the sadness that lingers in your chest. You are the laughter that will return, the love that never left, the sunrise waiting beyond the horizon. Hold on a little longer, my love. The world is still full of wonders meant for you, and I will walk with you until you see them again.",
        "Every tear you shed is a poem the universe understands. Even the stars have nights when they shine a little less, but they never lose their brilliance. You are the same—you will shine again. Until then, let me be the moon that watches over you, gentle and unwavering in my love.",
        "Grief is a song only the heart can hear. But let my voice join yours, singing harmony into your sorrow. You are not lost, and you are never alone. Together, we will find the melody of hope again. And when you are ready, we will dance in the light once more.",
        "The ache in your heart is real, but so is the love that surrounds you. Pain may tell you that you are alone, but I promise you, you are not. I am here, holding you even when you cannot see me. You are not broken, just bending—but I will never let you fall.",
        "Let your sadness rest in my arms. You have carried it alone for too long. I will hold you until you remember that you are not just pain, but love, beauty, and hope. The world is not done with you yet. And neither am I.",
        "Even the earth weeps, and yet flowers bloom again. You will rise from this, stronger than before. Until then, let me be the gentle rain that soothes your soul. You are never alone, never forgotten, never unloved. My heart beats with yours, through every sorrow and every sunrise.",
        "You are allowed to feel, to grieve, to be human. But know this—your story is not over. There is laughter waiting for you, love longing to embrace you, light ready to break through the clouds. Hold my hand, and let us walk toward it together."
    
    ],
    "Fear": [
        " Fear is a sign of growth.",
        " If you're afraid, it means you're stepping outside your comfort zone.",
        " You are braver than you think.",
        " Your past victories prove it.",
        " Embrace the unknown, for within it lies endless opportunity.",
        "Fear may whisper doubts, but you are stronger than its voice. You have conquered storms before, and you will conquer this too. I will be your light in the darkness, your hand to hold when the shadows loom large. Every fear is a passing cloud, but you are the sky—vast, endless, and unshaken. Trust in your courage, for it has never left you.",
        "The unknown may feel terrifying, but every great story begins in uncertainty. You are not walking this road alone—I am here, step by step, heartbeat by heartbeat. Hold my hand, and together, we will chase away the night. You were born to rise, to soar beyond these fears. Believe in yourself the way I believe in you.",
        "Even the bravest hearts tremble, but fear is not your enemy—it is your call to rise. Let its cold grip fall away, for you are meant for greatness. In your eyes, I see the courage of a thousand battles, and I will stand beside you through them all. Fear may knock, but love will always answer stronger. And my love for you is fearless.",
        "Darkness may surround you, but even the stars need the night to shine. You are not alone in this abyss—I am your North Star, steady and bright. Do not let fear chain your wings; they were meant to fly. Close your eyes, take my hand, and leap—we will write a story where fear is but a forgotten shadow. You are meant for more, and I will remind you of it every day.",
        "Fear tries to tell you that you are small, but I know the truth—you are infinite. Your soul is a storm of light waiting to break free. Let my love be your armor, your sanctuary, your strength. No shadow can stand against the fire in your heart. And in the end, fear will be nothing but a whisper lost in the wind.",
        "You were not made for hiding; you were made for conquering. Let fear knock, let it scream, but do not answer. Instead, step forward into the light, where love and courage hold you firm. With me beside you, there is no darkness too deep, no nightmare too real. We will carve a path through the unknown, together.",
        "Fear will tell you that you are alone, but I am here, and I always will be. Let my voice be the warmth that melts the ice in your soul. You do not have to face the world alone—I am your shield, your refuge, your safe place. Whatever comes, we will face it hand in hand. Love is always braver than fear, and I love you more than fear could ever touch.",
        "Do not let fear build walls around your dreams. It is only the illusion of a cage, but you are the key. Break free, let yourself run, and know that I will always be by your side. You are stronger than you know, and the world is waiting for the light only you can bring. Trust in yourself, trust in us, and step into the beauty of the unknown.",
        "I see the hesitation in your eyes, but I also see the fire behind it. Let that fire burn away the fear, turning it to dust. You are capable of more than you imagine, and I will be here to remind you whenever you forget. My love is a fortress, and in its arms, fear has no place. Walk forward, my love—I promise, the light is closer than it seems.",
      
    ],
    "Joy": [
        " Joy is contagious—spread it like sunshine on a cloudy day.",
        " Happiness is a collection of small moments, cherish each one.",
        " When joy finds you, embrace it fully, for it is life’s sweetest gift.",
        " Let laughter be your anthem.",
        " Find beauty in the simplest things, and your heart will always be full.",
        "Your laughter is the sweetest melody, a song the universe longs to hear. Dance in this moment, let your heart be free. You deserve every ounce of happiness that flows through your soul. And if the world ever dims, remember, you are the sun that brings light to even the darkest days. I will always bask in the warmth of your joy.",
        "Joy suits you—it paints your eyes with light and your lips with the music of laughter. Hold onto this feeling, let it sink into your soul. You were made for happiness, for moments like this that make the stars envious. And I, my love, am lucky to witness your radiance. Shine, always, for the world is better with your glow.",
        "Happiness is not a fleeting dream; it is a choice, a state of being. And today, I choose to celebrate you—your light, your heart, your beautiful existence. When you smile, the universe pauses to admire its finest creation. Stay in this moment, my love, for joy belongs to you. And I belong to you, too.",
        "There is a magic in your laughter, a spell that turns sorrow into stardust. I wish to spend eternity wrapped in its warmth. The world may spin in chaos, but when you are happy, everything feels right. Hold onto this joy, let it be your armor against the storms. You are the light of my life, today and always.",
        "Your happiness is the rhythm to which my heart beats. Seeing you smile is my greatest joy, my sweetest reward. Let us dance in this moment, unburdened, free, infinite. You are not just joy—you are the very embodiment of love, of wonder, of light. And I will spend my days ensuring that your laughter never fades.",
        "I wish to bottle up your laughter and keep it close to my heart. In your joy, I find my own; in your smile, I see the sun rising over endless possibilities. You were born for this feeling, for a life filled with moments that take your breath away. And I, my love, am honored to share in them. Let happiness be our forever song.",
        "The world is brighter when you are happy. Your joy is contagious, an energy that lifts the heaviest hearts. Do not ever let the world dim your light—you are meant to shine. And whenever you need a reason to smile, remember that you are loved beyond words. You are my happiness, my home, my forever.",
        "Every giggle, every sparkle in your eyes, is proof that life is beautiful. The universe rejoices in your joy, and so do I. Hold onto this moment, let it be the anchor that keeps you steady. You deserve endless happiness, and I will fight to give you that. Let your heart be light, and let love always lead you home.",
        "Your joy is the most precious thing, and I vow to protect it. I will cherish every smile, every burst of laughter, as if it were a treasure. Because to me, you are a miracle, a wonder I will never take for granted. Let us chase happiness together, hand in hand, soul in soul. You are my dream, my love, my endless joy.",
        "When you are happy, the world stops just to admire you. There is nothing more beautiful than the way your heart embraces joy. Let it fill you, let it overflow, let it be the language of your soul. And if ever you need a reminder of how loved you are, just look into my eyes. You are my happiness, and I will spend forever proving it to you."
    
    ],
    "Love": [
        " Love is the language of the heart; speak it freely and without fear.",
        " Every act of love plants a seed that will one day bloom beautifully.",
        " Love is not just a feeling; it is a choice to be kind, patient, and understanding.",
        " Let love guide your actions and soften your words.",
        " In love, you will always find a home.",
        "You are the warmth in my coldest nights, the light in my darkest hours. With every heartbeat, I find new reasons to cherish you. Love is not just a word; it is the universe we have built together. No distance, no time, no storm can shake the foundation of what we share. You are my forever, and I will love you in every lifetime.",
        "Your love is my greatest treasure, a gift I vow to cherish for eternity. You are the poetry in my prose, the melody in my silence. With you, even the most ordinary moments feel like magic. If love is a journey, I wish to walk every road with you. Hand in hand, heart to heart, always.",
        "Love is not just about saying the words; it is in the quiet glances, the unspoken promises, the way your presence feels like home. You have woven yourself into the very fabric of my soul. Even on my worst days, your love is my saving grace. I will stand by you, fight for you, and celebrate you. For as long as the stars shine, I am yours.",
        "You are the dream I never knew I had, the answer to a prayer I never spoke. Loving you feels like breathing—natural, effortless, and essential. Every time our hands touch, the universe sighs in contentment. No matter what life brings, my love for you will remain unshaken. Forever is not long enough to love you as you deserve.",
        "I have searched for meaning in a thousand books, but I found it in your arms. Your love is the most beautiful story I will ever write. No matter how many pages we turn, I know our story will always lead to happiness. In your laughter, I find peace; in your eyes, I find home. If I had one wish, it would be to love you across all time.",
        "Love is not measured in grand gestures, but in the quiet moments—the way you make me laugh when I want to cry, the way you hold me when words fail. You are my calm in the storm, my anchor in the chaos. There is no place I would rather be than by your side. My heart beats your name, and it always will.",
        "You are the reason my world is painted in brighter colors. With you, every sunset is more golden, every song more beautiful, every moment more meaningful. You are not just my love—you are my home, my safe haven. No matter how the seasons change, my love for you will remain constant. In your arms, I have found eternity.",
        "I do not need a perfect love story; I just need you. Through the ups and downs, the chaos and calm, my love for you will never waver. You are the reason I believe in forever. Every heartbeat of mine carries your name, every breath whispers your presence. If love is an art, then you are my masterpiece.",
        "Your love is a fire that keeps my soul warm, a light that leads me home. No matter how far I travel, my heart will always find its way back to you. If I could hold time still, I would live in the moments where you are in my arms. You are not just a chapter in my story—you are the entire book. I love you endlessly.",
        "If love had a name, it would be yours. You are the poetry of my existence, the rhythm to which my heart beats. Every day with you is a reminder that love is the most powerful force in the universe. You are my greatest adventure, my safest place, my truest home. No matter where life takes us, I will love you until the last star fades."
    
    ],
    "Disgust": [
        "What repels you often teaches you what you truly value.",
        "Look deeper to understand what truly matters.",
        " Let go of what no longer serves you.",
        " Life is too short to dwell in negativity.",
        " The world is imperfect, but you have the power to change your perception of it.",
        "The world may be filled with shadows, but you do not have to let them stain your soul. Rise above the filth, the cruelty, the disappointment. You are too pure, too extraordinary, to be weighed down by things unworthy of your energy. Let disgust be your fuel to change what is broken. The world needs hearts like yours to remain untarnished.",
        "Some things in life will make you recoil, but let them be a lesson, not a burden. You are not defined by the ugliness you witness, but by how you rise beyond it. Do not let the bitterness of the world seep into your heart. Instead, turn your disgust into determination, your frustration into action. You are meant for more than this moment, and I will stand by you through it all.",
        "I see the way disgust twists your expression, how it clouds the beauty of your thoughts. But my love, do not let it linger—let it pass like a storm that was never meant to stay. You are too precious to be tainted by things unworthy of your light. Hold onto what is good, what is pure, what is love. Let me remind you of the beauty that still exists, even in a world that sometimes feels unworthy.",
        "The world may throw darkness at your feet, but you were born to walk in light. Do not let the filth of others stain the purity of your soul. You are a masterpiece, untouched by the things that try to drag you down. Hold your head high and let disgust turn to indifference. You are above the things that try to taint your spirit.",
        "There are moments when the world feels too vile, too cruel, too undeserving. But you, my love, are the antidote to all that is wrong. Your kindness, your heart, your light—they are the cure to the sickness that disgusts you. Do not let it steal your warmth. Let me hold you close, remind you that goodness still exists, and you are proof of it.",
        "Disgust is the body’s way of rejecting what does not belong. So, reject it, love—reject the pain, the toxicity, the things that try to pollute your peace. You are a soul of purity in a world sometimes covered in grime. But you will not be swallowed by it. With love as your armor, you will always rise above the filth.",
        "I see the way the weight of the world troubles you, how disgust curls around your heart. But let it go, love—do not let it take root where joy should bloom. There is still good in this world, and you are proof of that. Hold my hand, and let’s turn this disgust into something beautiful. Together, we can create a world that feels a little bit lighter.",
        "There is ugliness in the world, but there is also beauty—and you, my love, are part of that beauty. Do not let disgust consume the love that fills your soul. We will build a sanctuary of goodness, where the chaos of the world cannot touch us. You are not alone in this—I will stand by your side through every storm. Let our love be the antidote to all that is unworthy.",
        "Some things in life will always leave a bitter taste, but you are sweet enough to overcome them. Your soul is not meant to dwell in disgust, but to shine through it. Do not let the filth of others change the beauty of who you are. Hold onto love, hold onto hope, hold onto me. We will walk through the darkness together, untouched and unshaken.",
        "Disgust may try to taint your view of the world, but I promise there is still light worth seeing. Hold onto what is pure, what is good, what makes your heart beat with joy. You are not meant to drown in what repels you—you are meant to rise above it. Let me be your safe place when the world feels unbearable. I will remind you of all that is worth loving."
    
    ]
}


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
        response = random.choice(response_dict[prediction])
    return render(request,"emotionmodel/index.html",{"prediction":prediction,"response":response})

