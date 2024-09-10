# python3

class Query:
  def __init__(self, query):
    self.type = query[0]
    self.number = int(query[1])
    if self.type == 'add':
      self.name = query[2]

def read_queries():
  n = int(input())
  return [Query(input().split()) for i in range(n)]

def write_responses(result):
  print('\n'.join(result))

def process_queries(queries):
  result = []
  # Keep list of all existing (i.e. not deleted yet) contacts.
  contacts = []
  for cur_query in queries:
    
    if cur_query.type == 'add':
      # 1. if we already have contact with such number,
      # we should rewrite contact's name
      found = False
      for contact in contacts:
        if contact.number == cur_query.number:
          contact.name = cur_query.name
          found = True
          break
      if not found:
        contacts.append(cur_query)
      else: # 2. otherwise, just add it
        contacts.append(cur_query)
    elif cur_query.type == 'del':
      # 3. Delete a person with phone number from contact
      contacts = [contact for contact in contacts if contact.number != cur_query.number]
    else:
      response = 'not found'
      # 4.Search for a person with phone number
      # Return "not found" if there isn't such person in the contacts
      for contact in contacts:
        if contact.number == cur_query.number:
          response = contact.name
          break
      result.append(response)


  return result

if __name__ == '__main__':
  write_responses(process_queries(read_queries()))
