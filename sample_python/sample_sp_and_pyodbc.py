import requests

sp_site_url = ""
sp_library_name = "Site_Attachments"

url = f'{sp_site_url}/_api/web/lists/GetByTitle(\'{sp_library_name}\')/items'
headers = {'Accept': 'application/json;odata=nometadata'}
response = requests.get(url, headers=headers)
data = response.json()

print(data)