print("bienvenidos, ingresa una función: ")
print("1. Presión",'\n'
      "2. Gradiente Presion",'\n'
      "3. Peso del lodo",'\n')
while True: #ciclo condicional para entrar a la calculadora
    s = input("Ingrese formula:")
    if s == "0": break
    if s in ("Presión","Gradiente Presión","presión_hidrostatica"):
        if s == "Presión":
            Fuerza = float(input("Ingrese fuerza:"))
            area =float(input("ingresa el área: "))
            print(Fuerza/area, "psi")
        elif s == "Gradiente Presión":
            mud = float(input("Ingrese peso del lodo:"))
            print(0.052 * mud)
        elif s == "presion hidrostatica":
            mud = float(input("ingresa peso del lodo:"))
            tvd = float(input("Ingresa la TVD: "))
            print(0.052*mud*tvd)        
    else:
        print("dale cero para terminar programa")    
