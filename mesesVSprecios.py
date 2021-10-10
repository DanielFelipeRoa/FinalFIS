import pandas as pd
import matplotlib.pyplot as plt
import random


def mesesVSprecios ( entrada ):
    base = pd.read_csv ("Base.csv", header = None,
                        names = ["periodo", "mes", "codigoDepartamento", "nombreDepartamento", "codigoMunicipio",
                                 "municipio", "nombreComercial", "empresa", "direccion", "producto", "precio",
                                 "estado"])

    # filtramos el Dataframe
    mascara = base ["producto"] == entrada
    base_filtrada = base [mascara]

    lista = []
    for i in range (13):
        mascara = base_filtrada ["mes"] == i
        base_filtrada2 = base_filtrada [mascara]
        valor = base_filtrada2 ["precio"].mean ( )
        lista.append (valor)
    lista.pop (0)

    # Grafica
    eje_x = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
             'Noviembre', 'Diciembre']
    eje_y = [lista [0], lista [1], lista [2], lista [3], lista [4], lista [5], lista [6], lista [7], lista [8],
             lista [9], lista [10], lista [11]]
    color = ["#" + ''.join ([random.choice ('0123456789ABCDEF') for j in range (6)])]
    plt.bar (eje_x, eje_y, color=color,  width = 0.8)
    plt.ylabel ('Precio')
    plt.xlabel ('Meses')
    plt.title ('Gráfica de meses vs precios de ' + entrada)

    # Mostramos Gráfica
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    plt.show ( )
