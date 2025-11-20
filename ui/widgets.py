from textual.widgets import Static
from src.ui.drawer import draw_grid_panel, draw_score_panel

class BoardWidget(Static):
    """게임 보드를 표시하는 Textual 위젯"""
    def render_game(self, grid, piece):
        self.update(draw_grid_panel(grid, piece))

class InfoWidget(Static):
    """점수와 다음 블록 정보를 표시하는 Textual 위젯"""
    def render_info(self, score_obj, next_name):
        self.update(draw_score_panel(score_obj, next_name))