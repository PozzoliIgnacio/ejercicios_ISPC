"""EJERCICIO 3: Un hincha de fútbol desea conocer la cantidad de puntos que su equipo 
lleva acumulados en el campeonato, para ello recibe cada semana la información de la cantidad total de
partidos, desde el inicio del campeonato, que el equipo ha perdido, ha empatado y ha ganado.
Por cada partido empatado recibe un punto, por cada partido ganado tres puntos y por los perdidos cero puntos."""

partidosperdidos=int(input("cantidad de partidos perdidos:" ))
partidosempatados=int(input("cantidad de partidos empatados:" ))
partidos_ganados=int(input("cantidad de partidos ganado:" ))

cantid_partidos=partidosperdidos+partidos_ganados+partidosempatados

cantpuntos=(partidos_ganados*3)+(partidosperdidos*0)+(partidosempatados*1)

print("la cantidad de partidos jugados fue:", cantid_partidos)
print("los puntos del equipo son: ", cantpuntos)