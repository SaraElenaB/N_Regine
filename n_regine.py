import copy
from time import time
#facciamo una classe perchè dato che dobbiamo richiamare più volte è più sicuro
class NRegine():

    def __init__(self):
        #quante volte raggiungiamo il nodo terminale
        self.nSoluzioni = 0
        self.nChiamate=0
        self.combinazioniSol=[]

    #--------------------------------------------------------------------------------------------------------------------------
    def solve(self, n):
        self.nSoluzioni = 0; #ogni volta che la chiami si aggiorna
        self._ricorsione([], n)

    # --------------------------------------------------------------------------------------------------------------------------
    def isAmmissibile(self, regina1, regina2):
        #1) verifico riga --> se non va bene return false
        if regina1[0] == regina2[0]:
            return False
        #2) verifico colonna
        if regina1[1] == regina2[1]:
            return False
        #3) verifico diagonale 1
        if regina1[0]+regina1[1] == regina2[0]+regina2[1]:
            return False
        #4) verifico giagonale 2
        if regina1[0]-regina1[1] == regina2[0]-regina2[1]:
            return False
        #5) ha passato tutti i controlli
        return True

    # --------------------------------------------------------------------------------------------------------------------------
    def isSoluzione(self, parziale):
        #per ogni regina guardare tutte le altre regine
        for i in range(len(parziale)-1):  #devi assicurarti che siano diverse
            for j in range(i+1, len(parziale)):  #stesso indice --> stessa regina ovvio che non ha combinazione
                ris= self.isAmmissibile(parziale[i], parziale[j])
                if ris==False:
                    return False
        return True

    # --------------------------------------------------------------------------------------------------------------------------
    def isValida(self, nuovaRegina, parziale):
        for regina in parziale:
            if not self.isAmmissibile(nuovaRegina, regina):
                return False
        return True

    def isSenzaDoppioni(self, parziale):

        ordinata = sorted(parziale)
        for sol in self.combinazioniSol:
            if ordinata in sol:
                return False
        return True

    # --------------------------------------------------------------------------------------------------------------------------
    def _ricorsione(self, parziale, n):
        self.nChiamate += 1
        #condizione terminale:
        if len(parziale) == n:
            # a1. verifico se questa è una soluzione --> va bene ma è un controllo alla fine, meglio farla prima
                # if self.isSoluzione(parziale):
            # Verifica se quella combinazione esiste già solo in ordine diverse
            # Copio il parziale per non modificarlo dopo con il backtracking
            copia = copy.deepcopy(parziale)
            if self.isSenzaDoppioni(copia):
                print(parziale)
                self.combinazioniSol.append(sorted(copia))
                self.nSoluzioni += 1

        #condizione ricorsiva:
        else:
            #possiamo mettere la regina in qualsiasi posizione tra quelle esistenti
            for riga in range(n):
                for colonna in range(n):
                    # a1. check sulla regina che vado ad aggiungere --> se vediamo che qauel posto è già occupato subito non mettiamo
                    nuovaRegina = [riga, colonna]
                    if self.isValida( nuovaRegina, parziale):
                        #provo nuova ipotesi
                        parziale.append([riga, colonna])
                        #vado avanti nella ricorsione
                        self._ricorsione(parziale, n)
                        #backtracking
                        parziale.pop()

#spiegazione
    #parziale è una lista dove volta per votla aggiungiamo una regina --> fatto fino a quando non abbiamo n regine
    #condzione terminale: semplice
        #num sufficiente di elementi
        #temrinato tutte le possibili condizioni
    #condizione ricorsiva:
        # .append() --> pezzettino di soluzione
        # .ricorsione --> continua a ciclare e ne metto un altro
        # .pop() --> arriva alla fine e torna indietro

if __name__ == "__main__":
    nreg = NRegine()
    start = time()
    print(nreg.solve(4))
    end = time()
    print(f"Elapsed time: {end - start}")
    print(f"Ho trovato {nreg.nSoluzioni} soluzioni possibili")
    print(f"N. chiamate ricorsive {nreg.nChiamate} ")
