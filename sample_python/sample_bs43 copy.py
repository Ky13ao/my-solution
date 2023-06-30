import pandas as pd
from bs4 import BeautifulSoup


def bodyString(body_dict):
    import urllib
    return '&'.join(['{0}={1}'.format(k, urllib.parse.quote(str(body_dict[k]).encode('utf8') if body_dict[k] else '', safe=''))
                     for k in body_dict])


def xhRequest(url_string, method='get', body_string='', headers={}, user_name="jabil\\svchcm_zebra", pwd="97v6CGFcYM"):
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'
    from win32com.client import Dispatch as CreateObject
    __xhr = CreateObject("msxml2.xmlhttp.6.0")
    __result = {}
    __bAsync = method != 'get'
    __completed = False

    __xhr.open(method.upper(), url_string, __bAsync, user_name, pwd)
    for __header in headers:
        __xhr.setRequestHeader(__header, headers[__header])
    __xhr.send(body_string)
    if __bAsync:
        __readyState = -1
        while not __completed:
            if __xhr.readyState == 4:
                __completed = True
            if __xhr.readyState != __readyState:
                __readyState = __xhr.readyState
                # if __readyState == 1:
                #     __xhr.send(body_string)
                print(__readyState, __bAsync, __completed)
    __result = __xhr
    return __result

# res = interRequest(
#     'https://hcmlocal1.corp.jabil.org/eDashboardPlus/_webforms/home.aspx')


res = xhRequest(
    'https://hcmlocal1.corp.jabil.org/eDashboardPlus/_webforms/rep_serialnumbers_bystep.aspx')

# html = open('rep_serialnumbers_bystep_c27.html', 'r').read()
# soup = BeautifulSoup(html, features="html.parser")
soup = BeautifulSoup(res.responseText, features="html.parser")
table = soup.find_all("input", attrs={"type": "hidden"})

print(res.getAllResponseHeaders())
aspHiddenFields = {_.get('id'): _.get(
    'value') if _.get('value') else '' for _ in table}
aspHiddenFields['hidCustomer_ID'] = '27'
aspHiddenFields['__EVENTTARGET'] = 'lnkbtnExportToExcel'
res = xhRequest('https://hcmlocal1.corp.jabil.org/eDashboardPlus/_webforms/rep_serialnumbers_bystep.aspx?c=27',
                method='post',
                headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body_string=bodyString(aspHiddenFields))


# print(type(res.content), res.status_code, res.headers, res.request.body)
# fh = io.BytesIO(res.content)
# df = pd.io.excel.read_excel(fh, sheet_name='MESAgingReport', engine='openpyxl')
with open('rep_serialnumbers_bystep_c27.log', 'wb') as f:
    f.write(res.responseBody)
    f.close()
# print(df.head())
print('done')
# res.close()
