#coding=utf-8
'''
python connector mysql,mysqlfor python
1.python访问db的开发官方接口规范
2.python开发db程序的开发环境
3.python访问db的connection,cursor俩大对象,分别用于连接，交互 exception异常
host port uesr passwd db charset
 1.connection 对象的方法
    cursor()            使用该连接创建并返回游标
    commit()            提交当前事务   autocommit(Flase)
    rollback()          回滚当前事务
    close()             关闭连接
 2.cursor对象
    execute(op[,args])  执行一个数据库查询和命令
    fetchone()          去结果集的下一行
    fetchmany(size)     获取结果集的下几行
    fetchall()          获取结果集中剩下的所有行
    rowcount            最近一次execute返回数据的行数或影响行数
    close()             关闭游标对象
    python执行insert,update,delete语句
4.python执行增删改查
5.完整实例:银行转账
'''
import MySQLdb
conn=MySQLdb.Connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='skysnow',
                         db='imooc',
                         charset='utf8'
                         )
cursor=conn.cursor()

insert="insert into user values(1,'sky','kkkkk','i am bad man')"
try:
    cursor.execute(insert)
    conn.commit()
except Exception as e:
    print e
    conn.rollback()
    print cursor.rowcount
    cursor.execute("select * from user")
    print cursor.fetchone()

cursor.close()
conn.close()

