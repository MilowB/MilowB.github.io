# Correction du TP2 de Cryptographie - IUT informatique 2ème année - Université Savoie Mont Blanc
# Auteur: Toby Connor-Kebbell -> https://github.com/tobyck/rsa-encryption - 02/2022
# Modifié par Mickael Bettinelli - 11/2022
# Implementation de RSA

import random

# Retourne le pgcd de a et b
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Génération et retourne un nombre premier
def generate_random_prime():
    isPrime = False
    # On boucle tant que nous n'avons pas de nombre premier
    while not isPrime:
        # Sélectionne un nombre aléatoire compris entre 1000 et 1,000,000
        x = random.randrange(pow(10,3), pow(10,6), 1)
        # Le flag passe à vrai quand le nombre n'est pas premier
        flag = False
        # La boucle s'arrête lorsque le nombre n'est pas premier (flag devient True) ou s'il est premier (isPrime devient True)
        while not flag and not isPrime:
            # Cherche des facteurs
            for i in range(2, x):
                if (x % i) == 0:
                    flag = True
                    break
            if not flag:
                isPrime = True
    return x

# Génération de e en fonction de phi
def generate_e(phi):
    flag = False
    # On boucle tant que e n'est aps premier avec phi
    while not flag:
        # Sélectionne un nombre aléatoire compris entre 100 et phi
        e = random.randint(100, phi)
        if gcd(e, phi) == 1:
            flag = True
    return e

# Algorithme d'Euclide étendu
# a est le nombre dont on veut connaître l'inverse
# b est la taille de l'ensemble Z/bZ (phi dans le cas de cet algo)
# x et y sont respectivement un des coefficients de bézout et le même coefficient à l'étape n-1
# Algo décrit ici: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
def egcd(a, b, x = 0, y = 1):
    x, y = y, x - (b // a) * y
    # Si le reste de b//a est 0, alors on a fini
    if b % a == 0:
        return x, y
    # A chaque nouvelle étape, on rappelle egcd() avec a = b % a et b = a
    # -> Comme dans l'algorithme d'Euclique que l'on a vu en CM
    return egcd(b % a, a, x, y)

# Génère les clés privées et publiques et les retourne dans un dictionnaire
def generate_key_pair():
    # Génère deux nombres premiers p et q
    p, q = generate_random_prime(), generate_random_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = generate_e(phi)
    d = egcd(e, phi)[0]
    # Si l'inverse de e (d) est d < 0 ou d > phi, le remettre dans l'intervalle [0, phi-1]
    d %= phi
    keys = {
        "p": p,
        "q": q,
        "phi": phi,
        "public": e,
        "private": d,
        "modulus": n
    }
    return keys

# Liste de caractères dans l'alphabet
chars = [char for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`1234567890-=~!@#$%^&*()_+[]\\{}|;':,./<>? "]

def encrypt(m, e, n):
    c = []
    # chars.index(m[i]) -> index dans l'alphabet l81
    for i in range(len(m)):
        # Cette opération est celle décrite dans le CM2, elle chiffre une lettre du message complet
        c.append(pow(chars.index(m[i]), e, n))
    # Chaque lettre chiffrée est séparée d'un tiret
    return "-".join([str(num) for num in c])

def decrypt(c, d, n):
    m = []
    # On re-sépare les caractères chiffrés en splittant sur le tiret
    for i in c.split("-"):
        # On les déchiffre avec l'équation présentée dans le CM2
        m.append(chars[pow(int(i), d, n)])
    # Et on re-colle le message
    return "".join(m)


key_pair = generate_key_pair()
cipher = encrypt("Hello world!", key_pair["public"], key_pair["modulus"])
print("Message chiffré: ", cipher)
decrypted_message = decrypt(cipher, key_pair["private"], key_pair["modulus"])
print("Message déchiffré: ", decrypted_message)
