#coding=utf-8

import MySQLdb,sys


class TransferMoney(object):
    def __init__(self,conn):
        self.conn=conn

    def check_acct_available(self,acctid):
        cursor = self.conn.cursor()
        try:
            sql="select * from account where acctid=%s"%acctid
            print 'check_acct_available'+':'+sql
            cursor.execute(sql)
            rs=cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号%s不存在" %acctid)
        finally:
            cursor.close()

    def has_enough_money(self,source_acctid,money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid=%s and money>%s" %(source_acctid,money)
            print 'has_enough_money' +':'+ sql
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账户%s余额不足" %source_acctid)
        finally:
            cursor.close()

    def reduce_money(self,source_acctid,money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money-%s where acctid=%s" %(money,source_acctid)
            print 'reduce_money' +':'+ sql
            cursor.execute(sql)
            rs = cursor.fetchall()
            if cursor.rowcount != 1:
                raise Exception("账户%s无法转钱" % source_acctid)
        finally:
            cursor.close()

    def add_money(self,target_acctid,money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money+%s where acctid=%s" % (money, target_acctid)
            print 'add_money'+':' + sql
            cursor.execute(sql)
            rs = cursor.fetchall()
            if cursor.rowcount != 1:
                raise Exception("账户%s未能成功充值" % target_acctid)
        finally:
            cursor.close()

    def transfer(self,source_acctid,target_acctid,money):
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid,money)
            self.reduce_money(source_acctid,money)
            self.add_money(target_acctid,money)
            self.conn.commit()
        except Exception as e:
            print "转账失败"
            raise e



if __name__ == '__main__':
    # source_acctid=sys.argv[1]
    # target_acctid=sys.argv[2]
    # money=sys.argv[3]

    conn = MySQLdb.Connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           passwd='skysnow',
                           db='imooc',
                           charset='utf8'
                           )
    tr_money=TransferMoney(conn)
    tr_money.transfer(1,2,100)