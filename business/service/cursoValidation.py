from infra.error.dataException import DataException
import re

class CursoValidation:
    def __init__(self):
        pass

    def validate_nome(self, nome):
        if not nome:
            raise DataException("Entrada inválida. O nome do curso não pode estar vazio!")
        if len(nome) > 100:
            raise DataException("Entrada inválida. O nome do curso não pode ultrapassar 100 caracteres!")
        if any(char.isdigit() for char in nome):
            raise DataException("Entrada inválida. O nome do curso não pode conter números!")

    def validate_carga_horaria_total(self, carga):
        if carga is None:
            raise DataException("Entrada inválida. A carga horária total não pode ser nula!")
        if not isinstance(carga, int):
            raise DataException("Entrada inválida. A carga horária total deve ser um número inteiro!")
        if carga <= 0:
            raise DataException("Entrada inválida. A carga horária total deve ser maior que zero!")

    def validate_codigo(self, codigo):
        if not codigo:
            raise DataException("Entrada inválida. O código do curso não pode estar vazio!")
        if not re.match(r'^[/d]{2,10}$', codigo):
            raise DataException("Entrada inválida. O código do curso deve ter entre 2 e 10 caracteres numéricos!")

    def validate_area(self, area):
        if not area:
            raise DataException("Entrada inválida. A área do curso não pode estar vazia!")
        if len(area) > 50:
            raise DataException("Entrada inválida. A área do curso não pode ultrapassar 50 caracteres!")

    def validate_periodos(self, periodos):
        if periodos is None:
            raise DataException("Entrada inválida. A quantidade de períodos não pode ser nula!")
        if not isinstance(periodos, int):
            raise DataException("Entrada inválida. A quantidade de períodos deve ser um número inteiro!")
        if periodos <= 0:
            raise DataException("Entrada inválida. A quantidade de períodos deve ser maior que zero!")

    def validate_carga_horaria_optativa(self, optativa):
        if optativa is None:
            raise DataException("Entrada inválida. A carga horária optativa não pode ser nula!")
        if not isinstance(optativa, int):
            raise DataException("Entrada inválida. A carga horária optativa deve ser um número inteiro!")
        if optativa < 0:
            raise DataException("Entrada inválida. A carga horária optativa não pode ser negativa!")

    def validate_carga_horaria_minima(self, minima):
        if minima is None:
            raise DataException("Entrada inválida. A carga horária mínima não pode ser nula!")
        if not isinstance(minima, int):
            raise DataException("Entrada inválida. A carga horária mínima deve ser um número inteiro!")
        if minima < 0:
            raise DataException("Entrada inválida. A carga horária mínima não pode ser negativa!")

    def validate_carga_horaria_maxima(self, maxima):
        if maxima is None:
            raise DataException("Entrada inválida. A carga horária máxima não pode ser nula!")
        if not isinstance(maxima, int):
            raise DataException("Entrada inválida. A carga horária máxima deve ser um número inteiro!")
        if maxima < 0:
            raise DataException("Entrada inválida. A carga horária máxima não pode ser negativa!")

    def validate_qtd_favoritos(self, qtd):
        if qtd is None:
            raise DataException("Entrada inválida. A quantidade de favoritos não pode ser nula!")
        if not isinstance(qtd, int):
            raise DataException("Entrada inválida. A quantidade de favoritos deve ser um número inteiro!")
        if qtd < 0:
            raise DataException("Entrada inválida. A quantidade de favoritos não pode ser negativa!")
