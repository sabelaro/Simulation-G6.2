rhoEau = 1000
g = 9.81
def determination_k(m, V, tempos1, p, jusquaquelk, fraction_sec=1000):
    """Fonction permettant de calculer la valeur de k en introduisant la masse et le volume
    lors de la descente,
    un tuple (temps, position) déterminé par la simulation,
    p, une valeur donnant la précision du calcul,
    jusquaquelk : déterminer jusqu'à quel valeur de k on va tester,
    fraction_sec : valeur pour la précision du calcul"""
    klol = []
    c = 1/fraction_sec
    temps = []
    while c < jusquaquelk :
        acc_I = -g + (rhoEau * g * V / m)
        a = acc_I
        v = 0
        x = 0
        t = 0
        vit = [0]
        pos = [0]
        tem = [0]
        acc = [acc_I]
        while x >= -2:
            t += 1 / fraction_sec
            v += a * 1 / fraction_sec
            a = acc_I - c / m * v
            x += v * 1 / fraction_sec
            acc.append(a)
            vit.append(v)
            pos.append(x)
            tem.append(t)
            """print(t, x)"""
            print(c)

            if round(t, p) == round(tempos1[0], p)  :
                temps.append(t)
        """print(temps)"""
        if temps != [] and round(tempos1[1], p)-10**(-p) <= round(pos[tem.index(temps[0])], p) <= round(tempos1[1], p)+10**(-p) :
            klol.append(c)
        temps = []
        c += 1/fraction_sec
    k = (max(klol)+min(klol))/2
    return k

print(determination_k(1.174, 0.001, (2.355, -1.631), 2, 2, 100))