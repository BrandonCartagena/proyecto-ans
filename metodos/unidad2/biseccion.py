import sympy as sp
from sympy.abc import x

aprox_actual, aprox_anterior = sp.symbols('aprox_actual aprox_anterior')
error_aproximado = ((aprox_actual - aprox_anterior) / aprox_actual) * 100

def biseccion(funcion, x1, x2, cifras_significativas):
    f_x = sp.sympify(funcion.strip().replace('^','**').replace('e', 'E'))

    Es = 0.5 * (10 ** (2 - cifras_significativas))
    Ea = 100

    rows = []

    iteracion = 0

    while Ea > Es:
        iteracion += 1

        xr = (x1 + x2) / 2

        f_x1 = f_x.evalf(subs={x:x1})
        f_xr = f_x.evalf(subs={x:xr})

        if iteracion >= 2: Ea = abs(error_aproximado.evalf(subs={aprox_actual:xr, aprox_anterior:xr_anterior}))

        rows.append({
            'iteracion': iteracion, 
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

    return {
        'rows': rows,
        'raiz': xr,
        'error': round(Ea, cifras_significativas)
    }