from object_game import *
import sys


class Menu():
    
    def __init__(self):
        self.utente=None
        self.scelta={"1":self.make_film,
                     "2":self.storico,
                     "3":self.media_film,
                     "4":self.do_research,
                     "5":self.show_genre,
                     "0":self.quit}
        
    def show_menu(self):
        print('''Inserisci:
              1 per creare un nuovo film,
              2 per visualizzare lo storico dei tuoi film,
              3 per visualizzare la media dei tuoi film,
              4 per sbloccare nuovi generi (DEVI AVERE 10 PUNTI RICERCA),
              5 per visualizzare tutti i generi che possiedi.
              0 per uscire. 
              ''')
        
    def start_user(self, nome="", casa=""):
        while nome=="":
            nome=input("Inserisci il nome del tuo personaggio: ")
        while casa=="":
            casa=input("Inserisci il nome per la tua casa di produzione: ")
        generi=Genere()
        storico=Storico_Film()
        user=User(nome, casa, generi, storico)
        return user
          
    def run(self):
        self.utente=self.start_user()
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
        
         
    def make_film(self, titolo="", genere="", sonoro=41, storia=41, tecnica=41):
        parametri=[]
        while titolo=="":
            titolo=input("Inserisci un titolo per il tuo nuovo film! ")
        while genere=="":
            print("RICORDA! Possiedi questi generi: ")
            self.utente.generi.print_unlock()
            genere=input("Inserisci un genere per il tuo nuovo film: ")
            for i in self.utente.generi.sbloccati:
                if i.upper()==genere.upper():
                    break
            else:
                genere=""
        print("RICORDA! Puoi spendere al massimo 40 punti totali, cerca di creare un buon film in base al genere selezionato!")
        print("FIRST STAGE: Sonoro")
        while sonoro>40:
            sonoro=self.first_stage()
        print("SECOND STAGE. Sceneggiatura&Booking")
        while storia>40 or sonoro+storia>40:
            storia=self.second_stage()
        print("THIRD STAGE. Tecnica")
        while tecnica>40 or sonoro+tecnica+storia>40:
            tecnica=self.third_stage()
        parametri.append(sonoro)
        parametri.append(storia)
        parametri.append(tecnica)
        self.utente.make_film(titolo, genere.capitalize(), parametri)
            
        
    def first_stage(self, col_son="", vol_eff="", imm=""):
        while col_son=="" or col_son.isnumeric()==False:
            col_son=input("Inserisci un punteggio per la colonna sonora: ")
        while vol_eff=="" or vol_eff.isnumeric()==False:
            vol_eff=input("Inserisci un punteggio per il volume degli effetti: ")
        while imm=="" or imm.isnumeric()==False:
            imm=input("Inserisci un punteggio per l'immersività del sonoro: ")
        tot=int(col_son)+int(vol_eff)+int(imm)
        print("Hai speso in totale "+str(tot)+".")
        return tot
        
    def second_stage(self, sto="", dia="", att=""):
        while sto=="" or sto.isnumeric()==False:
            sto=input("Inserisci un punteggio per la storia: ")
        while dia=="" or dia.isnumeric()==False:
            dia=input("Inserisci un punteggio per i dialoghi: ")
        while att=="" or att.isnumeric()==False:
            att=input("Inserisci un punteggio per gli attori: ")
        tot=int(sto)+int(dia)+int(att)
        print("Hai speso in totale "+str(tot)+ ".")
        return tot
        
    def third_stage(self, cgi="", fot="", rit=""):
        while cgi=="" or cgi.isnumeric()==False:
            cgi=input("Inserisci un punteggio per la CGI/Effetti speciali: ")
        while fot=="" or fot.isnumeric()==False:
            fot=input("Inserisci un punteggio per la fotografia: ")
        while rit=="" or rit.isnumeric()==False:
            rit=input("Inserisci un punteggio per il ritmo: ")
        tot=int(cgi)+int(fot)+int(rit)
        print("Hai speso in totale "+str(tot))
        return tot
        
    def storico(self):
        self.utente.storico.stampa_storico()
        
    def media_film(self):
        self.utente.storico.media_voti()
            
    def do_research(self):
        self.utente.research()
        
    def show_genre(self):
        self.utente.generi.print_unlock()
        
    def quit(self):
        print("Arrivederci!")
        sys.exit(1)
            
if __name__=="__main__":
    Menu().run()
            