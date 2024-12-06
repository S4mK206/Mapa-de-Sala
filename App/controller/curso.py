from App.model.curso import Curso
from App.controller.utils import validarInputs

def cadastrarCurso(idArea, dados):
    if validarInputs(dados) and idArea:
        cursoModel = Curso(dados[1], dados[2], dados[3], dados[4], dados[5], dados[6])
        if cursoModel.cadastrar_curso(idArea):
            return True
    print('Preencha todos os campos')
    return False

def infosCursos():
    print("reserva")

def listarCurso():
    todasSalas = Curso.retorna_ofertaId_cursos()
    listarCursos = {i[1]:i[0] for i in todasSalas}
    return(listarCursos)

def buscarCursosId(idCurso=1):
    if not isinstance(idCurso, int):
        return {"error": "ID inválido. Deve ser um número inteiro."}
    
    try:
        resultado = Curso.retorna_todas_infos_curso(idCurso)
        if not resultado or len(resultado) < 7:
            return {"error": "Curso não encontrado"}
        return {
            "idCurso": resultado[0],
            "idArea": resultado[1],
            "nome": resultado[2],
            "oferta": resultado[3],
            "periodo": resultado[4],
            "cargaHoraria": resultado[5],
            "horasDia": resultado[6],
            "qtdAlunos": resultado[7],
        }
    except Exception as e:
        return {"error": f"Erro ao buscar sala: {e}"}

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
