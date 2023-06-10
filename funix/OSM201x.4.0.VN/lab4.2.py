tc1 = [
        {'PName': 0, 'Arrtime': 0, 'Burtime': 24},
        {'PName': 1, 'Arrtime': 1, 'Burtime': 3},
        {'PName': 2, 'Arrtime': 2, 'Burtime': 3}
      ]

tc2 = [
        {'PName': 0, 'Arrtime': 0, 'Burtime': 12},
        {'PName': 1, 'Arrtime': 2, 'Burtime': 7},
        {'PName': 2, 'Arrtime': 5, 'Burtime': 8},
        {'PName': 3, 'Arrtime': 9, 'Burtime': 3},
        {'PName': 4, 'Arrtime': 12, 'Burtime': 6}
      ]

def FCFScomputed(tasks):
  tasks.sort(key=lambda x: x['Arrtime'])
  curTime = 0
  for task in tasks:
    task["Start"] = max(task["Arrtime"], curTime)
    task["WaitTime"] = curTime - task["Arrtime"]
    task["Finish"] = task["Start"] + task["Burtime"]
    task["TAT"] = task["Finish"] - task["Arrtime"]
    curTime = task["Finish"]
  tasks.sort(key=lambda x: x["PName"])
  print_computed_tasks(tasks)

def print_input_tasks(tasks):
  columns = ['PName', 'Arrtime', 'Burtime']
  print('|'+'|'.join(f" {k:^{len(k)}} " for k in columns)+'|')
  print('|'+'|'.join("-"*(len(k)+2) for k in columns)+'|')
  for task in tasks:
    print('|'+'|'.join(f" {task[k]:>{len(k)}} " for k in columns)+'|')

def print_computed_tasks(tasks):
  columns = ['PName', 'Arrtime', 'Burtime', 'Start', 'TAT', 'Finish', 'WaitTime']
  print('|'+'|'.join(f" {k:^{len(k)}} " for k in columns)+'|')
  print('|'+'|'.join("-"*(len(k)+2) for k in columns)+'|')
  for task in tasks:
    print('|'+'|'.join(f" {task[k]:>{len(k)}} " for k in columns)+'|')


if __name__ == '__main__':
  test_case = tc1
  print('---INPUT----')
  print_input_tasks(test_case)
  print('\n---OUTPUT----')
  FCFScomputed(test_case)