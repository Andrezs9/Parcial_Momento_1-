monto = int(input("Ingrese el valor de su compra: "))
if monto<50:
    print ("No hay descuento")
elif (monto>=50 and monto<=100):
    descuento=monto*0.05
    total=monto-descuento
    print (f"Su descuento es de ${descuento} y el total a pagar es de ${total}")
elif (monto>100):
    descuento=monto*0.10
    total=monto-descuento
    print (f"Su descuento es de ${descuento} y el total a pagar es de ${total}")
