curl 'http://localhost:8888/login?next=%2Flab%3F' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894' \
  -H 'Origin: http://localhost:8888' \
  -H 'Referer: http://localhost:8888/login?next=%2Flab%3F' \
  -H 'Sec-Fetch-Dest: document' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-User: ?1' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55' \
  -H 'sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '_xsrf=2%7Ca42007a9%7Cb8044f07cb0b878eb1e0705a96fbd7f3%7C1674832894&password=zxc' \
  --compressed

POST /login?next=%2Flab%3F HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,ko;q=0.8
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 79
Content-Type: application/x-www-form-urlencoded
Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894
Host: localhost:8888
Origin: http://localhost:8888
Referer: http://localhost:8888/login?next=%2Flab%3F
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55
sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"


HTTP/1.1 302 Found
Server: TornadoServer/6.2
Content-Type: text/html; charset=UTF-8
Date: Fri, 27 Jan 2023 15:21:51 GMT
X-Content-Type-Options: nosniff
Content-Security-Policy: frame-ancestors 'self'; report-uri /api/security/csp-report
Access-Control-Allow-Origin: *
Location: /lab?
Content-Length: 0
Set-Cookie: username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"; expires=Sun, 26 Feb 2023 15:21:51 GMT; HttpOnly; Path=/

# ----------------------------------------------------

curl 'http://localhost:8888/api/kernelspecs?1674832912530' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894; username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"' \
  -H 'Referer: http://localhost:8888/lab?' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55' \
  -H 'X-XSRFToken: 2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894' \
  -H 'sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --compressed

GET /api/kernelspecs?1674832912530 HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,ko;q=0.8
Connection: keep-alive
Content-Type: application/json
Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894; username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"
Host: localhost:8888
Referer: http://localhost:8888/lab?
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55
X-XSRFToken: 2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894
sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"

HTTP/1.1 200 OK
Server: TornadoServer/6.2
Content-Type: application/json
Date: Fri, 27 Jan 2023 15:21:53 GMT
X-Content-Type-Options: nosniff
Content-Security-Policy: frame-ancestors 'self'; report-uri /api/security/csp-report; default-src 'none'
Access-Control-Allow-Origin: *
Etag: "1e945dbf9f23e03d9eb2e85e80ee8cc3beacd834"
Content-Length: 1308

{"default": "python3", "kernelspecs": {"python3": {"name": "python3", "spec": {"argv": ["/opt/conda/bin/python", "-m", "ipykernel_launcher", "-f", "{connection_file}"], "env": {}, "display_name": "Python 3 (ipykernel)", "language": "python", "interrupt_mode": "signal", "metadata": {"debugger": true}}, "resources": {"logo-svg": "/kernelspecs/python3/logo-svg.svg", "logo-64x64": "/kernelspecs/python3/logo-64x64.png", "logo-32x32": "/kernelspecs/python3/logo-32x32.png"}}, "ir": {"name": "ir", "spec": {"argv": ["R", "--slave", "-e", "IRkernel::main()", "--args", "{connection_file}"], "env": {}, "display_name": "R", "language": "R", "interrupt_mode": "signal", "metadata": {}}, "resources": {"kernel.js": "/kernelspecs/ir/kernel.js", "logo-svg": "/kernelspecs/ir/logo-svg.svg", "logo-64x64": "/kernelspecs/ir/logo-64x64.png"}}, "julia-1.8": {"name": "julia-1.8", "spec": {"argv": ["/opt/julia-1.8.3/bin/julia", "-i", "--color=yes", "--project=@.", "/opt/julia/packages/IJulia/6TIq1/src/kernel.jl", "{connection_file}"], "env": {}, "display_name": "Julia 1.8.3", "language": "julia", "interrupt_mode": "signal", "metadata": {}}, "resources": {"logo-svg": "/kernelspecs/julia-1.8/logo-svg.svg", "logo-64x64": "/kernelspecs/julia-1.8/logo-64x64.png", "logo-32x32": "/kernelspecs/julia-1.8/logo-32x32.png"}}}}


# ------------------

curl 'http://localhost:8888/api/kernels?1674832912590' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894; username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"' \
  -H 'Referer: http://localhost:8888/lab?' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55' \
  -H 'X-XSRFToken: 2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894' \
  -H 'sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --compressed

GET /api/kernels?1674832912590 HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,ko;q=0.8
Connection: keep-alive
Content-Type: application/json
Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894; username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"
Host: localhost:8888
Referer: http://localhost:8888/lab?
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55
X-XSRFToken: 2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894
sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"

HTTP/1.1 200 OK
Server: TornadoServer/6.2
Content-Type: application/json
Date: Fri, 27 Jan 2023 15:21:53 GMT
X-Content-Type-Options: nosniff
Content-Security-Policy: frame-ancestors 'self'; report-uri /api/security/csp-report; default-src 'none'
Access-Control-Allow-Origin: *
Etag: "44452e1ed50c0472f8bb54e50b35dcc8d900e329"
Content-Length: 320

