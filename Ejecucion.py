lista_productos=[]
azucar=["azucar",800,87]
yerba=["yerba",2600,43]
fideo=["fideo",1200,64]
arroz=["arroz",1600,38]
galleta=["galletas",950,65]
lista_productos.append(azucar)
lista_productos.append(yerba)
lista_productos.append(fideo)
lista_productos.append(arroz)
lista_productos.append(galleta)

opcion=None
#inicio
while opcion!=5:
     
    
 print("Bienvenido 👋:")
 print("Indique la opcion que desea realizar:")
 print("1️⃣ -Abrir la lista de productos:")
 print("2️⃣ -Agregar un nuevo producto a la lista:")
 print("3️⃣ -Eliminar un producto de la lista:")
 print("4️⃣ - Ver que producto esta bajo de stock:")
 print("5️⃣ -Salir de la pagina:")
 producto_nuevo=[]


 opcion=int(input("Ingrese la opcion deseada (1/5):"))
 if opcion==1:
     print("****LISTA DE PRODUCTOS:****")
     for e, i in enumerate(lista_productos):
          print(e,":", i)
 elif opcion==2:
    print("NUEVO PRODUCTO")
    nombre_np=input("Ingrese el nombre::")
    producto_nuevo.append(nombre_np)
    precio_np=float(input("ingrese el precio:"))
    producto_nuevo.append(precio_np)
    stock_np=int(input("Ingrese el stock:"))
    producto_nuevo.append(stock_np)
    lista_productos.append(producto_nuevo)
    print("El nuevo producto ingresado es:", producto_nuevo)
    print("Lista de productos actualizada:", lista_productos)
