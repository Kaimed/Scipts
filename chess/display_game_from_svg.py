import chess
import chess.pgn
import chess.svg

from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MainWindow(QWidget):

    def draw(self, mainlineMove):
        self.i += 1
        self.chessboard.push(mainlineMove)
        self.chessboardSvg = chess.svg.board(self.chessboard).encode('UTF-8')
        self.widgetSvg.load(self.chessboardSvg)

    def __init__(self, game):

        super().__init__()
        self.i = 0
        if game == None:
            self.chessboard = chess.Board()
        else:
            self.chessboard = game.board()
            self.MOVES = [x for x in game.mainline_moves()]
            print(self.MOVES)

        self.setGeometry(100, 100, 1000, 1000)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 960, 960)

        self.button = QPushButton("Next Move")
        self.button.clicked.connect(self.draw(self.MOVES[self.i]))

        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)


if __name__ == "__main__":
    pgn = open('C:/Users/kaime/Downloads/CHESS/Open_Sicillian__as_Black.pgn')
    myGame = chess.pgn.read_game(pgn)
    app = QApplication([])
    window = MainWindow(myGame)
    window.show()
    app.exec()
# pgn = open('C:/Users/kaime/Downloads/CHESS/Open_Sicillian__as_Black.pgn')
# game = chess.pgn.read_game(pgn)
#
# board = game.board()
# for move in game.mainline_moves():
#     print(board)
#     print(chess.svg.board(board,squares=chess.SQUARES,size = 350))
#     board.push(move)
#     q = input()
#     if(q == 'q' or q=='quit'):
#         exit(0)
