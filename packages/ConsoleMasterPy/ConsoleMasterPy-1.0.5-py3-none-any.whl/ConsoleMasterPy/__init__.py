import os
import sys
import datetime
import ctypes
from ctypes import wintypes
import random

from sty import bg, fg, rs
import cursor

if sys.platform == "win32":
    os.system("color")

LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11


class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    def __init__(self, x, y):
        self.X = x
        self.Y = y


class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_ulong),
        ("nFont", ctypes.c_ulong),
        ("dwFontSize", COORD),
        ("FontFamily", ctypes.c_uint),
        ("FontWeight", ctypes.c_uint),
        ("FaceName", ctypes.c_wchar * LF_FACESIZE),
    ]


class CONSOLE_SCREEN_BUFFER_INFOEX(ctypes.Structure):
    _fields_ = (
        ("cbSize", wintypes.ULONG),
        ("dwSize", COORD),
        ("dwCursorPosition", COORD),
        ("wAttributes", wintypes.WORD),
        ("srWindow", wintypes.SMALL_RECT),
        ("dwMaximumWindowSize", COORD),
        ("wPopupAttributes", wintypes.WORD),
        ("bFullscreenSupported", wintypes.BOOL),
        ("ColorTable", wintypes.DWORD * 16),
    )

    def __init__(self, *args, **kwds):
        super(CONSOLE_SCREEN_BUFFER_INFOEX, self).__init__(*args, **kwds)
        self.cbSize = ctypes.sizeof(self)


def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            timestamp = datetime.datetime.now().isoformat()
            with open("log.txt", "a") as f:
                f.write(timestamp)
                f.write(f" {func.__name__} {e}\n")

    return inner_function


class ConsoleMaster:

    title = ""
    font_size = ""
    window_width = ""
    window_height = ""

    def __init__(
        self, title="New Window", font_size=17, window_width=30, window_height=25
    ):
        self.change_windows_title(title)
        self.change_pixel_size(font_size)
        self.change_windows_size(window_width, window_height)
        self.hide_cursor()

    @exception_handler
    def pause(self):
        input()

    @exception_handler
    def print_with_color(self, rgb_background, rgb_foreground, element_to_print):
        print(
            "".join(
                [
                    fg(rgb_foreground[0], rgb_foreground[1], rgb_foreground[2]),
                    bg(rgb_background[0], rgb_background[1], rgb_background[2]),
                    element_to_print,
                    rs.all,
                ]
            ),
            end="",
            flush=True,
        )

    @exception_handler
    def change_console_color(self, background_color, foreground_color):
        console_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        console_screen_information = CONSOLE_SCREEN_BUFFER_INFOEX()
        ctypes.windll.kernel32.GetConsoleScreenBufferInfoEx(
            console_handle, ctypes.byref(console_screen_information)
        )
        console_screen_information.srWindow.Bottom += 1
        console_screen_information.ColorTable[0] = (
            background_color[0]
            + (background_color[1] * 256)
            + (background_color[2] * 256 * 256)
        )
        console_screen_information.ColorTable[7] = (
            foreground_color[0]
            + (foreground_color[1] * 256)
            + (foreground_color[2] * 256 * 256)
        )
        ctypes.windll.kernel32.SetConsoleScreenBufferInfoEx(
            console_handle, ctypes.byref(console_screen_information)
        )
        os.system("cls")

    @exception_handler
    def go_xy(self, x, y):
        INIT_POS = COORD(x, y)
        STD_OUTPUT_HANDLE = -11
        hOut = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        ctypes.windll.kernel32.SetConsoleCursorPosition(hOut, INIT_POS)

    @exception_handler
    def change_pixel_size(self, size):
        font = CONSOLE_FONT_INFOEX()
        font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
        # font.nFont = 12
        font.dwFontSize.X = size
        font.dwFontSize.Y = size
        # font.FontFamily = 54
        # font.FontWeight = 400
        font.FaceName = "Terminal"

        handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        ctypes.windll.kernel32.SetCurrentConsoleFontEx(
            handle, ctypes.c_long(False), ctypes.pointer(font)
        )
        self.font_size = size

    @exception_handler
    def change_windows_size(self, width, height):
        cmd = "mode " + str(width) + "," + str(height)
        os.system(cmd)
        self.window_width = width
        self.window_height = height

    @exception_handler
    def show_cursor(self):
        cursor.show()

    @exception_handler
    def hide_cursor(self):
        cursor.hide()

    @exception_handler
    def change_windows_title(self, title):
        os.system("title " + str(title))
        self.title = title

    @exception_handler
    def clean_zone(self, x_coord_init, y_coord_init, x_coord_end, y_coord_end):
        for y in range(y_coord_init, y_coord_end):
            self.go_xy(x_coord_init, y)
            for x in range(x_coord_init, x_coord_end):
                print(" ", end="", flush=True)

    @exception_handler
    def clean_windows(self):
        os.system("cls")


# aeiou
# bcdfghjklmnpqrstvwxyz
# AEIOU
# BCDFGHJKLMNPQRSTVWXYZ
def generate_name():
    bloc_1 = "aeiou"
    bloc_2 = "bcdfghjklmnpqrstvwxyz"
    bloc_3 = "AEIOU"
    bloc_4 = "BCDFGHJKLMNPQRSTVWXYZ"
    name = ""

    option = random.randint(0, 5)
    # print(str(option) + "-")
    if option < 2:
        name += random.choice(bloc_3)
    elif option < 5:
        name += random.choice(bloc_4) + random.choice(bloc_1)
    else:
        name += random.choice(bloc_4) + random.choice(bloc_1) + random.choice(bloc_2)

    name_long = random.randint(2, 4)
    for i in range(name_long):
        option = random.randint(0, 5)
        # print(str(option) + "+")
        if option < 2:
            name += random.choice(["'", "", "", ""]) + random.choice(bloc_1)
        elif option < 5:
            name += random.choice(bloc_2) + random.choice(bloc_1)
        else:
            name += (
                random.choice(bloc_2) + random.choice(bloc_1) + random.choice(bloc_2)
            )

    if random.randint(0, 1):
        if random.randint(0, 1):
            option = random.randint(0, 2)
            # print(str(option) + "_")
            if option == 0:
                name += " " + random.choice(bloc_3)
            elif option == 1:
                name += " " + random.choice(bloc_4) + random.choice(bloc_1)
            elif option == 2:
                name += " " + (
                    random.choice(bloc_4)
                    + random.choice(bloc_1)
                    + random.choice(bloc_2)
                )
        name += " "
        option = random.randint(0, 2)
        # print(str(option) + "*")
        if option == 0:
            name += random.choice(bloc_3)
        elif option == 1:
            name += random.choice(bloc_4) + random.choice(bloc_1)
        elif option == 2:
            name += (
                random.choice(bloc_4) + random.choice(bloc_1) + random.choice(bloc_2)
            )
        name_long = random.randint(2, 4)
        for i in range(name_long):
            option = random.randint(0, 5)
            # print(str(option) + "/")
            if option < 2:
                name += random.choice(["'", "", "", ""]) + random.choice(bloc_1)
            elif option < 5:
                name += random.choice(bloc_2) + random.choice(bloc_1)
            else:
                name += (
                    random.choice(bloc_2)
                    + random.choice(bloc_1)
                    + random.choice(bloc_2)
                )
    return name
