import pandas as pd
import matplotlib.pyplot as plt
import random


def preciosProductos ():
    base = pd.read_csv ("Base.csv", header = None,
                        names = ["periodo", "mes", "codigoDepartamento", "nombreDepartamento", "codigoMunicipio",
                                 "municipio", "nombreComercial", "empresa", "direccion", "producto", "precio",
                                 "estado"])

    lista = []

    # filtramos el Dataframe
    mascara = base ["producto"] == "GASOLINA CORRIENTE OXIGENADA"
    base_filtrada = base [mascara]
    valor = base_filtrada ["precio"].mean ( )
    lista.append(valor)

    mascara = base ["producto"] == "GASOLINA EXTRA OXIGENADA"
    base_filtrada = base [mascara]
    valor = base_filtrada ["precio"].mean ( )
    lista.append (valor)

    mascara = base ["producto"] == "BIODIESEL EXTRA"
    base_filtrada = base [mascara]
    valor = base_filtrada ["precio"].mean ( )
    lista.append (valor)

    mascara = base ["producto"] == "ACPM - DIESEL"
    base_filtrada = base [mascara]
    valor = base_filtrada ["precio"].mean ( )
    lista.append (valor)

    # Grafica
    eje_x = ["Corriente", "Extra", "Biodiesel", "ACPM"]
    eje_y = [lista[0], lista[1], lista[2], lista[3] ]
    color = ["#" + ''.join ([random.choice ('0123456789ABCDEF') for j in range (6)])]
    plt.bar (eje_x, eje_y, color=color,  width = 0.6)
    plt.ylabel ('Precio')
    plt.xlabel ('Producto')
    plt.title ('Gráfica de productos vs precios')

    # Mostramos Gráfica
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    plt.show ( )
