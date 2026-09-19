age = int(input("Enter your age: "))
country = input("Enter your country: ")

if country == "india" and age >= 18:
    print("you are eligible to vote")

elif country != "india":
    print("you are not eligible to vote")

elif age < 18:
    print("you are not eligible to vote, because you are below 18" )

else:
    print("error")