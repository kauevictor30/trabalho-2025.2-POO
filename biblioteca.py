class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.__disponivel = True

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

    def get_disponivel(self): 
        return self.__disponivel
    
    def set_disponivel(self, valor: bool):
        self.__disponivel = valor

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def pegar_livro(self, livro:  Livro):
        print(f'>> O usuário {self.nome} pegou o livro {livro}')

        if livro.get_disponivel():
            livro.set_disponivel(False)
            self.livros_emprestados.append(livro)
            print('>> Livro emprestado')
        else:
            print('>> Falha o livro não está disponivel')
    
    def devolver_livro(self, livro: Livro):
        print(f'>> O usuario {self.nome} devolveu o livro {livro}')
        if livro in self.livros_emprestados:
            livro.set_disponivel(True)
            self.livros_emprestados.remove(livro)
            print('>> Sucesso livro devolvido')
        else:
            print('>> Falha na ação...')

    def listar_livros(self):
        print(f'>> Livros no usuario {self.nome}:')
        if not self.livros_emprestados:
            print('>> O usuário não tem emprestimos no momento')
        else:
            for livro in self.livros_emprestados:
                print(f'>> {livro}')
            print('-' * 30)

print(">> Criando acervo da biblioteca...")
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
livro2 = Livro("Batman: A Piada Mortal", "Alan Moore")
print(f"Livro 1: {livro1} | Disponível: {livro1.get_disponivel()}")
print(f"Livro 2: {livro2} | Disponível: {livro2.get_disponivel()}")

print(">> Criando usuarios...")
usuario1 = Usuario("Kleber")
usuario2 = Usuario("Rogerio")
print(f"Usuário 1: {usuario1.nome}")
print(f"Usuário 2: {usuario2.nome}")

usuario1.pegar_livro(livro1)
usuario2.pegar_livro(livro1)

usuario1.listar_livros()
usuario2.listar_livros()

usuario1.devolver_livro(livro1)
usuario2.pegar_livro(livro1)

usuario1.listar_livros()
usuario2.listar_livros()