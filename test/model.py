import pymysql
# 打开数据库连接
db = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='zxyaily',charset='utf8')


def sel():
    cursor = db.cursor()
    res = cursor.execute("select * from zxyaily")
    if(res):
        return res
    else:
        return 'error'
