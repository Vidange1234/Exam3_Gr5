"""
fonction_double_chiffrement:Elle va chiffrer deux fois le message secret avec une clé de cryptage donné

#Clé de cryptage(liste)
    cle_gr5 = [
    [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z],
    [m,u,k,e,n,o,r,z,q,v,c,s,t,l,i,b,a,j,y,h,p,x,d,f,g]
    ]
#Choisir un message a transmettre de façon extra confidentielle

    message_a_encoder="J'ai hâte que l'examen soit fini"
#definir un nb_cesar
    nb_cesar=5
#definir existence de message_code
    message_code=""

#inspiration venant du corrigé d'un exercice de cryptographie
    pour chaque i in range(len(message_a_encoder)):
        # position = trouver caractère dans cle_gr5
        position = cle_gr5.index(message_a_encoder[i])
        position += nb_cesar
        message_code += cle_gr5[position]
        pour chaque charactere in range(len(message_a_encoder)):
            # position = trouver caractère dans cle_gr5
            position = cle_gr5[1].index(message_a_encoder[i])
            position += nb_cesar
            message_code += cle_gr5[1][position]

    retour message_code
"""
def fonction_double_chiffrement():
    cle_gr5 = [
        ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        ["m","u","k","e","n","o","r","z","q","v","c","s","t","l","i","b","a","j","y","h","p","x","d","f","g"]
    ]
    message_a_encoder = "J'ai hâte que l'examen soit fini"
    nb_cesar=5
    message_code = ""

    for i in range(len(message_a_encoder)):
    # position = trouver caractère dans cle_gr5
        position = cle_gr5.index([i])
        position += nb_cesar
        message_code += cle_gr5[position]
        for charactere in range(len(message_code)):
    # position = trouver caractère dans cle_gr5,deuxième liste
            position = cle_gr5[1].index([i])
            position += nb_cesar
            message_code += cle_gr5[1][position]

    return message_code