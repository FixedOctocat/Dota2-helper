import sys
import time
import json
import win32pipe
import win32file
import pywintypes


def get_data():
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
            return json.loads(dota_data.decode("utf-8"))
        except pywintypes.error as e:
            if e.args[0] == 2:
                time.sleep(1)
            elif e.args[0] == 109:
                quit = True


if __name__ == "__main__":
    pass
