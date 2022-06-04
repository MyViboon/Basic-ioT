from tkinter import*
import socket
import threading

def runserver():
    #####################
    serverip = '192.168.1.3'
    port = 9000
    #####################

    buffsize = 4096

    while True:
            server = socket.socket()
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            server.bind((serverip,port))
            server.listen(1)
            print('waiting micropython...')

            client, addr = server.accept()
            print('connected from:', addr)

            data = client.recv(buffsize).decode('utf-8')
            print('Data from MicroPython: ',data)
            
            data_split = data.split(':')
            if data_split[1] == 'ON':
                v_status.set('{} สถานะ {}'.format(data_split[0],data_split[1]))
                L2.configure(fg='green')
            else:
                v_status.set('{} สถานะ {}'.format(data_split[0],data_split[1]))
                L2.configure(fg='red')
                
            client.send('received your messages.'.encode('utf-8'))
            client.close()
            
GUI = Tk()
GUI.geometry('400x400')
GUI.title('โปรแกรมติดตามสถานะ IOT By วิบูลย์')

FONT = ('Angsana New',20)
L1= Label(GUI, text='สถานะ LED จาก MicroPython',font=FONT)
L1.pack()

v_status = StringVar()
v_status.set('<<<< No Status >>>>')
L2 = Label(GUI, textvariable= v_status, font=FONT)
L2.configure(fg='red')
L2.pack()

############# RUNSERVER ###############
task = threading.Thread(target=runserver)
task.start()
#######################################
GUI.mainloop()
