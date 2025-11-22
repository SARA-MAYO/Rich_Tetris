from src.config.settings import BOARD_WIDTH, BOARD_HEIGHT

def create_empty_grid():
    return [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def place_block_on_grid(grid, piece):
    """블록을 그리드에 영구적으로 기록"""
    for x, y in piece["coords"]:
        nx, ny = piece["x"] + x, piece["y"] + y
        if 0 <= ny < BOARD_HEIGHT and 0 <= nx < BOARD_WIDTH:
            grid[ny][nx] = piece["color"]
    return grid