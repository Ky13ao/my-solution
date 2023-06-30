import requests
from requests_ntlm import HttpNtlmAuth #, HttpNtlmSspiAuth

# site_url = 'https://hcmlocal1.corp.jabil.org/eDashboardPlus/_webforms/rep_mes_birthaging.aspx'
site_url = 'https://hcmlocal1.corp.jabil.org/eDashboardPlus/_webforms/mes_batchreport.aspx?b=S225-83826-230526'
reqHeaders = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.69'
}
ntlmAuth = HttpNtlmAuth('JABIL\SVCHCM_QSS', 'Quality6sigma!@#')
res = requests.get(site_url, auth=ntlmAuth, verify=False, headers = reqHeaders)

with open('rep_mes_birthaging_c26.html', 'w') as file:
# with open('rep_mes_birthaging.html', 'w') as file:
  file.write(res.text)
  file.close()
print('Done!')