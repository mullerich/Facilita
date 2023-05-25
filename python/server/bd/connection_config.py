import pymysql

# Conectando ao banco de dadps
def createConnection(local=False):
    # Dados do banco de dados online
    
    bd_online = {
        'host': 'sql10.freesqldatabase.com',
        'name': 'sql10620948',
        'user': 'sql10620948',
        'password': 'nCZyq6rlFj',
        'port': 3306
    }

    bd_local1 = {
        'Host': 'localhost',
        'Database name': 'sisu',
        'Database user': 'root',
        'Database password': '',
        'Port number': 3306
    }
    
    bd = bd_local1 if local else bd_online
    connection = pymysql.connect(host=bd['host'], user=bd['user'], password=bd['password'], database=bd['name'])
    return connection
