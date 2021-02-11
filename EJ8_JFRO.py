# Julia Fernanda Ramirez Oviedo

Conejos={0:0, 1:1}

def ParejasC(nmes):
    if nmes not in Conejos:
        Conejos[nmes]= ParejasC(nmes-1)+ParejasC(nmes-2)
    return Conejos[nmes]

nmes=int(input("Ingrese el número de mes: "))
print("Hay",ParejasC(nmes),"pareja(s) en el mes #"+str(nmes))
