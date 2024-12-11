
def somme_chiffres(n):
    return sum(int(chiffre) for chiffre in str(n))

def sont_complementaires(N1, N2):
    if somme_chiffres(N1) == somme_chiffres(N2):
        print(f"les nombres sont complémentaires.")
    else:
        print(f"les nombres ne sont pas complémentaires.")

N1 = int(input("Entrez le premier entier (N1) : "))
N2 = int(input("Entrez le second entier (N2) : "))

sont_complementaires(N1, N2)






# def numbres_complementaires(Nombre):
    
    # oldNbr = 0
    # for i in str(Nombre):
        # oldNbr = oldNbr+int(i)
    # return oldNbr
        
    # total = sum(int(chiffre) for chiffre in str(Nombre) )
    # return total
        

# def verify_complementaires(N1, N2):
    # if numbres_complementaires(N1) == numbres_complementaires(N2):
        # print("Nombres complémentaires")
    # else:
        # print("Nombres non complémentaires")
        
    
# N1 = int(input("Entrez nombre 1 : "))
# N2 = int(input("Entrez nombre 2 : "))
# verify_complementaires(N1, N2)