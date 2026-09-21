def safe_int(value):
    """Convert a number-like input to an integer and handle errors gently."""
    try:
        return int(value)
    except ValueError:
        return None


def get_valid_age():
    """Keep asking until the user provides a valid age."""
    while True:
        age_input = input("How old are you? ")
        age = safe_int(age_input)
        if age is not None and age >= 1:
            return age
        print("Please enter a real age greater than 0.")


def get_mood():
    """Let the user select a current mood."""
    moods = {
        "1": "Happy",
        "2": "Calm",
        "3": "Focused",
        "4": "Tired",
        "5": "Excited"
    }

    print("Choose your current mood:")
    for key, value in moods.items():
        print(f"  {key}. {value}")

    while True:
        mood_choice = input("Enter a number: ").strip()
        if mood_choice in moods:
            return moods[mood_choice]
        print("That choice is not valid. Please pick a number from 1 to 5.")


def get_activity():
    """Prompt the user for their favorite activity."""
    activities = [
        "Reading",
        "Gaming",
        "Coding",
        "Drawing",
        "Music",
        "Sports",
        "Studying"
    ]

    print("Pick your favorite activity:")
    for index, activity in enumerate(activities, start=1):
        print(f"  {index}. {activity}")

    while True:
        choice = input("Enter a number: ").strip()
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(activities):
                return activities[index]
        print("Please choose a valid number from the list.")


def calculate_next_birthday(age):
    """Estimate the number of years until the user's next birthday."""
    return 1 if age % 1 == 0 else 0


def build_profile(name, age, mood, activity):
    """Create a short profile summary."""
    if age < 13:
        category = "young explorer"
    elif age < 18:
        category = "growing learner"
    elif age < 30:
        category = "young adult"
    elif age < 60:
        category = "experienced adult"
    else:
        category = "wise mentor"

    return {
        "name": name.title(),
        "age": age,
        "mood": mood,
        "activity": activity,
        "category": category,
        "summary": (
            f"{name.title()} is a {category} who enjoys {activity.lower()} "
            f"and currently feels {mood.lower()}."
        )
    }


def give_recommendation(profile):
    """Offer a simple personalized suggestion based on mood and activity."""
    suggestions = {
        "Happy": "Keep that energy going and share it with someone you care about.",
        "Calm": "Take a peaceful break and reflect on what is going well for you.",
        "Focused": "Use this momentum to finish one important task before taking a break.",
        "Tired": "Try a short reset: stretch, hydrate, and do something easy for a few minutes.",
        "Excited": "Channel that excitement into a project or goal you have been waiting to start."
    }

    activity_hint = {
        "Reading": "Try to pick a book that challenges your thinking in a fun way.",
        "Gaming": "Set a small goal for the next session, like leveling up or mastering a skill.",
        "Coding": "Write one useful feature or fix one bug to keep improving.",
        "Drawing": "Try a new style or draw something inspired by your favorite mood.",
        "Music": "Create a playlist that matches your current energy and focus.",
        "Sports": "Move your body for at least 15 minutes to boost your mood and energy.",
        "Studying": "Break your work into short tasks so it feels more manageable."
    }

    return (
        f"Recommendation: {suggestions[profile['mood']]} "
        f"{activity_hint[profile['activity']] }"
    )


def print_menu():
    """Display the system menu."""
    print("\nMini System Menu")
    print("1. View profile")
    print("2. Change mood")
    print("3. Change activity")
    print("4. Get recommendation")
    print("5. Exit")


def main():
    """Run the interactive mini system."""
    print("Welcome to the Personal Mini System!")
    print("This tool helps you build a simple profile and get thoughtful suggestions.")

    name = input("What is your name? ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("What is your name? ").strip()

    age = get_valid_age()
    mood = get_mood()
    activity = get_activity()
    profile = build_profile(name, age, mood, activity)

    print("\nProfile created successfully!")
    print(profile["summary"])

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print(f"\nName: {profile['name']}")
            print(f"Age: {profile['age']}")
            print(f"Mood: {profile['mood']}")
            print(f"Favorite activity: {profile['activity']}")
            print(f"Profile type: {profile['category']}")

        elif choice == "2":
            profile["mood"] = get_mood()
            print(f"Your mood was updated to {profile['mood']}.")

        elif choice == "3":
            profile["activity"] = get_activity()
            print(f"Your favorite activity was updated to {profile['activity']}.")

        elif choice == "4":
            print("\n" + give_recommendation(profile))

        elif choice == "5":
            print("\nThanks for using the Personal Mini System. See you next time!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 5.")

        profile["summary"] = (
            f"{profile['name']} is a {profile['category']} who enjoys {profile['activity'].lower()} "
            f"and currently feels {profile['mood'].lower()}."
        )


if __name__ == "__main__":
    main()
