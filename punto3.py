#crear un menu de dos opciones
contador=0
productos=[]

print(".......SHOP OF PYTHON.......")
print("*****    Este es el Ménu, selecciona una opción   *******")
print("1. Agregar Productos")
print("2. Mostrar Producto")
print("3. SALIR")

while(contador!=3):
    producto={}
    contador=int(input("------->Digita una opción: "))
    if(contador==1):
        producto['codigo']=input("Ingrese el código del producto: ")
        producto['nombre']=input("Ingrese el nombre del producto: ")
        producto['precio']=input("Ingrese el precio del producto: ")
        productos.append(producto)
        print("Agregando producto")
    elif(contador==2):
        print("Mostrando producto: ")
        print(productos)
    elif(contador==3):
        print("SALIR: ")
        break
    else: 
        print("Opción invalida: ")