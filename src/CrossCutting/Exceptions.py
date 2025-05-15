#classe para eu salvar minhas exceções personalizadas
class UsuarioNaoEncontradoException(Exception):
    """Erro quando é informado um usuario que não existe exception."""
    pass

class UsuarioJaCadastradoException(Exception):
    """Erro quando é informado um usuario que já existe exception."""
    pass

class UsuarioInvalidoException(Exception):
    """Erro quando é informado um usuario inválido exception."""
    pass