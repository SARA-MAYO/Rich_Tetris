from src.config.settings import BOARD_WIDTH, BOARD_HEIGHT

def create_empty_grid():
    return [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

