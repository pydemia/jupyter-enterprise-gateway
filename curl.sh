
curl 'http://localhost:8888/login?next=%2F' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: _xsrf=2|b4ecab14|6dfc53412e6e3f0214b25c1aa9a361b2|1671529525' \
  -H 'Origin: http://localhost:8888' \
  -H 'Referer: http://localhost:8888/login' \
  -H 'Sec-Fetch-Dest: document' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-User: ?1' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61' \
  -H 'sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '_xsrf=2%7Cd8fb629d%7C01eb9ac84279f68b78a59593c5b4a83b%7C1671529525&password=zxc' \
  --compressed

HTTP/1.1 302 Found
Server: TornadoServer/6.2
Content-Type: text/html; charset=UTF-8
Date: Thu, 26 Jan 2023 08:54:11 GMT
X-Content-Type-Options: nosniff
Content-Security-Policy: frame-ancestors 'self'; report-uri /api/security/csp-report
Access-Control-Allow-Origin: *
Location: /
Content-Length: 0
Set-Cookie: username-localhost-8888=2|1:0|10:1674723251|23:username-localhost-8888|196:eyJ1c2VybmFtZSI6ICIwOTIyN2FhZjdjMzg0MDM0YWRiYjdlMjhlZGU2NmY4NCIsICJuYW1lIjogIkFub255bW91cyBJb2Nhc3RlIiwgImRpc3BsYXlfbmFtZSI6ICJBbm9ueW1vdXMgSW9jYXN0ZSIsICJpbml0aWFscyI6ICJBSSIsICJjb2xvciI6IG51bGx9|5fa4961c1dfe6cdda0c7826abfa4aa92002a031238a4ec6127afa6dd1c06e59d; expires=Sat, 25 Feb 2023 08:54:11 GMT; HttpOnly; Path=/



curl 'http://localhost:8888/api/kernelspecs?1674723253072' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: _xsrf=2|b4ecab14|6dfc53412e6e3f0214b25c1aa9a361b2|1671529525; username-localhost-8888=2|1:0|10:1674723251|23:username-localhost-8888|196:eyJ1c2VybmFtZSI6ICIwOTIyN2FhZjdjMzg0MDM0YWRiYjdlMjhlZGU2NmY4NCIsICJuYW1lIjogIkFub255bW91cyBJb2Nhc3RlIiwgImRpc3BsYXlfbmFtZSI6ICJBbm9ueW1vdXMgSW9jYXN0ZSIsICJpbml0aWFscyI6ICJBSSIsICJjb2xvciI6IG51bGx9|5fa4961c1dfe6cdda0c7826abfa4aa92002a031238a4ec6127afa6dd1c06e59d' \
  -H 'Referer: http://localhost:8888/lab?' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61' \
  -H 'X-XSRFToken: 2|b4ecab14|6dfc53412e6e3f0214b25c1aa9a361b2|1671529525' \
  -H 'sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --compressed

HTTP/1.1 200 OK
Server: TornadoServer/6.2
Content-Type: application/json
Date: Thu, 26 Jan 2023 08:54:13 GMT
X-Content-Type-Options: nosniff
Content-Security-Policy: frame-ancestors 'self'; report-uri /api/security/csp-report; default-src 'none'
Access-Control-Allow-Origin: *
Etag: "1e945dbf9f23e03d9eb2e85e80ee8cc3beacd834"
Content-Length: 1308

{"default": "python3", "kernelspecs": {"python3": {"name": "python3", "spec": {"argv": ["/opt/conda/bin/python", "-m", "ipykernel_launcher", "-f", "{connection_file}"], "env": {}, "display_name": "Python 3 (ipykernel)", "language": "python", "interrupt_mode": "signal", "metadata": {"debugger": true}}, "resources": {"logo-svg": "/kernelspecs/python3/logo-svg.svg", "logo-64x64": "/kernelspecs/python3/logo-64x64.png", "logo-32x32": "/kernelspecs/python3/logo-32x32.png"}}, "ir": {"name": "ir", "spec": {"argv": ["R", "--slave", "-e", "IRkernel::main()", "--args", "{connection_file}"], "env": {}, "display_name": "R", "language": "R", "interrupt_mode": "signal", "metadata": {}}, "resources": {"kernel.js": "/kernelspecs/ir/kernel.js", "logo-svg": "/kernelspecs/ir/logo-svg.svg", "logo-64x64": "/kernelspecs/ir/logo-64x64.png"}}, "julia-1.8": {"name": "julia-1.8", "spec": {"argv": ["/opt/julia-1.8.3/bin/julia", "-i", "--color=yes", "--project=@.", "/opt/julia/packages/IJulia/6TIq1/src/kernel.jl", "{connection_file}"], "env": {}, "display_name": "Julia 1.8.3", "language": "julia", "interrupt_mode": "signal", "metadata": {}}, "resources": {"logo-svg": "/kernelspecs/julia-1.8/logo-svg.svg", "logo-64x64": "/kernelspecs/julia-1.8/logo-64x64.png", "logo-32x32": "/kernelspecs/julia-1.8/logo-32x32.png"}}}}




