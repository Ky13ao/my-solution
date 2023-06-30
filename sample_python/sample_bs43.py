from bs4 import BeautifulSoup
import re
import requests
from requests_ntlm import HttpNtlmAuth

site_url = 'https://hcmlocal1.corp.jabil.org/eDashboardPlus/_webforms/home.aspx'
reqHeaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.69'
}
ntlmAuth = HttpNtlmAuth('JABIL\SVCHCM_QSS', 'Quality6sigma!@#')
res = requests.get(site_url, auth=ntlmAuth, verify=False, headers=reqHeaders)
soup = BeautifulSoup(res.text, features="html.parser")
table = soup.find_all("input", attrs={"type": "hidden"})

aspHiddenFields = {}
for _ in table:
    idVal = _.get('id')
    valueVal = _.get('value')
    aspHiddenFields[idVal] = 'value'

aspHiddenFields['__EVENTTARGET'] = 'lnkbtnExportToExcel'

for _ in 'Step;Assembly;SerialNumber;WipGroup'.split(';'):
    aspHiddenFields['hid'+_] = ''

aspHiddenFields['hidCustomer_ID'] = 27

print(aspHiddenFields)

site_url = 'https://hcmlocal1.corp.jabil.org/eDashboardPlus/_webforms/rep_serialnumbers_bystep.aspx?c=27'
res = requests.post(site_url, auth=ntlmAuth, verify=False,
                    headers=reqHeaders, data=aspHiddenFields)

with open('rep_serialnumbers_bystep_c27.log', 'w') as file:
    # with open('rep_mes_birthaging.html', 'w') as file:
    file.write(res.text)
    file.close()
print('Done!')
# print(aspHiddenFields)
