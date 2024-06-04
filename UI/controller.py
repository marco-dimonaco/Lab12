import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        nazioni = self._model.getAllCountries()
        for n in nazioni:
            self._listCountry.append(n)
            self._view.ddcountry.options.append(ft.dropdown.Option(n))

        for anno in range(2015, 2019):
            self._listYear.append(anno)
            self._view.ddyear.options.append(ft.dropdown.Option(str(anno)))
        self._view.update_page()

    def handle_graph(self, e):
        country = self._view.ddcountry.value
        year = str(self._view.ddyear.value)
        self._model.buildGraph(country, year)
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {len(self._model._grafo.nodes)} "
                                                      f"Numero di archi: {len(self._model._grafo.edges)}"))
        self._view.update_page()

    def handle_volume(self, e):
        volumi = self._model.getVolumiVendita()
        for k, v in volumi.items():
            if v > 0:
                self._view.txtOut2.controls.append(ft.Text(f"{k} --> {v}"))
        self._view.update_page()

    def handle_path(self, e):
        pass
