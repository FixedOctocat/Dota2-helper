import sys
import time
import json
import dota2gsi
import win32pipe
import win32file
import pywintypes


def send_data(data):
    pipe = win32pipe.CreateNamedPipe(
        r"\\.\pipe\dota_data",
        win32pipe.PIPE_ACCESS_DUPLEX,
        win32pipe.PIPE_TYPE_MESSAGE
        | win32pipe.PIPE_READMODE_MESSAGE
        | win32pipe.PIPE_WAIT,
        1,
        65536,
        65536,
        0,
        None,
    )

    try:
        win32pipe.ConnectNamedPipe(pipe, None)
        dota_data = str.encode(f"{data}")
        win32file.WriteFile(pipe, dota_data)
    finally:
        win32file.CloseHandle(pipe)


def game_state(last_state, state):
    dota_data = {}

    try:
        dota_data['status'] = 1

        dota_data['time'] = state["map"]["clock_time"]

        dota_data['gold'] = state["player"]["gold"]
        dota_data['gold_reliable'] = state["player"]["gold_reliable"]
        dota_data['gold_unreliable'] = state["player"]["gold_unreliable"]
        dota_data['gold_from_hero_kills'] = state["player"]["gold_from_hero_kills"]
        dota_data['gold_from_creep_kills'] = state["player"]["gold_from_creep_kills"]
        dota_data['gold_from_income'] = state["player"]["gold_from_income"]
        dota_data['gold_from_shared'] = state["player"]["gold_from_shared"]

        dota_data['gpm'] = state["player"]["gpm"]
        dota_data['xpm'] = state["player"]["xpm"]
    except:
        dota_data['status'] = 0

    try:
        send_data(json.dumps(dota_data))
    except:
        pass


def main():
    server = dota2gsi.Server()
    server.on_update(game_state)
    server.start()


if __name__ == "__main__":
    main()
