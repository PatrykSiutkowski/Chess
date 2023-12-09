from graphics import *

board = [
    [["BR"], ["BN"], ["BB"], ["BQ"], ["BK"], ["BB"], ["BN"], ["BR"]],
    [["BP"], ["BP"], ["BP"], ["BP"], ["BP"], ["BP"], ["BP"], ["BP"]],
    [[], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], []],
    [["WP"], ["WP"], ["WP"], ["WP"], ["WP"], ["WP"], ["WP"], ["WP"]],
    [["WR"], ["WN"], ["WB"], ["WQ"], ["WK"], ["WB"], ["WN"], ["WR"]]
]


def draw_chessboard(window, colours, square_width, board_squares):
    i = 0
    for x in range(square_width, square_width*9, square_width):
        if i == 1:
            i = 2
        else:
            i = 1
        for y in range(square_width, square_width*9, square_width):
            if i > 1:
                i = 0
            time.sleep(0.08)
            top_left = Point(x, y)
            bottom_right = Point(x + square_width, y + square_width)
            square = Rectangle(top_left, bottom_right)
            square.setFill(colours[i])
            square.draw(window)
            patch_square = {
                "topX & topY": [square],
                "Colour code": [i]
            }
            board_squares.append(patch_square)
            i += 1


def draw_piece(window, x, y, text, text_colour, font):
    text_object = Text(Point(x, y), text)
    text_object.setTextColor(text_colour)
    text_object.draw(window)
    return text_object


def draw_text(window, x, y, text, text_colour, font):
    text_object = Text(Point(x, y), text)
    text_object.setTextColor(text_colour)
    text_object.draw(window)
    return text_object

def draw_black(window, square_width, all_pieces):
    square_half = square_width/2
    for x in range(int(square_width + square_half), int((square_width + square_half) * 6), int(square_width)):
        draw_piece(window, x, (square_width + (square_width/2) * 2 + square_width/2), "BP", "pink", "")
        pawn_pieces = {
            "topX & topY": [[x], [square_width + (square_width / 2)]],
            "Square Piece": ['BP'],
            "Colour": "B",
            "times moved": 0
        }
        all_pieces.append(pawn_pieces)
        index = int(x/square_width - 1)
        print(x, index, board[7][index])
        draw_piece(window, x, (square_width + (square_width/2)), board[0][index], "pink", "")
        piece = {
            "topX & topY": [[x], [square_width + (square_width/2)]],
            "Square Piece": board[0][index],
            "Colour": "B",
            "times moved": 0
        }
        all_pieces.append(piece)


def draw_white(window, square_width, all_pieces):
    square_half = square_width / 2
    for x in range(int(square_width + square_half), int((square_width + square_half) * 6), int(square_width)):
        draw_piece(window, x, (square_width + (square_width / 2) * 2 + square_width / 2 + (square_width*5)), "WP", "pink", "")
        pawn_pieces = {
            "topX & topY": [[x], [square_width + (square_width / 2)]],
            "Square Piece": ['WP'],
            "Colour": "W",
            "times moved": 0
        }
        all_pieces.append(pawn_pieces)
        index = int(x / square_width - 1)
        draw_piece(window, x, (square_width + (square_width / 2 + (square_width*7))), board[7][index], "pink", "")
        piece = {
            "topX & topY": [[x], [square_width + (square_width / 2)]],
            "Square Piece": board[7][index],
            "Colour": "W",
            "times moved": 0
        }
        all_pieces.append(piece)

def get_piece(square, square_width, all_pieces):
    for piece in all_pieces:
        print(square["topX & topY"][0])
        if square["topX & topY"][0].getX() < piece.x < square["topX & topY"][0].getX() + square_width and square["topX & topY"][0].getY() < piece.y < square["topX & topY"][0].getY() + square_width:
            return piece


def selection_mode(window, board_squares, square_width, selected_piece, piece_endpoint, all_pieces):
    while True:
        user_click = window.getMouse()
        for i in range(len(board_squares)):
            object = board_squares[i]
            for shape in (object["topX & topY"]):
                point_1 = shape.getP1()
                if point_1.getX() < user_click.x < point_1.getX() + square_width and point_1.getY() < user_click.y < point_1.getY() + square_width:
                    if object not in selected_piece and len(selected_piece) < 1:
                        shape.setWidth(3)
                        shape.setOutline("blue")
                        selected_piece.append(object)
                    elif object not in selected_piece:
                        selected_piece[0]["topX & topY"][0].setWidth(1)
                        selected_piece[0]["topX & topY"][0].setOutline("black")
                        piece_endpoint[0]["topX & topY"][0].setWidth(1)
                        piece_endpoint[0]["topX & topY"][0].setOutline("black")
                        for i in selected_piece:
                            del selected_piece[0]
                        #print(selected_piece)
                        shape.setWidth(3)
                        shape.setOutline("blue")
                        selected_piece.append(object)
                    else:
                        print("Piece already selected")
                    print(get_piece(selected_piece[0], square_width, all_pieces))
        user_click_2 = window.getMouse()
        for i in range(len(board_squares)):
            object = board_squares[i]
            for shape in (object["topX & topY"]):
                point_1 = shape.getP1()
                if point_1.getX() < user_click_2.x < point_1.getX() + square_width and point_1.getY() < user_click_2.y < point_1.getY() + square_width:
                    if object not in selected_piece and len(piece_endpoint) < 1:
                        shape.setWidth(3)
                        shape.setOutline("red")
                        piece_endpoint.append(object)
                    elif object not in selected_piece:
                        print(piece_endpoint)
                        piece_endpoint[0]["topX & topY"][0].setWidth(1)
                        piece_endpoint[0]["topX & topY"][0].setOutline("black")
                        for i in piece_endpoint:
                            del piece_endpoint[0]

                        shape.setWidth(3)
                        shape.setOutline("red")
                        piece_endpoint.append(object)
                    else:
                        print("Piece already selected")


def deselect(selected_patches):
    for i in range(len(selected_patches)):
        for shape in (selected_patches[i]["topX & topY"]):
            shape.setWidth(1)
    for i in range(len(selected_patches)):
        del selected_patches[0]
    print(selected_patches)

def player_turn(window, square_width):
    player_turn = draw_text(window, square_width*5, int(square_width/2), "It is WHITE's turn", "black", "")



# def move_pawn(chess_board, square, ):
#
# def move_knight():


def main():
    square_width = 50
    all_pieces = []
    board_squares = []
    selected_piece = []
    piece_endpoint = []
    window = GraphWin("Chess Board", square_width*10, square_width*10)
    colours = ["white", "black"]
    draw_chessboard(window, colours, square_width, board_squares)
    print(board_squares)
    draw_black(window, square_width, all_pieces)
    print(all_pieces)
    draw_white(window, square_width, all_pieces)
    print(all_pieces)
    player_turn(window, square_width)
    selection_mode(window, board_squares, square_width, selected_piece, piece_endpoint, all_pieces)

    window.mainloop()

if __name__ == '__main__':
    main()