curl 'http://localhost:8888/api/kernels?1674723253096' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: _xsrf=2|b4ecab14|6dfc53412e6e3f0214b25c1aa9a361b2|1671529525; username-localhost-8888=2|1:0|10:1674723251|23:username-localhost-8888|196:eyJ1c2VybmFtZSI6ICIwOTIyN2FhZjdjMzg0MDM0YWRiYjdlMjhlZGU2NmY4NCIsICJuYW1lIjogIkFub255bW91cyBJb2Nhc3RlIiwgImRpc3BsYXlfbmFtZSI6ICJBbm9ueW1vdXMgSW9jYXN0ZSIsICJpbml0aWFscyI6ICJBSSIsICJjb2xvciI6IG51bGx9|5fa4961c1dfe6cdda0c7826abfa4aa92002a031238a4ec6127afa6dd1c06e59d' \
  -H 'Referer: http://localhost:8888/lab?' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61' \
  -H 'X-XSRFToken: 2|b4ecab14|6dfc53412e6e3f0214b25c1aa9a361b2|1671529525' \
  -H 'sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --compressed

HTTP/1.1 200 OK
Server: TornadoServer/6.2
Content-Type: application/json
Date: Thu, 26 Jan 2023 08:54:13 GMT
X-Content-Type-Options: nosniff
Content-Security-Policy: frame-ancestors 'self'; report-uri /api/security/csp-report; default-src 'none'
Access-Control-Allow-Origin: *
Etag: "472ee95283bfd41a08477b3ac704042424e10242"
Content-Length: 320

[{"id": "60313c3d-224a-4f0b-9278-7e19aee2730d", "name": "python3", "last_activity": "2023-01-26T08:52:46.226933Z", "execution_state": "idle", "connections": 0}, {"id": "2de7f000-4f63-4d8b-ad20-4acd0c96edc5", "name": "python3", "last_activity": "2023-01-26T08:52:45.871823Z", "execution_state": "idle", "connections": 0}]




curl 'http://localhost:8888/api/sessions?1674723253098' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: _xsrf=2|b4ecab14|6dfc53412e6e3f0214b25c1aa9a361b2|1671529525; username-localhost-8888=2|1:0|10:1674723251|23:username-localhost-8888|196:eyJ1c2VybmFtZSI6ICIwOTIyN2FhZjdjMzg0MDM0YWRiYjdlMjhlZGU2NmY4NCIsICJuYW1lIjogIkFub255bW91cyBJb2Nhc3RlIiwgImRpc3BsYXlfbmFtZSI6ICJBbm9ueW1vdXMgSW9jYXN0ZSIsICJpbml0aWFscyI6ICJBSSIsICJjb2xvciI6IG51bGx9|5fa4961c1dfe6cdda0c7826abfa4aa92002a031238a4ec6127afa6dd1c06e59d' \
  -H 'Referer: http://localhost:8888/lab?' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61' \
  -H 'X-XSRFToken: 2|b4ecab14|6dfc53412e6e3f0214b25c1aa9a361b2|1671529525' \
  -H 'sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --compressed

HTTP/1.1 200 OK
Server: TornadoServer/6.2
Content-Type: application/json
Date: Thu, 26 Jan 2023 08:54:13 GMT
X-Content-Type-Options: nosniff
Content-Security-Policy: frame-ancestors 'self'; report-uri /api/security/csp-report; default-src 'none'
Access-Control-Allow-Origin: *
Etag: "898d4ac146bde063c47aa85f7eec8ba746a9946e"
Content-Length: 693

