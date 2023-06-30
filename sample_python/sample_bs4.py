from bs4 import BeautifulSoup
import re 

html = open('rep_mes_birthaging.log', 'r').read()

soup = BeautifulSoup(html, features="html.parser")
table = soup.find("table", attrs={"id":"gvData"})

# The first tr contains the field names.
# headings = [th.get_text() for th in table.find("tr").find_all("th")]

customers = []
for row in table.find_all("tr")[1:]:
  row_cells = row.find_all("td")
  if(len(row_cells)>1):
    if(row_cells[1].get_text()!='0' and row_cells[-1].get_text()!='0'):
      customer = {'c_name': row_cells[0].get_text(), 'c_query': re.sub(r'\D+\?', '', row_cells[0].find_all('a')[0].get('href'))}
      customers.append(customer)
