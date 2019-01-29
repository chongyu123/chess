
from game.settings import white, black, brown, width, height, king_icon_1, king_icon_2
from pieces import Piece

class King(Piece):

    def __init__(self, tile, team):
        Piece.__init__(self, tile, team)


    def render(self):
        if (self.player.team == 1):
            self.current_tile.board.screen.blit(king_icon_1, (self.x_pos, self.y_pos))
        else:
            self.current_tile.board.screen.blit(king_icon_2, (self.x_pos, self.y_pos))

    def check_move(self, tile):
        
        available_moves = []

        # Check 3 on right
        if (self.check_tile(self.x - 1, self.y - 1)):
            available_moves.append((self.x - 1, self.y - 1))
        if (self.check_tile(self.x - 1, self.y)):
            available_moves.append((self.x - 1, self.y))
        if (self.check_tile(self.x - 1, self.y + 1)):
            available_moves.append((self.x - 1, self.y + 1))

        # Check 3 on left
        if (self.check_tile(self.x + 1, self.y - 1)):
            available_moves.append((self.x + 1, self.y - 1))
        if (self.check_tile(self.x + 1, self.y)):
            available_moves.append((self.x + 1, self.y))
        if (self.check_tile(self.x + 1, self.y + 1)):
            available_moves.append((self.x + 1, self.y + 1))
        
        # Remaining 2
        if (self.check_tile(self.x, self.y + 1)):
            available_moves.append((self.x, self.y + 1))
        if (self.check_tile(self.x, self.y - 1)):
            available_moves.append((self.x, self.y - 1))

        if ( (tile.x, tile.y) in available_moves):
            return True

        return False
    
    def check_tile(self, x, y):
        if (x < 0 or x >= 8 or y < 0 or y >= 8):
            return False
        else:
            tile = self.current_tile.board.board[y][x]
            if (tile and not tile.piece):
                return True
            elif (tile and tile.piece and tile.piece.player.team != self.player.team):
                return True
            return False
