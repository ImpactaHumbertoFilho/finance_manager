#classe para eu salvar minhas exceções personalizadas
class BaseException(Exception):
    """Classe base para todas as exceções personalizadas."""
    def __init__(self, message):
        """Inicializa a exceção com uma mensagem personalizada."""
        # Preciso salvar como um log

        super().__init__(message)
        self.message = message

class UsuarioNaoEncontradoException(BaseException):
    """Erro quando é informado um usuario que não existe exception."""
    pass

class UsuarioJaCadastradoException(BaseException):
    """Erro quando é informado um usuario que já existe exception."""
    pass

class UsuarioInvalidoException(BaseException):
    """Erro quando é informado um usuario inválido exception."""
    pass