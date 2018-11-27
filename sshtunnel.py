import pymysql
from sshtunnel import SSHTunnelForwarder

ssh_host = ""  # 堡垒ip
ssh_port = 22  # 端口
ssh_user = ""  # 堡垒机上用户名
ssh_password = ""  # 堡垒机上用户密码
mysql_host = "localhost"
mysql_port = 3306
mysql_user = "root"
mysql_password = "mysql"
mysql_db = ""

with SSHTunnelForwarder(
        (ssh_host, ssh_password),
        ssh_username=ssh_user,
        ssh_password=ssh_password,
        remote_bind_addredd=(mysql_host, mysql_port)) as server:
    conn = pymysql.connect(host=mysql_host, port=server.local_bind_port, user=mysql_user, passwd=mysql_password,
                           db=mysql_db)
    cursor = conn.cursor()
    cursor.execute("select * from user")
    print(cursor.fetchall())
    conn.commit()
    cursor.close()
    conn.close()
