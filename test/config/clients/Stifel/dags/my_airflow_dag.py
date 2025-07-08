#---------------------------------------
# SETUP

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator

# Module for manipulating dates and times
from datetime import datetime, timedelta

# To change timezones, use Pendulum https://pendulum.eustace.io/

# Some convenience functions
from textwrap import dedent

#---------------------------------------

# DEFAULT DAG ARGUMENTS

with DAG(
        # the following string is the unique identifier for your DAG
        'my_airflow_dag',
        # These args will get passed on to each operator
        # You can override them on a per-task basis during operator initialization
        default_args=
    {
        'depends_on_past': False,
        'email': ['my-email@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2022, 6, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function,
        # 'on_success_callback': some_other_function,
        # 'on_retry_callback': another_function,
        # 'sla_miss_callback': yet_another_function,
        # 'trigger_rule': 'all_success'
    },
        description='A simple tutorial DAG',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2022, 5, 1),
        catchup=False,
        tags=['example'],
) as dag:

    #---------------------------------------

    # DEFINE OPERATERS
    # t1, t2 and t3 are examples of tasks created by instantiating operators
    # they all will use the default_args we defined above

    t1 = BashOperator(
        task_id='task_print_date',
        bash_command='date',
    )

    # We can add documentation for each single task.
    t1.doc_md = dedent("""\
    #### Task Documentation
    You can document your task using the attributes `doc_md` (markdown),
    `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
    rendered in the UI's Task Instance Details page.

    ![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)

    """)

    #----------------

    t2 = BashOperator(
        task_id='task_sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        # override the retries parameter with 3
        retries=3,
    )

    #----------------

    # EXAMPLE OF TEMPLATING WITH JINJA

    # The templated_command contains code logic in {% %} blocks,
    # references parameters like {{ ds }}   #[ds = today's "date stamp"]
    # and calls a function as in {{ macros.ds_add(ds, 7)}}

    templated_command = dedent("""
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
    {% endfor %}
    """)

    # To see examples of more templates, visit https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html#templates-ref

    t3 = BashOperator(
        task_id='task_templated',
        depends_on_past=False,
        bash_command=templated_command,
    )

    #----------------

    # SETTING UP DEPENDENCIES
    # We have tasks t1, t2 and t3 that do not depend on each other.
    # Here's an example of how you can define dependencies between them:

    # We use the bit shift operator to chain operations:

    t1 >> [t2, t3]
