
class User:
    def __init__(self, nome, casa, generi, storico_film):
        self.nome=nome
        self.casa=casa
        self.generi=generi
        self.esperienza=0
        self.livello=1
        self.punti_ricerca=10
        self.storico=storico_film
    
    def research(self, oggetto):
        if self.punti_ricerca>=10:
            self.generi=oggetto.sbloccati
        else:
            print("Non hai abbastanza punti ricerca!")
        
    def make_film(self, titolo, genere, parametri):
        new_film=Movie(titolo, genere, parametri)
        voto=new_film.review()
        self.storico.aggiungi_film(new_film.titolo, voto)
        self.experience_up(voto)
        
        
    
    def level_up(self):
        if self.esperienza>=10:
            self.livello+=1
            self.esperienza=self.esperienza-10
        print("Il tuo livello è: livello "+str(self.livello)+ ". La tua esperienza ammonta a: "+str(self.esperienza)+ " punti.")
        input()
        
    def point_research_up(self, voto):
        if voto==10:
            self.punti_ricerca+=30
        elif voto <=10 and voto >8:
            self.punti_ricerca+=20
        elif voto<=8 and voto>5.9:
            self.punti_ricerca+=10
        elif voto<6 and voto>4:
            self.punti_ricerca+=5
        else:
            print("Nessun punto ricerca guadagnato...")
            input()
            
    def experience_up(self, voto):
        if voto==10:
            self.esperienza+=10
        elif voto <=10 and voto >8:
            self.esperienza+=5
        elif voto<=8 and voto>5.9:
            self.esperienza+=3
        elif voto<6 and voto>4:
            self.esperienza+=2
        else:
            self.esperienza+=1 
        self.level_up()
           
    def research(self):
        if self.punti_ricerca>=10:
            self.generi.sblocca(1)
            print("Congratulazioni! Hai sbloccato un nuovo genere: "+str(self.generi.sbloccati[-1]))
            self.punti_ricerca-=10
        else:
            print("Non hai abbastanza punti ricerca! Sviluppa film di successo per ottenerne di più! ")
        print("Punti ricerca: "+str(self.punti_ricerca))
        input()

class Genere:
    def __init__(self):
        self.sbloccati=[]
        self.bloccati=["Azione", "Avventura", "Commedia", "Horror", "Drama",
                  "Casual", "Supereroi", "Guerra", "Storici", "Documentario",
                  "Thriller", "Famiglia", "Teenagers", "Fantasy", "Medievale", "Spazio",
                  "Fantascienza"]
        self.sblocca(3)
    
    def sblocca(self, numero):
        for i in range(numero):
            if len(self.bloccati)==0:
                print("Hai già sbloccato tutti i generi!")
                break
            self.sbloccati.append(self.bloccati[0])
            self.bloccati.pop(0)
            
    def print_unlock(self):
        for i in self.sbloccati:
            print(i)
            
        

class Storico_Film:
    def __init__(self):
        self.lista=[]
    
    def aggiungi_film(self, film, voto):
        self.lista.append([film, voto])

    def stampa_storico(self):
        if len(self.lista)==0:
            print("Non hai ancora creato nessun film!")
            return
        for i in self.lista:
            print(i)
        input()
        
    def media_voti(self):
        if len(self.lista)==0:
            print("Non hai ancora creato nessun film!")
            return
        media=0
        for i in self.lista:
            media+=i[-1]
        print("La media dei voti dei tuoi film è: "+str(media/len(self.lista)))
        input()
        
class Movie: 
    table_content={"Azione":[15,5,20],
        "Avventura":[0,30,10],
        "Commedia":[10,10,20],
        "Horror":[20,15,5],
        "Drama":[15,20,5],
        "Casual":[20,0,20],
        "Supereroi":[5,10,25],
        "Guerra":[0,20,20],
        "Storici":[0,35,5],
        "Documentario":[5,10,25],
        "Thriller":[20,20,0],
        "Famiglia":[20,0,20],
        "Teenagers":[15,10,15],
        "Fantasy":[5,20,15],
        "Medievale":[5,25,10],
        "Spazio":[10,5,25],
        "Fantascienza":[5,15,20]
    }
    def __init__(self, titolo, genere, parametri):
        self.titolo=titolo
        self.genere=genere
        self.parametri=parametri

    def review(self):
        valori=self.table_content[self.genere]
        voto=[]
        media=0
        for i in range(len(valori)):
            dif=abs(self.parametri[i]-valori[i])
            if dif>10:
                voto.append(3)
            elif dif<=10 and dif>8:
                voto.append(4.5)
            elif dif<=8 and dif>6:
                voto.append(5)
            elif dif<=6 and dif>4:
                voto.append(6)
            elif dif <=4 and dif>3:
                voto.append(7)
            elif dif<=3 and dif>2:
                voto.append(8)
            elif dif <=2 and dif>1:
                voto.append(8.5)
            elif dif<=1 and dif>0.6:
                voto.append(9)
            else:
                voto.append(10)
        for j in voto:
            media+=j
        print("Il voto per "+self.titolo, "è: "+str(media/3))
        input()
        return media/3
