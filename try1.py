import re
import os
import threading
import socket
import ssl

# semaph = threading.Semaphore(4)

def get_url_images_in_text(text):
    urls = []
    results = re.findall(r'\/wp-content\/[^\"]*(?:png|jpg)', text)
    for x in results:
      urls.append(x)

    return urls

def get_images_from_url(url):
  domain = url.split("//")[-1].replace("/","")
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysock:
    mysock = ssl.wrap_socket(mysock, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
    mysock.connect ( (socket.gethostbyname(domain), 443 ) )
    mysock.sendall ("GET / HTTP/1.1\r\nHost: {0}\r\nConnection: close\r\n\r\n".format(domain).encode("utf-8"))

    content_response = ""

    while True: 
      data = mysock.recv(1024)
      if len(data) == 0:
        break
      content_response += data.decode("utf-8")

    return get_url_images_in_text(content_response)

def dowload_img(path):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect(("utm.md" , 443))
    s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
    s.sendall("GET {0} HTTP/1.1\r\nHost: utm.md\r\nConnection: close\r\n\r\n".format(path).encode("utf-8"))

    img_bytes = b''

    while True:

      data = s.recv(1024)
      if not data:
        img_bytes = img_bytes.split(b"\r\n\r\n")
        if "200" not in img_bytes[0].decode("utf-8"):
          print(path)
        img_path = os.path.join(os.getcwd(), "FailImages", path.rpartition("/")[-1])
        with open(img_path, "wb") as f:
          f.write(img_bytes[-1])
        break
      
      img_bytes+=data

img_list = get_images_from_url("utm.md")

thread_list = [ ]

for i in img_list:
  # semaph.acquire()
  t = threading.Thread(target=dowload_img, args=(i,))
  thread_list.append(t)
  t.start()
  # semaph.release()
  # print (str(t)+" started")

for i in thread_list:
  i.join()
  # print (str(i)+" fihished ")
