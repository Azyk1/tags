from settings import game, colors, names, texts, board_rect, interval_between_pieces, piece_size


def draw_board(canvas, images, start_point):
    x, y = start_point
    for i in range(4):
        for j in range(4):
            if game.cur_configuration[i][j] != 0:
                canvas.create_image(x, y, image=images[game.cur_configuration[i][j] - 1])
            x += piece_size[0] + interval_between_pieces[0]
        x = start_point[0]
        y += piece_size[1] + interval_between_pieces[1]


def draw_piece(canvas, images, point, indexes):
    if game.cur_configuration[indexes[0]][indexes[1]] != 0:
        canvas.create_image(point[0] + piece_size[0] // 2, point[1] + piece_size[1] // 2,
                            image=images[game.cur_configuration[indexes[0]][indexes[1]] - 1])
    else:
        canvas.create_rectangle(point[0], point[1], point[0] + piece_size[0], point[1] + piece_size[1],
                                fill=colors["background_color"], outline=colors["background_color"])


def is_relevant_area(areas, x, y, x_bound, y_bound):
    if x_bound[0] <= x <= x_bound[1] and y_bound[0] <= y <= y_bound[1]:
        for name in areas:
            rect = areas[name]
            if rect[0] <= x <= rect[0] + rect[2] and rect[1] <= y <= rect[1] + rect[3]:
                return True, name
    return False, None


def draw_game_scene(canvas, images, rect_point1, rect_point2, start_point):
    canvas.create_rectangle(rect_point1[0], rect_point1[1], rect_point2[0], rect_point2[1],
                            fill=colors["background_color"], outline=colors["background_color"])
    draw_board(canvas, images, start_point)
    canvas.create_text(board_rect[0] + board_rect[2] + 180, board_rect[1] + 10,
                       text=texts["steps_number"] + str(game.steps_number), font=(names["font_name"], 18))
