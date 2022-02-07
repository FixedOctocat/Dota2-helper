import sys
import time
import json
import win32pipe
import win32file
import pywintypes
import PySimpleGUI as sg


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


def main():
    text_gmp = "Gold per minute:"
    text_gold_crips = "Gold from crips:"
    text_gold_heroes = "Gold from heroes:"
    text_gold_passive = "passive gold:"

    sg.SetOptions(margins=(0, 0), element_padding=(0, 0))

    layout = [
        [
            sg.Graph(
                canvas_size=(1500, 300),
                graph_bottom_left=(0, 0),
                graph_top_right=(0, 0),
                background_color="red",
                key="graph",
            )
        ],
        [sg.Text(text_gmp)],
        [sg.Text(text_gold_crips)],
    ]

    window = sg.Window(
        "Graph test",
        layout,
        background_color="red",
        transparent_color="red",
        no_titlebar=True,
        alpha_channel=0.5,
        grab_anywhere=True,
        keep_on_top=True,
    ).Finalize()

    graph = window.FindElement("graph")  # type: sg.Graph
    while True:
        event, values = window.Read()
        if event is None:
            break


if __name__ == "__main__":
    main()
