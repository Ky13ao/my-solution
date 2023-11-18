import re

str='The advancements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com Then The New Yorker article on wind farms...'
#Type your answer here.

regex=r'[a-z0-9]+@\w+\.\w+'
emails=re.findall(regex, str)

print(emails)
#output: ['franky@google.com', 'sinatra123@yahoo.com']
