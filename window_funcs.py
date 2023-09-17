import os.path

import tkinter as tk
from tkinter import messagebox as mb
from PIL import Image, ImageTk

import draw_funcs
import data_funcs
import event_funcs
from settings import *


def create_main_window():
    main_window = tk.Tk()
    num_images = [ImageTk.PhotoImage(Image.open("num" + str(i) + ".bmp")) for i in range(1, 16)]
    about_image = ImageTk.PhotoImage(Image.open(names["about_image_name"]))
    main_window.title(titles["project_name"])
    main_window.geometry("1080x760")
    main_window.iconbitmap(default=names["icon_name"])
    main_window.resizable(width=False, height=False)
    main_window.protocol("WM_DELETE_WINDOW", event_funcs.exit_)
    main_menu = tk.Menu(main_window)
    main_window.config(menu=main_menu)

    file_menu = tk.Menu(main_menu, bg=colors["background_color"], tearoff=0)
    file_menu.add_command(label=menu_labels["new_game"],
                          command=lambda: create_new_game_window(canvas, num_images,
                                                                 (board_rect[0] + piece_size[0] // 2,
                                                                  board_rect[1] + piece_size[1] // 2)))
    file_menu.add_command(label=menu_labels["save_game"], command=lambda: create_save_window(names["datafile_name"]))
    file_menu.add_command(label=menu_labels["load_game"],
                          command=lambda: create_load_window(canvas, num_images))
    file_menu.add_command(label=menu_labels["leaderboard.txt"], command=create_leaderboard_window)
    file_menu.add_command(label=menu_labels["exit"], command=event_funcs.exit_)
    help_menu = tk.Menu(main_menu, bg=colors["background_color"], tearoff=0)
    help_menu.add_command(label=menu_labels["about_game"], command=lambda: create_about_window(about_image))
    help_menu.add_command(label=menu_labels["help"], command=lambda: create_help_window(about_image))
    main_menu.add_cascade(label=menu_labels["file_submenu"], menu=file_menu)
    main_menu.add_cascade(label=menu_labels["help_submenu"], menu=help_menu)

    canvas = tk.Canvas(master=main_window, bg=colors["background_color"], highlightthickness=0)
    draw_funcs.draw_game_scene(canvas, num_images, (0, 0), (1080, 760),
                               (board_rect[0] + piece_size[0] // 2, board_rect[1] + piece_size[1] // 2))
    canvas.pack(fill=tk.BOTH, expand=True)

    main_window.bind("<Button-1>", lambda event: event_funcs.try_make_step(event, canvas, num_images))
    main_window.bind('1', lambda event: create_new_game_window(canvas, num_images,
                                                               (board_rect[0] + piece_size[0] // 2,
                                                                board_rect[1] + piece_size[1] // 2)))
    main_window.bind('2', lambda event: create_save_window(names["datafile_name"]))
    main_window.bind('3', lambda event: create_load_window(canvas, num_images))
    main_window.bind('4', lambda event: create_leaderboard_window())
    main_window.bind('5', lambda event: event_funcs.exit_())
    main_window.bind('6', lambda event: create_about_window(about_image))
    main_window.bind('7', lambda event: create_help_window(about_image))

    if not os.path.isfile(names["datafile_name"]):
        data_funcs.write_data(names["datafile_name"])
    if not os.path.isfile(names["leaderboard_file_name"]):
        data_funcs.write_data(names["leaderboard_file_name"])

    main_window.mainloop()


def create_new_game_window(canvas, images, start_point, need_to_ask=True):
    answer = mb.askyesno(titles["warning"], messages["new_game_question"]) if need_to_ask else True
    if answer:
        game.__init__()
        draw_funcs.draw_game_scene(canvas, images, (0, 0), (1080, 760), start_point)


def create_save_window(file_name):
    save_window = tk.Toplevel()
    save_window.title(titles["save_game"])
    save_window.geometry("600x350")
    save_window.resizable(width=False, height=False)
    save_window.grab_set()
    save_window.protocol("WM_DELETE_WINDOW", lambda: event_funcs.close_no_args_window(save_window))

    canvas = tk.Canvas(master=save_window, bg=colors["background_color"], highlightthickness=0)
    canvas.create_text(200, 130, text=texts["enter_save_name"], font=(names["font_name"], 16))
    entry_name = tk.Entry(master=save_window, font=(names["font_name"], 14), background=colors["edit_background_color"])
    save_button = tk.Button(master=save_window, text=texts["save_button"], background=colors["button_color"],
                            font=(names["font_name"], 16), foreground=colors["font_color"],
                            command=lambda: data_funcs.save_data(save_window, entry_name.get(), file_name))

    canvas.pack(fill=tk.BOTH, expand=True)
    entry_name.place(x=350, y=120)
    save_button.place(x=240, y=165)


def create_load_window(canvas, images):
    saves_list = data_funcs.read_data(names["datafile_name"])
    if len(saves_list) == 0:
        mb.showinfo(titles["notification"], messages["no_data"])

    load_window = tk.Toplevel()
    load_window.title(titles["load_game"])
    load_window.geometry("1080x760")
    load_window.resizable(width=False, height=False)
    load_window.grab_set()
    load_window.protocol("WM_DELETE_WINDOW",
                         lambda: event_funcs.close_load_window(load_window, saves_list))

    load_canvas = tk.Canvas(master=load_window, bg=colors["background_color"], highlightthickness=0)
    saves_var = tk.Variable(value=data_funcs.prepare_data(saves_list))
    load_list = tk.Listbox(master=load_window, background=colors["edit_background_color"], selectmode="SINGLE",
                           listvariable=saves_var, width=65, height=15, font=(names["font_name"], 20),
                           selectbackground=colors["button_color"], borderwidth=0, highlightthickness=0)
    scrollbar = tk.Scrollbar(load_window, orient="vertical")
    scrollbar.config(command=load_list.yview)
    load_list.config(yscrollcommand=scrollbar.set)
    load_button = tk.Button(master=load_window, text=texts["load_button"], background=colors["button_color"],
                            font=(names["font_name"], 20), foreground=colors["font_color"],
                            command=lambda: event_funcs.load_game(load_window, canvas, images, saves_list,
                                                                  load_list.curselection()))
    delete_button = tk.Button(master=load_window, text=texts["delete_button"], background=colors["button_color"],
                              font=(names["font_name"], 20), foreground=colors["font_color"],
                              command=lambda: event_funcs.delete_game(load_list, saves_list, load_list.curselection()))
    show_button = tk.Button(master=load_window, text=texts["show_cur_config_button"],
                            background=colors["button_color"],
                            font=(names["font_name"], 20), foreground=colors["font_color"],
                            command=lambda: event_funcs.show_config(saves_list, load_list.curselection(), False))

    load_canvas.pack(fill=tk.BOTH, expand=True)
    load_list.place(x=75, y=80)
    scrollbar.place(x=985, y=80, height=480)
    load_button.place(x=390, y=580, width=140)
    delete_button.place(x=540, y=580, width=140)
    show_button.place(x=390, y=650)


def create_leaderboard_window():
    leader_list = data_funcs.read_data(names["leaderboard_file_name"])
    if len(leader_list) == 0:
        mb.showinfo(titles["notification"], messages["no_data"])

    leaderboard_window = tk.Toplevel()
    leaderboard_window.title(titles["leaderboard"])
    leaderboard_window.geometry("1080x760")
    leaderboard_window.resizable(width=False, height=False)
    leaderboard_window.grab_set()
    leaderboard_window.protocol("WM_DELETE_WINDOW", lambda: event_funcs.close_no_args_window(leaderboard_window))

    load_canvas = tk.Canvas(master=leaderboard_window, bg=colors["background_color"], highlightthickness=0)
    leader_list.sort(key=lambda cur_game: cur_game.steps_number)
    leader_var = tk.Variable(value=data_funcs.prepare_data(leader_list))
    leaderboard_list = tk.Listbox(master=leaderboard_window, background=colors["edit_background_color"],
                                  selectmode="SINGLE",
                                  listvariable=leader_var, width=65, height=15, font=(names["font_name"], 20),
                                  selectbackground=colors["button_color"], borderwidth=0, highlightthickness=0)
    show_button = tk.Button(master=leaderboard_window, text=texts["show_start_config_button"],
                            background=colors["button_color"], font=(names["font_name"], 20),
                            foreground=colors["font_color"],
                            command=lambda: event_funcs.show_config(leader_list, leaderboard_list.curselection()))

    load_canvas.pack(fill=tk.BOTH, expand=True)
    leaderboard_list.place(x=75, y=80)
    show_button.place(x=380, y=600)


def create_about_window(image):
    about_window = tk.Toplevel()
    about_window.title(titles["about"])
    about_window.geometry("850x400")
    about_window.resizable(width=False, height=False)

    canvas = tk.Canvas(master=about_window, bg=colors["background_color"], highlightthickness=0)
    canvas.create_image(150, 190, image=image)
    canvas.create_text(560, 170, text=texts["about_text"], font=(names["font_name"], 18))
    canvas.pack(fill=tk.BOTH, expand=True)


def create_help_window(image):
    about_window = tk.Toplevel()
    about_window.title(titles["about"])
    about_window.geometry("1080x600")
    about_window.resizable(width=False, height=False)

    canvas = tk.Canvas(master=about_window, bg=colors["background_color"], highlightthickness=0)
    canvas.create_image(170, 380, image=image)
    canvas.create_text(530, 130, text=texts["game_rules"], font=(names["font_name"], 18))
    canvas.create_text(680, 365, text=texts["menu_items"], font=(names["font_name"], 18))
    canvas.pack(fill=tk.BOTH, expand=True)
