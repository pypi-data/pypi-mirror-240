

__all__ = [
    "AuthenticationError",
    "InvalidParameterError",
    "UnknownError"
]


class ProdiaError(Exception):
    pass


class AuthenticationError(ProdiaError):
    pass


class InvalidParameterError(ProdiaError):
    pass


class UnknownError(ProdiaError):
    pass
