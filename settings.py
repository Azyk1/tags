import tag_game_cls

game = tag_game_cls.TagGame()

max_len_game_name = 10
piece_size = (50, 50)
interval_between_pieces = (3, 3)
board_rect = (350, 200,
              piece_size[0] * 4 + interval_between_pieces[0] * 3, piece_size[1] * 4 + interval_between_pieces[1] * 3)

piece_rects = {}
x, y = board_rect[0], board_rect[1]
counter = 0
for i in range(4):
    for j in range(4):
        piece_rects[counter] = (x, y, piece_size[0], piece_size[1])
        counter += 1
        x += piece_size[0] + interval_between_pieces[0]

    x = board_rect[0]
    y += piece_size[1] + interval_between_pieces[1]

colors = {
    "background_color": "#ffc34d",
    "font_color": "#ff0000",
    "button_color": "#000000",
    "edit_background_color": "#fee12b"
}
names = {
    "datafile_name": "saves.bin",
    "leaderboard_file_name": "leaderboard.bin",
    "icon_name": "icon.ico",
    "about_image_name": "about_num.png",
    "font_name": "Times new roman"
}
menu_labels = {
    "new_game": "Новая игра",
    "save_game": "Сохранить игру",
    "load_game": "Загрузить игру",
    "leaderboard.txt": "Таблица лидеров",
    "exit": "Выход",
    "about_game": "Об игре",
    "help": "Помощь",
    "file_submenu": "Файл",
    "help_submenu": "Справка"
}
titles = {
    "project_name": "Пятнашки",
    "notification": "Уведомление",
    "warning": "Предупреждение",
    "save_game": "Сохранение игры",
    "load_game": "Загрузка игры",
    "leaderboard": "Таблица лидеров",
    "start_config": "Стартовое поле",
    "about": "Об игре"
}
messages = {
    "incorrect_game_name": f"Некорректное название (должно быть от 1 до {max_len_game_name} символов)!",
    "win": "Поздравляю, вы победили!",
    "successful save": "Сохранение успешно завершено",
    "empty_game": "Не выбрана игра для дальнейших действий",
    "steps_limit": "Игра окончена - достигнуто максимальное количество ходов!",
    "unmoved_piece": "Эту фишку нельзя подвинуть",
    "no_data": "Здесь пока нет данных",
    "replace_save_question": "Сохранение с таким именем уже существует. Хотите заменить его на текущее?",
    "exit_question": "При выходе из игры все несохраненные данные будут утеряны. Вы уверены, что хотите выйти?",
    "new_game_question":
        "При начале новой игры все несохраненные данные будут утеряны. Вы уверены, что хотите начать новую игру?",
    "load_question":
        "При загрузке игры все несохраненные данные будут утеряны. Вы уверены, что хотите загрузить выбранную игру?",
    "delete_question": "Вы уверен, что хотите удалить выбранную игру?",
    "save_win_question": "Вы можете сохранить свой результат(нажмите да) или сразу начать новую игру. "
                         "Если ваш сохраненный результат оказывается в десятке лучших, то попадает в таблицу лидеров"
}
texts = {
    "steps_number": "Количество сделанных ходов: ",
    "enter_save_name": "Введите название сохранения:",
    "save_button": "Сохранить",
    "load_button": "Загрузить",
    "delete_button": "Удалить",
    "show_start_config_button": "Показать стартовое поле",
    "show_cur_config_button": "Показать текущее поле",
    "about_text": 'название игры: "Пятнашки"\n'
                  "дата создания: август 2023 года\n"
                  "разработчик: Зыков Антон Дмитриевич\n"
                  "по вопросам сотрудничества: zazyk235@gmail.com",
    "game_rules": "Правила игры:\n"
                  "Поле представляет собой квадрат 4 на 4, в котором расположены 15 фишек и пустая клетка.\n"
                  "Задача игрока - расставить фишки в порядке возрастания: первая строка - 1,2,3,4, вторая -\n"
                  "5,6,7,8 и так далее. За один ход можно подвинуть фишку на соседнее место, если оно не занято.\n"
                  "Условие победы - фишки расставлены от 1 до 15 в порядке возрастания слева направо и сверху\nвниз. "
                  f"Условие поражения - победа не достигнута за {game.MAX_STEPS} ходов.",
    "menu_items": "Описание пунктов меню:\n"
                  "Новая игра - начало новой игры\n"
                  "Сохранить игру - сохранение текущей игры\n"
                  "Загрузить игру - загрузка или удаление сохраненных ранее игр\n"
                  "Таблица лидеров - десять самых быстрых по количеству ходов побед\n"
                  "Выход - выход из приложения\n"
                  "Об игре - краткая информация об игре и ее разработчике\n"
                  "Помощь - краткое описание всего приложения"
}
