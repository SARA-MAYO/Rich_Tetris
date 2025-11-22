"""
테트로미노의 현재 좌표를 기반으로 시계방향 90도 회전된 새 좌표를 계산해서 반환
- 회전 기능 구현을 위해 회전 계산만 담당하는 순수 로직 제공
"""

"""
표준 SRS 기반 테트리스 회전 계산
pivot = (1,1) 고정 회전
"""
def calculate_rotation(shape_name, current_coords):
    # O 블록은 회전 없음
    if shape_name == "O":
        return current_coords

    # 🔥 pivot = (1,1) 고정
    px, py = 1, 1

    rotated = []
    for x, y in current_coords:
        # pivot 기준 상대 좌표
        rx = x - px
        ry = y - py

        # 90도 회전 (x,y)->(-y,x)
        nx = -ry + px
        ny = rx + py

        rotated.append((nx, ny))
    return rotated
