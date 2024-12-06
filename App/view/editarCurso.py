from PyQt5.QtWidgets import QWidget, QCompleter
from PyQt5.QtCore import QTimer, pyqtSlot

from App.controller.area import listarAreas
from App.controller.curso import buscarCursosId

from App.controller.curso import atualizarCurso
from App.controller.utils import validarAcao
from PyQt5.uic import loadUi

class EditarCurso(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarCurso.ui',self)
        self.dicionarioDeAreas = listarAreas()

        self.dicionarioDeCursos = buscarCursosId()
        self.dicionarioDeOfertas = buscarCursosId(3)
        self.popularJanela()

    def popularJanela(self):
        self.comboxArea()
        # self.comboOferta()

    @pyqtSlot()
    def on_btnEditarCurso_clicked(self):
        idCurso = self.dicionarioDeCursos[info[0]]
        info = self.getEditarCurso()
        if atualizarCurso(idCurso, info):
            validarAcao()

    def comboxArea(self):
        areas = self.dicionarioDeAreas.keys()
        self.campoArea.addItems(areas)
        print(f"Lista completa: {self.dicionarioDeCursos}")

    def comboOferta(self):
        dados = self.dicionarioDeCursos.keys()
        self.ofertaCurso.addItems(dados)

    def getEditarCurso(self):
        oferta = self.ofertaCurso.currentText().strip()
        nome = self.nomeCurso.text().strip()
        area = self.campoArea.currentText().strip()
        periodo = self.periodoCurso.currentText().strip()
        carga = self.cargaCurso.text().strip()
        horas = self.horasPorDia.text().strip()
        alunos = self.quantidadeAlunos.text().strip()
        return(nome, oferta, periodo, carga, area, horas, alunos)

    def validandoDados(self):
        self.respostas.setText('EDITANDO...')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostas))

    def dadosInvalidos(self):
        texto = 'DADOS INCOMPLETOS.'
        self.respostas.setText(texto)
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostas))

    def limparCampos(self, campo):
        campo.clear()
        