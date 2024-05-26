"""2. Crear un programa que nos permita ingresar varias veces distintos correos electronicos y que como salida muestre si el correo ingresado 
es correcto o no. Tener en cuenta que para que el correo sea correcto debe tener un @ y como max dos puntos."""

correo=input("Ingrese su correo: ")

while correo !="0":
    cont_arroba=0
    conta_punto=0
    for letra in correo:
        if letra=="@":
            cont_arroba+=1
        if letra==".":
            conta_punto+=1
    if (cont_arroba==1 and conta_punto>0) and conta_punto<3:
        print("El correo ingresado es correcto")
    else:
        print("el correo ingresado es incorrecto")
    correo=input("Ingrese su correo: ")
    