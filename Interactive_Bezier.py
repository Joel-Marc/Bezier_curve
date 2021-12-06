import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

t = sp.symbols('t')


def fact(x): return x*fact(x-1) if x > 1 else 1


def PB_Curve(n, pt):
    P_y = P_x = 0
    for i in range(n):
        P_x += (ber_pol(n-1, i)*pt[n-i-1][0])
        P_y += (ber_pol(n-1, i)*pt[n-i-1][1])
    return [P_x, P_y]


def ber_pol(n, i):
    global t
    ft = (fact(n)/(fact(i)*fact(n-i)))
    return ft * ((1-t)**(n-i))*(t**i)


x = np.arange(0, 10)
y = x**2

fig = plt.figure()
ax = fig.add_subplot(111)
# ax.plot(x, y)

z = []
fin = []


def onclick(event): # Gets the points for each sub curve and stores it as List of Lists in the variable fin 
    global ix, iy, z, fin, coords
    ix, iy = event.xdata, event.ydata
    print('x = {}, y ={}'.format(ix, iy))
    if ix > 0.9 and iy > 0.9: # Clicking any point over (0.9,0.9) ends getting points for that sub curve
        fin.append(z)
        z = []
        return coords

    coords = [ix, iy]
    z.append([ix, iy])
    return coords


for i in range(0, 1):
    cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()

print(z)
fig.canvas.mpl_disconnect(cid)

# CUBIC BEZIER CURVE

for z in fin:   # The Sub curves are constructed individually
    fin = PB_Curve(len(z), z)
    # print(fin[0].subs(t, i))
    # print(fin[1].subs(t, i))
    x = []
    y = []
    for i in np.linspace(0, 1, 501):
        x.append(fin[0].subs(t, i))
        y.append(fin[1].subs(t, i))

    #print(x, y)

    ox = [hm[0] for hm in z]
    oy = [hm[1] for hm in z]
    # print(ox,oy)
    plt.plot(ox, oy, 'ro-')
    plt.plot(x, y, 'b-')

plt.show()