[{"id": "c5e99fdf-9081-47a3-9ba9-8ad15208cde6", "path": "Untitled.ipynb", "name": "Untitled.ipynb", "type": "notebook", "kernel": {"id": "60313c3d-224a-4f0b-9278-7e19aee2730d", "name": "python3", "last_activity": "2023-01-26T08:52:46.226933Z", "execution_state": "idle", "connections": 0}, "notebook": {"path": "Untitled.ipynb", "name": "Untitled.ipynb"}}, {"id": "7d0a7c03-49ba-4f19-a58e-ee602c3701ea", "path": "f1e163d1-463c-414b-b4d4-3e51fe427e5f", "name": "jovyan-f1e163d1-463c-414b-b4d4-3e51fe427e5f", "type": "file", "kernel": {"id": "2de7f000-4f63-4d8b-ad20-4acd0c96edc5", "name": "python3", "last_activity": "2023-01-26T08:52:45.871823Z", "execution_state": "idle", "connections": 0}}]





curl 'http://localhost:8888/api/kernelspecs?1674723253154' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: _xsrf=2|b4ecab14|6dfc53412e6e3f0214b25c1aa9a361b2|1671529525; username-localhost-8888=2|1:0|10:1674723251|23:username-localhost-8888|196:eyJ1c2VybmFtZSI6ICIwOTIyN2FhZjdjMzg0MDM0YWRiYjdlMjhlZGU2NmY4NCIsICJuYW1lIjogIkFub255bW91cyBJb2Nhc3RlIiwgImRpc3BsYXlfbmFtZSI6ICJBbm9ueW1vdXMgSW9jYXN0ZSIsICJpbml0aWFscyI6ICJBSSIsICJjb2xvciI6IG51bGx9|5fa4961c1dfe6cdda0c7826abfa4aa92002a031238a4ec6127afa6dd1c06e59d' \
  -H 'Referer: http://localhost:8888/lab?' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61' \
  -H 'X-XSRFToken: 2|b4ecab14|6dfc53412e6e3f0214b25c1aa9a361b2|1671529525' \
  -H 'sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --compressed

HTTP/1.1 200 OK
Server: TornadoServer/6.2
Content-Type: application/json
Date: Thu, 26 Jan 2023 08:54:13 GMT
X-Content-Type-Options: nosniff
Content-Security-Policy: frame-ancestors 'self'; report-uri /api/security/csp-report; default-src 'none'
Access-Control-Allow-Origin: *
Etag: "1e945dbf9f23e03d9eb2e85e80ee8cc3beacd834"
Content-Length: 1308

{"default": "python3", "kernelspecs": {"python3": {"name": "python3", "spec": {"argv": ["/opt/conda/bin/python", "-m", "ipykernel_launcher", "-f", "{connection_file}"], "env": {}, "display_name": "Python 3 (ipykernel)", "language": "python", "interrupt_mode": "signal", "metadata": {"debugger": true}}, "resources": {"logo-svg": "/kernelspecs/python3/logo-svg.svg", "logo-64x64": "/kernelspecs/python3/logo-64x64.png", "logo-32x32": "/kernelspecs/python3/logo-32x32.png"}}, "ir": {"name": "ir", "spec": {"argv": ["R", "--slave", "-e", "IRkernel::main()", "--args", "{connection_file}"], "env": {}, "display_name": "R", "language": "R", "interrupt_mode": "signal", "metadata": {}}, "resources": {"kernel.js": "/kernelspecs/ir/kernel.js", "logo-svg": "/kernelspecs/ir/logo-svg.svg", "logo-64x64": "/kernelspecs/ir/logo-64x64.png"}}, "julia-1.8": {"name": "julia-1.8", "spec": {"argv": ["/opt/julia-1.8.3/bin/julia", "-i", "--color=yes", "--project=@.", "/opt/julia/packages/IJulia/6TIq1/src/kernel.jl", "{connection_file}"], "env": {}, "display_name": "Julia 1.8.3", "language": "julia", "interrupt_mode": "signal", "metadata": {}}, "resources": {"logo-svg": "/kernelspecs/julia-1.8/logo-svg.svg", "logo-64x64": "/kernelspecs/julia-1.8/logo-64x64.png", "logo-32x32": "/kernelspecs/julia-1.8/logo-32x32.png"}}}}



curl 'http://localhost:8888/lab/api/build?1674723254581' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: _xsrf=2|b4ecab14|6dfc53412e6e3f0214b25c1aa9a361b2|1671529525; username-localhost-8888=2|1:0|10:1674723251|23:username-localhost-8888|196:eyJ1c2VybmFtZSI6ICIwOTIyN2FhZjdjMzg0MDM0YWRiYjdlMjhlZGU2NmY4NCIsICJuYW1lIjogIkFub255bW91cyBJb2Nhc3RlIiwgImRpc3BsYXlfbmFtZSI6ICJBbm9ueW1vdXMgSW9jYXN0ZSIsICJpbml0aWFscyI6ICJBSSIsICJjb2xvciI6IG51bGx9|5fa4961c1dfe6cdda0c7826abfa4aa92002a031238a4ec6127afa6dd1c06e59d' \
  -H 'Referer: http://localhost:8888/lab?' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61' \
  -H 'X-XSRFToken: 2|b4ecab14|6dfc53412e6e3f0214b25c1aa9a361b2|1671529525' \
  -H 'sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --compressed

