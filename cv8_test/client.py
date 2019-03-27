from xmlrpc.client import ServerProxy

def show_data(data):
    for row in data:
        print(row, ":", data[row])

server = ServerProxy("http://localhost:10001")
data = server.download_data()
show_data(data)

server.insert("jir213", 5)
print("BAJ555:", server.get_best_6("baj555"))
print("BEJ790:", server.get_best_6("bej790"))
data = server.download_data()
show_data(data)
