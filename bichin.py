class Bichin:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 20
        self.saude = 80
        self.idade = 1
    def AlterarNome(self, novoNome):
        self.nome = novoNome
    def AlterarFome(self, valorF):
        self.fome += valorF
        if self.fome > 100:
            self.fome = 100
        elif self.fome < 0:
            self.fome = 0
    def AlterarSaude(self, valorS):
        self.saude += valorS
        if self.saude > 100:
            self.saude = 100
        elif self.saude < 0:
            self.saude = 0
    def AlterarIdade(self):
        self.idade += 1
    def RetornarNome(self):
        return self.nome
    def RetornarFome(self):
        return self.fome
    def RetornarSaude(self):
        return self.saude
    def RetornarIdade(self):
        return self.idade
    def RetornarHumor(self):
        humor = self.saude + self.fome 
        return humor

nomeB = input('Qual o nome que deseja colocar no seu bichin? ')
Bichin = Bichin(nome = nomeB)
while (Bichin.saude > 0) and (Bichin.fome < 100):
    Bichin.AlterarFome(+2)
    Bichin.AlterarSaude(-2)
    Bichin.AlterarIdade()
    resposta = input(f"""\n------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   o   o   |
  \____Y_____/
    \__-__/
     \nOlá meu nome é {Bichin.nome}. O que você deseja fazer comigo agora? \n1- Alimentar (-10 de fome)\n2- Dormir (+10 de saúde)\n3- Alterar nome\n4- Visualizar humor\n5- Visualizar idade\n6- Visualizar fome\n7- Visualizar saúde\nResposta: """)
    print('\n')
    if resposta == '1':
        Bichin.AlterarFome(-10)
        print("-10 de fome! Obrigado!")
    elif resposta == '2':
        Bichin.AlterarSaude(+10)
        print("+10 de saúde! Obrigado!")
    elif resposta == '3':
        nome2 = input('Qual nome deseja colocar? \n')
        Bichin.AlterarNome(nome2)
    elif resposta == '4':
        print("Humor: ", Bichin.RetornarHumor())
    elif resposta == '5':
        print("Idade: ", Bichin.RetornarIdade())
    elif resposta == '6':
        print("Fome: ", Bichin.RetornarFome())
    elif resposta == '7':
        print("Saude: ", Bichin.RetornarSaude())
    else:
        print('Escolha um número válido!')
else:
    print("""\n------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   X   X   |
  \____Y_____/
    \__-__/\nVocê me deixou morrer!\n""")