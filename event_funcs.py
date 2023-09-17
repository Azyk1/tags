import tkinter as tk
from tkinter import messagebox as mb

import draw_funcs
import data_funcs
import window_funcs
from settings import *


def try_make_step(event, canvas, num_images):
    is_mouse_in_piece, index = draw_funcs.is_relevant_area(piece_rects, event.x, event.y,
                                                           (board_rect[0], board_rect[0] + board_rect[2]),
                                                           (board_rect[1], board_rect[1] + board_rect[3]))
    if is_mouse_in_piece and game.cur_configuration[index // 4][index % 4] != 0:
        find_zero = make_step(canvas, num_images, index)
        if game.is_lost():
            mb.showinfo(titles["notification"], messages["steps_limit"])
            window_funcs.create_new_game_window(canvas, num_images, (board_rect[0], board_rect[1]), False)
        if not find_zero and game.cur_configuration[i][j] != 0:
            mb.showinfo(titles["notification"], messages["unmoved_piece"])


def make_step(canvas, num_images, index):
    i, j = index // 4, index % 4
    adjs = ((-1, 0), (1, 0), (0, 1), (0, -1))
    find_zero = False

    for delta_i, delta_j in adjs:
        new_i, new_j = i + delta_i, j + delta_j
        if -1 < new_i < 4 and -1 < new_j < 4 and game.cur_configuration[new_i][new_j] == 0:
            game.steps_number += 1
            find_zero = True
            game.cur_configuration[i][j], game.cur_configuration[new_i][new_j] = \
                game.cur_configuration[new_i][new_j], game.cur_configuration[i][j]
            draw_funcs.draw_piece(canvas, num_images, (piece_rects[index][0], piece_rects[index][1]), (i, j))
            draw_funcs.draw_piece(canvas, num_images,
                                  (piece_rects[new_i * 4 + new_j][0], piece_rects[new_i * 4 + new_j][1]),
                                  (new_i, new_j))
            canvas.create_rectangle(board_rect[0] + board_rect[2], 0, board_rect[0] + board_rect[2] + 400, 500,
                                    fill=colors["background_color"], outline=colors["background_color"])
            canvas.create_text(board_rect[0] + board_rect[2] + 180, board_rect[1] + 10,
                               text=texts["steps_number"] + str(game.steps_number), font=(names["font_name"], 18))
            if game.is_win():
                mb.showinfo(titles["notification"], messages["win"])
                if mb.askyesno(titles["notification"], messages["save_win_question"]):
                    window_funcs.create_save_window(names["leaderboard_file_name"])
    return find_zero


def load_game(window, canvas, images, saves, save):
    if len(save) == 0:
        mb.showinfo(titles["notification"], messages["empty_game"])
    else:
        window.destroy()
        if mb.askyesno(titles["warning"], messages["load_question"]):
            i = save[0]
            game.__init__(False, saves[i].start_configuration, saves[i].cur_configuration, saves[i].steps_number,
                          saves[i].name, saves[i].save_time)
            draw_funcs.draw_game_scene(canvas, images, (0, 0), (1080, 760),
                                       (board_rect[0] + piece_size[0] // 2, board_rect[1] + piece_size[1] // 2))


def delete_game(load_list, saves_list, save):
    if len(save) == 0:
        mb.showinfo(titles["notification"], messages["empty_game"])
    else:
        if mb.askyesno(titles["warning"], messages["delete_question"]):
            load_list.delete(save[0])
            saves_list.pop(save[0])


def show_config(leader_list, cur_game, show_start_config=True):
    if len(cur_game) == 0:
        mb.showinfo(titles["notification"], messages["empty_game"])
    else:
        show_window = tk.Toplevel()
        show_window.title(titles["start_config"])
        show_window.geometry("300x300")
        show_window.resizable(width=False, height=False)
        show_window.grab_set()
        show_window.protocol("WM_DELETE_WINDOW", lambda: close_no_args_window(show_window))

        canvas = tk.Canvas(master=show_window, bg=colors["background_color"], highlightthickness=0)
        text = make_configuration(leader_list[cur_game[0]].start_configuration) if show_start_config \
            else make_configuration(leader_list[cur_game[0]].cur_configuration)
        canvas.create_text(140, 140, text=text, font=(names["font_name"], 25))
        canvas.pack(fill=tk.BOTH, expand=True)


def make_configuration(config):
    result_text = []
    for i in range(len(config)):
        cur_str = []
        for j in range(len(config[0])):
            cur_str.append(str(config[i][j]) if config[i][j] > 9 else '  ' + str(config[i][j]))
        result_text.append('  '.join(cur_str))
    return '\n'.join(result_text)


def close_load_window(window, saves):
    data_funcs.write_data(names["datafile_name"], saves)
    window.destroy()


def close_no_args_window(window):
    window.destroy()


def exit_():
    if mb.askyesno(titles["warning"], messages["exit_question"]):
        exit()