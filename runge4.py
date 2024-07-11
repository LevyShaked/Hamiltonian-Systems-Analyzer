import numpy as np

def f_new_cord(ode_f, coord, time, dt): # 4 vectors evaluation. returns follow coord.
    F1 = ode_f(coord, time)
    F2 = ode_f(coord+(dt/2)*F1, (time+(dt/2)))
    F3 = ode_f(coord+(dt/2)*F2, time+dt/2)
    F4 = ode_f(coord+(dt)*F3, time+dt)
    new_coord = coord+(dt/6)*(F1+2*F2+2*F3+F4)
    return new_coord

def f_ode(coord, time, mass, force, x_amount, p_amount): # euler differential solver of hamiltons eq. 
    m = mass
    x = coord[0:x_amount*p_amount]
    p = coord[x_amount*p_amount:]
    t = time*np.ones(shape=x.shape)
    velocity = coord[x_amount*p_amount:]
    from numpy import (
        abs, arccos, arccosh, arcsin, arcsinh, arctan, arctan2,arctanh, cos, cosh, sin, sinh, exp, log, log10, sqrt, sign, eye)
    coord_deriv =  np.concatenate((velocity, np.array(eval(force))/m), axis=0)
    return coord_deriv