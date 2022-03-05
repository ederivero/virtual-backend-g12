from camelcase import CamelCase
# CamelCase 0.2
# CamelCase 0.5
# CamelCase(words=['mundo','del'])

instanciaCC = CamelCase('mundo','del')

texto = 'Bienvenidos al mundo del backend'

print(instanciaCC.hump(texto))

# TODO: hacer lo mismo que el camelcase sin la libreria
