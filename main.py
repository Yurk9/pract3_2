import random

def generate_cat_name():
    prefixes = ["Бар", "Мур", "Вась", "Рыж", "Снеж"]
    suffixes = ["ик", "ок", "ка", "ко", "ан"]
    return random.choice(prefixes) + random.choice(suffixes)

print(generate_cat_name())  # Например: "Мурок" или "Снежка"