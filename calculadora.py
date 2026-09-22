from mi_paquete import operaciones
from mi_paquete.utils import mostrar_mensaje
from mi_paquete.operaciones import sumar, restar, dividir, multiplicar
mostrar_mensaje()
print("5 + 3 =", operaciones.sumar(5,3))
print("2 * 7 =", operaciones.multiplicar(2, 7))
print("4 / 5 =", operaciones.dividir(4, 5))
print("4 / 0 =", operaciones.dividir(4, 0))

