# 1. Classe
class Aluno:
    # 2. Objeto
    def __init__(self, nome, nota, media_instituicao):
        self.nome = nome
        self.nota = nota
        self.media_instituicao = media_instituicao

    # 3. Mensagem
    def avaliar(self):
        if self.nota >= self.media_instituicao:
            print(self.nome + ' passou.')
        else:
            print(self.nome + ' reprovou.')

# 4. Abstração: A classe Aluno abstrai as características e comportamentos de um aluno.

# 5. Encapsulamento: Atributos como 'nome', 'nota' e 'media_instituicao' 
#são encapsulados dentro da classe Aluno e podem ser acessados apenas 
#através de métodos.

# 6. Herança: Vamos criar uma classe derivada 'AlunoGraduacao' que herda de 'Aluno'.
class AlunoGraduacao(Aluno):
    def __init__(self, nome, nota, media_instituicao, curso):
        super().__init__(nome, nota, media_instituicao)
        self.curso = curso

# 7. Polimorfismo: Vamos criar outra classe derivada 'AlunoPosGraduacao' 
#que redefine o método 'avaliar'.
class AlunoPosGraduacao(Aluno):
    def __init__(self, nome, nota, media_instituicao, programa):
        super().__init__(nome, nota, media_instituicao)
        self.programa = programa

    # Método polimórfico que modifica o comportamento da avaliação.
    def avaliar(self):
        if self.nota >= self.media_instituicao:
            print(self.nome + ' passou no programa de pós-graduação.')
        else:
            print(self.nome + ' foi reprovado no programa de pós-graduação.')

# 8. Classe abstrata: Podemos criar uma classe abstrata 'Pessoa' que 
#serve como base para 'Aluno'.
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def apresentar(self):
        pass

# 9. Interfaces: Vamos criar uma interface 'Avaliavel' que define o método 'avaliar'.
class Avaliavel(ABC):
    @abstractmethod
    def avaliar(self):
        pass

# Agora, a classe Aluno implementa a interface Avaliavel.
class Aluno(Pessoa, Avaliavel):
    def __init__(self, nome, nota, media_instituicao):
        super().__init__(nome)
        self.nota = nota
        self.media_instituicao = media_instituicao

    def avaliar(self):
        if self.nota >= self.media_instituicao:
            print(self.nome + ' passou.')
        else:
            print(self.nome + ' reprovou.')
          
    def apresentar(self):
        return super().apresentar()
      
# Exemplo de uso das classes
aluno1 = Aluno('João', 8.5, 7.0)
aluno1.avaliar()

graduacao1 = AlunoGraduacao('Maria', 6.0, 6.0, 'Engenharia')
graduacao1.avaliar()

pos_graduacao1 = AlunoPosGraduacao('Carlos', 7.5, 7.0, 'Mestrado')
pos_graduacao1.avaliar()
