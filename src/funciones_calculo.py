import numpy as np

def eficiencia_dbo(DBO_in, DBO_out):
    """
    Calcula la eficiencia del tratamiento de DBO.
    """
    return (DBO_in - DBO_out) / DBO_in

def cumplimiento_norma(DBO_out, limite=50):
    """
    Retorna 1 si cumple la norma, 0 si no cumple.
    """
    return 1 if DBO_out <= limite else 0
