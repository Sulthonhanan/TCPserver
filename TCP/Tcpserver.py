import socket

HOST = '127.0.0.1'
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[SERVER] LISTENING on {HOST}:{PORT}...")

    conn, addr = s.accept()
    with conn:
        print(f"[SERVER] Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"[SERVER] Diterima: {data.decode()}")
            conn.sendall(b"Pesan Diterima dari server!")
            