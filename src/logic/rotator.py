"""
테트로미노의 현재 좌표를 기반으로 시계방향 90도 회전된 새 좌표를 계산해서 반환
- 회전 기능 구현을 위해 회전 계산만 담당하는 순수 로직 제공
"""

def calculate_rotation(shape_name, current_coords):

    # 예외 처리 '0' 블록은 회전안 함(정사각형 형태)
    if shape_name == "O":
        return current_coords  

    # 기준점(pivot) 계산
    pivot = current_coords[2]
    px, py = pivot

    # 회전 후 새로운 배열
    # - rx, ry(블록의 pivot 기준 x, y 방향으로 떨아진 거리)
    # - nx, ny(회전 후 x, y 좌표)
    new_coords = []
    for x, y in current_coords:
        # 회전 공식: (x, y) -> (-y, x)
        # 피벗 기준 상대 좌표로 변환 -> 회전 -> 다시 절대 좌표로 복구
        rx, ry = x - px, y - py
        nx, ny = -ry + px, rx + py
        new_coords.append((int(nx), int(ny)))  # 정수로 변환, 튜플로 만듦, 리스트에 넣음

    return new_coords

