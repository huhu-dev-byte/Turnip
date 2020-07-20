# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 10:25
# @Author  : TingXiu.KE

import os
import xlrd

class turnip():
    Sun = float(0)
    Mom_AM = float(0)
    Mom_PM = float(0)
    Tue_AM = float(0)
    Tue_PM = float(0)
    Wen_AM = float(0)
    Wen_PM = float(0)
    Thr_AM = float(0)
    Thr_PM = float(0)
    Fri_AM = float(0)
    Fri_PM = float(0)
    Sat_AM = float(0)
    Sat_PM = float(0)
    One_Model = False #波形
    Two_Model = False #递减型
    Three_Model = False
    Four_Model = False
    addprice = 0
    reduceprice = 0
    expec = 0


    def readprice(self):
        data = xlrd.open_workbook('turnip.xlsx')
        table =data.sheets()[0]
        self.Sun = table.cell_value(1,0)
        self.Mom_AM = table.cell_value(1,1)
        self.Mom_PM = table.cell_value(1,2)
        self.Tue_AM = table.cell_value(1,3)
        self.Tue_PM = table.cell_value(1,4)
        self.Wen_AM = table.cell_value(1,5)
        self.Wen_PM = table.cell_value(1,6)
        self.Thr_AM = table.cell_value(1,7)
        self.Thr_PM = table.cell_value(1,8)
        self.Fri_AM = table.cell_value(1,9)
        self.Fri_PM = table.cell_value(1,10)
        self.Sat_AM = table.cell_value(1,11)
        self.Sat_PM = table.cell_value(1,12)
        return self.Sun,self.Mom_AM,self.Mom_PM,self.Tue_AM,self.Tue_PM,self.Wen_AM,self.Wen_PM,self.Thr_AM,self.Thr_PM,self.Fri_AM,self.Fri_PM,self.Sat_AM,self.Sat_PM


    def inputsunPrice(self):
        a = input('输入周日价格：')
        return a
    def sunPriceCheck(self,price):
        #price = self.inputsunPrice()
        if str(price).replace('.','').isdigit():
            if float(90) <= float(price) <= float(110) :
                self.Sun = price
            else:
                print("大头菜价格在90-110之间，请重新输入")
                self.Sun = self.inputsunPrice()
        else:
            print('需要输入整数')
            self.Sun = self.inputsunPrice()
        return self.Sun
    def inputPrice(self):
        a = input('输入价格（没有输入0）：')
        try:
            a.isdigit()
        except Exception as e:
            print(e)
        return a

    def TurnipModel(self):
        if float(self.Mom_AM)/float(self.Sun)*float(100) > float(91):
            self.One_Model = True
            self.Four_Model = True
            self.Two_Model = False
            self.Three_Model = False
            print('当前可能是波形或者四期型')
        elif float(85)<= float(self.Mom_AM)/float(self.Sun)*float(100) <= float(91):
            self.Three_Model = True
            self.Four_Model = True
            self.Two_Model =True
            self.One_Model = False
            print('当前可能是3期或者4期或者递减型')
        elif float(80)<=float(self.Mom_AM)/float(self.Sun)*float(100) < float(85):
            self.Three_Model = True
            self.Four_Model = True
            self.One_Model = False
            self.Two_Model = False
            print('当前可能是3期或者4期')
        elif float(60)<= float(self.Mom_AM)/float(self.Sun)*float(100)<float(80):
            self.One_Model = True
            self.Four_Model = True
            self.Two_Model = False
            self.Three_Model = False
            print('当前可能是波形或者4期')
        elif float(self.Mom_AM)/float(self.Sun)*float(100) <float(60):
            self.Four_Model = True
            self.One_Model = False
            self.Two_Model = False
            self.Three_Model = False
            print('接近4期')
            print('四期的范围在：' + str(round(float(1.4) * float(self.Sun), 2)) + '~' + str(round(float(2) * float(self.Sun), 2)) + '之间')
        #print(self.One_Model,self.Two_Model,self.Three_Model,self.Four_Model)
        return  self.One_Model,self.Two_Model,self.Three_Model,self.Four_Model

    def TurnipMake(self):
        if self.One_Model and self.Four_Model:
           if float(self.Mom_AM) >float(self.Mom_PM) and float(self.Mom_PM)>float(self.Mom_AM) and float(self.Tue_AM)>float(self.Mom_PM) and float(self.Tue_PM) >float(self.Tue_AM):
               self.addprice = 4
           elif float(self.Mom_PM)>float(self.Mom_AM) and float(self.Tue_AM)>float(self.Mom_PM) and float(self.Tue_PM) >float(self.Tue_AM) and float(self.Wen_AM)>float(self.Tue_PM):
               self.addprice = 4
           elif float(self.Tue_AM)>float(self.Mom_PM) and float(self.Tue_PM) >float(self.Tue_AM) and float(self.Wen_AM)>float(self.Tue_PM) and float(self.Wen_PM)>float(self.Wen_AM):
               self.addprice = 4
           elif float(self.Tue_PM) >float(self.Tue_AM) and float(self.Wen_AM)>float(self.Tue_PM) and float(self.Wen_PM)>float(self.Wen_AM) and float(self.Thr_AM)>float(self.Wen_PM):
               self.addprice = 4
           elif float(self.Wen_AM)>float(self.Tue_PM) and float(self.Wen_PM)>float(self.Wen_AM) and float(self.Thr_AM)>float(self.Wen_PM) and float(self.Thr_PM)>float(self.Thr_AM):
               self.addprice = 4
           elif float(self.Wen_PM)>float(self.Wen_AM) and float(self.Thr_AM)>float(self.Wen_PM) and float(self.Thr_PM)>float(self.Thr_AM) and float(self.Fri_AM)>float(self.Thr_PM):
               self.addprice = 4
           elif float(self.Thr_AM)>float(self.Wen_PM) and float(self.Thr_PM)>float(self.Thr_AM) and float(self.Fri_AM)>float(self.Thr_PM) and float(self.Fri_PM)>float(self.Fri_AM):
               self.addprice = 4
           elif float(self.Thr_PM)>float(self.Thr_AM) and float(self.Fri_AM)>float(self.Thr_PM) and float(self.Fri_PM)>float(self.Fri_AM) and float(self.Sat_AM)>float(self.Fri_PM):
               self.addprice = 4
           else:
                print('当前是波动性,如果范围当前售价在:'+str(round(float(1.1)*float(self.Sun),2))+'~'+str(round(float(1.5)*float(self.Sun),2))+',可以卖掉')

        elif self.Two_Model and self.Three_Model and self.Four_Model:
            if float(self.Mom_AM) > float(self.Mom_PM) and float(self.Mom_PM) > float(self.Mom_AM) and float(self.Tue_AM) > float(self.Mom_PM) and float(self.Tue_PM) < float(self.Tue_AM):
                self.addprice = 3
            elif float(self.Mom_PM)>float(self.Mom_AM) and float(self.Tue_AM)>float(self.Mom_PM) and float(self.Tue_PM) >float(self.Tue_AM) and float(self.Wen_AM)<float(self.Tue_PM):
                self.addprice = 3
            elif float(self.Tue_AM)>float(self.Mom_PM) and float(self.Tue_PM) >float(self.Tue_AM) and float(self.Wen_AM)>float(self.Tue_PM) and float(self.Wen_PM)<float(self.Wen_AM):
                self.addprice = 3
            elif float(self.Tue_PM) > float(self.Tue_AM) and float(self.Wen_AM) > float(self.Tue_PM) and float(self.Wen_PM) > float(self.Wen_AM) and float(self.Thr_AM)<float(self.Wen_PM):
                self.addprice = 3
            elif float(self.Wen_AM) > float(self.Tue_PM) and float(self.Wen_PM) > float(self.Wen_AM) and float(self.Thr_AM) > float(self.Wen_PM) and float(self.Thr_PM)<float(self.Thr_AM):
                self.addprice = 3
            elif float(self.Wen_PM) > float(self.Wen_AM) and float(self.Thr_AM) > float(self.Wen_PM) and float(self.Thr_PM) > float(self.Thr_AM) and float(self.Fri_AM)<float(self.Thr_PM):
                self.addprice = 3
            elif float(self.Thr_AM) > float(self.Wen_PM) and float(self.Thr_PM) > float(self.Thr_AM) and float(self.Fri_AM) > float(self.Thr_PM) and float(self.Fri_PM)<float(self.Fri_AM):
                self.addprice = 3
            elif float(self.Thr_PM) > float(self.Thr_AM) and float(self.Fri_AM) > float(self.Thr_PM) and float(self.Fri_PM) > float(self.Fri_AM) and float(self.Sat_AM)<float(self.Fri_PM):
                self.addprice = 3
            elif float(self.Mom_AM) > float(self.Mom_PM) and float(self.Mom_PM) > float(self.Mom_AM) and float(self.Tue_AM) > float(self.Mom_PM) and float(self.Tue_PM) > float(self.Tue_AM):
                self.addprice = 4
            elif float(self.Mom_PM) > float(self.Mom_AM) and float(self.Tue_AM) > float(self.Mom_PM) and float(self.Tue_PM) > float(self.Tue_AM) and float(self.Wen_AM) > float(self.Tue_PM):
                self.addprice = 4
            elif float(self.Tue_AM) > float(self.Mom_PM) and float(self.Tue_PM) > float(self.Tue_AM) and float(self.Wen_AM) > float(self.Tue_PM) and float(self.Wen_PM) > float(self.Wen_AM):
                self.addprice = 4
            elif float(self.Tue_PM) > float(self.Tue_AM) and float(self.Wen_AM) > float(self.Tue_PM) and float(self.Wen_PM) > float(self.Wen_AM) and float(self.Thr_AM) > float(self.Wen_PM):
                self.addprice = 4
            elif float(self.Wen_AM) > float(self.Tue_PM) and float(self.Wen_PM) > float(self.Wen_AM) and float(self.Thr_AM) > float(self.Wen_PM) and float(self.Thr_PM) > float(self.Thr_AM):
                self.addprice = 4
            elif float(self.Wen_PM) > float(self.Wen_AM) and float(self.Thr_AM) > float(self.Wen_PM) and float(self.Thr_PM) > float(self.Thr_AM) and float(self.Fri_AM) > float(self.Thr_PM):
                self.addprice = 4
            elif float(self.Thr_AM) > float(self.Wen_PM) and float(self.Thr_PM) > float(self.Thr_AM) and float(self.Fri_AM) > float(self.Thr_PM) and float(self.Fri_PM) > float(self.Fri_AM):
                self.addprice = 4
            elif float(self.Thr_PM) > float(self.Thr_AM) and float(self.Fri_AM) > float(self.Thr_PM) and float(self.Fri_PM) > float(self.Fri_AM) and float(self.Sat_AM) > float(self.Fri_PM):
                self.addprice = 4
            else:
                 print('可能时间还没到,如果已经周四下午，那么就是递减型了')

        elif self.Three_Model and self.Four_Model:
            if float(self.Mom_AM) > float(self.Mom_PM) and float(self.Mom_PM) > float(self.Mom_AM) and float(self.Tue_AM) > float(self.Mom_PM) and float(self.Tue_PM) < float(self.Tue_AM):
                self.addprice = 3
            elif float(self.Mom_PM)>float(self.Mom_AM) and float(self.Tue_AM)>float(self.Mom_PM) and float(self.Tue_PM) >float(self.Tue_AM) and float(self.Wen_AM)<float(self.Tue_PM):
                self.addprice = 3
            elif float(self.Tue_AM)>float(self.Mom_PM) and float(self.Tue_PM) >float(self.Tue_AM) and float(self.Wen_AM)>float(self.Tue_PM) and float(self.Wen_PM)<float(self.Wen_AM):
                self.addprice = 3
            elif float(self.Tue_PM) > float(self.Tue_AM) and float(self.Wen_AM) > float(self.Tue_PM) and float(self.Wen_PM) > float(self.Wen_AM) and float(self.Thr_AM)<float(self.Wen_PM):
                self.addprice = 3
            elif float(self.Wen_AM) > float(self.Tue_PM) and float(self.Wen_PM) > float(self.Wen_AM) and float(self.Thr_AM) > float(self.Wen_PM) and float(self.Thr_PM)<float(self.Thr_AM):
                self.addprice = 3
            elif float(self.Wen_PM) > float(self.Wen_AM) and float(self.Thr_AM) > float(self.Wen_PM) and float(self.Thr_PM) > float(self.Thr_AM) and float(self.Fri_AM)<float(self.Thr_PM):
                self.addprice = 3
            elif float(self.Thr_AM) > float(self.Wen_PM) and float(self.Thr_PM) > float(self.Thr_AM) and float(self.Fri_AM) > float(self.Thr_PM) and float(self.Fri_PM)<float(self.Fri_AM):
                self.addprice = 3
            elif float(self.Thr_PM) > float(self.Thr_AM) and float(self.Fri_AM) > float(self.Thr_PM) and float(self.Fri_PM) > float(self.Fri_AM) and float(self.Sat_AM)<float(self.Fri_PM):
                self.addprice = 3
            if float(self.Mom_AM) > float(self.Mom_PM) and float(self.Mom_PM) > float(self.Mom_AM) and float(self.Tue_AM) > float(self.Mom_PM) and float(self.Tue_PM) > float(self.Tue_AM):
                self.addprice = 4
            elif float(self.Mom_PM) > float(self.Mom_AM) and float(self.Tue_AM) > float(self.Mom_PM) and float(self.Tue_PM) > float(self.Tue_AM) and float(self.Wen_AM) > float(self.Tue_PM):
                self.addprice = 4
            elif float(self.Tue_AM) > float(self.Mom_PM) and float(self.Tue_PM) > float(self.Tue_AM) and float(self.Wen_AM) > float(self.Tue_PM) and float(self.Wen_PM) > float(self.Wen_AM):
                self.addprice = 4
            elif float(self.Tue_PM) > float(self.Tue_AM) and float(self.Wen_AM) > float(self.Tue_PM) and float(self.Wen_PM) > float(self.Wen_AM) and float(self.Thr_AM) > float(self.Wen_PM):
                self.addprice = 4
            elif float(self.Wen_AM) > float(self.Tue_PM) and float(self.Wen_PM) > float(self.Wen_AM) and float(self.Thr_AM) > float(self.Wen_PM) and float(self.Thr_PM) > float(self.Thr_AM):
                self.addprice = 4
            elif float(self.Wen_PM) > float(self.Wen_AM) and float(self.Thr_AM) > float(self.Wen_PM) and float(self.Thr_PM) > float(self.Thr_AM) and float(self.Fri_AM) > float(self.Thr_PM):
                self.addprice = 4
            elif float(self.Thr_AM) > float(self.Wen_PM) and float(self.Thr_PM) > float(self.Thr_AM) and float(self.Fri_AM) > float(self.Thr_PM) and float(self.Fri_PM) > float(self.Fri_AM):
                self.addprice = 4
            elif float(self.Thr_PM) > float(self.Thr_AM) and float(self.Fri_AM) > float(self.Thr_PM) and float(self.Fri_PM) > float(self.Fri_AM) and float(self.Sat_AM) > float(self.Fri_PM):
                self.addprice = 4

        elif self.One_Model and self.Four_Model:
            if float(self.Mom_AM) > float(self.Mom_PM) and float(self.Mom_PM) > float(self.Mom_AM) and float(self.Tue_AM) > float(self.Mom_PM) and float(self.Tue_PM) > float(self.Tue_AM):
                self.addprice = 4
                print('当前最高值')
            elif float(self.Mom_PM) > float(self.Mom_AM) and float(self.Tue_AM) > float(self.Mom_PM) and float(self.Tue_PM) > float(self.Tue_AM) and float(self.Wen_AM) > float(self.Tue_PM):
                self.addprice = 4
                print('当前最高值')
            elif float(self.Tue_AM) > float(self.Mom_PM) and float(self.Tue_PM) > float(self.Tue_AM) and float(self.Wen_AM) > float(self.Tue_PM) and float(self.Wen_PM) > float(self.Wen_AM):
                self.addprice = 4
            elif float(self.Tue_PM) > float(self.Tue_AM) and float(self.Wen_AM) > float(self.Tue_PM) and float(self.Wen_PM) > float(self.Wen_AM) and float(self.Thr_AM) > float(self.Wen_PM):
                self.addprice = 4
            elif float(self.Wen_AM) > float(self.Tue_PM) and float(self.Wen_PM) > float(self.Wen_AM) and float(self.Thr_AM) > float(self.Wen_PM) and float(self.Thr_PM) > float(self.Thr_AM):
                self.addprice = 4
            elif float(self.Wen_PM) > float(self.Wen_AM) and float(self.Thr_AM) > float(self.Wen_PM) and float(self.Thr_PM) > float(self.Thr_AM) and float(self.Fri_AM) > float(self.Thr_PM):
                self.addprice = 4
            elif float(self.Thr_AM) > float(self.Wen_PM) and float(self.Thr_PM) > float(self.Thr_AM) and float(self.Fri_AM) > float(self.Thr_PM) and float(self.Fri_PM) > float(self.Fri_AM):
                self.addprice = 4
            elif float(self.Thr_PM) > float(self.Thr_AM) and float(self.Fri_AM) > float(self.Thr_PM) and float(self.Fri_PM) > float(self.Fri_AM) and float(self.Sat_AM) > float(self.Fri_PM):
                self.addprice = 4
            else:
                print('当前可能是波动性,如果范围当前售价在:'+str(float(1.1)*float(self.Sun))+'~'+str(float(1.45)*float(self.Sun))+',可以卖掉')

        elif self.One_Model == False and self.Two_Model == True and self.Three_Model == False and self.Four_Model ==False:
            print('哦豁。递减！！！！')

        if self.addprice == 3:
            print('现在是三期最大值，可以卖掉\n'+'三期的范围在：'+str(round(float(2)*float(self.Sun),2))+'~'+str(round(float(6)*float(self.Sun),2))+'之间')
        elif self.addprice == 4:
            print('现在是四期最大值，可以卖掉\n'+'四期的范围在：'+str(round(float(1.4)*float(self.Sun),2))+'~'+str(round(float(2)*float(self.Sun),2))+'之间')




