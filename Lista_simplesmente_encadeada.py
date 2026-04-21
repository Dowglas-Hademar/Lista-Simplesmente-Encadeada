class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class Aluno:
    def __init__(self, nome, matricula, status = True):
        self.nome = nome
        self.matricula = matricula
        self.status = status


    def __str__(self):
        return f'Nome: {self.nome}'

class List:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def __str__(self):
        result = ""
        perc = self.head
        for element in range(self.size):
            result = f"{result + str(perc.value)}, "
            perc = perc.next

        return f"[{result[:-2]}]"

    def __len__(self):
        return self.size

    def add(self, value)-> bool:

        if type(value) != Aluno:
            return False

        if self.get_document(value.matricula) is not None:
            return False

        no = Node(value)
        self.size += 1
        if self.head is None:
            self.head = no
            self.last = no
            return True

        self.last.next = no
        self.last = no
        return True
    # Regras:
    # 1 - Só pode aceitar value do tipo Aluno
    # 2 - Não pode ter matricula repetida

    def insert(self, index, value)-> bool:
        if type(value) != Aluno:
            return False

        if self.get_document(value.matricula) is not None:
            return False

        no = Node(value)

        if index <= 0:
            self.size += 1
            no.next = self.head
            self.head = no
            return True
        elif index >= self.size:
            self.size += 1
            self.last.next = no
            self.last = no
            return True
        else:
            self.size += 1
            perc = self.head
            for element in range(index -1):
                perc = perc.next
            no.next = perc.next
            perc.next = no
            return True
        #Regras:
        #1 - Só pode aceitar value do tipo Aluno
        #2 - Não pode ter matricula repetida

    def get_document(self, doc) -> Aluno:
        perc = self.head
        for element in range(self.size):
            if doc == perc.value.matricula:
                return perc.value

            perc = perc.next

        return None
        #retornar o aluno com a matricula igual ao doc, ou null se nao existir

    def get_index(self, index) -> Aluno:
        if index <= 0:
            return self.head.value
        elif index >= self.size:
            return self.last.value
        else:
            perc = self.head
            for element in range(index):
                perc = perc.next
            return perc.value
        #retornar o aluno no index passado

    def remover_doc(self, doc) -> Aluno:
        perc = self.head

        if perc is None:
            return None

        if perc.value.matricula == doc:
            self.head = perc.next
            perc.next = None
            self.size -= 1
            return perc.value


        perc2 = None
        for element in range(self.size):
            if doc == perc.value.matricula:
                if self.last == perc:
                    self.last = perc2
                    perc2.next = None
                    self.size -= 1
                    return perc.value

                perc2.next = perc.next
                perc.next = None
                self.size -= 1
                return perc.value
            perc2 = perc
            perc = perc.next
        return None
        #remover o aluno com a matricula igual ao doc, ou null se nao existir
        #depois de remover, retornar o aluno

    def get_alunos(self, name)-> list:
        temp_list = List()
        perc = self.head
        for element in range(self.size):
            if name in perc.value.nome:
                temp_list.add(perc.value)

            perc = perc.next

        return temp_list
        #vai retornar a lista de Alunos que contem o nome

    def get_total(self):
        return self.size

    def get_alunos_por_status(self, status):
        temp_list = List()
        perc = self.head
        for element in range(self.size):
            if perc.value.status == status:
                temp_list.add(perc.value)

            perc = perc.next
        return temp_list
        #retornar uma lista de alunos com status igual ao parametro

    def ordenar_por_nome(self):
        if self.head is None:
            return None
        trocou = True

        while trocou:
            perc = self.head
            perc2 = None
            trocou = False

            while perc and perc.next is not None:
                prox = perc.next
                if perc.value.nome.lower() > prox.value.nome.lower():
                    trocou = True

                    if perc2 is None:
                        self.head = prox
                    else:
                        perc2.next = prox

                    perc.next = prox.next
                    prox.next = perc

                    perc2 = prox
                else:
                    perc2 = perc
                    perc = perc.next

        perc = self.head
        while perc.next is not None:
            perc = perc.next

        self.last = perc
        #vai reoordenar a lista por nome

    def print(self):
        if self.head is None:
            return '[]'

        perc = self.head

        string = '['
        for element in range(self.size):
            string += perc.value.nome + ", "

            perc = perc.next
        string = string[:-2]
        string += ']'

        return string
        #retornar a lista com os nomes dos alunos separando por ,
        # [heldon,joão, pedro]
        # Saída: [Dowglas, Carlos, Yara, Jonas]

#TESTES
listaAlunos = List()
aluno1 = Aluno("Dowglas", 123, True)
aluno2 = Aluno("Jonas", 234, True)
aluno3 = Aluno("Carlos", 587, False)
aluno5 = Aluno("Camila", 111, True)
aluno4 = Aluno("Yara", 888, True)
aluno6 = Aluno("Luan", 487, True)
listaAlunos.add(aluno1)
listaAlunos.add(aluno3)
listaAlunos.add(aluno4)
listaAlunos.add(aluno2)
listaAlunos.add(aluno5)
listaAlunos.insert(5, aluno6)

print(listaAlunos)
listaAlunos.ordenar_por_nome()
listaAlunos.print()


