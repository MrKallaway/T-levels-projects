def show_banner():
    print("=" * 40)
    print("     STUDENT DEVELOPER PROFILE")
    print("=" * 40)

def get_profile():
    name = input("Enter your name: ")
    language = input("Enter your language: ")
    interest = input("Enter your interests: ")
    career = input("Enter your career goal: ")
    level_valid = False
    while not level_valid:
        level = input("Choose skill level (1-3): ")
        if level in ("1", "2", "3"):
            level_valid = True
        else:
            print("Invalid input, please enter 1, 2 or 3")
    return name, language, interest, career, level

def display_profile(name, language, interest, career, level):
    print("\nMY DEVELOPER PROFILE")
    print("Name:", name)
    print("Language:", language)
    print("Interest:", interest)
    print("Career Goal:", career)

    if level == "1":
        print("Skill Level: Beginner Developer")
    elif level == "2":
        print("Skill Level: Intermediate Developer")
    elif level == "3":
        print("Skill Level: Advanced Developer")



show_banner()
display_profile(*get_profile())
print("Welcome to my GitHub portfolio!")
