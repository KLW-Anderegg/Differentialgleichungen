##############################
##### Eingaben ###############
##############################

# Schrittweite
h = 0.1


# DGL x' = f(x,t)
# f(x,t)ist die rechte Seite der expliziten DGL
def f(x, t):
    return x - 2 * t


# Anfangsbedingung
# x(t_0) = x_0
t_0 = 0
x_0 = 0.5

# Intervall [t_0, t_ende]
t_ende = 2


##############################
##### Berechnungen ###########
##############################

# Initialisierung
t = t_0
x = x_0
t_werte = []
x_werte = []

# Berechnungen
while t <= t_ende:
    print("x(", t, ") = ", x)
    t_werte.append(t)
    x_werte.append(x)
    # nächster t-Wert
    t += h
    # Berechnung der neuen x-Werte
    # hier kommt Ihr Code hin!


##############################
##### Plot ###################
##############################
import matplotlib.pyplot as plt

plt.plot(t_werte, x_werte)
plt.xlabel("t")
plt.ylabel("x")
plt.show()
