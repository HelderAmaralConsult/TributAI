import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

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

conn.close()
