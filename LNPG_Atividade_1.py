from tkinter import *
# fazer um programa que salve dados em um arquivo separado, mostre esses dados em uma listbox, e através da listbox
# ele consiga apagar os dados no arquivo

def main_janela():
    global entrada_cpf, entrada_end, entrada_idade, entrada_nome, lista_dados
    #criar janela
    janela_main = Tk()
    janela_main.title("Inscrição")
    janela_main.geometry('1920x1080')
    janela_main.configure(background='light grey')
    # criar os labels
    lbl_nome = Label(janela_main, font= 18, text="Nome:", background='light grey')
    lbl_end = Label(janela_main, font= 18, text="End:", background='light grey')
    lbl_cpf = Label(janela_main, font= 18, text="CPF:", background='light grey')
    lbl_idade = Label(janela_main, font= 18, text="Idade:", background='light grey')
    lbl_agenda = Label(janela_main, font=18, text="Agenda:",background='light grey')
    # localizar os labels
    lbl_nome.place(x=0, y=0)
    lbl_end.place(x=0, y=50)
    lbl_cpf.place(x=0, y=100)
    lbl_idade.place(x=0, y=150)
    lbl_agenda.place(x=0, y=250)
    # criar as entrys
    entrada_nome = Entry(janela_main, bd=5)
    entrada_end = Entry(janela_main, bd=5)
    entrada_cpf = Entry(janela_main, bd=5)
    entrada_idade = Entry(janela_main, bd=5)
    # localizar as entrys
    entrada_nome.place(x=50, y=0)
    entrada_end.place(x=50, y=50)
    entrada_cpf.place(x=50, y=100)
    entrada_idade.place(x=50, y=150)
    # button pra salvar dados
    btn_save = Button(janela_main, text="Salvar", command=save_data)
    btn_save.place(x=50, y=200)
    # button pra deletar dados
    btn_delete = Button(janela_main, text="Deletar", command=delete_data)
    btn_delete.place(x=130, y=200)
    # criar listbox
    lista_dados = Listbox(janela_main, height=30, width=50, selectmode='single')
    lista_dados.place(x=0, y=280)
    janela_main.mainloop()
    

def save_data() :
    global linhas_lista, arquivo, read, ler_arquivo
    lista_dados.delete(0, END)
    nome = entrada_nome.get()
    end = entrada_end.get()
    cpf = entrada_cpf.get()
    idade = entrada_idade.get()
    arquivo = open('registro_dados.txt', 'a', encoding='utf-8')
    arquivo.write(f'Nome:{nome} | Endereço:{end} | CPF:{cpf} | Idade:{idade}\n')
    ler_arquivo = open('registro_dados.txt', 'r', encoding='utf-8')
    read = ler_arquivo.read()
    linhas_lista = set(read.split('\n'))
    for linha in linhas_lista:
        if linha in linhas_lista:
            pass
        lista_dados.insert(END, str(linha))
    arquivo.close()
    
               
def delete_data():
    selected = lista_dados.curselection()
    lista_dados.delete(selected)    
    apagar =  open('registro_dados.txt', 'r+', encoding='utf-8')
    alvo = apagar.readlines()
    apagar.seek(0)
    for linha in alvo:
        if linha == str(selected):
            apagar.write(linha)
    apagar.truncate()
                    

if __name__ == '__main__':
    main_janela()