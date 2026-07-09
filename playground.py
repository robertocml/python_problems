import os
import random
import time
import sys

# ANSI escape codes
RESET   = "\033[0m"
BOLD    = "\033[1m"
CLEAR   = "\033[2J\033[H"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

GREEN_SHADES = [
    "\033[38;5;22m",   # verde oscuro
    "\033[38;5;28m",
    "\033[38;5;34m",
    "\033[38;5;40m",
    "\033[38;5;46m",   # verde brillante
    "\033[38;5;82m",
    "\033[38;5;118m",
    "\033[97m",        # blanco (cabeza de gota)
]

KATAKANA = (
    "アイウエオカキクケコサシスセソタチツテトナニヌネノ"
    "ハヒフヘホマミムメモヤユヨラリルレロワヲン"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"
)

def get_terminal_size():
    size = os.get_terminal_size()
    return size.columns, size.lines

def move_cursor(x, y):
    print(f"\033[{y};{x}H", end="")

def color_char(char, intensity):
    shade = GREEN_SHADES[min(intensity, len(GREEN_SHADES) - 1)]
    return f"{shade}{char}{RESET}"

class Drop:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.x = random.randint(1, cols)
        self.y = random.uniform(-rows, 0)
        self.speed = random.uniform(0.3, 1.2)
        self.length = random.randint(5, 20)
        self.chars = [random.choice(KATAKANA) for _ in range(self.length)]
        self.active = True

    def update(self):
        self.y += self.speed
        if random.random() < 0.05:
            idx = random.randint(0, self.length - 1)
            self.chars[idx] = random.choice(KATAKANA)
        if self.y - self.length > self.rows:
            self.active = False

    def draw(self):
        head = int(self.y)
        for i in range(self.length):
            row = head - i
            if 1 <= row <= self.rows:
                char = self.chars[i % len(self.chars)]
                if i == 0:
                    intensity = 7
                elif i < 3:
                    intensity = 6
                elif i < 6:
                    intensity = 5
                else:
                    intensity = max(0, 4 - (i - 6) // 3)
                move_cursor(self.x, row)
                print(color_char(char, intensity), end="", flush=False)

        erase_row = head - self.length
        if 1 <= erase_row <= self.rows:
            move_cursor(self.x, erase_row)
            print(" ", end="", flush=False)


def banner_text(cols, rows):
    lines = [
        "  ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗",
        "  ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║",
        "  ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║",
        "  ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║",
        "  ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║",
        "  ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝",
        "",
        "        >> Saludos desde Codeando Unidos <<",
    ]
    start_row = rows // 2 - len(lines) // 2
    start_col_offset = cols // 2 - 30
    for i, line in enumerate(lines):
        row = start_row + i
        if 1 <= row <= rows:
            move_cursor(max(1, start_col_offset), row)
            if i < 6:
                print(f"\033[38;5;46m{BOLD}{line}{RESET}", end="", flush=False)
            else:
                print(f"\033[38;5;82m{BOLD}{line}{RESET}", end="", flush=False)


def main():
    print(HIDE_CURSOR, end="")
    print(CLEAR, end="")

    try:
        drops = []
        frame = 0

        while True:
            cols, rows = get_terminal_size()
            frame += 1

            # Agregar nuevas gotas
            if random.random() < 0.4:
                drops.append(Drop(cols, rows))

            # Limitar número de gotas activas
            drops = [d for d in drops if d.active]
            if len(drops) > cols // 2:
                drops = drops[-(cols // 2):]

            # Dibujar todo
            for drop in drops:
                drop.update()
                drop.draw()

            # Banner cada 60 frames
            if frame % 60 < 40:
                banner_text(cols, rows)

            sys.stdout.flush()
            time.sleep(0.05)

    except KeyboardInterrupt:
        print(CLEAR, end="")
        print(SHOW_CURSOR, end="")
        move_cursor(1, 1)
        print(f"\033[38;5;46m{BOLD}¡Hasta la próxima! 👾{RESET}")


if __name__ == "__main__":
    main()
