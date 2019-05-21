import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b):
    return a*x + b


n=np.array([9,9,9,8,7])
#Hier Werte der Beschleunigungsspannung
plot_ub =  1/(np.array([250, 300, 350, 400, 450]))

params = np.zeros(5)
x_line = np.linspace(-20,35)


for i in range(0, 5):
    werte = csv_read("csv/elektrisch" + str(i) +  ".csv")

    xdata = np.zeros(n[i])
    ydata = np.zeros(n[i])

    for j in range(0, n[i]):
        xdata[j] = float(werte[j+1][0])
        ydata[j] = float(werte[j+1][1])

    x_line = np.linspace(np.amin(xdata), np.amax(xdata))
    plt.figure(i)
    plt.plot(xdata, ydata, "r.", label="Messwerte")
    popt, pcov = curve_fit(func, xdata, ydata)
    params[i] = popt[0]
    plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")
    #a_i sind D/U_d
    #b_i sind nur Korrekturkoeffizienten
    print("a" + str(i) + " = " + str(popt[0]) + "+/-" + str(np.sqrt(pcov[0,0])))
    print("b" + str(i) + " = " + str(popt[1]) + "+/-" + str(np.sqrt(pcov[1,1])))

    plt.xlabel(r"$U_d$ / V")
    plt.ylabel(r"$D$ / mm")
    plt.legend()
    plt.tight_layout()
    plt.savefig("build/plot_elektrisch_" + str(i) + ".pdf")

x_line2 = np.linspace(np.amin(plot_ub), np.amax(plot_ub))
plt.figure(5)
plt.plot(plot_ub, params, "r.", label="Messwerte")
popt, pcov = curve_fit(func, plot_ub, params) 

print("------------------------------------")
#a ist die Steigung, b ein Korrekturkoeffizient
print("a6 = " + str(popt[0]) + "+/-" + str(np.sqrt(pcov[0,0])))
print("b6 = " + str(popt[1]) + "+/-" + str(np.sqrt(pcov[1,1])))

plt.plot(x_line2, func(x_line2, *popt), "b-", label="Fit")
plt.xlabel(r"$\frac{1}{U_B}$ / $\frac{1}{\symup{V}}$")
plt.ylabel(r"$\frac{D}{U_d}$ / $\frac{\symup{mm}}{\symup{V}}$")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot_ub.pdf")