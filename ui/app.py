from textual.app import App, ComposeResult
from textual.containers import Container
from textual.binding import Binding

# 모듈화된 기능들 import
from src.config.settings import DEFAULT_SPEED
from src.logic import grid_manager, spawner, collision, rotator, line_manager
from src.state.score import ScoreManager
from src.ui.widgets import BoardWidget, InfoWidget
from src.ui.screens import PauseScreen, GameOverScreen

class TetrisApp(App):
    CSS = """
    Screen { align: center middle; }
    #main { layout: horizontal; width: 60; height: 25; }
    BoardWidget { width: 60%; height: 100%; }
    InfoWidget { width: 40%; height: 100%; }
    #dialog { grid-size: 1 4; align: center middle; width: 40; height: 20; border: thick $background 80%; background: $surface; }
    #title { text-align: center; width: 100%; }
    """

    BINDINGS = [
        Binding("left", "move(-1)", "Left"),
        Binding("right", "move(1)", "Right"),
        Binding("down", "soft_drop", "Down"),
        Binding("up", "rotate", "Rotate"),
        Binding("z", "rotate", "Rotate"),
        Binding("space", "hard_drop", "Drop"),
        Binding("p", "toggle_pause", "Pause"),
        Binding("escape", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        with Container(id="main"):
            yield BoardWidget()
            yield InfoWidget()

    def on_mount(self):
        self.start_game()

    def start_game(self):
        # 상태 초기화
        self.grid = grid_manager.create_empty_grid()
        self.score_manager = ScoreManager()
        self.current_piece = spawner.get_random_piece()
        self.next_piece = spawner.get_random_piece()
        self.is_paused = False
        self.is_over = False
        
        # 타이머 설정 (0.5초마다 game_tick 실행)
        self.timer = self.set_interval(DEFAULT_SPEED, self.game_tick)
        self.refresh_view()

    def game_tick(self):
        """일정 시간마다 블록 자동 하강"""
        if self.is_paused or self.is_over: return

        # 한 칸 아래로 이동 시도
        if not collision.check_collision(self.grid, self.current_piece["coords"], 
                                         self.current_piece["x"], self.current_piece["y"], dy=1):
            self.current_piece["y"] += 1
        else:
            self.lock_piece()
        self.refresh_view()

    def lock_piece(self):
        """블록 고정 및 후처리 로직"""
        # 1. 고정
        grid_manager.place_block_on_grid(self.grid, self.current_piece)
        # 2. 줄 삭제
        cleared = line_manager.clear_full_lines(self.grid)
        self.score_manager.add_lines(cleared)
        # 3. 새 블록 생성
        self.current_piece = self.next_piece
        self.next_piece = spawner.get_random_piece()
        
        # 4. 게임 오버 체크 (생성되자마자 충돌하면 끝)
        if collision.check_collision(self.grid, self.current_piece["coords"], 
                                     self.current_piece["x"], self.current_piece["y"]):
            self.is_over = True
            self.show_game_over()

    def action_move(self, dir_str):
        dx = int(dir_str)
        if not self.is_paused and not self.is_over:
            if not collision.check_collision(self.grid, self.current_piece["coords"], 
                                             self.current_piece["x"], self.current_piece["y"], dx=dx):
                self.current_piece["x"] += dx
                self.refresh_view()

    def action_soft_drop(self):
        self.game_tick() # 틱 강제 실행으로 한 칸 내리기

    def action_hard_drop(self):
        if not self.is_paused and not self.is_over:
            # 바닥에 닿을 때까지 반복해서 내림
            while not collision.check_collision(self.grid, self.current_piece["coords"], 
                                                self.current_piece["x"], self.current_piece["y"], dy=1):
                self.current_piece["y"] += 1
            self.lock_piece()
            self.refresh_view()

    def action_rotate(self):
        if not self.is_paused and not self.is_over:
            new_coords = rotator.calculate_rotation(self.current_piece["name"], self.current_piece["coords"])
            # 회전 후 위치가 유효한지 검사
            if not collision.check_collision(self.grid, new_coords, 
                                             self.current_piece["x"], self.current_piece["y"]):
                self.current_piece["coords"] = new_coords
                self.refresh_view()

    def action_toggle_pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.push_screen(PauseScreen())
        else:
            self.pop_screen()

    def show_game_over(self):
        def callback(restart):
            if restart: self.start_game()
            else: self.exit()
        self.push_screen(GameOverScreen(self.score_manager.score), callback)

    def refresh_view(self):
        self.query_one(BoardWidget).render_game(self.grid, self.current_piece)
        self.query_one(InfoWidget).render_info(self.score_manager, self.next_piece["name"])