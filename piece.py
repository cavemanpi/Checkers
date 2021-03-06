__author__ = 'Kokouvi Djogbessi'
import pygame
class Piece:
    """Contains information about a checkers piece. A piece is a pawn at creation,
    use make_king() to elevate."""
    img_folder = "img/"
    black_piece = img_folder+"black_piece.png"
    white_piece = img_folder+"white_piece.png"
    #screen

    def __init__(self, screen, is_white, pos, width, height):
        """Instantiates a piece object with given properties"""

        self.screen = screen
        self.is_king = False
        self.is_white = is_white
        self.pos = pos
        self.width = width
        self.height = height
        size = width, height

        image =  self.white_piece if is_white else self.black_piece

        #loads 16 images, 1 per piece. TODO: Load one image used by every piece
        self.piece_image = pygame.image.load(image)
        self.piece_image = pygame.transform.scale(self.piece_image, size)

    def make_king(self):
        """Sets this piece as king"""

        self.is_king = True

    def draw(self):
        self.screen.blit(self.piece_image, (self.pos[0]*self.width, (self.pos[1])*self.height))
    def _get_pos(self):
        return self.pos

    def _set_pos(self, pos):
        self.pos = pos

    def _set_is_white(self, is_white):
        print("You can't change the color of a piece!")

    def __repr__(self):
        """Displays the position and type of the piece"""
        if self.is_white:
            color = "White"
        else:
            color = "Black"
        return "{} at {}".format(color, self.pos)