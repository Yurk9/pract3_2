import random

conflict = "1"

def fake_news_generator():
    subjects = ["Ученые", "Кошки", "Правительство", "Инопланетяне", "ИИ ChatGPT"]
    actions = ["скрывают", "обнаружили", "создали", "взломали", "съели"]
    objects = ["эликсир бессмертия", "секретную теорию заговора", "новый вид энергии", "доказательство плоской Земли"]
    return f"{random.choice(subjects)} {random.choice(actions)} {random.choice(objects)}!"

print(fake_news_generator())  # Например: "Инопланетяне съели эликсир бессмертия!"