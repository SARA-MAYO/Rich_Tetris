from src.config.settings import SCORE_MAP

class ScoreManager:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.total_lines = 0

    def add_lines(self, lines):
        if lines > 0:
            self.total_lines += lines
            # 점수 계산
            self.score += SCORE_MAP.get(lines, 0) * self.level
            # 레벨업 (10줄마다)
            self.level = 1 + (self.total_lines // 10)