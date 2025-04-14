import random

def main():
    name = "Aryan Singh"
    admission_no = "21JE1234"
    print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_no}) 🔮")

    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").lower()

    fortunes = {
        "happy": [
            f"Great things await you, {name}! Keep smiling.💛",
            "Your energy is contagious — use it wisely!💛",
        ],
        "sad": [
            f"After rain comes the rainbow. Better days are ahead.Keep hope {name}🩵",
            "Your strength is greater than you think.🩵",
        ],
        "neutral": [
            "Stay open to opportunities, surprises are coming.🧡",
            "Sometimes calm is the best place for new ideas.🧡",
        ],
        "stressed": [
            f"Breathe in peace, breathe out stress. Clarity is coming.Stay calm {name}❤️",
            "You’ve got this. One step at a time.❤️",
        ]
    }

    if mood in fortunes:
        print("✨ Your fortune:", random.choice(fortunes[mood]), "✨")
    else:
        print("❓ Sorry, I don't recognize that mood. Try happy, sad, neutral, or stressed.")

if __name__ == "__main__":
    main()
