import math
import PySimpleGUI as sg

from backend import get_data


def overlay_gold_helper():
    text_gmp = "gpm:"
    text_xpm = "xpm:"
    GRAPH_SIZE = (500, 500)
    DATA_SIZE = (500, 500)
    GRAPH_SIZE_PIE_CHART = (500, 100)
    BAR_SPACING = 40
    EDGE_OFFSET = 3
    VERTICAL_OFFSET = 70

    HORIZONTAL_OFFSET = 43
    BAR_WIDTH = 40

    sg.SetOptions(margins=(0,0), element_padding=(0,0))
    graph = sg.Graph(GRAPH_SIZE, (0, 0), DATA_SIZE, background_color='red', key='-GRAPH-')
    layout = [
        [graph],
        [sg.Button(' change view ')],
        [sg.Button(' hide '), sg.Button(' exit ')]
    ]

    flag = True

    window = sg.Window('ищу тяночку, кандидатки звоните по телефону 89851144689', layout, background_color='red', transparent_color='red', no_titlebar=True, alpha_channel=.5, grab_anywhere=True, keep_on_top=True).Finalize()

    while True:
        data = get_data()
    
        passive_gold = data["gold_from_income"]
        gold_from_crips = data["gold_from_creep_kills"]
        gold_from_heroes = data["gold_from_hero_kills"]
        sum_gold = passive_gold + gold_from_crips + gold_from_heroes
        print(passive_gold)

        event, values = window.Read()
        if event is None or event == ' exit ':
            break
        if event == ' change view ':
            flag = not flag
        if flag:
            print(1)
            graph.Erase()
            graph.DrawRectangle(top_left=(0, 70 + 500* max(gold_from_crips/sum_gold, gold_from_heroes/sum_gold, passive_gold/sum_gold)), bottom_right=(120, 0), fill_color='grey') ##общий фон
            graph.DrawRectangle(top_left=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET, 500*(gold_from_crips)/(sum_gold) + VERTICAL_OFFSET), ##крипы
                                bottom_right=(BAR_SPACING + EDGE_OFFSET + BAR_WIDTH - HORIZONTAL_OFFSET, VERTICAL_OFFSET),
                                fill_color='pink')
            graph.DrawText(text=gold_from_crips,
                           color='black',
                           location=(BAR_SPACING + 20 - HORIZONTAL_OFFSET, VERTICAL_OFFSET + 25))
            graph.DrawText(text=round(gold_from_crips/sum_gold * 100),
                           color='black',
                           location=(BAR_SPACING + 20 - HORIZONTAL_OFFSET, VERTICAL_OFFSET + 15))
            graph.DrawText(text='%',
                           color='black',
                           location=(BAR_SPACING + 30 - HORIZONTAL_OFFSET, VERTICAL_OFFSET + 15))


            graph.DrawRectangle(top_left=(2 * BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET, 500*(gold_from_heroes)/(sum_gold) + VERTICAL_OFFSET), ##герои
                                bottom_right=(2 * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH - HORIZONTAL_OFFSET, VERTICAL_OFFSET),
                                fill_color='green')
            graph.DrawText(text=gold_from_heroes,
                           color='black',
                           location=(2 * BAR_SPACING + 20 - HORIZONTAL_OFFSET, VERTICAL_OFFSET + 25))
            graph.DrawText(text=round(gold_from_heroes/sum_gold * 100),
                           color='black',
                           location=(2 * BAR_SPACING + 20 - HORIZONTAL_OFFSET, VERTICAL_OFFSET + 15))
            graph.DrawText(text='%',
                           color='black',
                           location=(2 * BAR_SPACING + 30 - HORIZONTAL_OFFSET, VERTICAL_OFFSET + 15))

            graph.DrawRectangle(top_left=(3 * BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET, 500*(passive_gold)/(sum_gold) + VERTICAL_OFFSET), ##пассивный доход
                                bottom_right=(3 * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH - HORIZONTAL_OFFSET, VERTICAL_OFFSET),
                                fill_color='orange')
            graph.DrawText(text=passive_gold,
                           color='black',
                           location=(3 * BAR_SPACING + 20 - HORIZONTAL_OFFSET, VERTICAL_OFFSET + 25))
            graph.DrawText(text=round(passive_gold/sum_gold * 100),
                           color='black',
                           location=(3 * BAR_SPACING + 20 - HORIZONTAL_OFFSET, VERTICAL_OFFSET + 15))
            graph.DrawText(text='%',
                           color='black',
                           location=(3 * BAR_SPACING + 30 - HORIZONTAL_OFFSET, VERTICAL_OFFSET + 15))

            graph.DrawText(text=text_xpm,                           ## описание к графику
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 20, 15))
            graph.DrawText(text='значение',
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 20 + 45, 15))

            graph.DrawText(text=text_gmp,
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 19, 25))
            graph.DrawText(text='значение',
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 19 + 45, 25))

            graph.DrawText(text='orange : passive gold',
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 59, 35))

            graph.DrawText(text='green : from heroes',
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 54.5, 45))

            graph.DrawText(text='pink : from crips',
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 48, 55))
        else:
            graph.erase()
            graph.DrawRectangle(top_left=(0,200), bottom_right=(120,0), fill_color='grey')
            graph.DrawArc((0, 70), (DATA_SIZE[0] - 380, DATA_SIZE[1] - 300), extent=(gold_from_crips/sum_gold)*360, start_angle=0, arc_color='pink', fill_color='pink')
            graph.DrawArc((0, 70), (DATA_SIZE[0] - 380, DATA_SIZE[1] - 300), extent=(gold_from_heroes/sum_gold)*360, start_angle=(gold_from_crips/sum_gold)*360, arc_color='green', fill_color='green')
            graph.DrawArc((0, 70), (DATA_SIZE[0] - 380, DATA_SIZE[1] - 300), extent=(passive_gold/sum_gold)*360, start_angle=(gold_from_crips/sum_gold)*360 + (gold_from_heroes/sum_gold)*360, arc_color='orange', fill_color='orange')

            graph.DrawText(text=gold_from_crips,
                           color='black',

                           location=(62 + 31 * math.cos((gold_from_crips/sum_gold) * math.pi),
                                     136 + 31 * math.sin((gold_from_crips/sum_gold) * math.pi)))



            graph.DrawText(text=gold_from_heroes,
                           color='black',
                           location=(62 + 31 * (math.cos((gold_from_heroes / sum_gold) * math.pi + (gold_from_crips/sum_gold)*math.pi*2)),
                                     136 + 31 * (math.sin((gold_from_heroes / sum_gold) * math.pi + (gold_from_crips/sum_gold)*math.pi*2))))


            graph.DrawText(text=passive_gold,
                           color='black',
                           location=(62 + 31 * (math.cos((passive_gold / sum_gold) * math.pi + (gold_from_crips/sum_gold)*math.pi*2 + (gold_from_heroes/sum_gold)*math.pi*2)),
                                     136 + 31 * (math.sin((passive_gold / sum_gold) * math.pi + (gold_from_crips/sum_gold)*math.pi*2 + (gold_from_heroes/sum_gold)*math.pi*2))))


            graph.DrawText(text=text_xpm,  ## описание к графику
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 20, 15))
            graph.DrawText(text='значение',
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 20 + 45, 15))

            graph.DrawText(text=text_gmp,
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 19, 25))
            graph.DrawText(text='значение',
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 19 + 45, 25))

            graph.DrawText(text='orange : passive gold',
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 59, 35))

            graph.DrawText(text='green : from heroes',
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 54.5, 45))

            graph.DrawText(text='pink : from crips',
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 48, 55))

        if event == ' hide ':
            graph.erase()
            graph.DrawRectangle(top_left=(0, 70), bottom_right=(120, 0), fill_color='grey')
            graph.DrawText(text=text_xpm,  ## описание к графику
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 20, 15))
            graph.DrawText(text='значение',
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 20 + 45, 15))

            graph.DrawText(text=text_gmp,
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 19, 25))
            graph.DrawText(text='значение',
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 19 + 45, 25))

            graph.DrawText(text=passive_gold,
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 13, 35))
            graph.DrawText(text=' : passive gold',
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 59, 35))

            graph.DrawText(text=gold_from_heroes,
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 13, 45))
            graph.DrawText(text=' : from heroes',
                               location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 58, 45))

            graph.DrawText(text=gold_from_crips,
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 13, 55))
            graph.DrawText(text=' : from crips',
                           location=(BAR_SPACING + EDGE_OFFSET - HORIZONTAL_OFFSET + 53, 55))
    window.Close()


if __name__ == "__main__":
    overlay_gold_helper()
