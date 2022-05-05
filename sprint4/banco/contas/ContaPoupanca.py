from banco.contas.Conta import Conta


class ContaPoupanca(Conta):
    """
    Classe representa a conta poupança de uma pessoa.
    Limite padrão da conta: R$ 0,00

    Args:
        Conta (kwargs): Dicionário com dados da conta
    """
    def __init__(self, **kwargs):
        """
        Construtor da classe ContaPoupanca.
        Extrai do dicionário kwargs:
        - Nome
        - CPF
        - Saldo
        """
        super(ContaPoupanca, self).__init__(**kwargs)
        self.limite = kwargs.get('limite', 0)
        self.cpf = kwargs.get('cpf', None)
        if self.cpf is None:
            raise ValueError('CPF inválido')

    def saque(self, valor):
        """
        Método para realizar saque.
        Este método suporta somente números maiores que zero.

        Args:
            valor (float ou int): Valor positivo do saque

        Raises:
            ValueError: Erro ocorre quando é informado valor negativo.
            TypeError: Quando o tipo passado não for inteiro ou float.

        Returns:
            Float: Valor do saque realizado.
        """
        if isinstance(valor, (float, int)):
            if valor > (self.saldo + self.limite):
                raise ValueError('Valor do saque supera seu saldo.')
            self.saldo = self.saldo - valor
            self.extrato.append(('S', valor))
            return valor
        raise TypeError('O valor do saque precisa ser numérico')

    def rendimento_aniversario(self, juros):
        """
        Método simula o rendimento no valor de aniversário.

        Args:
            juros (float ou int): Valor do juros.

        Raises:
            ValueError: Erro ocorre quando é informado um juros maior que 1 e menor que 0.

        Returns:
            Float: Valor do saldo atualizado com os juros.
        """
        if juros >= 0 and juros <= 1:
            self.saldo = self.saldo + (self.saldo * juros)
            return self.saldo
        raise ValueError('Os juros precisam ser entre 0 (0%) e 1 (100%).')

    def __str__(self):
        return f"Conta Poupança:{self.nome}, saldo={self.saldo}"

    def __repr__(self):
        return f"Conta Poupança:{self.nome}, saldo={self.saldo}"
