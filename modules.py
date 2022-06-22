def start(update, context):
    arg = context.arg
    if not arg:
        context.bot.send_messege(update.effective_chat_id, "Привет")
    else:
        context.bot.send_messege(update.effective_chat_id, f"{' '.join(arg)}")

def info(update, context):
    context.bot.send_messege(update.effective_chat_id, "Планируем дела")

def to_do(update, context):
    arg = context.arg
    if not arg:
        context.bot.send_messege(update.effective_chat_id, "Добавить новую задачу - 1 Редактировать задачу - 2  Просмотр  дел -3 Выход - 4 :")
        try:
            if arg < 1 or arg > 4:
                context.bot.send_messege(update.effective_chat_id, "Введен не правельный запрос!")
            elif arg == 1:
                user_input = context.bot.send_messege(update.effective_chat_id,"Введите задачу в формате (Дата задача примечание): ")
                record = tuple( i for i in user_input.split(' '))
                with open('planned_task.csv', 'a+') as file:
                    for e in record:
                        file.write(f'{e} ')
                    file.write('\n')
            elif arg == 2:
                var_choice = context.bot.send_messege(update.effective_chat_id, "Отметить задачу выполненной - c Удалить задачу - d :")
                if var_choice == 'c':
                    user_input = context.bot.send_messege(update.effective_chat_id, "Введите задачу которую выполнили(в конце пробел): ")
                    with open('planned_task.csv', 'r') as file:
                        p_data = file.read()
                    c_data = p_data.replace(user_input, user_input +'+')
                    with open('planned_task.csv', 'w') as file:
                        file.write(c_data)
                elif var_choice == 'd':
                    user_input = context.bot.send_messege(update.effective_chat_id, "Введите задачу которую удаляем(в конце пробел): ")
                    with open('planned_task.csv', "r") as file:
                        lines = file.readlines()
                    with open('planned_task.csv', 'w') as new_file:
                        for line in lines:
                            if line != (user_input +"\n"):
                                new_file.write(line)
            elif arg == 3:
                 with open('planned_task.csv', "r") as file:
                    context.bot.send_messege(update.effective_chat_id, file.read())
                   

        except ValueError:
            context.bot.send_messege(update.effective_chat_id, "Введен не корректный запрос!")        
def messege(update, context):
    text = update.messege.text
    if text.lower() == 'привет':
        context.bot.send_messege(update.effective_chat_id, "И тебе привет...")
    else:
        context.bot.send_messege(update.effective_chat_id, "Я тебя не понимаю")

def unknown(update, context):
    context.bot.send_messege(update.effective_chat_id, "Ты несешь какую-то дичь...")
