from matplotlib.figure import Figure

import solara


@solara.component_vue("vue_files/viewlistener.vue")
def ViewListener(view_data=None, on_view_data=None, children=[], style={}):
    ...


@solara.component
def Plot1():
    dpi = 100
    view_data = solara.use_reactive({"width": 800, "height": 600})
    width, height = view_data.value["width"], view_data.value["height"]
    fig = Figure(figsize=(width / dpi, height / dpi), dpi=dpi)
    ax = fig.subplots()

    ax.plot([1, 2, 3], [1, 4, 9])
    with ViewListener(view_data=view_data.value, on_view_data=view_data.set, style={"width": "100%", "height": "40vh"}):
        solara.FigureMatplotlib(fig)


@solara.component
def Plot2():
    dpi = 100
    view_data = solara.use_reactive({"width": 800, "height": 600})
    width, height = view_data.value["width"], view_data.value["height"]
    fig = Figure(figsize=(width / dpi, height / dpi), dpi=dpi)
    ax = fig.subplots()

    ax.bar([1, 2, 3], [1, 4, 9])
    with ViewListener(view_data=view_data.value, on_view_data=view_data.set, style={"width": "100%", "height": "40vh"}):
        solara.FigureMatplotlib(fig)


@solara.component
def Page():
    with solara.ColumnsResponsive(12, 12, 6):
        with solara.Card("This months profits"):
            Plot1()
        with solara.Card("This months expenses"):
            Plot2()
