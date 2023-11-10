import sympy as sym
import numpy as np
import sympy.physics.mechanics as me
from sympy.abc import t

def Vee4(E):
    val = sym.Matrix([[0]]*6)
    val[:3,0] = E[:3,3]
    val[3,0] = E[2,1]
    val[4,0] = E[0,2]
    val[5,0] = E[1,0]
    return val
    
def Vee(S):
    return sym.Matrix([S[2,1],S[0,2],S[1,0]])

def Wedge4(V):
    val = sym.Matrix([[0]*4]*4)
    val[:3,3] = V[:3,0]   
    val[0,1] = -V[-1]
    val[1,0] = V[-1]
    val[2,0] = -V[-2]
    val[0,2] = V[-2]
    val[1,2] = -V[-3]
    val[2,1] = V[-3]
    return val

def Wedge(V):
    val = sym.Matrix([[0]*3]*3)
    val[0,1] = -V[2]
    val[1,0] = V[2]
    val[2,0] = -V[1]
    val[0,2] = V[1]
    val[1,2] = -V[0]
    val[2,1] = V[0]
    return val

def partial_wrt_t(expr,q):
    qs = len(q)
    qd = q.diff(t)
    # insert  dummy variables
    U = sym.Matrix(sym.symbols(f'u_:{qs*2}'))
    l = dict(zip([*q,*qd],U))
    expr = me.msubs(expr,l)
    return expr.diff(t)

def trigsimp(expr):
        return sym.trigsimp(sym.powsimp(sym.cancel(sym.expand(expr)))) 

def linearise_matrix(M,x,x_f):
    # reverse order of states to ensure velocities are subbed first
    x_subs = {x[i]:x_f[i] for i in range(len(x))}

    # get the value of M at the fixed point
    M_f = me.msubs(M,x_subs)

    # add a gradient term for each state about the fixed point
    
    for i,xi in enumerate(x):
        M_f += me.msubs(M.diff(xi),x_subs)*(xi-x_f[i])
    return M_f

def extract_eigen_value_data(evals,evecs,margin=1e-9,sortby=None):       
    # get unique eigen values
    unique = []
    unique_vecs = []
    for idx,val in enumerate(evals):
        if np.iscomplex(val):
            # check the complex conjugate is not already in the list
            if not any(np.isclose(np.conj(val),unique)):
                unique.append(val)
                unique_vecs.append(evecs[:,idx])
        else:
            # and real poles straight away
            unique.append(val)
            unique_vecs.append(evecs[:,idx].tolist())

    # Generate data
    real = np.real(unique)
    imag = np.imag(unique)
    F = np.where(np.iscomplex(unique),np.abs(unique)/(2*np.pi),0)
    D = np.where(np.iscomplex(unique),np.cos(np.angle(unique)),np.NaN)
    S = np.max(real)<=margin

    # got order to be sorted in
    if sortby == 'F':
        ind = np.argsort(F)
    elif sortby == 'D':
        ind = np.argsort(D)
    else:
        ind = range(len(unique)) 

    # place data in a dict and sort
    res = []
    Mode = 0
    for i in ind:
        res_dict = {}
        res_dict['Real'] = real[i]
        res_dict['Imag'] = imag[i]
        res_dict['Frequency'] = F[i]
        res_dict['Damping'] = D[i]
        res_dict['Stable'] = S
        res_dict['Eigen Vector'] = unique_vecs[i]
        res_dict['Mode'] = Mode
        Mode += 1
        res.append(res_dict)

    return res
