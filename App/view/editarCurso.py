from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer, pyqtSlot
from App.controller.curso import listarCursos
from App.controller.curso import atualizarCurso
from App.controller.utils import validarAcao
from PyQt5.uic import loadUi

class EditarCurso(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarCurso.ui',self)
        self.dicionarioDeAreas = listarCursos()
        self.popularJanela()

    def popularJanela(self):
        self.comboxArea()

    @pyqtSlot()
    def on_btnEditarCurso_clicked(self):
        print(self.dicionarioDeAreas)
        info = self.getEditarCurso()
        idCurso = self.dicionarioDeAreas[info[0]]
        if atualizarCurso(idCurso, info):
            validarAcao()

    def comboxArea(self):
        areas = self.dicionarioDeAreas.keys()
        self.campoArea.addItems(areas)

    def getEditarCurso(self):
        area = self.campoArea.currentText().strip()
        nome = self.nomeCurso.text().strip()
        oferta = self.ofertaCurso.text().strip()
        periodo = self.periodoCurso.currentText().strip()
        carga = self.cargaCurso.text().strip()
        horas = self.horasPorDia.text().strip()
        alunos = self.quantidadeAlunos.text().strip()
        
        return(area, nome, oferta, periodo, carga, horas, alunos)
    
    def validandoDados(self):
        self.respostas.setText('EDITANDO...')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostas))

    def dadosInvalidos(self):
        texto = 'DADOS INCOMPLETOS.'
        self.respostas.setText(texto)
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostas))

    def limparCampos(self, campo):
        campo.clear()
        