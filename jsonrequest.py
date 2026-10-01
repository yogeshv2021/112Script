import json
import socket


def json_receive(local_ip, local_port):

   try:
       s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       s.bind((local_ip, local_port))
       print("Bind the local ip and port %s,%s" %(local_ip, local_port))
       s.listen()
       while True:
           conn,address = s.accept()
           data = conn.recv(65535).decode('utf-8')
           correlation_id = None
           if "Expect: 100-continue" in data: 
               conn.sendall(b"HTTP/1.1 100 Continue\r\n\r\n")
               body = conn.recv(65535).decode('utf-8') 
               print("Received body:\n", body) 
           else: 
               body = data.split("\r\n\r\n", 1)[1] if "\r\n\r\n" in data else ""

           for line in data.split("\r\n"): 
               print(line)
               if line.startswith("X-Correlation-Id:"): 
                   correlation_id = line.split(":", 1)[1].strip()
                   break
           print(correlation_id)
           response_obj = { "code": "0", "message": "request has reached", "status": "processed" ,"X-Correlation-Id": correlation_id, "Correlation-id": correlation_id}
           json_str = json.dumps(response_obj)
           response = ( "HTTP/1.1 200 OK\r\n" f"Content-Type: application/json\r\n" f"Content-Length: {len(body)}\r\n" "Connection: close\r\n" "\r\n" + json_str )
           json_bytes = response.encode('utf-8')
           print("received json request %s" %data)
           conn.sendall(json_bytes)
           print("sent json request %s" %json_bytes)
           conn.close()

   except Exception as error:
       print("Exception occured %s" %error)


json_receive("192.168.151.112",5740)



