import os
import oracledb 
from dotenv import load_dotenv

load_dotenv()

dsn = "(description=(retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.sa-saopaulo-1.oraclecloud.com))(connect_data=(service_name=gf843f88c3e3b9d_tributaidb_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))"

conn = oracledb.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    dsn=os.getenv("DB_DSN"),
    config_dir=os.getenv("WALLET_DIR"),
    wallet_location=os.getenv("WALLET_DIR")
    )

print("Conectou!")
print(conn.version)
with conn.cursor() as cur:
    cur.execute("select sysdate from dual")
    print(cur.fetchone())

with conn.cursor() as cur:
   cur.execute("""SELECT table_name
                  FROM user_tables
              ORDER BY table_name
   """)
   for row in cur:
     print(row[0])

conn.close()

