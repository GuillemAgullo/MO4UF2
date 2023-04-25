import xmltodict
import random



#CARREGUEM ELS ARXIUS:
llista_enemy = ["C:\\Users\\guima\\Documents\\MO4UF2\\enemy.xml", "C:\\Users\\guima\\Documents\\MO4UF2\\enemy1.xml", "C:\\Users\\guima\\Documents\\MO4UF2\\enemy2.xml","C:\\Users\\guima\\Documents\\MO4UF2\\enemy3.xml"]
eleccio_llista = random.choice(llista_enemy)

with open(eleccio_llista, "r") as f:
    xml_string = f.read()
    #CONVERTIR EL ARCHIVO XML A UN DICCIONARIO PYTHON
    enemy_dict = xmltodict.parse(xml_string)

#DATOS
nom = enemy_dict["enemy"]["name"]
desc = enemy_dict["enemy"]["description"]
vida = int(enemy_dict["enemy"]["hp"])
dmg = int(enemy_dict["enemy"]["dmg"])
vida_player = 7

print("Encontraste a un enemigo. Si me hago entender?")
print("El enemigo se iso yamar: "+str(nom))
print("Su descripsion es la sigiente :"+str(desc))
print("Su salud màxima és: "+str(vida))
print("Su daño es de: "+str(dmg))



fideljoc:bool = False

while not(fideljoc):
    print("\n Escribe ataca para atacar:")
    atac = input(">>>")
    if atac == "ataca":
        random_number = random.randint(1,5)
        print("Te dispusiste a aserle "+ str(random_number) +" de lindos puntos de daño papurrinchi!!!")
        vida = vida - random_number
        random_dmg = random.randint(0,dmg)
        print("Però él también aprovechó parse! Te iso "+ str(random_dmg) +" de lastimasión.")
    else: 
        print("ayayay papurri no pusiste bien la simple palabra.")
        continue

    if vida <= 0:
        print("ganaste bendito!!!!")
        fideljoc = True
    elif vida_player <= 0:
        print("Perdiste. Mala suerte papu")
        fideljoc = True

