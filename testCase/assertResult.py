#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-
import time
import json
from common.settledAccount import settledAccount
from tools.write_log import write_log
from termcolor import *
class assertResult():
    def assert_result(self,dict,exception):
        re=settledAccount().POST(dict)
        result=re.encode('gbk')#��unicodeתΪstr
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if exception==result:
            write_log('\n' + nowTime + " test sucessful" + '\n')
            print  colored(('\n' + nowTime + "test  sucessful" + '\n'), "green")
        else:
            print ("exception:%s"%exception)
            print ("result:%s"%result)
            write_log(colored(('\n' + nowTime + "  test fail" + '\n'), "red"))
            print colored(('\n' + nowTime + " test fail" + '\n'), "red")


#dict={'loanNo':"640102016041803097"}
#exception="{\"message\":\"��ѯʧ�ܣ������Ŵ�����߸ô���δ���ڣ�\",\"settleState\":\"\",\"normalState\":\"\",\"code\":0}"
#f=assertResult().assert_result(dict,exception)

