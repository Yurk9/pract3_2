import random

conflict = "1"

def fake_news_generator():
    subjects = ["Ученые", "Кошки", "Правительство", "Инопланетяне", "ИИ ChatGPT"]
    actions = ["скрывают", "обнаружили", "создали", "взломали", "съели"]
    objects = ["эликсир бессмертия", "секретную теорию заговора", "новый вид энергии", "доказательство плоской Земли"]
    return f"{random.choice(subjects)} {random.choice(actions)} {random.choice(objects)}!"

print(fake_news_generator())  # Например: "Инопланетяне съели эликсир бессмертия!"

def is_dozhd(text):
    rain_words = {"дождь", "листья", "осень", "метель", "память", "электричка"}
    return any(word in text.lower() for word in rain_words)

print(is_dozhd("За окном снова дождь"))  # True
print(is_dozhd("Солнце светит ярко"))    # False

def should_i_go_out():
    problems = ["На улице метель", "У вас нет штанов", "Завтра конец света", "Вы превращаетесь в зомби"]
    if random.random() > 0.7:
        return "Да, но только если возьмете счастливый носок!"
    else:
        return f"Нет. Причина: {random.choice(problems)}."

print(should_i_go_out())