[{"id": "60313c3d-224a-4f0b-9278-7e19aee2730d", "name": "python3", "last_activity": "2023-01-27T03:54:59.641540Z", "execution_state": "idle", "connections": 0}, {"id": "2de7f000-4f63-4d8b-ad20-4acd0c96edc5", "name": "python3", "last_activity": "2023-01-27T03:48:45.566533Z", "execution_state": "idle", "connections": 0}]


# ----------------

curl 'http://localhost:8888/api/sessions?1674832912592' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894; username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"' \
  -H 'Referer: http://localhost:8888/lab?' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55' \
  -H 'X-XSRFToken: 2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894' \
  -H 'sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --compressed

GET /api/sessions?1674832912592 HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,ko;q=0.8
Connection: keep-alive
Content-Type: application/json
Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894; username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"
Host: localhost:8888
Referer: http://localhost:8888/lab?
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55
X-XSRFToken: 2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894
sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"

HTTP/1.1 200 OK
Server: TornadoServer/6.2
Content-Type: application/json
Date: Fri, 27 Jan 2023 15:21:53 GMT
X-Content-Type-Options: nosniff
Content-Security-Policy: frame-ancestors 'self'; report-uri /api/security/csp-report; default-src 'none'
Access-Control-Allow-Origin: *
Etag: "ff191fea613fc856a553e1a2a1497150a3dcda98"
Content-Length: 693

[{"id": "c5e99fdf-9081-47a3-9ba9-8ad15208cde6", "path": "Untitled.ipynb", "name": "Untitled.ipynb", "type": "notebook", "kernel": {"id": "60313c3d-224a-4f0b-9278-7e19aee2730d", "name": "python3", "last_activity": "2023-01-27T03:54:59.641540Z", "execution_state": "idle", "connections": 0}, "notebook": {"path": "Untitled.ipynb", "name": "Untitled.ipynb"}}, {"id": "7d0a7c03-49ba-4f19-a58e-ee602c3701ea", "path": "f1e163d1-463c-414b-b4d4-3e51fe427e5f", "name": "jovyan-f1e163d1-463c-414b-b4d4-3e51fe427e5f", "type": "file", "kernel": {"id": "2de7f000-4f63-4d8b-ad20-4acd0c96edc5", "name": "python3", "last_activity": "2023-01-27T03:48:45.566533Z", "execution_state": "idle", "connections": 0}}]


# ----------------

curl 'http://localhost:8888/api/kernelspecs?1674832912613' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894; username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"' \
  -H 'Referer: http://localhost:8888/lab?' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55' \
  -H 'X-XSRFToken: 2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894' \
  -H 'sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --compressed

GET /api/kernelspecs?1674832912613 HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,ko;q=0.8
Connection: keep-alive
Content-Type: application/json
Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894; username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"
Host: localhost:8888
Referer: http://localhost:8888/lab?
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55
X-XSRFToken: 2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894
sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"

HTTP/1.1 200 OK
Server: TornadoServer/6.2
Content-Type: application/json
Date: Fri, 27 Jan 2023 15:21:53 GMT
X-Content-Type-Options: nosniff
Content-Security-Policy: frame-ancestors 'self'; report-uri /api/security/csp-report; default-src 'none'
Access-Control-Allow-Origin: *
Etag: "1e945dbf9f23e03d9eb2e85e80ee8cc3beacd834"
Content-Length: 1308

{"default": "python3", "kernelspecs": {"python3": {"name": "python3", "spec": {"argv": ["/opt/conda/bin/python", "-m", "ipykernel_launcher", "-f", "{connection_file}"], "env": {}, "display_name": "Python 3 (ipykernel)", "language": "python", "interrupt_mode": "signal", "metadata": {"debugger": true}}, "resources": {"logo-svg": "/kernelspecs/python3/logo-svg.svg", "logo-64x64": "/kernelspecs/python3/logo-64x64.png", "logo-32x32": "/kernelspecs/python3/logo-32x32.png"}}, "ir": {"name": "ir", "spec": {"argv": ["R", "--slave", "-e", "IRkernel::main()", "--args", "{connection_file}"], "env": {}, "display_name": "R", "language": "R", "interrupt_mode": "signal", "metadata": {}}, "resources": {"kernel.js": "/kernelspecs/ir/kernel.js", "logo-svg": "/kernelspecs/ir/logo-svg.svg", "logo-64x64": "/kernelspecs/ir/logo-64x64.png"}}, "julia-1.8": {"name": "julia-1.8", "spec": {"argv": ["/opt/julia-1.8.3/bin/julia", "-i", "--color=yes", "--project=@.", "/opt/julia/packages/IJulia/6TIq1/src/kernel.jl", "{connection_file}"], "env": {}, "display_name": "Julia 1.8.3", "language": "julia", "interrupt_mode": "signal", "metadata": {}}, "resources": {"logo-svg": "/kernelspecs/julia-1.8/logo-svg.svg", "logo-64x64": "/kernelspecs/julia-1.8/logo-64x64.png", "logo-32x32": "/kernelspecs/julia-1.8/logo-32x32.png"}}}}

