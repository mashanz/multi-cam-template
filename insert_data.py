import pymysql

db = pymysql.connect("127.0.0.1","root","op3nk3y","dbmulticam" )
cursor = db.cursor()
sql = """INSERT INTO OUTPUT(waktu, c11, c12, c13, c14, c15, c16, c21, c22, c23, c24, c25, c26) VALUES ('07:24:34', 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0)"""
try:
   cursor.execute(sql)
   db.commit()
   print("SUCCESS")
except:
   print("ERROR")
   db.rollback()
db.close()