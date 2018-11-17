def func(environ, start_response):
    body = str(environ['QUERY_STRING']).replace('&', '\n').encode()
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return iter([body])