HTTP/1.1 200 OK
Server: TornadoServer/6.2
Content-Type: application/json
Date: Thu, 26 Jan 2023 08:54:14 GMT
X-Content-Type-Options: nosniff
Content-Security-Policy: frame-ancestors 'self'; report-uri /api/security/csp-report; default-src 'none'
Access-Control-Allow-Origin: *
Etag: "a04f921aac2a555d8859c91deeff337ca6b6dedc"
Content-Length: 35

{"status": "stable", "message": ""}



curl 'ws://localhost:8888/api/kernels/2de7f000-4f63-4d8b-ad20-4acd0c96edc5/channels?session_id=96bb22ef-2044-4a19-b537-2478ae388084' \
  -H 'Pragma: no-cache' \
  -H 'Origin: http://localhost:8888' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Sec-WebSocket-Key: z1umn4DxFl/JRJjR4Svg1g==' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61' \
  -H 'Upgrade: websocket' \
  -H 'Cache-Control: no-cache' \
  -H 'Cookie: _xsrf=2|b4ecab14|6dfc53412e6e3f0214b25c1aa9a361b2|1671529525; username-localhost-8888=2|1:0|10:1674723251|23:username-localhost-8888|196:eyJ1c2VybmFtZSI6ICIwOTIyN2FhZjdjMzg0MDM0YWRiYjdlMjhlZGU2NmY4NCIsICJuYW1lIjogIkFub255bW91cyBJb2Nhc3RlIiwgImRpc3BsYXlfbmFtZSI6ICJBbm9ueW1vdXMgSW9jYXN0ZSIsICJpbml0aWFscyI6ICJBSSIsICJjb2xvciI6IG51bGx9|5fa4961c1dfe6cdda0c7826abfa4aa92002a031238a4ec6127afa6dd1c06e59d' \
  -H 'Connection: Upgrade' \
  -H 'Sec-WebSocket-Version: 13' \
  -H 'Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits' \
  --compressed

HTTP/1.1 101 Switching Protocols
Server: TornadoServer/6.2
Date: Thu, 26 Jan 2023 08:54:15 GMT
Access-Control-Allow-Origin: *
Upgrade: websocket
Connection: Upgrade
Sec-Websocket-Accept: ZTy6Cm0FvcBXgnty+91Ztvwm368=




curl 'http://localhost:8888/api/sessions?1674723255886' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: _xsrf=2|b4ecab14|6dfc53412e6e3f0214b25c1aa9a361b2|1671529525; username-localhost-8888=2|1:0|10:1674723251|23:username-localhost-8888|196:eyJ1c2VybmFtZSI6ICIwOTIyN2FhZjdjMzg0MDM0YWRiYjdlMjhlZGU2NmY4NCIsICJuYW1lIjogIkFub255bW91cyBJb2Nhc3RlIiwgImRpc3BsYXlfbmFtZSI6ICJBbm9ueW1vdXMgSW9jYXN0ZSIsICJpbml0aWFscyI6ICJBSSIsICJjb2xvciI6IG51bGx9|5fa4961c1dfe6cdda0c7826abfa4aa92002a031238a4ec6127afa6dd1c06e59d' \
  -H 'Referer: http://localhost:8888/lab?' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61' \
  -H 'X-XSRFToken: 2|b4ecab14|6dfc53412e6e3f0214b25c1aa9a361b2|1671529525' \
  -H 'sec-ch-ua: "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --compressed

HTTP/1.1 200 OK
Server: TornadoServer/6.2
Content-Type: application/json
Date: Thu, 26 Jan 2023 08:54:15 GMT
X-Content-Type-Options: nosniff
Content-Security-Policy: frame-ancestors 'self'; report-uri /api/security/csp-report; default-src 'none'
Access-Control-Allow-Origin: *
Etag: "898d4ac146bde063c47aa85f7eec8ba746a9946e"
Content-Length: 693

