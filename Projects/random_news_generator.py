import random
import time

fake_news_words = {
    "buzzwords": [
        "Spontaneous yeti uprising in Thamel",
        "Mysterious momo shortage crisis",
        "5G dal bhat conspiracy",
        "AI-powered sadhu predicts stock market",
        "Temple monkey runs for mayor",
        "Himalayan yeti caught using TikTok",
        "National load-shedding dance challenge",
        "Viral video of talking cow in Patan",
        "Government bans chiya to prevent revolution",
        "Kathmandu air declared new superfood"
    ],

    "characters": [
        "The TikTok lama of Boudha",
        "Tempo driver with secret PhD",
        "Momo queen with illegal chili recipe",
        "Swayambhunath monkey with a VPN",
        "Retired Gurkha who can split atoms",
        "Bhaktapur’s time-traveling potter",
        "Pokhara’s UFO tour guide",
        "The Kumari’s secret gaming channel",
        "Nepali politician who actually works",
        "Everest climber who hates heights"
    ],

    "places": [
        "Secret basement of Nepal Telecom",
        "Yeti nightclub in Langtang",
        "The forbidden 5th floor of Bhatbhateni",
        "Pokhara’s underground alien embassy",
        "Annapurna’s lost Starbucks",
        "Tinkune’s sentient traffic jam",
        "The real Singha Durbar (it’s in Dharan)",
        "Pashupatinath’s WiFi hotspot heaven",
        "Chitwan’s ninja rhino training camp",
        "The backroom of every Nepali cyber cafe"
    ],

    "inventions": [
        "Solar-powered khukuri charger",
        "Selfie stick for group photos with yetis",
        "Portable load-shedding generator",
        "AI that translates politician lies to truth",
        "Dal bhat protein shake",
        "NFTs of Kathmandu dust storms",
        "Smartphone app to find petrol queues",
        "Biometric thali measurement system",
        "Blockchain-based citizenship lottery",
        "TikTok filter that makes you look like a Kumari"
    ],

    "headlines": [
        "BREAKING: Yeti demands VPN access",
        "SHOCKING: Momo prices tied to bitcoin",
        "GOVERNMENT DENIES: Cows are better at traffic management",
        "STUDY PROVES: 90% of Nepalis are 10% through a government form",
        "EXPOSED: Tempo drivers control stock market",
        "LEAKED: Real reason Ncell speeds are slow (aliens)",
        "CONFIRMED: Pokhara is actually Atlantis",
        "URGENT: National anthem replaced by TikTok remix",
        "SCANDAL: Everest permits sold as NFTs",
        "JUST IN: Nepal declares itself Mars for tourism boost"
    ]
}

def generate_fake_news():
    buzzword=random.choice(fake_news_words["buzzwords"])
    character=random.choice(fake_news_words["characters"])
    place=random.choice(fake_news_words["places"])
    invention=random.choice(fake_news_words["inventions"])
    headline=random.choice(fake_news_words["headlines"])

    return f"\n{headline} {character} using a {invention} in {place} during a {buzzword}."

print("🎉 Welcome to the Nepali Fake News Generator!\n")
while True:
    print(generate_fake_news())
    time.sleep(1)
    user_response=input("\nDo you want to continue? (Yes/No)\t").strip().lower()
    

    if user_response == 'yes':
        continue
    elif user_response =='no':
        print("\n👋 Thanks for using the Fake News Generator!")
        break
    else:
        print("❌ Invalid response.Please visit us again.")
        
        break


# now we need to save these joke in  a file using the file handling concept