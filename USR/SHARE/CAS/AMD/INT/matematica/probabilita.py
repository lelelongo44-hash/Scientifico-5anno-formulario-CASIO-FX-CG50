print()
 GEOMETRIA ANALITICA
# ==========================================

# Distanza tra due punti
def distanza(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Punto medio
def punto_medio(x1, y1, x2, y2):
    return ((x1 + x2)/2, (y1 + y2)/2)

# Coefficiente angolare
def coeff_angolare(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# Intercetta q della retta y = mx + q
def intercetta_q(x, y, m):
    return y - m*x

# Retta passante per due punti
def retta_due_punti(x1, y1, x2, y2):
    m = coeff_angolare(x1, y1, x2, y2)
    q = intercetta_q(x1, y1, m)
    return m, q

# Verifica parallelismo
def parallele(m1, m2):
    return m1 == m2

# Verifica perpendicolarità
def perpendicolari(m1, m2):
    return m1 * m2 == -1

# ==========================================
# CIRCONFERENZA
# ==========================================

# Raggio conoscendo centro e un punto
def raggio_circonferenza(xc, yc, xp, yp):
    return distanza(xc, yc, xp, yp)

# ==========================================
# PARABOLA
# y = ax² + bx + c
# ==========================================

def delta(a, b, c):
    return b**2 - 4*a*c

def vertice(a, b, c):
    xv = -b / (2*a)
    yv = -delta(a, b, c) / (4*a)
    return (xv, yv)

# ==========================================
# CALCOLO COMBINATORIO
# ==========================================

def fatt(n):
    return factorial(n)

def disposizioni(n, k):
    return perm(n, k)

def permutazioni(n):
    return factorial(n)

def combinazioni(n, k):
    return comb(n, k)

def permutazioni_ripetizione(n, *gruppi):
    den = 1
    for g in gruppi:
        den *= factorial(g)
    return factorial(n) // den

# ==========================================
# PROBABILITA'
# ==========================================

def probabilita(favorevoli, possibili):
    return favorevoli / possibili

def contrario(p):
    return 1 - p

def intersezione(pa, pb):
    return pa * pb

def unione(pa, pb, pab):
    return pa + pb - pab

def condizionata(pab, pb):
    return pab / pb

def bayes(pb_a, pa, pb):
    return (pb_a * pa) / pb

# ==========================================
# ESEMPI DI UTILIZZO
# ==========================================

if __name__ == "__main__":

    print("Distanza:", distanza(0, 0, 3, 4))
    print("Punto medio:", punto_medio(1, 2, 5, 6))

    m, q = retta_due_punti(1, 2, 3, 6)
    print("Retta: y =", m, "x +", q)

    print("Vertice parabola:", vertice(1, -4, 3))

    print("C(10,3) =", combinazioni(10, 3))
    print("D(10,3) =", disposizioni(10, 3))

    print("Probabilità =", probabilita(3, 10))
