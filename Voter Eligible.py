age = int(input("Enter your age: "))
country = input("Enter your country: ").strip().lower()

if country != "india":
    print("You are not eligible to vote")
elif age < 18:
    print("You are not eligible to vote, because you are below 18")
else:
    print("You are eligible to vote")
