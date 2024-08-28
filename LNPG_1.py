# programa deve requisitar nome, sexo, numero de telefone e idade, colocar tudo num txt, e conseguir mostrar #
# cadastros ja feitos, pesquisar todos os cadastros de um sexo, e procurar nomes especificos nesse txt #


def get_name():
    global name, nomes
    name = input("Digite o seu nome: ")
    nomes = [name]
    return name


def get_age():
    global age
    try:
        age = int(input("Digite a sua idade: "))
    except TypeError and ValueError:
        age = "Resposta Inválida"
    return age


def get_number():
    global number
    try:
        number = int(input("Digite o seu telefone: ").strip('' and '-'))
    except TypeError and ValueError:
        number = "Resposta Inválida"
    return number


def get_sex():
    global sex
    try:
        sex = str(input("Digite o seu sexo (M ou F): ").upper())
    except TypeError and ValueError:
        sex = "Outros"
    if sex == "m":
        sex = "Masculino"
    elif sex == "f":
        sex = "Feminino"
    else:
        sex = "Resposta Inválida"
    return sex


def gravar_dados():
    global sex, name, number, age, arquiva
    name = ""
    nomes = []
    arquiva = open("LNPG_txt1.txt", "a", encoding="utf-8")
    while name != 0:
        print("Por favor preencha o formulário")
        print("-" * 25)
        get_name()
        if name == "0":
            break
        print("-" * 25)
        get_age()
        print("-" * 25)
        get_sex()
        print("-" * 25)
        get_number()
        print("-" * 25)
        arquiva.write(f"Nome:{name}|Idade:{age}anos|Sexo:{sex}|Número:{number}\n")
    print("Dados salvos com sucesso")
    arquiva.close()


def mostrar_dados():
    global sex, arquivo, ler_arquivo, dados
    arquivo = open("LNPG_txt1.txt", "r", encoding="utf-8")
    ler_arquivo = arquivo.read()
    dados = ler_arquivo.split("|")
    for n in dados:
        print(f"-{n}")
        print("-" * 25)
    arquivo.close()


def buscar_por_sexo(sexo_escolhido):
    global sex, arquivo, ler_arquivo, dados
    arquivo = open("LNPG_txt1.txt", "r", encoding="utf-8")
    ler_arquivo = arquivo.readlines()
    if sexo_escolhido == "f":
        for n in ler_arquivo:
            if "Feminino" in n:
                print(n.split("|"))
    elif sexo_escolhido == "m":
        for n in ler_arquivo:
            if "Masculino" in n:
                print(n.split("|"))
    else:
        for n in ler_arquivo:
            if "Outros" in n:
                print(n.split("|"))
    arquivo.close()


def buscar_por_nome(nome_procurado):
    global sex, arquivo, ler_arquivo
    arquivo = open("LNPG_txt1.txt", "r", encoding="utf-8")
    ler_arquivo = arquivo.readlines()
    for n in ler_arquivo:
        if f"Nome:{nome_procurado}" in n:
            print(n)
    arquivo.close()


if __name__ == '__main__':
    gravar_dados()
    mostrar = input("Quer ver todos os cadastros feitos?").lower()
    if mostrar == "s" or mostrar == "sim":
        mostrar_dados()
    busca_sexo = input("Quer fazer uma busca de cadastro por sexo? ").lower()
    if busca_sexo == "s" or busca_sexo == "sim":
        escolha = input("Cadastros de qual sexo devem ser mostrados? (M ou F): ").lower()
        buscar_por_sexo(escolha)
    busca_nome = input("Quer fazer uma busca de cadastro por nomes? ").lower()
    if busca_nome == "s" or busca_nome == "sim":
        nome_procurar = input("Digite o nome ou parte de nome que deve ser buscado: ")
        buscar_por_nome(nome_procurar)
