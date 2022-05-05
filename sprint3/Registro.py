from datetime import date

#07
class Registro:
    def __init__(self, args):
        if len(args) != 5:
            raise ValueError('Dados inválidos')
        self._id = args[0]
        self._nome = args[1]
        self._preco = args[2]
        self._quantidade = args[3]
        try:
            self._criado_em = date.fromisoformat(args[4])
        except ValueError:
            raise ValueError('Data não está no formado aaaa-MM-dd')
        except TypeError:
            raise TypeError('Informar a data no formado aaaa-MM-dd')

    @property
    def produto(self):
        return self._nome

    @produto.setter
    def produto(self, value):
        self._nome = value

#08       
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, value):
        self._preco = value

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, value):
        self._quantidade = value

    @property
    def data(self):
        return self._criado_em.isoformat()

#09
    def comprado_no_dia_mes(self, dia, mes):
        if int(dia) == int(self.data.split('-')[2]) and int(mes) == int(self.data.split('-')[1]):
            return True
        else:
            return False

#10
    def preco_entre(self, minimo, maximo):
        if minimo <= self.preco and self.preco <= maximo:
            return True
        else:
            return False

    def get_tupla(self):
        return (str(self._id), self.produto, str(self.preco), str(self.quantidade), self.data)

    def __str__(self):
        return self.produto + ' ' + self.data

    def __repr__(self):
        msg = 'id:' + str(self._id) + ' => ' + self.produto
        msg = msg + ' data: ' + self.data
        msg = msg + '  preço:' + str(self.preco)
        msg = msg + '  quantidade:' + str(self.quantidade)
        return msg
