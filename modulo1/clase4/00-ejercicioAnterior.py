paises = {
    "Venezuela": "Caracas",
    "Colombia": "Bogota",
    "Peru": "Lima",
    "Argentina": "Buenos Aires"
}

# La consiga dictaba de que el usuario meta por terminal el pais, y que le devuelva la capital del mismo

textoDelInput = "Ingrese el nombre del pais, inicializando con mayuscula: "

pais = input(textoDelInput) # Si aca escribis Argentina

print(paises[pais]) # Es como que aca hagas print(paises["Argentina"])