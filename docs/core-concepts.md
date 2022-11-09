# Core Concepts in Airflow

1. DAG - Directed Acyclic Graph. One directional flowchart with nodes(tasks) and have directed edges(dependencies).
2. Operator - A task to operate what you want to do. (e.g. Connecting to DB and running a SQL query)
  - Action Operator : Executes something (PythonOperator executes Python code, BashOperator executes Bash command)
  - Transfer Operator : Allows you to transfer data from point A to point B (e.g. Tranferring data from MySQL to Redshift)
  - Sensor Operator : They are used to wait for something to happen befoe moving to next task (e.g. If you are waiting for files you will use FileSensor)
3. Task - An operator is a task and when you run it, you get a task instance
