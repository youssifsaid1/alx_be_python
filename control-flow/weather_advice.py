# Ask the user about the weather
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Give clothing advice based on the weather
if weather == "sunny":
    print("Wear a light t-shirt and sunglasses 😎")
elif weather == "rainy":
    print("Take an umbrella and a raincoat ☔")
elif weather == "cold":
    print("Wear a warm jacket 🧥")
else:
    print("Not sure about the weather, be prepared for anything 🌤️")