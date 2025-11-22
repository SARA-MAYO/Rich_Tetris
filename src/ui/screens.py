from textual.screen import ModalScreen
from textual.widgets import Button, Label
from textual.containers import Grid
from textual.app import ComposeResult

class PauseScreen(ModalScreen):
    """게임 일시정지 시 나타나는 팝업 화면"""
    def compose(self) -> ComposeResult:
        yield Grid(
            Label("PAUSED", id="title"),
            Label("Press 'P' to Resume", id="subtitle"),
            id="dialog"
        )

class GameOverScreen(ModalScreen):
    """게임 종료 시 점수와 재시작 버튼을 보여주는 팝업 화면"""
    def __init__(self, score):
        super().__init__()
        self.score = score

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("GAME OVER", id="title"),
            Label(f"Score: {self.score}", id="score"),
            Button("Restart", id="restart"),
            Button("Quit", id="quit"),
            id="dialog"
        )

    def on_button_pressed(self, event):
        # Restart 버튼이면 True, Quit이면 False를 반환하며 팝업 닫기
        self.dismiss(event.button.id == "restart")