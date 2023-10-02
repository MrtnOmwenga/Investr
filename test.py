import numpy as np

def black_scholes_call(S, X, T, r, sigma):
    d1 = (np.log(S / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    N_d1 = 0.5 * (1 + np.math.erf(d1 / np.sqrt(2)))
    N_d2 = 0.5 * (1 + np.math.erf(d2 / np.sqrt(2)))
    
    call_price = S * N_d1 - X * np.exp(-r * T) * N_d2
    return call_price


def black_scholes_put(S, X, T, r, sigma):
    d1 = (np.log(S / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    N_minus_d1 = 0.5 * (1 - np.math.erf(d1 / np.sqrt(2)))
    N_minus_d2 = 0.5 * (1 - np.math.erf(d2 / np.sqrt(2)))
    
    put_price = X * np.exp(-r * T) * N_minus_d2 - S * N_minus_d1
    return put_price

print(black_scholes_put(10, 105, 0.5, 0.05, 0.2))
print(black_scholes_call(10, 105, 0.5, 0.05, 0.2))
