
from sqlmodel import Field, Relationship, SQLModel


class Pessoa(SQLModel):
    descricao: str
    icone: str | None = Field(default='icone.png')


class Pessoa(PessoaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    pessoa: list['Pessoa'] = Relationship(back_populates='pessoa')


class PessoaNome(PessoaBase):
    id: int


class PessoaApelido(SQLModel):
    description: str
    icone: str | None = Field(default='icone.png')
    estado_conexao: bool | None = Field(default=True)
    status: bool | None = Field(default=False)

    pessoa_id: int | None = Field(default=None, foreign_key="pessoa.id")


class PessoaNasciemnto(NascimentoBase):
    id: int
    nascimento_id: int | None = Field(default=None,foring_key="2000-10-01")
