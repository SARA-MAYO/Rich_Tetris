from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from src.config.settings import BOARD_HEIGHT, BOARD_WIDTH

def draw_grid_panel(grid, current_piece=None):
    """그리드 데이터 + 현재 움직이는 조각 -> Rich Panel 반환"""
    
    # 보여주기용 임시 그리드 복사
    display_grid = [row[:] for row in grid]
    
    # 현재 움직이는 조각 덧입히기 (오버레이)
    if current_piece:
        px, py = current_piece["x"], current_piece["y"]
        color = current_piece["color"]
        for x, y in current_piece["coords"]:
            nx, ny = px + x, py + y
            if 0 <= ny < BOARD_HEIGHT and 0 <= nx < BOARD_WIDTH:
                display_grid[ny][nx] = color

    # Rich Text로 변환
    text = Text()
    for row in display_grid:
        for cell in row:
            if cell:
                text.append("  ", style=f"on {cell}") # 블록 (배경색)
            else:
                text.append(" . ", style="dim grey")  # 빈 공간
        text.append("\n") # 줄바꿈
        
    return Panel(Align.center(text), title="TETRIS", border_style="blue")

def draw_score_panel(score_obj, next_piece_name):
    text = Text()
    text.append(f"\nSCORE\n", style="bold white")
    text.append(f"{score_obj.score}\n\n", style="bold yellow")
    text.append(f"LEVEL\n", style="bold white")
    text.append(f"{score_obj.level}\n\n", style="bold cyan")
    text.append(f"NEXT\n", style="bold white")
    text.append(f"{next_piece_name}\n", style="bold green")
    
    return Panel(Align.center(text), title="STATUS", border_style="white")