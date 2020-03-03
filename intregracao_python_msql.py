import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Lucas_12j',
    database = 'LojaTeste'
)

cursor = conexao.cursor()

cursor.execute("select * from cliente")

for i in cursor:
    print(i)