# -------------

curl 'http://localhost:8888/lab/api/build?1674832913889' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894; username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"' \
  -H 'Referer: http://localhost:8888/lab?' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55' \
  -H 'X-XSRFToken: 2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894' \
  -H 'sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --compressed

GET /lab/api/build?1674832913889 HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,ko;q=0.8
Connection: keep-alive
Content-Type: application/json
Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894; username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"
Host: localhost:8888
Referer: http://localhost:8888/lab?
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55
X-XSRFToken: 2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894
sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"

HTTP/1.1 200 OK
Server: TornadoServer/6.2
Content-Type: application/json
Date: Fri, 27 Jan 2023 15:21:55 GMT
X-Content-Type-Options: nosniff
Content-Security-Policy: frame-ancestors 'self'; report-uri /api/security/csp-report; default-src 'none'
Access-Control-Allow-Origin: *
Etag: "a04f921aac2a555d8859c91deeff337ca6b6dedc"
Content-Length: 35

{"status": "stable", "message": ""}

# ------------------

curl 'ws://localhost:8888/api/kernels/2de7f000-4f63-4d8b-ad20-4acd0c96edc5/channels?session_id=32295e48-8f94-4661-8126-e80b37e37302' \
  -H 'Pragma: no-cache' \
  -H 'Origin: http://localhost:8888' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Sec-WebSocket-Key: 6z5B5HM74/vSVVJTpxDUWA==' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55' \
  -H 'Upgrade: websocket' \
  -H 'Cache-Control: no-cache' \
  -H 'Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894; username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"' \
  -H 'Connection: Upgrade' \
  -H 'Sec-WebSocket-Version: 13' \
  -H 'Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits' \
  --compressed

GET ws://localhost:8888/api/kernels/2de7f000-4f63-4d8b-ad20-4acd0c96edc5/channels?session_id=32295e48-8f94-4661-8126-e80b37e37302 HTTP/1.1
Host: localhost:8888
Connection: Upgrade
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55
Upgrade: websocket
Origin: http://localhost:8888
Sec-WebSocket-Version: 13
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,ko;q=0.8
Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894; username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"
Sec-WebSocket-Key: 6z5B5HM74/vSVVJTpxDUWA==
Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits

HTTP/1.1 101 Switching Protocols
Server: TornadoServer/6.2
Date: Fri, 27 Jan 2023 15:21:57 GMT
Access-Control-Allow-Origin: *
Upgrade: websocket
Connection: Upgrade
Sec-Websocket-Accept: Uj7UAHnxWc5Wh31X8aaQHkMdNHs=

