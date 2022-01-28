import sys
import time
import win32pipe
import win32file
import pywintypes


def get_pipedata():
    quit = False

    while not quit:
        try:
            handle = win32file.CreateFile(
                r"\\.\pipe\dota_data",
                win32file.GENERIC_READ | win32file.GENERIC_WRITE,
                0,
                None,
                win32file.OPEN_EXISTING,
                0,
                None,
            )
            res = win32pipe.SetNamedPipeHandleState(
                handle, win32pipe.PIPE_READMODE_MESSAGE, None, None
            )

            result, dota_data = win32file.ReadFile(handle, 64 * 1024)
            return dota_data
        except pywintypes.error as e:
            if e.args[0] == 2:
                time.sleep(1)
            elif e.args[0] == 109:
                quit = True


if __name__ == "__main__":
    pass
