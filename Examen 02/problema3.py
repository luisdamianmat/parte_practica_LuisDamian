"""Reglas:
- Crear un diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Mostrar en pantalla sólo los values del diccionario y aumentar en 10 solo la edad
- Agregar un key adicional con el nombre de “profesion” y un valor para este key
nuevo.
- Eliminar el key dni y mostrar el nuevo diccionario."""
#CORREGIDO
diccionario = {}

diccionario['nombre'] = input('Nombre de la persona: ')
diccionario['apellidos'] = (input('Apellido de la persona: '))
diccionario['edad'] = int(input('Edad: '))
diccionario['dni'] = int(input('DNI: '))
diccionario['edad']=diccionario['edad']+10

print(diccionario.values())

diccionario['profesion'] = input('Profesion de la persona: ')

print(diccionario)

del diccionario['dni']
print(diccionario)
