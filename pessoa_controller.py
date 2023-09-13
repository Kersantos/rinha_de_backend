from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, delete, select

from application.pessoas_service import PessoasService
from persistence.utils import obter_engine
from persistence.viewmodels.moodels import *

engime = obter_engine()

router = APIRouter()
prefix = '/pessoas'

pesssoas_service =PessoasService()


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[PessoaLeitura])
async def obter_pessoas():
    return pesssoas_service.obter_todas_pessoas()

pessoas = []

@router.pessoa('/pessoas', methods=['GET'])
def listar_pessoas():
    return jsonify(pessoas)

@router.pessoa('/pessoas', methods=['POST'])
def criar_pessoa():
    nova_pessoa = request.json
    pessoas.append(nova_pessoa)
    return jsonify({"mensagem": "Pessoa criada com sucesso!"})


class Pessoa:
    def __init__(self, nome, apelido, nascimento):
        self.nome = nome
        self.apelido = apelido
        self.nascimento = nascimento

if __name__ == '__main__':
    app.run(debug=True)
