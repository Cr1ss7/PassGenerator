import random
import string
import colors as c

CONST_CARACTERES = string.ascii_letters + string.digits + string.punctuation

try:
    #Nombre de el archivo
    nombre = input(c.BOLD+"[-] Digite el nombre de el archivo donde guardar las constraseñas generadas:"+c.ENDC+c.WARNING+"\n[+] (Si lo deja en blanco el programa le pongra un nombre por defecto)"+c.ENDC+c.OKGREEN+"\n==>\t"+c.ENDC)
    nombre = nombre if nombre != "" else "Passwords"

    cantidad = int(input(c.BOLD+"[-] Dijite la cantidad de contraseñas que necesita:\n"+c.ENDC+c.OKGREEN+"==>\t"+c.ENDC))
    longitud = int(input(c.BOLD+"[-] Dijite la longitud de las contraseñas:\n"+c.ENDC+c.OKGREEN+"==>\t"+c.ENDC))
    
    #Generacion de las contraseñas
    with open(nombre+".txt", "w") as file_object:
        for i in range(cantidad):
            password = "".join(random.choice(CONST_CARACTERES) for x in range(longitud))
            file_object.write("Contraseña No "+str(i+1)+":\n")
            file_object.write("\t"+password)
            file_object.write("\n\n")
    
    print(c.OKGREEN+"[-] Generación de constraseñas completada!"+c.ENDC)

except KeyboardInterrupt:
    print("\nSaliendo de el programa...\n")
except Exception:
    print("\nDijite un valor valido...\n")