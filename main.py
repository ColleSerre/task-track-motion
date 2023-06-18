from asciiplot import asciiize, Color


def show_graph():
    data = []
    with open("log.csv") as f:
        for i in f.readlines():
            data.append(i.strip().split(","))
        f.close()

    print(asciiize(
        [int(i[1]) for i in data],
        x_axis_tick_labels=[i[0] for i in data],
        inter_points_margin=5,
        background_color=Color.GREY_7,
        title='Motion Tasks Completed per day',
        title_color=Color.MEDIUM_PURPLE,
        label_color=Color.MEDIUM_PURPLE,
        x_axis_description='Time',
        y_axis_description='Completed Tasks',
        center_horizontally=True
    ))


show_graph()
