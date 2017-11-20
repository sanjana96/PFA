import gc
import MySQLdb
db_host = "127.0.0.1"
db_name = 'pfa'
db_user = 'root'
db_pass = ''
user_table = 'user'
debt_table = 'debt'
transaction_table = 'transaction'

def DBclose(c, conn):
    c.close()
    conn.close()
    gc.collect()


def DBconnect():
    conn = MySQLdb.connect(
        host=db_host,
        user=db_user,
        passwd=db_pass,
        db=db_name,
    )
    c = conn.cursor(MySQLdb.cursors.DictCursor)

    return c, conn
