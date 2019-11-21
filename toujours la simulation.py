"""
Programme de simulation du groupe 6.2 danns le cadre du projet "Into the abyss", projet BA1 Polytechnique ULB
Le programme reçoit en entrée :
m : La masse initiale du bathyscaphe
V : Le volume initial du bathyscaphe
k : Le coefficient lié aux frottements et à la force de trainée
Vf: Le volume finale du bathyscaphe
mf: La masse finale du bathyscaphe
fraction_sec : plus cette valeur est grande, plus le calcul est précis :
1/fraction_sec : cette valeur est le temps infinitésimale "dt"
"""
import matplotlib.pyplot as plt
rhoEau = 1000
g = 9.81
def enclenchement_actionneur(m, V, c, Vf, mf, fraction_sec):
    profondeurs_proches_de_8 = []
    acc_I = -g + (rhoEau * g * V / m)
    a = acc_I
    v = 0
    x = 0
    t = 0
    vit = [0]
    pos = [0]
    tem = [0]
    acc = [acc_I]
    while x >= -8 :
        t += 1/fraction_sec
        v += a * 1/fraction_sec
        a = -g + (rhoEau * g * V / m) - c/m * v
        x += v * 1/fraction_sec
        acc.append(a)
        vit.append(v)
        pos.append(x)
        tem.append(t)
    for j in range(len(tem)) :
        a2 = acc[j]
        v2 = vit[j]
        x2 = pos[j]
        t2 = tem[j]
        while v2 < 0 and x2 > -8:
            t2 += 1 / fraction_sec
            v2 += a2 * 1 / fraction_sec
            a2 = -g +(rhoEau*g*Vf/mf) - c / mf * v2
            x2 += v2 * 1 / fraction_sec

        if -8 < x2 < -8 + 0.01 :
            profondeurs_proches_de_8.append((x2,j))
    if profondeurs_proches_de_8 != [] :
        indice_temps = profondeurs_proches_de_8.index(min(profondeurs_proches_de_8))
        indice = profondeurs_proches_de_8[indice_temps][1]
    else :
        indice = 0
    return indice, tem[indice], pos[indice], vit[indice], acc[indice]



def simulation(m, V, c, Vf, mf, fraction_sec, indice):
    acc_I = -g + (rhoEau * g * V / m)
    a = acc_I
    v = 0
    x = 0
    t = 0
    acc = [acc_I]
    vit = [0]
    pos = [0]
    tem = [0]
    i = 0
    while i < indice :
        t += 1/fraction_sec
        v += a * 1/fraction_sec
        a = acc_I - c/m * v
        x += v * 1/fraction_sec
        i += 1
        acc.append(a)
        vit.append(v)
        pos.append(x)
        tem.append(t)
    acc_8 = -g + (rhoEau*g*Vf/mf)
    while x <= 0 and x > -8 :
        t += 1/fraction_sec
        v += a * 1/fraction_sec
        a = acc_8 - c/mf * v
        x += v * 1/fraction_sec
        acc.append(a)
        vit.append(v)
        pos.append(x)
        tem.append(t)

    plt.subplot(222)
    plt.grid(True)
    plt.xlabel("temps(s)")
    plt.ylabel("position(m)")
    plt.plot(tem, pos)
    plt.subplot(221)
    plt.grid(True)
    plt.xlabel("position(m)")
    plt.ylabel("vitesse(m/s)")
    plt.plot(pos, vit)
    plt.subplot(212)
    plt.grid(True)
    plt.xlabel("vitesse(m/s)")
    plt.ylabel("acceleration(m/s²)")
    plt.plot(pos, acc)



def bathyscaphe(m, V, k, Vf, mf, fraction_sec=1000) :
    valeurs_enclenchement = enclenchement_actionneur(m, V, k, Vf, mf, fraction_sec)[:]
    print(valeurs_enclenchement)
    indice = valeurs_enclenchement[0]
    simulation(m, V, k, Vf, mf, fraction_sec, indice)
    print("Hey !, psst, tu ferais mieux de déclencheur l'actionneur à cette profondeur :", valeurs_enclenchement[2],"m")
    print("Hey !, psst, tu ferais mieux de déclencheur l'actionneur à ce timing :", valeurs_enclenchement[1], "s")


bathyscaphe(1.773, 0.0015, 2, 0.0015, 1.773, 1000)

plt.show()
