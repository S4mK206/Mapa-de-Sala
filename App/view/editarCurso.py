from PyQt5.QtWidgets import QWidget, QCompleter
from PyQt5.QtCore import QTimer, pyqtSlot

from App.controller.area import listarAreas
from App.controller.curso import listarCursos
from App.controller.curso import listarOfertas

from App.controller.curso import atualizarCurso
from App.controller.utils import validarAcao
from PyQt5.uic import loadUi

class EditarCurso(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarCurso.ui',self)
        self.dicionarioDeAreas = listarAreas()
        self.dicionarioDeCursos = listarCursos()
        self.popularJanela()

    def popularJanela(self):
        self.comboxArea()
        self.autoCompleteOferta()
        # self.comboxCurso()

    @pyqtSlot()
    def on_btnEditarCurso_clicked(self):
        info = self.getEditarCurso()
        idCurso = self.dicionarioDeCursos[info[0]]
        if atualizarCurso(idCurso, info):
            validarAcao()

    def comboxArea(self):
        areas = self.dicionarioDeAreas.keys()
        self.campoArea.addItems(areas)
        print(f"Lista de Areas: {self.dicionarioDeAreas}")

    # def comboxCurso(self):
    #     cursos = self.dicionarioDeCursos.keys()
    #     self.alterarCurso.addItem(cursos)
    #     print(f"Lista de Cursos: {self.dicionarioDeCursos}")

    def getEditarCurso(self):
        nome = self.nomeCurso.text().strip()
        oferta = self.ofertaCurso.text().strip()
        periodo = self.periodoCurso.currentText().strip()
        carga = self.cargaCurso.text().strip()
        # area = self.campoArea.currentText().strip()
        horas = self.horasPorDia.text().strip()
        alunos = self.quantidadeAlunos.text().strip()
        # curso = self.alterarCurso.currentText().strip()
        
        return(nome, oferta, periodo, carga, horas, alunos)
        # return(nome, oferta, area, periodo, carga, curso, horas, alunos)

    def autoCompleteOferta(self):
        dados = [str(row[0]) for row in listarOfertas()]
        completer = QCompleter(dados)
        completer.setCaseSensitivity(False)
        self.ofertaCurso.setCompleter(completer)
    
    def validandoDados(self):
        self.respostas.setText('EDITANDO...')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostas))

    def dadosInvalidos(self):
        texto = 'DADOS INCOMPLETOS.'
        self.respostas.setText(texto)
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostas))

    def limparCampos(self, campo):
        campo.clear()
        