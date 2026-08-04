# In questo laboratorio costruirai una tabella hash da zero. Una tabella hash è una struttura dati che archivia coppie chiave-valore. Una tabella hash funziona prendendo la chiave come input e poi eseguendo l'hash di questa chiave secondo una specifica funzione di hashing.
# Per questo laboratorio, la funzione di hashing sarà semplice: sommerà i valori Unicode di ogni carattere nella chiave. Il valore hash sarà poi usato come chiave effettiva per archiviare il valore associato. Lo stesso valore hash sarà usato anche per recuperare ed eliminare il valore associato alla chiave.



class HashTable:
    
    def __init__(self):
        self.collection = {}

    def hash(self, parola = str):
        somma_hash = 0
        for letter in parola:
            somma_hash += ord(letter)
        return somma_hash

    def add(self, chiave, valore): 
        hash_chiave = self.hash(chiave)
        if hash_chiave not in self.collection:
            self.collection[hash_chiave]={}
        self.collection[hash_chiave][chiave]=valore
        
         
    def remove(self, chiave):
        hash_chiave = self.hash(chiave)
        if hash_chiave in self.collection and chiave in self.collection[hash_chiave]:
            del self.collection[hash_chiave][chiave]
        else:
            return
    def lookup(self, chiave):
        hash_chiave = self.hash(chiave)
        if hash_chiave in self.collection and chiave in self.collection[hash_chiave]:
            return self.collection[hash_chiave][chiave]
        else:
            return None