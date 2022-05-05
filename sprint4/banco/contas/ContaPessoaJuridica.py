from banco.contas.Conta import Conta


class ContaPessoaJuridica(Conta):
    """
    Classe representa a conta corrente de um pessoa jurídica.
    Limite padrão da conta: R$ 1500,00

    Args:
        Conta (kwargs): Dicionário com dados da conta
    """
    def __init__(self,  **kwargs):
        super(ContaPessoaJuridica, self).__init__(**kwargs)
        """
        Construtor da classe PessoaJurídica.
        Extrai do dicionário kwargs:
        - Nome
        - CNPJ
        - Limite
        - Saldo
        """
        self.limite = kwargs.get('limite', 1500)
        self.cnpj = kwargs.get('cnpj', None)
        if self.cnpj is None:
            raise ValueError('CNPJ inválido')

    def __str__(self):
        return f"Conta PJ:{self.nome},saldo={self.saldo}"

    def __repr__(self):
        return f"Conta PJ:{self.nome},saldo={self.saldo}"
