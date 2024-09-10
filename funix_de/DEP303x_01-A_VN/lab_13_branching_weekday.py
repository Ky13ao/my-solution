from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator

from datetime import datetime

tabDays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
def _weekday_choice():
  return f"task_for_{tabDays[datetime.now().weekday()]}"


with DAG('branching_weekday', 
         start_date=datetime(2023,1,1), 
         schedule='@daily', 
         catchup=False) as dag:
  branching = BranchPythonOperator(
    task_id='branching',
    python_callable=_weekday_choice
  )
  for tabDay in tabDays:
    empty = EmptyOperator(task_id=f'task_for_{tabDay}')

    branching >> empty