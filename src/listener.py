import sys
import time
import dota2gsi
import win32pipe
import win32file
import pywintypes


def send_pipedata(data):
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
    time = state["map"]["clock_time"]
    pipe_server(time)


def main():
    server = dota2gsi.Server()
    server.on_update(game_state)
    server.start()


if __name__ == "__main__":
    main()
