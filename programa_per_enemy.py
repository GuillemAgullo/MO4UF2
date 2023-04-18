from xml.dom import minidom
import random

doc = minidom.parse("C:\\Users\\guima\\Documents\\MO4UF2\\enemy.xml")

#DATOS
nom = doc.getElementsByTagName("name")[0].firstChild.nodeValue
desc = doc.getElementsByTagName("description")[0].firstChild.nodeValue
vida = int(doc.getElementsByTagName("hp")[0].firstChild.nodeValue)
dmg = int(doc.getElementsByTagName("dmg")[0].firstChild.nodeValue)
vida_player = 7

print("Encontraste a un enemigo. Si me hago entender?")
print("El enemigo se iso yamar: "+str(nom))
print("Su descripsion es la sigiente :"+str(desc))
print("Su salud màxima és: "+str(vida))
print("Su daño es de: "+str(dmg))



fideljoc:bool = False

while fideljoc == False:
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

