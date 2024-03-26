import sympy as sp
from sympy.abc import x

aprox_actual, aprox_anterior = sp.symbols('aprox_actual aprox_anterior')
error_aproximado = ((aprox_actual - aprox_anterior) / aprox_actual) * 100

def falsa_posicion():
	pass