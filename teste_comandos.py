import pymysql


conexao = pymysql.connect(host = 'localhost',user = 'root',passwd = 'Lucas_12j', database = 'folhapgto')
cursor = conexao.cursor()


cursor.execute("select id from categoria")

for i in cursor:
    print(i[0])