{"buffers":[],"channel":"shell","content":{},"header":{"date":"2023-01-27T15:21:55.881Z","msg_id":"7110d52f-1e13-40e8-a265-0f6d16b20ad8","msg_type":"kernel_info_request","session":"32295e48-8f94-4661-8126-e80b37e37302","username":"","version":"5.2"},"metadata":{},"parent_header":{}}
{"header": {"msg_id": "85783d10-d0f7ea206007881c20510e66_65912_1206", "msg_type": "status", "username": "username", "session": "85783d10-d0f7ea206007881c20510e66", "date": "2023-01-27T15:21:57.063389Z", "version": "5.3"}, "msg_id": "85783d10-d0f7ea206007881c20510e66_65912_1206", "msg_type": "status", "parent_header": {"msg_id": "32295e48-8f94-4661-8126-e80b37e37302_7_1", "msg_type": "kernel_info_request", "username": "username", "session": "32295e48-8f94-4661-8126-e80b37e37302", "date": "2023-01-27T15:21:57.056554Z", "version": "5.3"}, "metadata": {}, "content": {"execution_state": "busy"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "85783d10-d0f7ea206007881c20510e66_65912_1208", "msg_type": "status", "username": "username", "session": "85783d10-d0f7ea206007881c20510e66", "date": "2023-01-27T15:21:57.067460Z", "version": "5.3"}, "msg_id": "85783d10-d0f7ea206007881c20510e66_65912_1208", "msg_type": "status", "parent_header": {"msg_id": "32295e48-8f94-4661-8126-e80b37e37302_7_0", "msg_type": "kernel_info_request", "username": "username", "session": "32295e48-8f94-4661-8126-e80b37e37302", "date": "2023-01-27T15:21:57.056024Z", "version": "5.3"}, "metadata": {}, "content": {"execution_state": "idle"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "85783d10-d0f7ea206007881c20510e66_65912_1209", "msg_type": "status", "username": "username", "session": "85783d10-d0f7ea206007881c20510e66", "date": "2023-01-27T15:21:57.069828Z", "version": "5.3"}, "msg_id": "85783d10-d0f7ea206007881c20510e66_65912_1209", "msg_type": "status", "parent_header": {"msg_id": "32295e48-8f94-4661-8126-e80b37e37302_7_1", "msg_type": "kernel_info_request", "username": "username", "session": "32295e48-8f94-4661-8126-e80b37e37302", "date": "2023-01-27T15:21:57.056554Z", "version": "5.3"}, "metadata": {}, "content": {"execution_state": "idle"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "85783d10-d0f7ea206007881c20510e66_65912_1211", "msg_type": "kernel_info_reply", "username": "username", "session": "85783d10-d0f7ea206007881c20510e66", "date": "2023-01-27T15:21:57.175826Z", "version": "5.3"}, "msg_id": "85783d10-d0f7ea206007881c20510e66_65912_1211", "msg_type": "kernel_info_reply", "parent_header": {"date": "2023-01-27T15:21:55.881000Z", "msg_id": "7110d52f-1e13-40e8-a265-0f6d16b20ad8", "msg_type": "kernel_info_request", "session": "32295e48-8f94-4661-8126-e80b37e37302", "username": "", "version": "5.2"}, "metadata": {}, "content": {"status": "ok", "protocol_version": "5.3", "implementation": "ipython", "implementation_version": "8.8.0", "language_info": {"name": "python", "version": "3.10.8", "mimetype": "text/x-python", "codemirror_mode": {"name": "ipython", "version": 3}, "pygments_lexer": "ipython3", "nbconvert_exporter": "python", "file_extension": ".py"}, "banner": "Python 3.10.8 | packaged by conda-forge | (main, Nov 22 2022, 08:26:04) [GCC 10.4.0]\nType 'copyright', 'credits' or 'license' for more information\nIPython 8.8.0 -- An enhanced Interactive Python. Type '?' for help.\n", "help_links": [{"text": "Python Reference", "url": "https://docs.python.org/3.10"}, {"text": "IPython Reference", "url": "https://ipython.org/documentation.html"}, {"text": "NumPy Reference", "url": "https://docs.scipy.org/doc/numpy/reference/"}, {"text": "SciPy Reference", "url": "https://docs.scipy.org/doc/scipy/reference/"}, {"text": "Matplotlib Reference", "url": "https://matplotlib.org/contents.html"}, {"text": "SymPy Reference", "url": "http://docs.sympy.org/latest/index.html"}, {"text": "pandas Reference", "url": "https://pandas.pydata.org/pandas-docs/stable/"}]}, "buffers": [], "channel": "shell"}


# --------------------------

curl 'ws://localhost:8888/terminals/websocket/1' \
  -H 'Pragma: no-cache' \
  -H 'Origin: http://localhost:8888' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Sec-WebSocket-Key: N7JGpGM4r5tvb29fdTkqcA==' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55' \
  -H 'Upgrade: websocket' \
  -H 'Cache-Control: no-cache' \
  -H 'Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894; username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"' \
  -H 'Connection: Upgrade' \
  -H 'Sec-WebSocket-Version: 13' \
  -H 'Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits' \
  --compressed

GET ws://localhost:8888/terminals/websocket/1 HTTP/1.1
Host: localhost:8888
Connection: Upgrade
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55
Upgrade: websocket
Origin: http://localhost:8888
Sec-WebSocket-Version: 13
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,ko;q=0.8
Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894; username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"
Sec-WebSocket-Key: N7JGpGM4r5tvb29fdTkqcA==
Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits

HTTP/1.1 101 Switching Protocols
Server: TornadoServer/6.2
Date: Fri, 27 Jan 2023 15:21:57 GMT
X-Content-Type-Options: nosniff
Content-Security-Policy: frame-ancestors 'self'; report-uri /api/security/csp-report
Access-Control-Allow-Origin: *
Upgrade: websocket
Connection: Upgrade
Sec-Websocket-Accept: FwswIkFHZNODLIhZH0icqJOoIxQ=

["setup", {}]
["set_size",24,80,-1,-1]

# ------------

curl 'ws://localhost:8888/api/kernels/60313c3d-224a-4f0b-9278-7e19aee2730d/channels?session_id=7267f082-ab1a-4fdc-adb7-4574ace41c9b' \
  -H 'Pragma: no-cache' \
  -H 'Origin: http://localhost:8888' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Sec-WebSocket-Key: SPt8wC0ojBYEFl0b8aI8SQ==' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55' \
  -H 'Upgrade: websocket' \
  -H 'Cache-Control: no-cache' \
  -H 'Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894; username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"' \
  -H 'Connection: Upgrade' \
  -H 'Sec-WebSocket-Version: 13' \
  -H 'Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits' \
  --compressed

