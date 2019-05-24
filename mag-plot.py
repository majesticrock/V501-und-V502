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


n=np.array([9,8])
#Hier Werte der Beschleunigungsspannung
ub = (np.array([250, 400]))

windungen = 20
spulenradius = 0.282 #m
L = 175 * 10**(-3) #Wirkungsbereich des B-Feldes in mm, Donna sagt 143mm
mu0 = 4 * np.pi * 10**(-7)

params = np.zeros(2)
x_line = np.linspace(-20,35)


for i in range(0, 2):
    if(i==0):
        werte = csv_read("csv/magnet250v.csv")
    else:
        werte = csv_read("csv/magnet400v.csv")

    xdata = np.zeros(n[i])
    ydata = np.zeros(n[i])

    for j in range(0, n[i]):
        xdata[j] = mu0 * (8/np.sqrt(125)) * windungen * (1/spulenradius) * float(werte[j+1][0]) * 10**(-3)
        ydata[j] = float(werte[j+1][1]) * 10**(-3) / (L**2 + (float(werte[j+1][1]) * 10**(-3))**2)

    x_line = np.linspace(np.amin(xdata), np.amax(xdata))
    plt.figure(i)
    plt.plot(xdata, ydata, "r.", label="Messwerte")
    popt, pcov = curve_fit(func, xdata, ydata)
    params[i] = popt[0]
    plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")
    #a_i sind D/U_d
    #b_i sind nur Korrekturkoeffizienten
    print("a" + str(i + 1) + " = " + str(popt[0]) + "+/-" + str(np.sqrt(pcov[0,0])))
    print("b" + str(i + 1) + " = " + str(popt[1]) + "+/-" + str(np.sqrt(pcov[1,1])))

    plt.xlabel(r"$B$ / $10^{-3}$ T")
    plt.ylabel(r"$\frac{D}{D^2 + L^2}$ / m")
    plt.legend()
    plt.tight_layout()
    plt.savefig("build/plot_magnetisch_" + str(i) + ".pdf")

with open("build/mag.check", "w") as f:
    f.write("Nur eine Überprüfungsdatei!")
