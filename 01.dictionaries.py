# Las listas son estructuras similares a las listas o arreglos, pero se accede a sus elementos mediante la llave y no su índice.
# Ejemplo:

first_dict = {
  "name": "Alice",
  "position": "Fullstack Developer",
  "skills": ["Python", "Git", "HTML","CSS","Javascript"]
}

# print(first_dict) 

# Accedemos a los elementos mediante la llave o el método .get():

# print(first_dict['skills'])
# print(first_dict.get("skills"))

# Los diccionarios tienen el tipo: "<class 'dict'>"

# print(type(first_dict))

# Podemos obtener todas las llaves con el método .keys()
# print(first_dict.keys())

# Los diccionarios pueden agregar nuevos elementos
  
# first_dict["dream"] = "Save the world with code"

# print(first_dict)

# Podemos ver todos los valores con el método .values()

# print(first_dict.values())

# Atención con el método .items(). Este método crea una vista que se actualiza cuando el diccionario cambia. 

# print(first_dict.items())

# Al igual que con las listas, podemos usar la estructura de control if para ver si existe cierta llave:

# if "position" in first_dict:
#   print("El diccionario sí tiene 'position'")

# Podemos actualizar los valores de una llave

# first_dict['position'] = "Sr. Fullstack developer"
# print(first_dict)

# Podemos hacer lo mismo utilizando el método .update()
# Este método recibe un diccionario

# first_dict.update({"position": "Sr. Fullstack developer"})
# print(first_dict)

# Si la llave no existe la agrega

# first_dict.update({"hobbies": ["Kill zombies and vampires", "plants", "sports"]})
# print(first_dict)

# Para remover una llave tenemos el método .pop("llave")

# first_dict.pop("position")
# print(first_dict)

# Además tenemos la palabra clave del

# del first_dict["position"]
# print(first_dict)

# del puede borrar todo el objeto

# del first_dict
# print(first_dict)

# Podemos limpiar (borrar el contenido) con el método .clear()

# first_dict.clear()
# print(first_dict)

# for key in first_dict:
#   print(key)

# for key in first_dict:
#   print(first_dict[key])

# for value in first_dict.values():
#   print(value)

# for key, value in first_dict.items():
#   print(key,":",value)