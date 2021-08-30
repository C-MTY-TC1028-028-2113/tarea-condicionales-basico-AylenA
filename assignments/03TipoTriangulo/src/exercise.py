def main():
    x = int(input("Ingresa la medida del lado 1: "))
    y = int(input("Ingresa la medida del lado 2: "))
    z = int(input("Ingresa la medida del lado 3: "))
    #Escribe aquí tu código...
    if(x+y>z)and(y+z>x)and(z+x>y):
        if(x==y and x==z and z==y):
            print("ES UN TRIANGULO EQUILATERO")
        elif(x==y or x==z or z==y):
            print("ES UN TRIANGULO ISOSCELES")
        else:
            print("ES UN TRIANGULO ESCALENO")
    else:
     print("NO ES TRIANGULO")


if __name__=='__main__':
    main()
