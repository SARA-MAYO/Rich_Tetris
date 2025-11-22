from src.config.settings import BOARD_WIDTH, BOARD_HEIGHT

def clear_full_lines(grid):
    """
    꽉 찬 줄을 찾아 삭제하고, 지워진 줄 수를 반환함.
    그리드는 자동으로 윗줄이 내려옴.
    """
    # None(빈공간)이 하나도 없는 줄만 남김 (즉, 꽉 찬 줄은 제거됨)
    # any(cell is None ...)이 True인 줄만 남기므로, 
    # None이 하나도 없는(꽉 찬) 줄은 False가 되어 리스트에서 제외됨.
    new_grid = [row for row in grid if any(cell is None for cell in row)]
    
    lines_cleared = BOARD_HEIGHT - len(new_grid)

    # 지워진 만큼 위쪽에 빈 줄 추가 (새 리스트의 맨 앞에 추가)
    for _ in range(lines_cleared):
        new_grid.insert(0, [None] * BOARD_WIDTH)

    # 원본 리스트 내용 교체 (참조 유지)
    # grid = new_grid 라고 하면 지역변수만 바뀌므로,
    # 원본 리스트의 요소를 하나씩 덮어써야 함.
    for i in range(BOARD_HEIGHT):
        grid[i] = new_grid[i]

    return lines_cleared