This is a project based on my personal need. \
Sometimes when im watching a movie or something and don't want to turn off my other monitors, i need a natural cover for them. Or sometimes i need a quick source of light when my room is dark. \
That's why i created this small project, which i have used intensively since i built it.

## ScreenDisplay
On start, this program displays a blank black window on every monitor currently connected to your computer.

By pressing the Enter key, you can switch between the states defined at the top of `screenDisplay.py`. By default, it only switches between a black and white screen, but you can edit `STATES` to define your own colors.

After starting, you can use the windows key or alt+tab to show the program you want.

Pressing Space brings all of this program's windows to the front, hiding every open program behind it.

To close the program, make sure the program's windows are focused (click into them) and then press Escape.

### Different Versions
There are the files `screenDisplay.py` and `screenDisplay.pyw`. The former is the basic program, the latter is a special file format which starts the program without a console. For general use, you should use the pyw-file, since you normally don't need the console if you aren't a developer.

I also added a shortcut file to my taskbar which executes the pyw-file, so i can access it easier.
