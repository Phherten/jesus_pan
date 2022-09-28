from datetime import date

resumen_mes = []
hoy = date.today()


def capturar_texto(texto):
    array_texto = texto.split(" ")
    resumen_mes.append(
        {"Fecha": hoy.day, "Conductor": array_texto[0], "Km_ruta": array_texto[1], "km_a_almacen": array_texto[2],
         "km_a_casa": array_texto[3]})


def consultar_mes():
    return resumen_mes


def resumen():
    km_ruta = 0
    dias_mes = 0
    km_ida = 0
    km_vuelta = 0
    for km in resumen_mes:
        km_ruta += int(km['Km_ruta'])
        km_ida += int(km['km_a_almacen'])
        km_vuelta += int(km['km_a_casa'])
        dias_mes += 1

    media_ruta = km_ruta / dias_mes
    media_ida = km_ida / dias_mes
    media_vuelta = km_vuelta / dias_mes
    km_totales = km_ruta + km_ida + km_vuelta

    return km_ruta, media_ruta, media_ida, media_vuelta, km_totales
