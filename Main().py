import pygame as pg
import time
import GUI


def main():
    win = pg.display.set_mode((600,600))
    pg.display.set_caption("Sudoku")
    board = GUI.Grid(9, 9, 540, 540)
    key = None
    run = True
    start = time.time()
    strikes = 0

    while run:
        # Initialize the time to zero
        play_time = round(time.time() - start)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    key = 1
                if event.key == pg.K_2:
                    key = 2
                if event.key == pg.K_3:
                    key = 3
                if event.key == pg.K_4:
                    key = 4
                if event.key == pg.K_5:
                    key = 5
                if event.key == pg.K_6:
                    key = 6
                if event.key == pg.K_7:
                    key = 7
                if event.key == pg.K_8:
                    key = 8
                if event.key == pg.K_9:
                    key = 9
                if event.key == pg.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pg.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                            strikes += 1
                        key = None

                        if board.is_done():
                            print("Game over")
                            run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

        GUI.redraw_window(win, board, play_time, strikes)
        pg.display.update()


main()
pg.quit()