import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 65433

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[SERVER] Listening on {HOST}:{PORT}...")

        conn, addr = s.accept()
        with conn:
            print(f"[SERVER] Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                pesan = data.decode()
                print(f"[SERVER] Received from {addr}: {pesan}")
                if pesan.lower() == 'exit':
                    break
                balasan = f"Pesan Server Diterima : {pesan}"
                conn.sendall(balasan.encode())
        print(f"[SERVER] Connection with {addr} closed.")
        print("[Main Program] Program selesai.")

def client():
    time.sleep(1)  #
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"[CLIENT] Masukkan Pesan (Ketik 'exit' untuk keluar) : ", end="")
        while True:
            pesan = input()
            s.sendall(pesan.encode())
            if pesan.lower() == 'exit':
                break
            data = s.recv(1024)
            print(f"[CLIENT] Server Membalas Pesan : {data.decode()}")
            print(f"[CLIENT] Masukkan Pesan (Ketik 'exit' untuk keluar) : ", end="")
        print("[CLIENT] Connection closed.")


server_thread = threading.Thread(target=server)
client_thread = threading.Thread(target=client)

server_thread.start()
client_thread.start()

server_thread.join()
client_thread.join()