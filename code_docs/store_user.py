from airflow.providers.postgres.hooks.postgres import PostgresHook

...
def _store_user():
    hook = PostgresHook(postgres_conn_id='postgres')
    hook.copy_expert(
        sql="COPY users FROM stdin WITH DELIMITER as ','",
        filename='/tmp/processed_user.csv'
    )

...

    store_user = PythonOperator(
        task_id='store_user',
        python_callable=_store_user
    )
