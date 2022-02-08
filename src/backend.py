import re
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


def rosha_state(time, roshan_death_time) -> [-1, 0, 1]:
    """
        -1 - roshan definitely dead
         0 - roshan possibly alive
         1 - roshan definitely alive
    """

    delta = time - roshan_death_time

    if delta < 8 * 60:
        return -1
    elif (delta >= 8 * 60) or (delta <= 11 * 60):
        return 0
    elif delta > 11 * 60:
        return 1

def read_server_log_file():
    SERVER_LOG_FILE = "D:\\SteamLibrary\\steamapps\\common\\dota 2 beta\\game\\dota\\server_log.txt"

    with open(SERVER_LOG_FILE) as file:
        for line in file:
            pass
        last_line = line

    profile_ids = re.findall(r'U:\d:\d{,15}', last_line)
    profile_ids = [profile_id.split(":")[2] for profile_id in profile_ids]


if __name__ == "__main__":
    read_server_log_file()
