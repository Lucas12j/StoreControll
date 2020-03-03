import pymysql
import tkinter as tk

class Adicionar(object):

    def __init__(self):
        self.conexao = pymysql.connect(host = 'localhost',user = 'root',passwd = 'Lucas_12j', database = 'LojaTeste')
        self.cursor = self.conexao.cursor()
        
        

    def adicidionar_categ(self, categoria):
        if categoria == "":
            self.popup_mensagem_atencao("ATENÇÃO. Campo em branco")
        else:
            comando = "insert into categoria (nome) values (%s)"
            categ_ins = (categoria)
            self.cursor.execute(comando, categ_ins)
            self.conexao.commit()
            self.popup_mensagem_sucesso("Categoria adicionada com sucesso")


    def adicionar_prod(self, nome, estoque, preco, nome_categ):
        id_categ = self.get_id(nome_categ, 3)
        try:
            if nome == "" or estoque == "" or preco == "" or nome_categ == "":
                self.popup_mensagem_atencao("ATENÇÃO. Um ou mais itens em branco")
            elif self.verif_exist(id_categ, 1) == False:
                self.popup_mensagem_atencao("ATENÇÃO. Esta categoria não existe.")
            else:
                comando = "insert into produto (nome, estoque, preco, categoria_id) values (%s,%s,%s,%s)"
                prod_ins = (nome, estoque, preco, id_categ)
                self.cursor.execute(comando, prod_ins)
                self.conexao.commit()
                self.popup_mensagem_sucesso("Produto adicionado com sucesso")
        except:
            self.popup_mensagem_erro()
        


    def adicionar_cliente(self, nome, cpf):
        if nome == "" or cpf == "":
            self.popup_mensagem_atencao("ATENÇÃO. Um ou mais itens em branco")
        else:
            comando = "insert into cliente (nome, cpf) values (%s, %s)"
            cliente_ins = (nome, cpf)
            self.cursor.execute(comando, cliente_ins)
            self.conexao.commit()
            self.popup_mensagem_sucesso("Cliente adicionado com sucesso")


    def adicionar_item_vend(self, quant, valor, nome_prod, id_venda):
        id_prod = self.get_id(nome_prod, 2)
        try:
            if quant == "" or valor == "" or nome_prod == "" or id_venda == "":
                self.popup_mensagem_atencao("ATENÇÃO. Um ou mais itens em branco")
            elif self.verif_exist(id_prod, 3) == False:
                self.popup_mensagem_atencao("ATENÇÃO. Este produto não existe.")
            elif self.verif_exist(int(id_venda), 4) == False:
                self.popup_mensagem_atencao("ATENÇÃO. Esta venda não existe.")
            else:
                comando = "insert into itemVendido (qtde, valor, venda_id, produto_id) values (%s,%s,%s,%s)"
                itemVendido_ins = (quant, valor, id_prod, id_venda)
                self.cursor.execute(comando, itemVendido_ins)
                self.conexao.commit()
                self.popup_mensagem_sucesso("Item vendido adicionado com sucesso")
        except:
            self.popup_mensagem_erro()
        

    def adicionar_venda(self, data, tipo, nome_cliente): #SEMPRE ENTRANDO NO "EXCEPT", VERIFICAR CAUSA
        id_cliente = self.get_id(nome_cliente, 1)
        try:
            if data == "" or nome_cliente == "":
                self.popup_mensagem_atencao("ATENÇÃO. Um ou mais itens em branco")
            elif self.verif_exist(id_cliente, 2) == False:
                self.popup_mensagem_atencao("ATENÇÃO. Este cliente não existe")
            else:
                data_formatada = self.format_data(data)
                comando = "insert into venda (_data, tipo, cliente_id) values (%s, %s, %s)"
                venda_ins = (data_formatada, tipo, id_cliente)
                self.cursor.execute(comando, venda_ins)
                self.conexao.commit()
                self.popup_mensagem_sucesso("Venda adicionada com sucesso")
        except:
            self.popup_mensagem_erro()

        
    def popup_mensagem_sucesso(self, msg):
        popup = tk.Tk()
        popup.wm_title("Concluído")
        popup.geometry("255x110+500+200")
        label = tk.Label(popup, text = msg, bg = "blue", fg = "yellow", font="NORM_FONT")
        label.grid(row=0, column = 0, sticky = "W")
        B1 = tk.Button(popup, text="Ok", command = popup.destroy, width = 20, bg = "cyan", fg = "black")
        B1.grid(row =1, column = 0, pady=53)
        
    def popup_mensagem_erro(self):
        popup = tk.Tk()
        popup.wm_title("ERRO!!")
        popup.geometry("255x110+1100+200")
        label = tk.Label(popup, text = "ERRO! Revise os dados inseridos.", bg = "red", fg = "yellow", font=("Arial", 11, "bold"))
        label.grid(row=0, column = 0)
        B1 = tk.Button(popup, text="Entendido", command = popup.destroy, width = 20, bg = "red", fg = "white")
        B1.grid(row =2, column = 0, pady=53)

    def popup_mensagem_atencao(self, msg):
        popup = tk.Tk()
        popup.wm_title("ATENÇÃO!!")
        popup.geometry("255x110+1100+200")
        label = tk.Label(popup, text = msg, bg = "yellow", fg = "black", font=("Arial", 10, "bold"))
        label.grid(row=0, column = 0)
        B1 = tk.Button(popup, text="Entendido", command = popup.destroy, width = 20, bg = "cyan", fg = "black")
        B1.grid(row =2, column = 0, pady=53)


    def format_data(self, data):
        data_sem_barra = ""
        lista = []
        for i in data:
            if i != "/":
                data_sem_barra = data_sem_barra + i
            else:
                pass
        for i in data_sem_barra:
            lista.append(i)
        ano = lista[4]+lista[5]+lista[6]+lista[7]
        mes = lista[2]+lista[3]
        dia = lista[0]+lista[1]
        data_farmatada = ano + "-" + mes + "-" + dia
        return(data_farmatada)
    
    def get_id (self, nome, opcao):
        if opcao == 1:
            self.cursor.execute("select nome,id from cliente")
            for i in self.cursor:
                if nome.lower() == i[0].lower():
                    return(i[1])
        if opcao == 2:
            self.cursor.execute("select nome,id from produto")
            for i in self.cursor:
                if nome.lower() == i[0].lower():
                    return(i[1])  
        
        if opcao ==3:
            self.cursor.execute("select nome,id from categoria")
            for i in self.cursor:
                if nome.lower() == i[0].lower():
                    return(i[1])
    def get_nome (self, id):
        self.cursor.execute("select nome,id from cliente")
        for i in self.cursor:
            if id == i[1]:
                return(i[0])



    def verif_exist(self, id, opcao):
        if opcao == 1:
            self.cursor.execute("select id from categoria")
            for i in self.cursor:
                if id == i[0]:
                    return True
                else:
                    pass
            return False
        elif opcao == 2:
            self.cursor.execute("select id from cliente")
            for i in self.cursor:
                if id == i[0]:
                    return True
                else:
                    pass
            return False
        elif opcao == 3:
            self.cursor.execute("select id from produto")
            for i in self.cursor:
                if id == i[0]:
                    return True
                else:
                    pass
            return False
        elif opcao == 4:
            self.cursor.execute("select id from venda")
            for i in self.cursor:
                if id == i[0]:
                    return True
                else:
                    pass
            return False

    
    def exibir_categorias(self):
        list_categ = []
        dic = {}
        cursor = self.conexao.cursor()
        cursor.execute("select * from categoria")
        for i in cursor:
            dic = {'id':i[0], 'nome':i[1]}
            list_categ.append(dic)
        return list_categ
    
    def exibir_produtos(self):
        list_prod = []
        dic = {}
        cursor = self.conexao.cursor()
        cursor.execute("select * from produto")
        for i in cursor:
            dic = {'id':i[0], 'nome':i[1], 'estoque':i[2], 'preco':i[3]}
            list_prod.append(dic)
        return list_prod

    def exibir_clientes(self):
        list_client = []
        dic = {}
        cursor = self.conexao.cursor()
        cursor.execute("select * from cliente")
        for i in cursor:
            dic = {'id':i[0], 'nome':i[1], 'cpf':i[2]}
            list_client.append(dic)
        return list_client
    
    def exibir_vendas(self):
        list_venda = []
        dic = {}
        cursor = self.conexao.cursor()
        cursor.execute("select * from venda")
        for i in cursor:
            nome = self.get_nome(i[2])
            dic = {'id':i[0], 'data':i[1], 'nome_cliente':nome}
            list_venda.append(dic)
        return list_venda
        
    def exibir_itens_vendidos(self):
        list_itens_vendidos= []
        dic = {}
        cursor = self.conexao.cursor()
        cursor.execute("select * from itemVendido")
        for i in cursor:
            dic = {'id':i[0], 'venda_id':i[1], 'produto_id':i[2], 'quantidade':i[3], 'valor':i[4]}
            list_itens_vendidos.append(dic)
        return list_itens_vendidos






    
    def verificar(self):
        cursor = self.conexao.cursor()
        cursor.execute("select * from venda")
        for i in cursor:
            print(i[1])




        


