conflict = "2"

def is_dozhd(text):
    rain_words = {"дождь", "листья", "осень", "метель", "память", "электричка"}
    return any(word in text.lower() for word in rain_words)

print(is_dozhd("За окном снова дождь"))  # True
print(is_dozhd("Солнце светит ярко"))    # False