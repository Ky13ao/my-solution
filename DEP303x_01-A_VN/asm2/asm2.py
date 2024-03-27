from airflow import DAG
# phiên bản 2.8.3 DummyOperator được thay bởi EmptyOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator, PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.trigger_rule import TriggerRule

from datetime import datetime
from os import path

# file google_drive_downloader.py đã down về đặt tên là gdd.py
from gdd import GoogleDriveDownloader as gdd

questions_csv_fpath = '/tmp/Questions.csv'
answers_csv_fpath = '/tmp/Answers.csv'

def _exe_gg_download(ti):
  file_ids = {
    'download_anwser_file': '1FflYh-YxXDvJ6NyE9GNhnMbB-M87az0Y',
    'download_question_file': '1pzhWKoKV3nHqmC7FLcr5SzF7qIChsy9B'
  }
  id = file_ids.get(ti.task_id)
  if id is None:
    return
  dests = {
    'download_anwser_file': answers_csv_fpath,
    'download_question_file': questions_csv_fpath
  }
  gdd.download_file_from_google_drive(file_id=id, dest_path=dests.get(ti.task_id))

def _mongoimport_command(task_for):
  mongodb_host = '172.31.48.1'
  file_path = {
    'Questions': questions_csv_fpath,
    'Answers': answers_csv_fpath,
    'SparkOutput': '/tmp/asm2_spark_output.csv'
  }.get(task_for)
  command = f'mongoimport --type csv -h {mongodb_host} -d ASM2_dev -c {task_for} --headerline --drop {file_path}'
  return command

def _branch_choice():
  if path.exists(questions_csv_fpath) and path.exists(answers_csv_fpath):
    return 'end'
  return 'clear_file'

with DAG('asm2_datapipeline_cloud_bigdata',
         start_date=datetime(2024,1,1),
         schedule='@daily',
         catchup=False) as dag:
  
  ## start task
  start = EmptyOperator(task_id='start')
  
  ## branching: check whether both questions.csv and answers.csv exists
  branching = BranchPythonOperator(
    task_id='branching',
    python_callable=_branch_choice
  )

  ## clear_file task
  clear_file = BashOperator(
    task_id='clear_file',
    bash_command=f'rm -f {questions_csv_fpath} && rm -f {answers_csv_fpath}'
  )

  ## download_anwser_file task
  download_anwser_file = PythonOperator(
    task_id='download_anwser_file',
    python_callable=_exe_gg_download)

  ## import_answers_mongo task
  import_answers_mongo = BashOperator(
    task_id='import_answers_mongo',
    bash_command=_mongoimport_command('Answers'))

  ## download_question_file task
  download_question_file = PythonOperator(
    task_id='download_question_file',
    python_callable=_exe_gg_download)

  ## import_questions_mongo
  import_questions_mongo = BashOperator(
    task_id='import_questions_mongo',
    bash_command=_mongoimport_command('Questions'))

  ## spark_process task, file asm2_spark_job.py được bỏ cùng folder với
  ##  asm2.py trong dags của $AIRFLOW_HOME
  spark_process = SparkSubmitOperator(
    task_id='spark_process', 
    conn_id='spark_local3',
    application='dags/asm2_spark_job.py',
    packages='org.mongodb.spark:mongo-spark-connector_2.12:3.0.1',
    env_vars={'PYSPARK_DRIVER_PYTHON':'python'})

  ## import_output_mongo
  import_output_mongo = BashOperator(
    task_id='import_output_mongo',
    bash_command="awk 'FNR==1 && NR!=1{next;}{print}' /tmp/asm2_spark_output/*.csv > /tmp/asm2_spark_output.csv && " + _mongoimport_command('SparkOutput'))

  ## end task
  end = EmptyOperator(task_id='end',
                      trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS)

  ## depencencies
  start >> branching >> [clear_file, end]
  clear_file >> [download_anwser_file, download_question_file]
  download_anwser_file >> import_answers_mongo >> spark_process
  download_question_file >> import_questions_mongo >> spark_process
  spark_process >> import_output_mongo >> end