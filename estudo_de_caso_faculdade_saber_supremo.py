# -*- coding: utf-8 -*-
"""Estudo de Caso - Faculdade Saber Supremo

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D1ymme2y6o8Uki1lVzvRA76pcB0r2HO_
"""

class Pessoa():
    def __init__(self, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.anoNasc = anoNasc
        self.mesNasc = mesNasc
        self.diaNasc = diaNasc
        self.sexo = sexo

    
    def Cadastrar(self):
        pass

    
    def Exibir(self):
        pass


class Aluno(Pessoa):
    alunos = []

    def __init__(self, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, codigo, interesse, desconto):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo)
        self.codigo = codigo
        self.interesse = interesse
        self.desconto = desconto

    def Cadastrar(self):
        Aluno.alunos.append(self)

    def Exibir(self):
        print("Alunos cadastrados:")
        for aluno in Aluno.alunos:
            print("Nome:", aluno.nome)
            print("Código:", aluno.codigo)
            print("Interesse:", aluno.interesse)
            print("Desconto:", aluno.desconto)
            print("-----")


class Matricula:
    matriculas = []

    def __init__(self, id, mesMatricula, anoMatricula):
        self.id = id
        self.mesMatricula = mesMatricula
        self.anoMatricula = anoMatricula

    def Matricular(self):
        Matricula.matriculas.append(self)

    def Exibir(self):
        print("Matrículas realizadas:")
        for matricula in Matricula.matriculas:
            print("ID:", matricula.id)
            print("Mês da Matrícula:", matricula.mesMatricula)
            print("Ano da Matrícula:", matricula.anoMatricula)
            print("-----")


class Curso:
    cursos = []

    def __init__(self, titulo, descricao, valor, sala):
        self.titulo = titulo
        self.descricao = descricao
        self.valor = valor
        self.sala = sala

    def Cadastrar(self):
        Curso.cursos.append(self)

    def Exibir(self):
        print("Cursos cadastrados:")
        for curso in Curso.cursos:
            print("Título:", curso.titulo)
            print("Descrição:", curso.descricao)
            print("Valor:", curso.valor)
            print("Sala:", curso.sala)
            print("-----")

    def CalcularNumMinAluno(self):
        salario_professor = 12568.43
        valor_aluno = 865.23
        min_alunos = float(salario_professor / valor_aluno) + 1
        min_alunos = "{:.2f}".format(min_alunos)
        return min_alunos


class Salario:
    def __init__(self, salarioBruto, salarioLiquido, inss, irrf, planoSaude):
        self.salarioBruto = salarioBruto
        self.salarioLiquido = salarioLiquido
        self.inss = inss
        self.irrf = irrf
        self.planoSaude = planoSaude
        

    def CalcularSalario(self):
        salario_liquido = self.salarioBruto - (self.inss + self.irrf + self.planoSaude + Funcionario.descontoPlanoSaude)
        self.salarioLiquido = salario_liquido


class Funcionario(Pessoa):
    funcionarios = []

    def __init__(self, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo)
        self.matricula = matricula
        self.setor = setor
        self.cargo = cargo
        self.nivel = nivel
        self.descontoPlanoSaude = 125.00

    def Cadastrar(self):
        Funcionario.funcionarios.append(self)

    def CalcularSalarioF(self):
      A = 1520.25
      B = 2362.67
      C = 2988.92
      D = 3572.77
      E = 4878.67
      

      if self.cargo == "A":
        salarioBase = A
      elif self.cargo == "B":
        salarioBase = B
      elif self.cargo == "C":
        salarioBase = C
      elif self.cargo == "D":
        salarioBase = D
      elif self.cargo == "E":
        salarioBase = E
      else:
        return 'Cargo invalido'

      self.salario = salarioBase - self.descontoPlanoSaude

      return self.salario


    def Exibir(self):
        print("Funcionários cadastrados:")
        for funcionario in Funcionario.funcionarios:
            print("Nome:", funcionario.nome)
            print("Matrícula:", funcionario.matricula)
            print("Setor:", funcionario.setor)
            print("Cargo:", funcionario.cargo)
            print("Nível:", funcionario.nivel)
            print("Desconto Plano de Saúde:", self.descontoPlanoSaude)
            print('O Salario do Funcionario:', self.salario)  
            print("-----")


class CoordenadorAdm(Funcionario):
    coordenadores_adm = []

    def __init__(self, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel, area):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel)
        self.area = area

    def Cadastrar(self):
        CoordenadorAdm.coordenadores_adm.append(self)

    def Exibir(self):
        print("Coordenadores Administrativos cadastrados:")
        for coordenador in CoordenadorAdm.coordenadores_adm:
            print("Nome:", coordenador.nome)
            print("Matrícula:", coordenador.matricula)
            print("Setor:", coordenador.setor)
            print("Cargo:", coordenador.cargo)
            print("Nível:", coordenador.nivel)
            print("Área:", coordenador.area)
            print("-----")

    def CalcularPlusSalario(self):
        salario_tecnico = 12568.43
        plus_salario = salario_tecnico * 0.135
        return plus_salario


