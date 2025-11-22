def calculate_rotation(shape_name, current_coords):
    """
    현재 좌표를 받아 시계방향(90도) 회전된 새 좌표 반환
    (x, y) -> (-y, x) 공식을 사용하여 원점 기준 회전
    """
    # 정사각형(O) 블록은 회전해도 모양이 같으므로 그대로 반환
    if shape_name == "O":
        return current_coords

    # 회전 축(Pivot) 결정
    # 블록 조각 중 하나를 중심으로 잡아야 제자리에서 돕니다.
    # 리스트의 중간 지점(index 1 또는 2)을 기준으로 잡습니다.
    pivot = current_coords[1] if len(current_coords) > 1 else (0, 0)
    px, py = pivot
    
    new_coords = []
    for x, y in current_coords:
        # 1. 중심점 기준으로 원점으로 이동 (상대 좌표 계산)
        rx, ry = x - px, y - py
        
        # 2. 90도 회전 공식 적용: (x, y) -> (-y, x)
        # 화면 좌표계(Y가 아래로 증가) 특성상 이 공식이 시계방향입니다.
        rotated_x, rotated_y = -ry, rx
        
        # 3. 다시 원래 위치(절대 좌표)로 복구
        nx, ny = rotated_x + px, rotated_y + py
        new_coords.append((int(nx), int(ny)))
        
    return new_coords
