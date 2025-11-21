
def signatures(message):
    """Signer le message en gardant les 2 avant derniêres lettres de chaque mots
    :param message: le message à signer
     :return: la signature
        """
    signature = ""
    mots = message.split("")
        for mot in mots :
            if len(mot) >2:
                siganture += mot[-3]
         return signature
        

    def verifier_hash(message,signature):
        """
        Vérifier si la signature est valide pour le message
        :param:message qui a supposément été signé
        :param: signature a vérifier
        """
        return signature ==signer(message)
    #main

if __name__== "__main__":
    messages_gr5 = {
        "pseudo": "IronCode",
        "messages": ["Le monstre est au niveau 7", "Code 9 activé demain", "La réponse est 142"],
        "signatures": ["fresea", "odivai", "nses14"]
    }
    
    ls_valide=[]
    ls_alteres = []
    for i in range(len(messages_gr5["messages"])):
        if verifier(messages_gr5)["messages"][i], messages_gr5["signature"]
        
    
