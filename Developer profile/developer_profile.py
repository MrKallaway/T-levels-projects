print("=" * 40)
print("     STUDENT DEVELOPER PROFILE")
print("=" * 40)

name = input("Enter your name: ")
language = input("Enter your language: ")
interest = input("Enter your interests: ")
career = input("Enter your career goal: ")
level = input("Choose skill level (1-3): ")

print("\nMY DEVELOPER PROFILE")
print("Name:", name)
print("Language:", language)
print("Interest:", interest)
print("Career Goal:", career)
print("Welcome to my GitHub portfolio!")

if level == "1":
    print("Skill Level: Beginner Developer")
elif level == "2":
    print("Skill Level: Intermediate Developer")
elif level == "3":
    print("Skill Level: Advanced Developer")
else:
    print("Skill level not recognised.")
