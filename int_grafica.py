from library import prototipo_back_end_adicionar, comandos_adicionar
import tkinter as tk
from tkinter import ttk

class Int_grafica(object):

  

    def __init__(self):
        janela = tk.Tk()
        janela["bg"] = 'cyan'
        janela.title("Loja Teste")
        janela.geometry("410x820+800+80")

        tabControl = ttk.Notebook(janela)

        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text = "Adicionar")
        tabControl.grid(row = 0, column = 0)

        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text = "Excluir")
        tabControl.grid(row = 0, column = 1, sticky = "E")


        menu = tk.Menu(janela)
        janela.config(menu = menu)
        menuExibir = tk.Menu(menu)
        menu.add_cascade(label = "Exibir", menu = menuExibir)
        menuExibir.add_command(label = "Clientes", command = self.exibir_clientes)
        menuExibir.add_command(label = "Categorias", command = self.exibir_categorias)
        menuExibir.add_command(label = "Produtos", command = self.exibir_produtos)
        menuExibir.add_command(label = "Vendas", command = self.exibir_vendas)
        menuExibir.add_command(label = "Itens Vendidos", command = self.exibir_itensVendidos)
        






        welcome = tk.Label(tab1, text="SEJA BEM-VINDO",bg = "blue", fg = "yellow")
        welcome.grid(row= 1, column = 0, columnspan = 6, sticky = "WE")

        label_categ = tk.Label(tab1, text = "ADICIONAR UMA CATEGORIA:")
        label_categ_nome = tk.Label(tab1, text = "NOME:")
        self.text_categ_nome = tk.Entry(tab1, width = 36)
        button_ins_categ = tk.Button(tab1,  text = "ADICIONAR CATEGORIA", command = self.envio_ins_categ)

        label_categ.grid(row = 2, column = 0, pady = 10, sticky = "W")
        label_categ_nome.grid(row = 3, column = 0, sticky = "W")
        self.text_categ_nome.grid(row=3, column = 1)
        button_ins_categ.grid(row = 4, column = 0, columnspan = 2, pady = 10)
        

        label_prod = tk.Label(tab1, text = "ADICIONAR UM PRODUTO:")
        label_prod_nome = tk.Label(tab1, text = "NOME:")
        label_prod_estoque = tk.Label(tab1, text = "ESTOQUE:")
        label_prod_preco = tk.Label(tab1, text = "PREÇO:")
        label_prod_categ = tk.Label(tab1, text = "CATEGORIA")
        self.text_prod_categ = tk.Entry(tab1, width = 36)
        self.text_prod_nome = tk.Entry(tab1, width = 36)
        self.text_prod_estoque = tk.Entry(tab1,width = 36)
        self.text_prod_preco = tk.Entry(tab1,width = 36)
        button_ins_prod = tk.Button(tab1,  text = "ADICIONAR PRODUTO", command = self.envio_ins_prod)


        label_prod.grid(row = 5, column = 0, sticky = "W", pady = 10)
        label_prod_nome.grid(row = 6, column = 0, sticky = "W")
        self.text_prod_nome.grid(row = 6, column = 1, sticky = "W")
        label_prod_estoque.grid(row = 7, column = 0, sticky = "W")
        self.text_prod_estoque.grid(row = 7, column = 1,sticky = "W" )
        label_prod_preco.grid(row = 8, column = 0, sticky = "W")
        self.text_prod_preco.grid(row = 8, column = 1, sticky = "W")
        label_prod_categ.grid(row = 9, column = 0, sticky = "W")
        self.text_prod_categ.grid(row = 9, column = 1, sticky = "W")
        button_ins_prod.grid(row = 10, column = 0, columnspan = 2, pady = 10)
        self.text_prod_preco.insert(0, "0.00")


        label_cliente = tk.Label(tab1, text = "ADICIONAR UM CLIENTE:")
        label_cliente_nome = tk.Label(tab1, text = "NOME:")
        label_cliente_cpf = tk.Label(tab1, text = "CPF:")
        button_ins_cliente = tk.Button(tab1,  text = "ADICIONAR CLIENTE", command = self.envio_ins_cliente)
        self.text_cliente_nome = tk.Entry(tab1, width = 36)
        self.text_cliente_cpf = tk.Entry(tab1, width = 36)

        label_cliente.grid(row = 11, column = 0, pady = 10, sticky = "W")
        label_cliente_nome.grid(row = 12, column = 0, sticky = "W")
        self.text_cliente_nome.grid(row  = 12, column = 1, sticky = "W")
        label_cliente_cpf.grid(row = 13, column = 0, sticky = "W")
        self.text_cliente_cpf.grid(row  = 13, column = 1, sticky = "W")
        button_ins_cliente.grid(row =14, column = 0, columnspan = 2, pady = 10)


        label_item_vend = tk.Label(tab1, text = "ADICIONAR UM INTEM VENDIDO:")
        label_item_vend_quant = tk.Label(tab1, text = "QUANTIDADE")
        label_item_vend_valor = tk.Label(tab1, text = "VALOR")
        label_item_vend_categ_venda = tk.Label(tab1, text = "CÓDIGO DA VENDA")
        label_item_vend_categ_prod = tk.Label(tab1, text = "NOME DO PRODUTO")
        self.text_item_vend_categ_venda = tk.Entry(tab1, width = 36)
        self.text_item_vend_nome_prod = tk.Entry(tab1, width = 36)
        self.text_item_vend_quant = tk.Entry(tab1, width = 36)
        self.text_item_vend_valor = tk.Entry(tab1, width = 36)
        self.text_item_vend_valor.insert(0, "0.00")
        button_ins_item_vend = tk.Button(tab1, text="ADICIONAR ITEM VENDIDO",command = self.envio_ins_itemVendido)

        label_item_vend.grid(row = 15, column = 0, sticky = "W", pady = 10)
        label_item_vend_quant.grid(row = 16, column = 0, sticky = "W")
        self.text_item_vend_quant.grid(row = 16, column = 1, sticky = "W")
        label_item_vend_valor.grid(row = 17, column = 0, sticky = "W")
        self.text_item_vend_valor.grid(row = 17, column = 1, sticky = "W")
        label_item_vend_categ_prod.grid(row = 18, column = 0, sticky = "W")
        label_item_vend_categ_venda.grid(row = 19, column = 0, sticky = "W")
        self.text_item_vend_categ_venda.grid(row = 19, column = 1, sticky = "W")
        self.text_item_vend_nome_prod.grid(row = 18, column = 1, sticky = "W")
        button_ins_item_vend.grid(row =20, column = 0, columnspan = 2, pady = 10)

        self.tipo_venda = tk.StringVar()

        label_venda = tk.Label(tab1, text = "ADICIONAR UMA VENDA:")
        label_venda_data = tk.Label(tab1, text = "DATA:")
        label_venda_tipo = tk.Label(tab1, text = "TIPO DE PAGAMENTO:")
        label_venda_cliente = tk.Label(tab1, text = "NOME CLIENTE")
        self.text_venda_cliente = tk.Entry(tab1, width = 36)
        self.text_venda_data = tk.Entry(tab1, width = 36)
        button_ins_venda = tk.Button(tab1, text = "ADICIONAR VENDA", command = self.envio_ins_venda)

        label_venda.grid(row = 21, column = 0, sticky = "W", pady = 10)
        label_venda_data.grid(row = 22, column = 0, sticky = "W")
        label_venda_tipo.grid(row = 24, column = 0, columnspan =2, pady = 10)
        self.text_venda_data.grid(row = 22, column = 1, sticky = "W")
        label_venda_cliente.grid(row = 23, column = 0, sticky = "W")
        self.text_venda_cliente.grid(row = 23, column = 1, sticky = "W")
        button_ins_venda.grid(row=26, column = 0, columnspan = 2, pady = 10)
        self.text_venda_data.insert(0, "dd/mm/aaaa")


        r1 = tk.Radiobutton(tab1, text = "DÉBITO", value = "Débito", variable = self.tipo_venda)
        r2 = tk.Radiobutton(tab1, text = "CRÉDITO", value = "Crédito", variable = self.tipo_venda)
        r3 = tk.Radiobutton(tab1, text = "DINHEIRO",  value = "Dinheiro", variable =  self.tipo_venda)
        r1.grid(row = 25, column = 0, sticky ="W")
        r2.grid(row = 25, column = 0, columnspan = 2)
        r3.grid(row = 25, column = 1,sticky ="E")


        janela.mainloop()


    def envio_ins_venda(self):
        comandos_adicionar.Adicionar().adicionar_venda(self.text_venda_data.get(), self.tipo_venda.get(), self.text_venda_cliente.get())
        self.text_venda_cliente.delete(0,tk.END)
        self.text_venda_data.delete(0,tk.END)
        



    def envio_ins_categ (self):
        comandos_adicionar.Adicionar().adicidionar_categ(self.text_categ_nome.get())
        self.text_categ_nome.delete(0,tk.END)
    
    def envio_ins_cliente(self):
        comandos_adicionar.Adicionar().adicionar_cliente(self.text_cliente_nome.get(), self.text_cliente_cpf.get())
        self.text_cliente_nome.delete(0,tk.END)
        self.text_cliente_cpf.delete(0,tk.END)
    
    def envio_ins_itemVendido (self):
        comandos_adicionar.Adicionar().adicionar_item_vend(self.text_item_vend_quant.get(), self.text_item_vend_valor.get(), self.text_item_vend_nome_prod.get(), self.text_item_vend_categ_venda.get())
        self.text_item_vend_categ_venda.delete(0,tk.END)
        self.text_item_vend_nome_prod.delete(0,tk.END)
        self.text_item_vend_quant.delete(0,tk.END)
        self.text_item_vend_valor.delete(0,tk.END)
    
    def envio_ins_prod(self):
        comandos_adicionar.Adicionar().adicionar_prod(self.text_prod_nome.get(), self.text_prod_estoque.get(), self.text_prod_preco.get(), self.text_prod_categ.get())
        self.text_prod_categ.delete(0,tk.END)
        self.text_prod_nome.delete(0,tk.END)
        self.text_prod_estoque.delete(0,tk.END)
        self.text_prod_preco.delete(0,tk.END)

    def exibir_categorias(self):
        list_dic = comandos_adicionar.Adicionar().exibir_categorias()
        popup = tk.Tk()
        popup.wm_title("Categoria(s)")
        popup.geometry("250x300+500+200")
        scrollbar = tk.Scrollbar(popup)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        list_categ = tk.Listbox(popup, yscrollcommand = scrollbar.set, background = "cyan", font="arial 12 ")
        for i in range(0, len(list_dic)):
            list_categ.insert(tk.END, "ID: " + str(list_dic[i]['id']) + "     NOME:  "+str(list_dic[i]['nome']))
        list_categ.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
        scrollbar.config(command = list_categ.yview)
    
    def exibir_produtos(self):
        list_dic = comandos_adicionar.Adicionar().exibir_produtos()
        popup = tk.Tk()
        popup.wm_title("Produto(s)")
        popup.geometry("450x200+500+200")
        scrollbar = tk.Scrollbar(popup)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        list_categ = tk.Listbox(popup, yscrollcommand = scrollbar.set, background = "cyan", font="arial 10 ")
        for i in range(0, len(list_dic)):
            list_categ.insert(tk.END, "ID: " + str(list_dic[i]['id']) + "        NOME: "+str(list_dic[i]['nome']) + "        ESTOQUE: "  + str(list_dic[i]['estoque']) +  "        PREÇO: "+ str(list_dic[i]['preco']))
        list_categ.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
        scrollbar.config(command = list_categ.yview)

    def exibir_clientes(self):
        list_dic = comandos_adicionar.Adicionar().exibir_clientes()
        popup = tk.Tk()
        popup.wm_title("Cliente(s)")
        popup.geometry("450x200+500+200")
        scrollbar = tk.Scrollbar(popup)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        list_categ = tk.Listbox(popup, yscrollcommand = scrollbar.set, background = "cyan", font="arial 12 ")
        for i in range(0, len(list_dic)):
            list_categ.insert(tk.END, "ID: " + str(list_dic[i]['id']) + "        NOME: "+str(list_dic[i]['nome']) + "        CPF: "  + str(list_dic[i]['cpf']) )
        list_categ.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
        scrollbar.config(command = list_categ.yview)

    def exibir_vendas(self):
        list_dic = comandos_adicionar.Adicionar().exibir_vendas()
        popup = tk.Tk()
        popup.wm_title("venda(s)")
        popup.geometry("450x200+500+200")
        scrollbar = tk.Scrollbar(popup)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        list_categ = tk.Listbox(popup, yscrollcommand = scrollbar.set, background = "cyan", font="arial 12 ")
        for i in range(0, len(list_dic)):
            list_categ.insert(tk.END, "ID: " + str(list_dic[i]['id']) + "        DATA: "+str(list_dic[i]['data']) + "        NOME do CLIENTE: "  + str(list_dic[i]['nome_cliente']) )
        list_categ.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
        scrollbar.config(command = list_categ.yview)

    def exibir_itensVendidos(self):
        list_dic = comandos_adicionar.Adicionar().exibir_itens_vendidos()
        popup = tk.Tk()
        popup.wm_title("Itens Vendidos")
        popup.geometry("600x200+500+200")
        scrollbar = tk.Scrollbar(popup)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        list_categ = tk.Listbox(popup, yscrollcommand = scrollbar.set, background = "cyan", font="arial 10")
        for i in range(0, len(list_dic)):
            list_categ.insert(tk.END, "ID: " + str(list_dic[i]['id']) + "        ID da VENDA: "+str(list_dic[i]['venda_id']) + "        ID do PRODUTO: "  + str(list_dic[i]['produto_id']) +  "           QUANTIDADE: "  +   str(list_dic[i]['quantidade'])  + "      VALOR: "  +  str(list_dic[i]['valor'])) 
        list_categ.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
        scrollbar.config(command = list_categ.yview)


Int_grafica()