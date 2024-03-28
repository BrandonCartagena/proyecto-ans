import sympy as sp
from sympy.abc import x
import matplotlib.pyplot as plt
import io
import urllib, base64

aprox_actual, aprox_anterior = sp.symbols('aprox_actual aprox_anterior')
error_aproximado = ((aprox_actual - aprox_anterior) / aprox_actual) * 100

def secante(funcion, x1, x2, cifras_significativas):
	f_x = sp.sympify(funcion.strip().replace('^','**').replace('sen', 'sin').replace('e', 'E'))

	Es = 0.5 * (10 ** (2 - cifras_significativas))
	Ea = 100

	rows = []

	iteracion = 0

	f_x1 = f_x.evalf(subs={x:x1})
	f_x2 = f_x.evalf(subs={x:x2})

	if f_x1 * f_x2 < 0:
		while Ea > Es:
			iteracion += 1

			xr = x2 - (f_x2 * ((x2 - x1) / (f_x2 - f_x1)))

			f_xr = f_x.evalf(subs={x:xr})

			if iteracion >= 2: Ea = abs(error_aproximado.evalf(subs={aprox_actual:xr, aprox_anterior:x2}))

			rows.append({
				'iteracion': iteracion, 
				'x1': x1, 
				'x2': x2, 
				'f_x1': f_x1,
				'f_x2': f_x2,
				'xr': xr, 
				'f_xr': f_xr, 
				'ea': '-' if iteracion == 1 else round(Ea, cifras_significativas)
			})

			x1 = x2
			x2 = xr

			f_x1 = f_x.evalf(subs={x:x1})
			f_x2 = f_x.evalf(subs={x:x2})

		sp.plot(f_x, ylim=(-20, 20))
		fig = plt.gcf()
		buf = io.BytesIO()
		fig.savefig(buf,format='png')
		buf.seek(0)
		uri = urllib.parse.quote(base64.b64encode(buf.read()))

		return {
			'f_x': sp.latex(f_x),
			'grafica': uri,
			'rows': rows,
			'raiz': xr,
			'error': round(Ea, cifras_significativas)
		}