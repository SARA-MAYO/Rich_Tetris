# 테트리스 게임에서 사용될 새로운 테트로미노 블록을 랜덤으로 생성하는 기능을 구현
# 생성은 랜덤으로 하며 모양, 색상, 위치를 정함

import random
from src.config.settings import TETROMINOS, BOARD_WIDTH

def get_random_piece():            # 새 블록 하나를 생성하는 함수
    name = random.choice(list(TETROMINOS.keys()))   # TETROMINOS에서 7종 블록 중 랜덤 선택
    data = TETROMINOS[name]   # 선택된 블록 이름에 해당하는 모양(shape)과 색상(color) 데이터를 가져옴

    # 새 블록의 객체를 dic형태로 반환
    return {
        "name": name,
        "coords": list(data["shape"]),  # 복사해서 사용
        "color": data["color"],
        "x": BOARD_WIDTH // 2 - 2,      # 시작 X 위치
        "y": 0                          # 시작 Y 위치
    }
