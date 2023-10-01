extract_user = SimpleHttpOperator(
    task_id='extract_user',
    http_conn_id='user_api',
    endpoint='api/',
    method='GET',
    response_filter=lambda response: json.loads(response.text),
    log_response=True
)
