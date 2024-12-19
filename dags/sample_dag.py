from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# This DAG is scheduled to run once a day at midnight.
# You can modify the schedule_interval or start_date as needed.
with DAG(
    dag_id='test_gitsync_dag',
    start_date=datetime(2021, 1, 1),  # Safe static start date
    schedule_interval='@daily',
    catchup=False,
    tags=['gitsync', 'test']
) as dag:

    # Simple Bash task that prints the current date
    print_date = BashOperator(
        task_id='print_date',
        bash_command='date'
    )

    # Add another small task to verify dependencies (optional)
    print_hello = BashOperator(
        task_id='print_hello',
        bash_command='echo "Hello from the synced DAG!"'
    )

    # Set the task order
    print_date >> print_hello
