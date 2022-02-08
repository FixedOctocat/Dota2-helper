import PySimpleGUI as sg


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
