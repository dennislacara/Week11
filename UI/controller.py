import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.crea_grafo()
        if not self._model.G:
            print('grafo non creato')

    def handleCompConnessa(self,e):
        if not self._model.G:
            print('grafo non creato')
            return
        valore_txt = self._view._txtIdOggetto.value
        if not valore_txt or not valore_txt.isdigit():
            print('Inserire id valido')
            return

        valore_convertito = int(valore_txt)
        if valore_convertito in self._model.G.nodes():
            print('ID ESISTENTE')
        else:
            print('ID NON ESISTENTE')
            return

        #gestione view
        nodi_comp_conn = self._model.calcola_componente_conn(valore_convertito)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Ecco i nodi appartenenti alla componente connessa dell'ID inserito:"))
        for tupla in nodi_comp_conn:
            self._view.txt_result.controls.append(ft.Text(f'{tupla[0]}  ---> PESO: {tupla[1]}'))

        self._view.update_page()

