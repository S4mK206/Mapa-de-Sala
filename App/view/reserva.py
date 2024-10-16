from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer

from App.controller.curso import listarCursos



class ReservaInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/reserva.ui',self)
        self.popular()

    def getDados(self)->dict:
        """Pegando o dados na interface e retornando os valores"""
        nomeDocenteResponsavel = self.nomeDocente.text().strip() 
        nomeSala = self.salaReserva.text().strip() 
        nomeCurso = self.cursoReserva.text().strip() 
        equipamentos = self.equipamentosReserva.text().strip() 
        inicio = self.inicioReserva.text().strip() 
        fim = self.fimReserva.text().strip() 
        observacao = self.observacaoReserva.text().strip() 
        
        dados = {"nomeDocente":nomeDocenteResponsavel, 
                 "nomeSala":nomeSala, 
                 "nomeCurso":nomeCurso,
                 "equipamentos":equipamentos,
                 "inicio":inicio,
                 "fim":fim,
                 "observações":observacao}
        return dados
    
    def popularJanela(self):
        pessoas = ['samuel', 'otavio', 'gabriel', 'bruno', 'richard', 'max', 'camila']
        sala = ['j01', 'j02', 'j03']
        curso = ['ds', 'culinaria', 'beleza']
        self.nomeDocente.addItems(pessoas)
        self.cursoReserva.addItems(curso)
        self.salaReserva.addItems(sala)

    def on_btnFazerReserva_clicked(self):
        listarCursos()


        
    def validandoDados(self):
        self.feedbackReserva.setText('Reserva realizada.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def dadosInvalidos(self):
        self.feedbackReserva.setText('Dados incomoletos.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def limparCampos(self, campo):
        campo.clear()


