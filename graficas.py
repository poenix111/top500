from database import DbTop500

#5 paises con mayor repunte HPCC desde 2009
db = DbTop500()
paises_top = db.query_count_paises(anio_mayor=2008, limite=5)
print(paises_top)

# crecimiento de paises con mayor repunte
paises_top_anios = {}
for anio in range(2009, 2020):
    paises_top_anio = []

    paises_anio = db.query_count_paises(anio_igual=anio)
    for pais in paises_anio:
        for pais_top in paises_top:
            if(pais_top[0] == pais[0]):
                paises_top_anio.append(pais) 

    paises_top_anios[anio] = paises_top_anio

print(paises_top_anios)
    
# Paises con menor aportacion desde 2009
paises_bot = db.query_count_paises(anio_mayor=2008, limite=10, descendente=False)
print(paises_bot)