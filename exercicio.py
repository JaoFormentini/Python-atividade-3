class Aluno:
    def __init__(self, nome, nota1, nota2) -> None:
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2

    def consultarInformacoes(self) -> None:
        print(f"Nome: {self.__nome}\n1.Nota: {self.__nota1}\n2.Nota: {self.__nota2}")
    
    def atribuirNome(self, nome) -> None:
        self.__nome = nome

    def atribuirNota1(self, nota1) -> None:
        if nota1 <= 10 and nota1 >= 0:
            self.__nota1 = nota1
        else:
            print("Nota invalida!")
    def atribuirNota2(self, nota2) -> None:
        if nota2 <= 10 and nota2 >= 0:    
            self.__nota2 = nota2
        else:    
            print("Nota invalida!")
    

aluno1 = Aluno("Joao", 6, 8)

aluno1.consultarInformacoes()

aluno1.atribuirNome(str(input("Digite o nome do aluno: ")))
aluno1.atribuirNota1(float(input("Digite a primeira nota do aluno: ")))
aluno1.atribuirNota2(float(input("Digite a segunda nota do aluno: ")))

aluno1.consultarInformacoes()

