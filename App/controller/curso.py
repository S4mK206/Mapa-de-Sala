from App.model.curso import Curso
from App.controller.utils import validarInputs

def cadastrarCurso(idArea, dados):
    if validarInputs(dados) and idArea:
        cursoModel = Curso(dados[1], dados[2], dados[3], dados[4], dados[5], dados[6])
        if cursoModel.cadastrar_curso(idArea):
            return True
    print('Preencha todos os campos')
    return False

def listarCursos():
    todosCursos = Curso.retorna_nomeId_cursos()
    listaCursos = {i[1]:i[0] for i in todosCursos}
    return listaCursos

def listarOfertas():
    return Curso.retorna_todas_oferta()

def deletarCurso(idCurso):
    if Curso.deletar(idCurso):
        return True
    return False
 
def atualizarCurso(idCurso, dados):
    if validarInputs(dados) and idCurso:
        cursoModel = Curso(dados[1], dados[2], dados[3], dados[4], dados[5], dados[6])
        if cursoModel.atualizar(idCurso, dados):
            return True
    return False
