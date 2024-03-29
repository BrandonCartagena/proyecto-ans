import sympy as sp
from sympy.abc import x
import matplotlib.pyplot as plt
import io
import urllib, base64

aprox_actual, aprox_anterior = sp.symbols('aprox_actual aprox_anterior')
error_aproximado = ((aprox_actual - aprox_anterior) / aprox_actual) * 100

def biseccion(funcion, x1, x2, cifras_significativas):
    f_x = sp.sympify(funcion.strip().replace('^','**').replace('sen', 'sin').replace('e', 'E'))

    Es = 0.5 * (10 ** (2 - cifras_significativas))
    Ea = 100

    iteraciones = []

    iteracion = 0

    while Ea > Es:
        iteracion += 1

        xr = (x1 + x2) / 2

        f_x1 = f_x.evalf(subs={x:x1})
        f_xr = f_x.evalf(subs={x:xr})

        if iteracion >= 2: Ea = abs(error_aproximado.evalf(subs={aprox_actual:xr, aprox_anterior:xr_anterior}))

        iteraciones.append({
            'n_iteracion': iteracion, 
            'x1': x1, 
            'x2': x2, 
            'xr': xr, 
            'f_x1': f_x1, 
            'f_xr': f_xr, 
            'f_x1_f_xr': f_x1 * f_xr, 
            'ea': '-' if iteracion == 1 else round(Ea, cifras_significativas)
        })
        
        if f_x1 * f_xr == 0: break 
        elif f_x1 * f_xr > 0: x1 = xr
        elif f_x1 * f_xr < 0: x2 = xr

        xr_anterior = xr

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
        'raiz': xr,
        'error': round(Ea, cifras_significativas)
    }