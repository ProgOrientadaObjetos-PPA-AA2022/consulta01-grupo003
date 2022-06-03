categorias = [['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M']]
popurri = {0: '', 1: '0', 2: '00', 3: '000', 4: '01', 5: '1', 6: '10', 7: '100', 8: '1000', 9: '02'}


def romanizardig(digito, categoria):
    logica = categorias[categoria]
    respuesta = ''
    dig_a_procesar = [x for x in popurri[int(digito)]]
    for x in dig_a_procesar:
        respuesta = respuesta + logica[int(x)]
    return respuesta


class Romano(object):
    def __init__(self, numero):
        self.number = str(numero)
        self.largo = len(self.number)

    def romanizar(self):
        respuestafinal = ''
        for x in range(0, self.largo):
            respuestafinal = respuestafinal + romanizardig(self.number[x], self.largo - x - 1)
        return respuestafinal


Prueba = Romano(14)
print(Prueba.romanizar())
