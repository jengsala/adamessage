"""Module inutile qui affiche des messages :-)."""
    
class MaClasse:
    
    def __init__(self, attribut1, attribut2):
        self.attribut1 = attribut1
        self.attribut2 = attribut2
    
    def bonjour(self, nom):
        """Dit Bonjour."""
        return "Bonjour " + nom

    def ciao(self, nom):
        """Dit Ciao."""
        return "Ciao " + nom

    def hello(self, nom):
        """Dit Hello."""
        return "Hello " + nom

    def quicktext(self):
        print('Hello, welcome to QuickSample package.')