[{"id": "c5e99fdf-9081-47a3-9ba9-8ad15208cde6", "path": "Untitled.ipynb", "name": "Untitled.ipynb", "type": "notebook", "kernel": {"id": "60313c3d-224a-4f0b-9278-7e19aee2730d", "name": "python3", "last_activity": "2023-01-26T08:52:46.226933Z", "execution_state": "idle", "connections": 0}, "notebook": {"path": "Untitled.ipynb", "name": "Untitled.ipynb"}}, {"id": "7d0a7c03-49ba-4f19-a58e-ee602c3701ea", "path": "f1e163d1-463c-414b-b4d4-3e51fe427e5f", "name": "jovyan-f1e163d1-463c-414b-b4d4-3e51fe427e5f", "type": "file", "kernel": {"id": "2de7f000-4f63-4d8b-ad20-4acd0c96edc5", "name": "python3", "last_activity": "2023-01-26T08:52:45.871823Z", "execution_state": "idle", "connections": 0}}]




curl 'ws://localhost:8888/api/kernels/2de7f000-4f63-4d8b-ad20-4acd0c96edc5/channels?session_id=6c3beddb-ca07-4132-9fd7-ff011cbae76b' \
  -H 'Pragma: no-cache' \
  -H 'Origin: http://localhost:8888' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Sec-WebSocket-Key: lihdpLFURn1uI2X3IBJ4/w==' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61' \
  -H 'Upgrade: websocket' \
  -H 'Cache-Control: no-cache' \
  -H 'Cookie: _xsrf=2|b4ecab14|6dfc53412e6e3f0214b25c1aa9a361b2|1671529525; username-localhost-8888=2|1:0|10:1674723251|23:username-localhost-8888|196:eyJ1c2VybmFtZSI6ICIwOTIyN2FhZjdjMzg0MDM0YWRiYjdlMjhlZGU2NmY4NCIsICJuYW1lIjogIkFub255bW91cyBJb2Nhc3RlIiwgImRpc3BsYXlfbmFtZSI6ICJBbm9ueW1vdXMgSW9jYXN0ZSIsICJpbml0aWFscyI6ICJBSSIsICJjb2xvciI6IG51bGx9|5fa4961c1dfe6cdda0c7826abfa4aa92002a031238a4ec6127afa6dd1c06e59d' \
  -H 'Connection: Upgrade' \
  -H 'Sec-WebSocket-Version: 13' \
  -H 'Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits' \
  --compressed

HTTP/1.1 101 Switching Protocols
Server: TornadoServer/6.2
Date: Thu, 26 Jan 2023 08:54:16 GMT
Access-Control-Allow-Origin: *
Upgrade: websocket
Connection: Upgrade
Sec-Websocket-Accept: FlxFtUeiPf3IjaQxRW+bQTD5eb8=




curl 'ws://localhost:8888/api/kernels/60313c3d-224a-4f0b-9278-7e19aee2730d/channels?session_id=4e037c01-ca4c-4fc5-ad93-65f9d0df90c7' \
  -H 'Pragma: no-cache' \
  -H 'Origin: http://localhost:8888' \
  -H 'Accept-Language: en-US,en;q=0.9,ko;q=0.8' \
  -H 'Sec-WebSocket-Key: MSXuHT9QvDjYhg7zzaUAYw==' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61' \
  -H 'Upgrade: websocket' \
  -H 'Cache-Control: no-cache' \
  -H 'Cookie: _xsrf=2|b4ecab14|6dfc53412e6e3f0214b25c1aa9a361b2|1671529525; username-localhost-8888=2|1:0|10:1674723251|23:username-localhost-8888|196:eyJ1c2VybmFtZSI6ICIwOTIyN2FhZjdjMzg0MDM0YWRiYjdlMjhlZGU2NmY4NCIsICJuYW1lIjogIkFub255bW91cyBJb2Nhc3RlIiwgImRpc3BsYXlfbmFtZSI6ICJBbm9ueW1vdXMgSW9jYXN0ZSIsICJpbml0aWFscyI6ICJBSSIsICJjb2xvciI6IG51bGx9|5fa4961c1dfe6cdda0c7826abfa4aa92002a031238a4ec6127afa6dd1c06e59d' \
  -H 'Connection: Upgrade' \
  -H 'Sec-WebSocket-Version: 13' \
  -H 'Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits' \
  --compressed

HTTP/1.1 101 Switching Protocols
Server: TornadoServer/6.2
Date: Thu, 26 Jan 2023 08:54:16 GMT
Access-Control-Allow-Origin: *
Upgrade: websocket
Connection: Upgrade
Sec-Websocket-Accept: T6qCnTtEkdgPnnZs7O+oCGrcQXc=






