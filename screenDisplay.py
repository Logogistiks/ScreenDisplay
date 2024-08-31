"""Creates a fullscreen window on each monitor with the first background state.
Press Enter or Numpad Enter to change the background color.
Press Space to bring all windows to the front.
Press Escape to close the program."""

import tkinter as tk
from screeninfo import get_monitors

STATES = {0: "#000000", 1: "#FFFFFF"} #edit here
state = 0
timetoggle = False

class Window:
    def __init__(self, title: str, bg: str, posX: int=None, posY: int=None, SizeX: int=None, SizeY: int=None, fullscreen=False) -> None:
        self.window = tk.Toplevel(bg=bg)
        if all(attr != None for attr in (posX, posY, SizeX, SizeY)):
            self.window.geometry(f"{SizeX}x{SizeY}+{posX}+{posY}")
        self.window.title(title)
        if fullscreen:
            self.window.overrideredirect(True)
            self.window.state("zoomed")

    def change_bg(self, bg: str) -> None:
        self.window.configure(bg=bg)

root = tk.Tk()
root.withdraw() # Hide the main root window

windows: list[Window] = []
for i, m in enumerate(get_monitors()): # Create a window for each monitor
    windows.append(Window(f"Monitor {i}", STATES[state], m.x, m.y, 0, 0, fullscreen=True))

def change_state() -> None: # Cycle through states
    global state
    state = (state + 1) % len(STATES)
    for window in windows:
        window.change_bg(STATES[state])

def put_on_top() -> None:
    for window in windows:
        window.window.lift()

root.bind_all("<Escape>", lambda _: root.quit()) # Exit program
root.bind_all("<Return>", lambda _: change_state()) # Enter or Numpad Enter to change color
root.bind_all("<space>", lambda _: put_on_top()) # Put windows on top

root.mainloop()