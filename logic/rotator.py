"""
테트로미노의 현재 좌표를 기반으로 시계방향 90도 회전된 새 좌표를 계산해서 반환
- 회전 기능 구현을 위해 회전 계산만 담당하는 순수 로직 제공
"""

def calculate_rotation(shape_name, current_coords):

    # 예외 처리 '0' 블록은 회전안 함(정사각형 형태)
    if shape_name == "O":
        return current_coords  

