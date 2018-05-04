#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time

from tools.readExcel import Excel
from tools.getDict import get_dc
from termcolor import *
from tools.write_log import write_log
from termcolor import *
import sys
class Driven:
    #实现数据驱动
    def driven_it(self):
        ex=Excel()
        table=ex.read_it("C:\\Users\\Administrator\\PycharmProjects\\aapium\\tools\\testData.xlsx")
        i=1
        for rownum in range(1,table.nrows):
            print "\n##### start Test Case"+str(i)+"  ####"
            '''获取行数据为列表形式'''
            list=table.row_values(rownum)
            print(list)
            #动态导入包
            __import__('testCase.'+list[1])#import testCase.Login
            #  #导入模块
            module=sys.modules['testCase.'+list[1]]#change Login()
            # #根据list[0]获取类
            c=getattr(module,list[1])#c=Login()
            # #实例化对象
            obj=c()#obi=Login()
            # #根据list[1]获取方法
            mtd=getattr(obj,list[2])#mtd=assert_suc
            try:
                dict=get_dc(list[3])
                print dict
                if list[4]=="":
                    mtd(dict)
                else:
                    mtd(dict,list[4])
            except Exception as e:
                nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                write_log(colored((nowTime+" error :"+str(e)+"\n"), "red"))
                print colored((nowTime+str(e)), "red")
                sys.exit()
            print("##### stop Test Case"+str(i)+"  ####\n")
            time.sleep(3)
            i+=1

dr=Driven()
dr.driven_it()
