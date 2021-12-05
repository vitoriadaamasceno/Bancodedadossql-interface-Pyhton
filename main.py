import tkinter as tk
import sqlite3
import pandas as pd
# #Criar o banco
# conect=sqlite3.connect('clientes.db')
# #criando o cursor para enviar
# c=conect.cursor()
# c.execute('''CREATE TABLE clientes(
#             nome text,
#             sobrenome text,
#             email text,
#             telefone text
#             )
# ''')
# #salvando
# conect.commit()
# conect.close()
#comentar criação do banco
#criando funçao de botões e integração
def cadastrar_clientes():
    conect=sqlite3.connect('clientes.db')
    #criando o cursor para enviar
    c=conect.cursor()
    c.execute("INSERT INTO clientes VALUES(:nome,:sobrenome, :email, :telefone)",
                {
                  'nome':entry_nome.get(),
                   'sobrenome': entry_sobrenome.get(),
                    'email': entry_email.get(),
                    'telefone': entry_telefone.get()

                }
              )
    #salvando
    conect.commit()
    conect.close()
    entry_nome.delete(0,'end')
    entry_sobrenome.delete(0, 'end')
    entry_email.delete(0, 'end')
    entry_telefone.delete(0, 'end')

def exporta_clientes():
    conect = sqlite3.connect('clientes.db')
    #criando o cursor para enviar
    c=conect.cursor()
    c.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados=c.fetchall()
    #exportando p execel
    clientes_cadastrados= pd.DataFrame(clientes_cadastrados, columns=['nome','sobrenome','email','telefone','id_cliente'])
    clientes_cadastrados.to_excel('banco_clientes.xlsx')
    #salvando
    conect.commit()
    conect.close()

#criar interface grafica
windows= tk.Tk()
windows.title('Cadastro de clientes')
#labels
label_nome=tk.Label(windows, text='NOME')
label_nome.grid(row=0, column=0, padx=10, pady=10 )

label_sobrenome=tk.Label(windows, text='SOBRENOME')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10 )

label_email=tk.Label(windows, text='E-MAIL')
label_email.grid(row=2, column=0, padx=10, pady=10 )

label_telefone=tk.Label(windows, text='TELEFONE')
label_telefone.grid(row=3, column=0, padx=10, pady=10 )
#entrada
entry_nome=tk.Entry(windows, text='NOME' ,width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10 )

entry_sobrenome=tk.Entry(windows, text='SOBRENOME' ,width=30)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10 )

entry_email=tk.Entry(windows, text='E-MAIL',width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10 )

entry_telefone=tk.Entry(windows, text='TELEFONE',width=30)
entry_telefone.grid(row=3, column=1, padx=10, pady=10 )
#botao
botao_cadastrar=tk.Button(windows, text='CADASTRAR CLIENTE',command=cadastrar_clientes)
botao_cadastrar.grid(row=4, column=0, padx=10, pady=10 ,columnspan=2, ipadx=80)
#botao exportar
botao_exportar=tk.Button(windows, text='EXPORTAR BASE',command=exporta_clientes)
botao_exportar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80 )
windows.mainloop()

#exportar(select+)
#pandas