# src/logic/grid_manager.py
from src.config.settings import BOARD_WIDTH, BOARD_HEIGHT

# [Todo: 빈 보드 초기화 함수 구현]
def create_empty_grid():
    """10x20 크기의 빈 2차원 리스트(None으로 채움)를 생성"""
    return [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def place_block_on_grid(grid, piece):
    """(기존 기능 유지) 블록을 그리드에 고정"""
    for x, y in piece["coords"]:
        nx, ny = piece["x"] + x, piece["y"] + y
        if 0 <= ny < BOARD_HEIGHT and 0 <= nx < BOARD_WIDTH:
            grid[ny][nx] = piece["color"]
    return grid

# [Todo: 보드 상태 출력 유틸 함수 구현 (새로 추가됨)]
def print_debug_grid(grid):
    """터미널에 현재 보드 상태를 텍스트로 간단히 찍어보는 함수"""
    print("--- DEBUG BOARD START ---")
    for row in grid:
        line = ""
        for cell in row:
            if cell is None:
                line += " . "  # 빈 공간
            else:
                line += " O "  # 블록 있는 곳
        print(line)
    print("--- DEBUG BOARD END ---")
    