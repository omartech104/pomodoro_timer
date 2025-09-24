import time, os, sys
from rich.console import Console
from rich.progress import Progress

WORK = 25
SHORT_BREAK= 5
LONG_BREAK = 15

WORK_MIN = WORK * 60
SHORT_BREAK_MIN = SHORT_BREAK * 60
LONG_BREAK_MIN = LONG_BREAK * 60

def clear_console():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    elif sys.platform == "win32":
        os.system("cls")
    else:
        Console.print("[bold red]GO AWAY !!!!!!!!!!")

console = Console()
clear_console()
console.print("Pomodoro Timer [bold cyan]started")

progress = Progress()
progress.start()

with Progress() as progress:
    task = progress.add_task(f"[green]Working for {WORK_MIN/60} min...", total=100)

    start = time.time()
    end = start + WORK_MIN

    while not progress.finished:
        now = time.time()
        elapsed = now - start
        percent = (elapsed / WORK_MIN) * 100

        progress.update(task, completed=percent)

        if now >= end:
            break

        time.sleep(0.5)
