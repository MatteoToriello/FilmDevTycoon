
from menu import *
import sys


class Started_Menu():
    
    def __init__(self):
        self.scelta={
            "1":self.new_game,
            "2":self.restart_game,
            "0":self.quit
        }
        
    def show_menu(self):
        print('''
              Benvenuto a HOLLYWOOD!
              Premi 1 per iniziare una nuova partita,
              Premi 2 per caricare un salvataggio esistente (NON DISPONIBILE),
              Premi 0 per uscire.
              ''')
        
    def run(self):
        while True:
            self.show_menu()
            scelta=input("Seleziona l'operazione: ")
            if scelta.isnumeric():
                azione=self.scelta.get(scelta)
            else:
                azione=False
            if azione:
                azione()
            else:
                print("Errore, operazione non ammessa. ")
    
    def new_game(self):
        Menu().run()
    
    def restart_game(self):
        pass
    
    def quit(self):
        print("Arrivederci!")
        sys.exit(1)


if __name__=="__main__":
    Started_Menu().run()