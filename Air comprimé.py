SECTION = 0.001 #m²
MM_AIR = 0.028965 #g/mol
R = 8.314 # constante universelle des gazs parfaits
TETA = 306.15 #Kelvin
def acctionneur(Vint, Pint, Vex, Pex, fraction_sec) :
    a = (SECTION*(Pint-Pex))*R*TETA/(Pint*Vint*MM_AIR)
    v = a * 1/fraction_sec
    Vsortie = v * SECTION
    print(Vsortie)
    msortie = (Pint*Vsortie*MM_AIR)/(R*TETA)
    mint = (Pint*Vint*MM_AIR)/(R*TETA)
    mint -= msortie
    mex = (Pex*Vex*MM_AIR)/(R*TETA)
    mex += msortie
    Vex = (mex*R*TETA)/(Pex*MM_AIR)
    Pint = (mint*R*TETA)/(Vint*MM_AIR)

    return Pint, Vex

Vint = 2
Pint = 400000
Vex = 2
Pex = 150000
for i in range(100000) :
    Pint, Vex = acctionneur(Vint, Pint, Vex, Pex, 1000)
print(Vint, Pint, Vex, Pex)