GET ws://localhost:8888/api/kernels/60313c3d-224a-4f0b-9278-7e19aee2730d/channels?session_id=7267f082-ab1a-4fdc-adb7-4574ace41c9b HTTP/1.1
Host: localhost:8888
Connection: Upgrade
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55
Upgrade: websocket
Origin: http://localhost:8888
Sec-WebSocket-Version: 13
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,ko;q=0.8
Cookie: security_authentication=Fe26.2**48887cc622990c9eb2dde5697b16ddf4e005e5ef191cc28a8e4633a1a1baf7c1*AXlcYA8qOc0jklAJyS0tjQ*4O0rmL8R_t7aLkynANfvT7vcbx5v49-xuVX2Mgl08ZILEALxITxORuV8-BM2SLP_488zW2Qcy694f0CsG_CD1HTAxdPyV5gc8KFCjvb92CpDBDxiIy5tJa6lHDR0MwgSI520vMoggZZxt18RfWOPgfKlIXlQ305BShn7FS7V9bIBU6gjBaCJj2kRwH2AtlaSp3938KlYSZeR9ukBxDayNCE7NFhQE2X_afYPxJlUGdWsa8WnJXkbe1-Qp8T7DcEY**bdcd620b7cca61ee4a82c2bd3104bcc556f7e220d53be8a2beaa4ad6f9f6a9e9*FwaQtYvZb7wA2QG7X6wky-BE0VhNalxSl05VffXlgdc; _xsrf=2|a42007a9|b8044f07cb0b878eb1e0705a96fbd7f3|1674832894; username-localhost-8888="2|1:0|10:1674832911|23:username-localhost-8888|192:eyJ1c2VybmFtZSI6ICJkMTcwMGI3ZTZiMDA0M2E0YWMzMWM4ZGU1NDE3N2NiMiIsICJuYW1lIjogIkFub255bW91cyBBaXRuZSIsICJkaXNwbGF5X25hbWUiOiAiQW5vbnltb3VzIEFpdG5lIiwgImluaXRpYWxzIjogIkFBIiwgImNvbG9yIjogbnVsbH0=|1c08fbc08bf77184f5670604363f1203c150f958142fcea578b7d742a9af1c37"
Sec-WebSocket-Key: SPt8wC0ojBYEFl0b8aI8SQ==
Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits

HTTP/1.1 101 Switching Protocols
Server: TornadoServer/6.2
Date: Fri, 27 Jan 2023 15:21:57 GMT
Access-Control-Allow-Origin: *
Upgrade: websocket
Connection: Upgrade
Sec-Websocket-Accept: yJHeULsotsFAm4WbvM9cExXTLUE=

