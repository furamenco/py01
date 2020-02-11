"""
WSGI config for myapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

# import MySQLdb
#
# def application(environ, start_response):
#     # 接続する
#     conn = MySQLdb.connect(
#     user='user88',
#     passwd='tq5rrfBP438Tdoni',
#     host='localhost',
#     db='django_db')
#
#     cur = conn.cursor()
#     sql = "select * from app_item;"
#     cur.execute(sql)
#     rows = cur.fetchall()
#     val = ""
#     for row in rows:
#         val += "56"
#     # 接続を閉じる
#     #conn.close
#
#     return echo(b'wwooo\r\nwooooo', start_response)
#
#
# def echo(value, start_response):
#     status = '200 OK'
#     output = value
#
#     response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]
#     start_response(status, response_headers)
#     return [output]


#djangoproject
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')

application = get_wsgi_application()
