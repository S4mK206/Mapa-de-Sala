from App.model.curso import Curso
from App.model.area import Area
from App.controller.utils import validarInputs
from datetime import timedelta

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

def timedelta_to_int(td: timedelta) -> int:
    """
    Converte um objeto timedelta para um inteiro no formato hhmmss.

    Args:
        td (timedelta): O objeto timedelta a ser convertido.

    Returns:
        int: Representação inteira no formato hhmmss.
    """
    # Obtém o total de segundos no timedelta
    total_seconds = int(td.total_seconds())

    # Calcula horas, minutos e segundos
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    # Formata como um número inteiro no formato hhmmss
    return hours * 10000 + minutes * 100 + seconds

def buscarCursosId(idCurso=1):
    if not isinstance(idCurso, int):
        return {"error": "ID inválido. Deve ser um número inteiro."}
    
    try:
        resultado = Curso.retorna_todas_infos_curso(idCurso)
        if not resultado or len(resultado) < 7:
            return {"error": "Curso não encontrado"}
        return {
            "idCurso": resultado[0],
            "idArea": str(Area.buscar_nome_area(resultado[1])),
            "nome": resultado[2],
            "oferta": resultado[3],
            "periodo": resultado[4],
            "cargaHoraria": resultado[5],
            "horasDia": timedelta_to_int(resultado[6]),
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
