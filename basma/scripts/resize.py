import termios
import struct
import fcntl
import os

def set_winsize(fd, row, col, xpix=0, ypix=0):
    winsize = struct.pack("HHHH", row, col, xpix, ypix)
    fcntl.ioctl(fd, termios.TIOCSWINSZ, winsize)

set_winsize(os.sys.stdout, 30, 100)
