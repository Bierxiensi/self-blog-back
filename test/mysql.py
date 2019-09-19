import pymysql

def get_conn():
    try:
        connection = pymysql.connect(host='localhost',
                                     port=3306,
                                     user='root',
                                     password='root',
                                     db='zxyaily',
                                     charset='utf8')
    except pymysql.err as e:
        print('error %d: %s' % (e.arg[0],e.args[1]))

    return connection
def sel():
    # 创建游标
    connection = get_conn()
    cursor = connection.cursor()
    effect_row = cursor.execute("select * from zxyaily")
    effect_row1= cursor.fetchall()
    print(effect_row,effect_row1)

def ins():
    try:
        connection = get_conn()
        # 获取链接和cursor
        cursor = connection.cursor()
        sql1 = "insert into zxyaily(id,a,say,b,time) values('%d','%s','%s','%s','%s')"%(4,'3','3','3','2019-09-02')
        # sql3 = ("insert into test value(%s,%s)")
        # 执行sql，提交数据到数据库
        cursor.execute(sql1)
        # cursor.execute(sql3,(2,'ly'))
        # 提交事务
        connection.commit()
        cursor.close()
        connection.close()
    except:
        print('error')
        connection.commit()
        # 回滚到提交前
        connection.rollback()
        connection.close()

if __name__ == '__main__':
    ins()
