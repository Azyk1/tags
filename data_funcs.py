import datetime

import pickle
from tkinter import messagebox as mb

from settings import game, titles, messages, names, max_len_game_name


def read_data(file_name):
    games = []
    with open(file_name, "rb") as file:
        flag = file.read(1)
        if flag:
            file.seek(-1, 1)
        while flag:
            games.append(pickle.load(file))
            flag = file.read(1)
            file.seek(-1, 1)
    return games


def write_data(file_name, games=None):
    if games is None:
        games = []
    with open(file_name, "wb") as file:
        for cur_game in games:
            pickle.dump(cur_game, file)


def save_data(window, text, file_name):
    if len(text) > max_len_game_name or len(text) == 0:
        mb.showinfo(titles["notification"], messages["incorrect_game_name"])
        return
    temp = str(datetime.datetime.now())
    game.name = text
    game.save_time = temp[: len(temp) - 7]
    games = read_data(file_name)
    is_unique_name = True
    for old_game in games:
        if game["name"] == old_game["name"]:
            is_unique_name = False
    if is_unique_name:
        games.append(game)
        write_data(file_name, games)
    else:
        answer = mb.askyesno(titles["warning"], messages["replace_save_question"])
        if answer:
            write_data(file_name, games)
        else:
            return
    window.destroy()
    mb.showinfo(titles["notification"], messages["successful save"])


def prepare_data(games):
    return [f"название: {cur_game.name}    кол-во ходов: {cur_game.steps_number}    дата создания: {cur_game.save_time}"
            for cur_game in games]