class Professor(Funcionario):
    professores = []

    def __init__(self, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel, formacao, disciplina):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel)
        self.formacao = formacao
        self.disciplina = disciplina

    def Cadastrar(self):
        Professor.professores.append(self)

    def Exibir(self):
        print("Professores cadastrados:")
        for professor in Professor.professores:
            print("Nome:", professor.nome)
            print("Matrícula:", professor.matricula)
            print("Setor:", professor.setor)
            print("Cargo:", professor.cargo)
            print("Nível:", professor.nivel)
            print("Formação:", professor.formacao)
            print("Disciplina:", professor.disciplina)
            print("Salário:", professor.CalcularSalario())
            print("Desconto Plano de Saúde:", self.descontoPlanoSaude)  
            print("Salário menos desconto: ", professor.CalularDescontoPlanosaude())
            print("-----")

    def CalcularSalario(self):
      salario_base_nivel1 = 6500.00
      salario_base_nivel2 = 8325.50
      salario_base_nivel3 = 12568.43
      valor_curso = 865.23
      bonus_coordenador = 0.15
      
      if self.nivel == "I":
          salario_base = salario_base_nivel1
      elif self.nivel == "II":
          salario_base = salario_base_nivel2
      elif self.nivel == "III":
          salario_base = salario_base_nivel3
      else:
          return "Nível inválido"

      salario = salario_base
      if self.cargo == "Coordenador":
          salario += (salario_base * bonus_coordenador)

      return salario

    def CalularDescontoPlanosaude(self):
      salario_base_nivel1 = 6500.00
      salario_base_nivel2 = 8325.50
      salario_base_nivel3 = 12568.43
      valor_curso = 865.23
      bonus_coordenador = 0.15  
      
      if self.nivel == "I":
          salario_base = salario_base_nivel1
      elif self.nivel == "II":
          salario_base = salario_base_nivel2
      elif self.nivel == "III":
          salario_base = salario_base_nivel3
      else:
          return "Nível inválido"

      salario = salario_base
      if self.cargo == "Coordenador":
          salario += (salario_base * bonus_coordenador)
      salario = salario - self.descontoPlanoSaude

      return salario



class Coordenador(Professor):
    coordenadores = []

    def __init__(self, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel, formacao, disciplina, area):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel, formacao, disciplina)
        self.area = area

    def Cadastrar(self):
        Coordenador.coordenadores.append(self)

    def Exibir(self):
        print("Coordenadores cadastrados:")
        for coordenador in Coordenador.coordenadores:
            print("Nome:", coordenador.nome)
            print("Matrícula:", coordenador.matricula)
            print("Setor:", coordenador.setor)
            print("Cargo:", coordenador.cargo)
            print("Nível:", coordenador.nivel)
            print("Formação:", coordenador.formacao)
            print("Disciplina:", coordenador.disciplina)
            print("Área:", coordenador.area)
            print("-----")

    def CalcularPlusSalario(self):
        salario_professor = 12568.43
        plus_salario = salario_professor * 0.15
        return plus_salario


# Exemplo de interação com o usuário

# Cadastro de Alunos
aluno1 = Aluno("João", "123456789", "987654321", 1990, 5, 10, "M", "001", "Ciências", 0.2)
aluno1.Cadastrar()

# Cadastro de Matrículas
matricula1 = Matricula("001", "Junho", 2023)
matricula1.Matricular()

# Cadastro de Funcionario nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, nivel
funcionario1 = Funcionario('Diego', '1257454','0210210', 2002, '07', '02', 'M', 808, 'Limpeza', 'A',1)
funcionario1.Cadastrar()
funcionario1.CalcularSalarioF()

# Cadastro de Cursos
curso1 = Curso("Matemática", "Curso avançado de matemática", 865.23, "Sala 1")
curso1.Cadastrar()

# Cadastro de Coordenadores Administrativos
coordenador1 = CoordenadorAdm("Carlos", "654321987", "321654987", 1985, 3, 15, "M", "001", "Administração", "Coordenador", "A", "Financeiro")
coordenador1.Cadastrar()

# Cadastro de Professores
professor1 = Professor("José", "654987321", "456123789", 1978, 7, 25, "M", "001", "Educação", "Professor", "II", "Mestrado", "Matemática")
professor1.Cadastrar()

# Cadastro de Coordenadores
coordenador1 = Professor("Maria", "987654321", "789123456", 1985, 3, 15, "F", "002", "Educação", "Coordenador", "III", "Doutorado", "Física")
coordenador1.Cadastrar()

# Exibição das informações

aluno1.Exibir()
matricula1.Exibir()
funcionario1.Exibir()
curso1.Exibir()
coordenador1.Exibir()
professor1.Exibir()
coordenador1.Exibir()

curso1 = Curso("Matemática", "Curso avançado de matemática", 865.23, "Sala 1")
min_alunos_curso1 = curso1.CalcularNumMinAluno()
print("O curso de", curso1.titulo, "precisa de no mínimo", min_alunos_curso1, "alunos para pagar o salário do professor nível III.")

#Mostra o desconto aplicado em um professor
professor1.Exibir()

curso1 = Curso("Test", "Test", 865.23, "Sala 1")
min_alunos_curso1 = curso1.CalcularNumMinAluno()
print("O curso de", curso1.titulo, "precisa de no mínimo", min_alunos_curso1, "alunos para pagar o salário do professor nível III.")

#Mostra o desconto aplicado em um professor
professor1.Exibir()