{"buffers":[],"channel":"shell","content":{},"header":{"date":"2023-01-27T15:21:56.575Z","msg_id":"c64918cd-a143-473a-929c-1d08c76caf3b","msg_type":"kernel_info_request","session":"7267f082-ab1a-4fdc-adb7-4574ace41c9b","username":"","version":"5.2"},"metadata":{},"parent_header":{}}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_991", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.832644Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_991", "msg_type": "status", "parent_header": {"msg_id": "7267f082-ab1a-4fdc-adb7-4574ace41c9b_7_1", "msg_type": "kernel_info_request", "username": "username", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "date": "2023-01-27T15:21:57.830906Z", "version": "5.3"}, "metadata": {}, "content": {"execution_state": "busy"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_993", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.833461Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_993", "msg_type": "status", "parent_header": {"msg_id": "7267f082-ab1a-4fdc-adb7-4574ace41c9b_7_0", "msg_type": "kernel_info_request", "username": "username", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "date": "2023-01-27T15:21:57.830762Z", "version": "5.3"}, "metadata": {}, "content": {"execution_state": "idle"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_994", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.834084Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_994", "msg_type": "status", "parent_header": {"msg_id": "7267f082-ab1a-4fdc-adb7-4574ace41c9b_7_1", "msg_type": "kernel_info_request", "username": "username", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "date": "2023-01-27T15:21:57.830906Z", "version": "5.3"}, "metadata": {}, "content": {"execution_state": "idle"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_995", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.840226Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_995", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:21:56.575000Z", "msg_id": "c64918cd-a143-473a-929c-1d08c76caf3b", "msg_type": "kernel_info_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "busy"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_997", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.841407Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_997", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:21:56.575000Z", "msg_id": "c64918cd-a143-473a-929c-1d08c76caf3b", "msg_type": "kernel_info_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "idle"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_996", "msg_type": "kernel_info_reply", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.840446Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_996", "msg_type": "kernel_info_reply", "parent_header": {"date": "2023-01-27T15:21:56.575000Z", "msg_id": "c64918cd-a143-473a-929c-1d08c76caf3b", "msg_type": "kernel_info_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"status": "ok", "protocol_version": "5.3", "implementation": "ipython", "implementation_version": "8.8.0", "language_info": {"name": "python", "version": "3.10.8", "mimetype": "text/x-python", "codemirror_mode": {"name": "ipython", "version": 3}, "pygments_lexer": "ipython3", "nbconvert_exporter": "python", "file_extension": ".py"}, "banner": "Python 3.10.8 | packaged by conda-forge | (main, Nov 22 2022, 08:26:04) [GCC 10.4.0]\nType 'copyright', 'credits' or 'license' for more information\nIPython 8.8.0 -- An enhanced Interactive Python. Type '?' for help.\n", "help_links": [{"text": "Python Reference", "url": "https://docs.python.org/3.10"}, {"text": "IPython Reference", "url": "https://ipython.org/documentation.html"}, {"text": "NumPy Reference", "url": "https://docs.scipy.org/doc/numpy/reference/"}, {"text": "SciPy Reference", "url": "https://docs.scipy.org/doc/scipy/reference/"}, {"text": "Matplotlib Reference", "url": "https://matplotlib.org/contents.html"}, {"text": "SymPy Reference", "url": "http://docs.sympy.org/latest/index.html"}, {"text": "pandas Reference", "url": "https://pandas.pydata.org/pandas-docs/stable/"}]}, "buffers": [], "channel": "shell"}
{"buffers":[],"channel":"control","content":{"type":"request","seq":0,"command":"debugInfo"},"header":{"date":"2023-01-27T15:21:56.234Z","msg_id":"999aa3f4-2cda-4f58-b818-e5b815a432f6","msg_type":"debug_request","session":"7267f082-ab1a-4fdc-adb7-4574ace41c9b","username":"","version":"5.2"},"metadata":{},"parent_header":{}}
{"buffers":[],"channel":"shell","content":{"comm_id":"0d6c987b-52e5-4f6b-9eed-58e9d278da70","target_name":"jupyter.widget.control","data":{}},"header":{"date":"2023-01-27T15:21:56.577Z","msg_id":"b7893367-bd4e-47d1-8588-090c9b1065e7","msg_type":"comm_open","session":"7267f082-ab1a-4fdc-adb7-4574ace41c9b","username":"","version":"5.2"},"metadata":{"version":"1.0.0"},"parent_header":{}}
{"buffers":[],"channel":"shell","content":{"comm_id":"0d6c987b-52e5-4f6b-9eed-58e9d278da70","data":{"method":"request_states"}},"header":{"date":"2023-01-27T15:21:56.578Z","msg_id":"7d80b65d-8553-4895-b555-56e8498b9644","msg_type":"comm_msg","session":"7267f082-ab1a-4fdc-adb7-4574ace41c9b","username":"","version":"5.2"},"metadata":{},"parent_header":{}}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_998", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.862330Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_998", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:21:56.577000Z", "msg_id": "b7893367-bd4e-47d1-8588-090c9b1065e7", "msg_type": "comm_open", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "busy"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_999", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.863320Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_999", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:21:56.234000Z", "msg_id": "999aa3f4-2cda-4f58-b818-e5b815a432f6", "msg_type": "debug_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "busy"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1001", "msg_type": "stream", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.863698Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1001", "msg_type": "stream", "parent_header": {"date": "2023-01-27T15:21:56.577000Z", "msg_id": "b7893367-bd4e-47d1-8588-090c9b1065e7", "msg_type": "comm_open", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"name": "stderr", "text": "No such comm target registered: jupyter.widget.control\n"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1000", "msg_type": "debug_reply", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.863443Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1000", "msg_type": "debug_reply", "parent_header": {"date": "2023-01-27T15:21:56.234000Z", "msg_id": "999aa3f4-2cda-4f58-b818-e5b815a432f6", "msg_type": "debug_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"type": "response", "request_seq": 0, "success": true, "command": "debugInfo", "body": {"isStarted": false, "hashMethod": "Murmur2", "hashSeed": 3339675911, "tmpFilePrefix": "/tmp/ipykernel_79776/", "tmpFileSuffix": ".py", "breakpoints": [], "stoppedThreads": [], "richRendering": true, "exceptionPaths": ["Python Exceptions"]}}, "buffers": [], "channel": "control"}
{"buffers":[],"channel":"control","content":{"type":"request","seq":0,"command":"debugInfo","arguments":{}},"header":{"date":"2023-01-27T15:21:56.617Z","msg_id":"dd196618-709f-4e7a-94eb-d9e2e687f7b0","msg_type":"debug_request","session":"7267f082-ab1a-4fdc-adb7-4574ace41c9b","username":"","version":"5.2"},"metadata":{},"parent_header":{}}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1002", "msg_type": "comm_close", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.863965Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1002", "msg_type": "comm_close", "parent_header": {"date": "2023-01-27T15:21:56.577000Z", "msg_id": "b7893367-bd4e-47d1-8588-090c9b1065e7", "msg_type": "comm_open", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"data": {}, "comm_id": "0d6c987b-52e5-4f6b-9eed-58e9d278da70"}, "buffers": [], "channel": "iopub"}
{"buffers":[],"channel":"shell","content":{"target_name":"jupyter.widget"},"header":{"date":"2023-01-27T15:21:56.619Z","msg_id":"d8e23f8e-8b5d-420c-9697-3fca17c63f29","msg_type":"comm_info_request","session":"7267f082-ab1a-4fdc-adb7-4574ace41c9b","username":"","version":"5.2"},"metadata":{},"parent_header":{}}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1003", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.864866Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1003", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:21:56.234000Z", "msg_id": "999aa3f4-2cda-4f58-b818-e5b815a432f6", "msg_type": "debug_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "idle"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1004", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.865119Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1004", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:21:56.577000Z", "msg_id": "b7893367-bd4e-47d1-8588-090c9b1065e7", "msg_type": "comm_open", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "idle"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1005", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.866008Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1005", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:21:56.578000Z", "msg_id": "7d80b65d-8553-4895-b555-56e8498b9644", "msg_type": "comm_msg", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "busy"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1006", "msg_type": "stream", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.866673Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1006", "msg_type": "stream", "parent_header": {"date": "2023-01-27T15:21:56.578000Z", "msg_id": "7d80b65d-8553-4895-b555-56e8498b9644", "msg_type": "comm_msg", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"name": "stderr", "text": "No such comm: 0d6c987b-52e5-4f6b-9eed-58e9d278da70\n"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1007", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.868231Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1007", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:21:56.578000Z", "msg_id": "7d80b65d-8553-4895-b555-56e8498b9644", "msg_type": "comm_msg", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "idle"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1008", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.887061Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1008", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:21:56.617000Z", "msg_id": "dd196618-709f-4e7a-94eb-d9e2e687f7b0", "msg_type": "debug_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "busy"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1010", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.887764Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1010", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:21:56.619000Z", "msg_id": "d8e23f8e-8b5d-420c-9697-3fca17c63f29", "msg_type": "comm_info_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "busy"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1012", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.888787Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1012", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:21:56.617000Z", "msg_id": "dd196618-709f-4e7a-94eb-d9e2e687f7b0", "msg_type": "debug_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "idle"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1009", "msg_type": "debug_reply", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.887274Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1009", "msg_type": "debug_reply", "parent_header": {"date": "2023-01-27T15:21:56.617000Z", "msg_id": "dd196618-709f-4e7a-94eb-d9e2e687f7b0", "msg_type": "debug_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"type": "response", "request_seq": 0, "success": true, "command": "debugInfo", "body": {"isStarted": false, "hashMethod": "Murmur2", "hashSeed": 3339675911, "tmpFilePrefix": "/tmp/ipykernel_79776/", "tmpFileSuffix": ".py", "breakpoints": [], "stoppedThreads": [], "richRendering": true, "exceptionPaths": ["Python Exceptions"]}}, "buffers": [], "channel": "control"}
{"buffers":[],"channel":"control","content":{"type":"request","seq":0,"command":"debugInfo"},"header":{"date":"2023-01-27T15:21:56.642Z","msg_id":"2c41545d-1f7f-49bd-a742-8f176b8e2495","msg_type":"debug_request","session":"7267f082-ab1a-4fdc-adb7-4574ace41c9b","username":"","version":"5.2"},"metadata":{},"parent_header":{}}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1011", "msg_type": "comm_info_reply", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.888060Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1011", "msg_type": "comm_info_reply", "parent_header": {"date": "2023-01-27T15:21:56.619000Z", "msg_id": "d8e23f8e-8b5d-420c-9697-3fca17c63f29", "msg_type": "comm_info_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"comms": {}, "status": "ok"}, "buffers": [], "channel": "shell"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1013", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.889227Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1013", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:21:56.619000Z", "msg_id": "d8e23f8e-8b5d-420c-9697-3fca17c63f29", "msg_type": "comm_info_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "idle"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1014", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.906637Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1014", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:21:56.642000Z", "msg_id": "2c41545d-1f7f-49bd-a742-8f176b8e2495", "msg_type": "debug_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "busy"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1015", "msg_type": "debug_reply", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.906753Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1015", "msg_type": "debug_reply", "parent_header": {"date": "2023-01-27T15:21:56.642000Z", "msg_id": "2c41545d-1f7f-49bd-a742-8f176b8e2495", "msg_type": "debug_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"type": "response", "request_seq": 0, "success": true, "command": "debugInfo", "body": {"isStarted": false, "hashMethod": "Murmur2", "hashSeed": 3339675911, "tmpFilePrefix": "/tmp/ipykernel_79776/", "tmpFileSuffix": ".py", "breakpoints": [], "stoppedThreads": [], "richRendering": true, "exceptionPaths": ["Python Exceptions"]}}, "buffers": [], "channel": "control"}
{"buffers":[],"channel":"control","content":{"type":"request","seq":1,"command":"debugInfo","arguments":{}},"header":{"date":"2023-01-27T15:21:56.662Z","msg_id":"03f5baa6-3d06-400d-b0b5-707d4e7c192b","msg_type":"debug_request","session":"7267f082-ab1a-4fdc-adb7-4574ace41c9b","username":"","version":"5.2"},"metadata":{},"parent_header":{}}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1016", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.907335Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1016", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:21:56.642000Z", "msg_id": "2c41545d-1f7f-49bd-a742-8f176b8e2495", "msg_type": "debug_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "idle"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1017", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.932673Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1017", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:21:56.662000Z", "msg_id": "03f5baa6-3d06-400d-b0b5-707d4e7c192b", "msg_type": "debug_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "busy"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1019", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.936148Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1019", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:21:56.662000Z", "msg_id": "03f5baa6-3d06-400d-b0b5-707d4e7c192b", "msg_type": "debug_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "idle"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1018", "msg_type": "debug_reply", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:21:57.933197Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1018", "msg_type": "debug_reply", "parent_header": {"date": "2023-01-27T15:21:56.662000Z", "msg_id": "03f5baa6-3d06-400d-b0b5-707d4e7c192b", "msg_type": "debug_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"type": "response", "request_seq": 1, "success": true, "command": "debugInfo", "body": {"isStarted": false, "hashMethod": "Murmur2", "hashSeed": 3339675911, "tmpFilePrefix": "/tmp/ipykernel_79776/", "tmpFileSuffix": ".py", "breakpoints": [], "stoppedThreads": [], "richRendering": true, "exceptionPaths": ["Python Exceptions"]}}, "buffers": [], "channel": "control"}
{"buffers":[],"channel":"shell","content":{"silent":false,"store_history":true,"user_expressions":{},"allow_stdin":true,"stop_on_error":true,"code":"print"},"header":{"date":"2023-01-27T15:22:01.230Z","msg_id":"52e155e5-4f5f-47ff-b6d9-a5db497f4002","msg_type":"execute_request","session":"7267f082-ab1a-4fdc-adb7-4574ace41c9b","username":"","version":"5.2"},"metadata":{"deletedCells":[],"recordTiming":false,"cellId":"5217ee5a-12f4-4a5a-b170-c2c6f4f06c67"},"parent_header":{}}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1020", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:22:02.498635Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1020", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:22:01.230000Z", "msg_id": "52e155e5-4f5f-47ff-b6d9-a5db497f4002", "msg_type": "execute_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "busy"}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1021", "msg_type": "execute_input", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:22:02.499750Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1021", "msg_type": "execute_input", "parent_header": {"date": "2023-01-27T15:22:01.230000Z", "msg_id": "52e155e5-4f5f-47ff-b6d9-a5db497f4002", "msg_type": "execute_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"code": "print", "execution_count": 4}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1022", "msg_type": "execute_result", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:22:02.503500Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1022", "msg_type": "execute_result", "parent_header": {"date": "2023-01-27T15:22:01.230000Z", "msg_id": "52e155e5-4f5f-47ff-b6d9-a5db497f4002", "msg_type": "execute_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"data": {"text/plain": "<function print>"}, "metadata": {}, "execution_count": 4}, "buffers": [], "channel": "iopub"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1023", "msg_type": "execute_reply", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:22:02.516384Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1023", "msg_type": "execute_reply", "parent_header": {"date": "2023-01-27T15:22:01.230000Z", "msg_id": "52e155e5-4f5f-47ff-b6d9-a5db497f4002", "msg_type": "execute_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {"started": "2023-01-27T15:22:02.499668Z", "dependencies_met": true, "engine": "a4ac1364-2d19-4d73-b9bf-c22ff9d2ce1d", "status": "ok"}, "content": {"status": "ok", "execution_count": 4, "user_expressions": {}, "payload": []}, "buffers": [], "channel": "shell"}
{"header": {"msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1024", "msg_type": "status", "username": "username", "session": "b4f292a8-464a511085903bb4126da0df", "date": "2023-01-27T15:22:02.518378Z", "version": "5.3"}, "msg_id": "b4f292a8-464a511085903bb4126da0df_79776_1024", "msg_type": "status", "parent_header": {"date": "2023-01-27T15:22:01.230000Z", "msg_id": "52e155e5-4f5f-47ff-b6d9-a5db497f4002", "msg_type": "execute_request", "session": "7267f082-ab1a-4fdc-adb7-4574ace41c9b", "username": "", "version": "5.2"}, "metadata": {}, "content": {"execution_state": "idle"}, "buffers": [], "channel": "iopub"}




# --------------------

