name = input("🕴️ Your name: ")
age = int(input("🎂 Your age: "))
city = input("🏙️ City You Live In: ")
food = input("😋 Your Favorite Food: ")
colour = input("🎨 Your Favorite Color: ").upper()
animal = input("🐾 Your Spirit Animal: ")
hobby = input("💟 One Thing You LOVE Doing: ")

print(f"\nYou're from {city}, a place of dreams!\n")
print(f"🍿 You love {food} and enjoy doing {hobby}.\n")
print(f"🎨 You vibe with the color {colour} and your spirit animal is the {animal}.\n")
print(f"📅 You've lived approximately {age * 12} months already.\n")

#If age < 18:
if age<18:
  print("🧩 You belong to the 'Young Explorer' tribe.\n")
#elif 18 ≤ age ≤ 30:
#elif 18=<age=<30:
elif 18<= age <=30:
  print("🧩 You belong to the 'Adventurer' tribe.\n")
elif age > 30:
  print("🧩 You belong to the 'Wise Owl' tribe.\n")

code=name[0]+str(age)[-1]+animal[0]+colour[0]
print(f"🔐 Your Secret Personality Code is: 💡 {code}")



