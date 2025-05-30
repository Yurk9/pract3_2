import random

def should_i_go_out():
    problems = ["На улице метель", "У вас нет штанов", "Завтра конец света", "Вы превращаетесь в зомби"]
    if random.random() > 0.7:
        return "Да, но только если возьмете счастливый носок!"
    else:
        return f"Нет. Причина: {random.choice(problems)}."

print(should_i_go_out())