if __name__ == '__main__':
    turn = turnip()
    turn.readprice()
    turn.sunPriceCheck(turn.Sun)

    a = ''
    while a != float(0):
        a = turn.Mom_AM
        if a == float(0):
            print('现在周日')
            continue
        turn.TurnipModel()
        a = turn.Mom_PM
        if a == float(0):
            print('现在周一上午')
            continue
        a = turn.Tue_AM
        if a == float(0):
            print('现在周一下午')
            continue
        a = turn.Tue_PM
        if a == float(0):
            print('现在周二上午')
            continue
        a = turn.Wen_AM
        if a == float(0):
            print('现在周二下午')
            continue
        a = turn.Wen_PM
        if a == float(0):
            print('现在周三上午')
            continue
        a = turn.Thr_AM
        if a == float(0):
            print('现在周三下午')
            continue
        a = turn.Thr_PM
        if a == float(0):
            print('现在周四上午')
            continue
        a = turn.Fri_AM
        if a == float(0):
            print('现在周四下午')
            continue
        a = turn.Fri_PM
        if a == float(0):
            print('现在周五上午')
            continue
        a = turn.Sat_AM
        if a == float(0):
            print('现在周五下午')
            continue
        a = turn.Sat_PM
        if a == float(0):
            print('现在周六上午')
            continue
        break
    else:
        pass
    turn.TurnipMake()





