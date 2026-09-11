## Una universidad desea saber si un estudiante puede inscribirse a un curso avanzado.
##Para ello, debe cumplir dos condiciones:
##    Haber aprobado el curso introductorio.
##Tener un promedio igual o superior a 3.5.
##Escribe un programa que:
##a) Solicite al usuario si aprobó el curso introductorio (sí o no).
##b) Solicite su promedio.
##c) Evalue la condición y muestre directamente True si puede inscribirse o False
##si no puede.

respuesta = input("¿Aprobaste el curso introductorio? (sí/no): ")
promedio = float(input("Introduce tu promedio: "))
aprobo_introductorio = respuesta.lower() in ("sí", "si")
puede_inscribirse = aprobo_introductorio and (promedio >= 3.5)
print(puede_inscribirse)
