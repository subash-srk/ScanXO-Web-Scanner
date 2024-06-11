import requests
from flask import Flask, render_template, request
import socket


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/details', methods=['POST'])
def details():
    if request.method == 'POST':
        url = request.form['url']
        # print(url)

        if url == "":
            return render_template("index.html")

        req_url = url
        if 'https://' in req_url:
            pass
        else:
            req_url = 'https://'+req_url
            
        response = requests.get(url=req_url)
        headers = response.headers
        # print(headers)

        AVAIL_HEADERS = []
        NO_HEADERS = []

        if 'Referrer-Policy' in headers:
            AVAIL_HEADERS.append('Referrer-Policy')
        if 'Referrer-Policy' not in headers:
            NO_HEADERS.append('Referrer-Policy')

        if 'Content-Security-Policy' in headers:
            AVAIL_HEADERS.append("Content-Security-Policy")
        if 'Content-Security-Policy' not in headers:
            NO_HEADERS.append("Content-Security-Policy")

        if 'Strict-Transport-Security' in headers:
            AVAIL_HEADERS.append("Strict-Transport-Security")
        if 'Strict-Transport-Security' not in headers:
            NO_HEADERS.append("Strict-Transport-Security")

        if 'X-Frame-Options' in headers:
            AVAIL_HEADERS.append("X-Frame-Options")
        if 'X-Frame-Options' not in headers:
            NO_HEADERS.append("X-Frame-Options")

        if 'X-Content-Type-Options' in headers:
            AVAIL_HEADERS.append("X-Content-Type-Options")
        if 'X-Content-Type-Options' not in headers:
            NO_HEADERS.append("X-Content-Type-Options")

        if 'Permissions-Policy' in headers:
            AVAIL_HEADERS.append("Permissions-Policy")
        if 'Permissions-Policy' not in headers:
            NO_HEADERS.append("Permissions-Policy")

        # print(len(AVAIL_HEADERS))
        # print(NO_HEADERS)

        def get_ip_6(host, port=0):

            if 'https://' in host:
                host = host.split('https://')[1]
                if '/' in host:
                    host = host.split('/')[0]
            else:
                pass

            alladdr = socket.getaddrinfo(host, port)
            ip6 = filter(
                lambda x: x[0] == socket.AF_INET6,
                alladdr
            )
            return list(ip6)[0][4][0]

        ip = get_ip_6(req_url)

        return render_template("details.html", URL=req_url, NO_HEADERS=NO_HEADERS, AVAIL_HEADERS=AVAIL_HEADERS, IP=ip)






