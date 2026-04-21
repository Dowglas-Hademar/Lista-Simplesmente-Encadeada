# Lista Simplesmente Encadeada - Gestão de Alunos 🎓

Este repositório contém uma implementação completa de uma **Lista Simplesmente Encadeada** (Singly Linked List) desenvolvida em Python para a disciplina de **Análise e Estrutura de Dados (AED)**.

O projeto simula um sistema de gerenciamento de alunos, permitindo operações de inserção, busca, remoção e ordenação.

## 🚀 Funcionalidades

A classe `List` possui os seguintes métodos principais:

- **`add(aluno)`**: Adiciona um aluno ao final da lista (evita matrículas duplicadas).
- **`insert(index, aluno)`**: Insere um aluno em uma posição específica.
- **`remover_doc(matricula)`**: Remove um aluno da lista através do seu número de matrícula.
- **`get_document(matricula)`**: Busca um aluno específico pela matrícula.
- **`ordenar_por_nome()`**: Reorganiza toda a lista em ordem alfabética (Bubble Sort adaptado para listas encadeadas).
- **`get_alunos_por_status(status)`**: Filtra e retorna uma nova lista de alunos ativos ou inativos.
- **`print()`**: Retorna uma representação visual formatada dos nomes presentes na lista.

## 🛠️ Estrutura do Código

O projeto é dividido em três classes principais:

1.  **`Node`**: Representa cada "nó" da lista, guardando o valor (`Aluno`) e a referência para o próximo elemento.
2.  **`Aluno`**: Objeto que contém os dados (Nome, Matrícula e Status).
3.  **`List`**: A estrutura de dados principal que gerencia os nós, controlando o `head` (início), `last` (fim) e o `size` (tamanho).

## 💻 Como rodar o projeto

1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone o repositório:
   ```bash
   git clone https://github.com/Dowglas-Hademar/Lista-Simplesmente-Encadeada.git

## 📝 Aprendizados de AED

Neste projeto, foram aplicados conceitos fundamentais de Estrutura de Dados:

* **Alocação Dinâmica:** A lista cresce conforme a necessidade, utilizando a memória de forma eficiente.
* **Manipulação de Ponteiros:** Uso do atributo `next` para encadear os objetos na memória.
* **Complexidade de Algoritmos:** * Busca e Remoção: $O(n)$ - no pior caso, percorremos a lista toda.
    * Inserção no Início/Fim: $O(1)$ - graças ao controle dos ponteiros `head` e `last`.
* **Ordenação:** Implementação do algoritmo Bubble Sort adaptado para referências de memória.
