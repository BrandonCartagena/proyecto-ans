import sympy as sp
from sympy.abc import x
import matplotlib.pyplot as plt
import io
import urllib, base64

aprox_actual, aprox_anterior = sp.symbols('aprox_actual aprox_anterior')
error_aproximado = ((aprox_actual - aprox_anterior) / aprox_actual) * 100

def newton_raphson_modificado(funcion, xi, cifras_significativas):
	f_x = sp.sympify(funcion.strip().replace('^','**').replace('sen', 'sin').replace('e', 'E'))
	f_x_1ra_derivada = f_x.diff(x)
	f_x_2da_derivada = f_x_1ra_derivada.diff(x)

	Es = 0.5 * (10 ** (2 - cifras_significativas))
	Ea = 100

	f_xi = f_x.evalf(subs={x:xi})
	f_xi_1ra_derivada = f_x_1ra_derivada.evalf(subs={x:xi})
	f_xi_2da_derivada = f_x_2da_derivada.evalf(subs={x:xi})

	convergencia = abs((f_xi * f_xi_2da_derivada) / f_xi_1ra_derivada**2) < 1

	iteraciones = []

	iteracion = 0

	if convergencia:
		while Ea > Es:
			iteracion += 1

			xi_anterior = xi

			xi = xi - (f_xi * f_xi_1ra_derivada / ((f_xi_1ra_derivada**2) - f_xi * f_xi_2da_derivada))

			Ea = abs(error_aproximado.evalf(subs={aprox_actual:xi, aprox_anterior:xi_anterior}))

			iteraciones.append({
				'n_iteracion': iteracion,
				'xi': xi_anterior, 
				'f_xi': f_xi, 
				'f_xi_1ra_derivada': f_xi_1ra_derivada,
				'f_xi_2da_derivada': f_xi_2da_derivada,
				'xr': xi, 
				'ea': '-' if iteracion == 1 else round(Ea, cifras_significativas)
			})

			f_xi = f_x.evalf(subs={x:xi})
			f_xi_1ra_derivada = f_x_1ra_derivada.evalf(subs={x:xi})
			f_xi_2da_derivada = f_x_2da_derivada.evalf(subs={x:xi})

		sp.plot(f_x, ylim=(-20, 20))
		fig = plt.gcf()
		buf = io.BytesIO()
		fig.savefig(buf,format='png')
		buf.seek(0)
		uri = urllib.parse.quote(base64.b64encode(buf.read()))

		return {
			'f_x': sp.latex(f_x),
			'grafica': uri,
			'n_iteraciones': iteracion,
			'iteraciones': iteraciones,
			'raiz': xi,
			'error': round(Ea, cifras_significativas)
		}