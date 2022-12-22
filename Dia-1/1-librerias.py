from camelcase import CamelCase

instancia = CamelCase()

texto = 'hola yo deberia estar camel caseado'

resultado = instancia.hump(texto)

print(resultado)
