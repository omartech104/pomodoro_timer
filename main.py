import time, os, sys
from rich.console import Console
from rich.progress import progress

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15

def clear_console():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    if sys.platform == "win32":
        os.system("cls")

console = Console()

console.print("Pomodoro Timer [bold cyan]started")


