from src.config.settings import BOARD_HEIGHT, BOARD_WIDTH

def check_collision(grid, piece_coords, piece_x, piece_y, dx=0, dy=0):
    """
    ✅ 목적: 이동할 위치(dx, dy)에 장애물이 있는지 확인함
    - grid: 2차원 배열
    - piece_coords: 블록의 상대 좌표
    - piece_x, piece_y: 현재 블록의 위치(블록 시작 위치 좌표값)
    - dx=0, dy=0: 움직이려는 방향

    ✅ 계산 로직: 현재 위치 + 모양 내부 좌표 + 이동하려는 변화값 = 새로운 x 또는 y좌표 산출
    """
    for x, y in piece_coords:   # 각각 칸 좌표에 대해 충돌 여부 체크
        nx = piece_x + x + dx  
        ny = piece_y + y + dy

        # 예외 처리 1: 기본 블록 영역 벗어남
        if nx < 0 or nx > BOARD_WIDTH or nx >= BOARD_HEIGHT:
            return True
        
        if ny >= 0 and grid[ny][nx] is not None:
            return True

    return False