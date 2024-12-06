from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer, pyqtSlot

from App.controller.curso import listarCurso, buscarCursosId

from PyQt5.uic import loadUi

class EditarCurso(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarCurso.ui',self)
        self.dicionarioDeCursos = listarCurso()
        self.popularJanela()
        self.ofertaCurso.currentIndexChanged.connect(self.popularCurso)

    def popularJanela(self):
        self.comboOferta()

    @pyqtSlot()
    def on_btnEditarCurso_clicked(self):
        ...

    def comboOferta(self):
        dados = self.dicionarioDeCursos.keys()
        print(dados)
        self.ofertaCurso.addItems(dados)

    def popularCurso(self):
        idCurso = self.getIdOferta()
        info = buscarCursosId(idCurso)
        nome = info['nome']
        cargaHoraria = info['cargaHoraria']

    # def popularSala(self):
    #     idSalaCombobox = self.getIdSala()
    #     info = buscarSalaId(idSalaCombobox)
    #     nomeSala = info["nome"]
    #     tipoSala = info["tipo"]
    #     predio = info["predio"]
    #     equipamentos = info["equipamentos"]
    #     capacidade = info["capacidade"]
    #     obs = info["observacao"]
    #     if (nomeSala, tipoSala, predio, equipamentos, capacidade, obs):
    #         self.tipoSala.setCurrentText(tipoSala)
    #         self.nomePredio.setCurrentText(predio)
    #         self.tipoEquipamento.setText(equipamentos)
    #         self.mediaCapacidade.setText(str(capacidade))
    #         self.feedbackText.setText(obs)

    # def getEditarCurso(self):
    #     oferta = self.ofertaCurso.currentText().strip()
    #     nome = self.nomeCurso.text().strip()
    #     area = self.campoArea.currentText().strip()
    #     periodo = self.periodoCurso.currentText().strip()
    #     carga = self.cargaCurso.text().strip()
    #     horas = self.horasPorDia.text().strip()
    #     alunos = self.quantidadeAlunos.text().strip()
    #     return(nome, oferta, periodo, carga, area, horas, alunos)

    def getIdOferta(self):
        oferta = self.ofertaCurso.currentText()
        return self.dicionarioDeCursos.get(oferta)