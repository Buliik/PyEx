from xmlrpc.server import SimpleXMLRPCServer


class SPJAServer(object):

    def __init__(self):
        self.dct = {}
        self.filename = "points.txt"
        self.load_data()

    def download_data(self):
        return self.dct

    def load_data(self):
        #TODO 1 (1b)
        #nacte data ze souboru points.txt
        #data ulozte do slovniku self.dct
        with open("points.txt") as f:
            for line in f:
                (key, val) = line.split(':')
                self.dct[key] = val
        pass

    def save_data(self):
        #TODO 2 (1b)
        #ulozi data do souboru ve spravnem formatu (viz soubor points.txt)
        #data jsou ulozena ve slovniku self.dct
        file = open("points2.txt", "w")
        for i in self.dct:
            file.write(i, " : ", self.dct[i])
        file.close()       
        pass

    def insert(self, login, points):
        #TODO 3 (1b)
        je = False
        for i in self.dct:
            if i[key] == login:
                self.dct[login].append(points)
                je = True

        if not je:
            self.dct[login] = points
        
        self.save_data()
        # vlozi vysledek studentovi (nezapomente osetrit, pokud student jeste neni v seznamu)
        # po pridani vysledku ulozte data (save_data)
        pass
    
    def get_best_6(self, login):
        arr = self.dct[login]
        arr.argsort()[-6:][::-1]
        #TODO 4 (1.5b)
        #vrati soucet 6-ti nejlepsich vysledku studenta
        return arr
            
def main():

    instance = SPJAServer()
    server_address = ('localhost', 10001)
    server = SimpleXMLRPCServer(server_address)
    #TODO 5 (0.5b)
    #zaregistrujte funkce, ktere budou pristupne z klienta (3 funkce)
    server.register_function(instance.download_data(),'download_data')
    server.register_function(instance.insert,'insert')
    server.register_function(instance.get_best_6, 'get_best_6')
    server.register_introspection_functions()
    print("Starting SPJA server, use <Ctrl-C> to stop")
    server.serve_forever()
    
if __name__ == "__main__":
    main()
