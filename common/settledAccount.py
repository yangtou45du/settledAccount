import requests
class settledAccount():
    def POST(self,dict):
        url="http://amstest4.phkjcredit.com/ams_web/ContextServlet"
        dict['action']= "com.hansy.forsaler.action.ForSalerAction"
        dict['method']="queryLoanTypeByLoanNo"
        re=requests.post(url,data=dict)
        return re.text
#dict={'loanNo':"640102016041803097"}
#f=settledAccount().POST(dict)
