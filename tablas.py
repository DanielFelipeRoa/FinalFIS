import pandas as pd


def departamento (  ):
    base = pd.read_csv ("Base.csv", header = None,
                        names = ["periodo", "mes", "Codigo", "Departamento", "codigoMunicipio",
                                 "municipio", "nombreComercial", "empresa", "direccion", "producto", "precio",
                                 "estado"])

    baseModificada = base.drop_duplicates(['Codigo', 'Departamento'], keep='last')
    baseModificada.drop (['periodo', 'mes','codigoMunicipio', 'municipio', 'nombreComercial',
                                           'empresa', 'direccion', 'producto', 'precio', 'estado'],
                                          axis = 'columns', inplace = True)

    baseModificada.to_html('templates/codigoDepartamento.html', index = False, justify = "left", border = 3)


def municipio():
    base = pd.read_csv ("Base.csv", header = None,
                        names = ["periodo", "mes", "codigoDepartamento", "nombreDepartamento", "Codigo",
                                 "Municipio", "nombreComercial", "empresa", "direccion", "producto", "precio",
                                 "estado"])

    baseModificada = base.drop_duplicates (['Municipio'], keep = 'last')
    baseModificada.drop (['periodo', 'mes', 'codigoDepartamento', 'nombreDepartamento', 'nombreComercial',
                          'empresa', 'direccion', 'producto', 'precio', 'estado'],
                         axis = 'columns', inplace = True)

    baseModificada.to_html ('templates/codigoMunicipio.html', index = False, justify = "left", border = 3)


def empresaProducto ( ):
    base = pd.read_csv ("Base.csv", header = None,
                        names = ["periodo", "mes", "codigoDepartamento", "nombreDepartamento", "codigoMunicipio",
                                 "municipio", "nombreComercial", "Empresa", "direccion", "Producto", "precio",
                                 "estado"])
    baseModificada = base.drop_duplicates (['Empresa', 'Producto'], keep = 'last')
    ordenada = baseModificada.sort_values ('Empresa')
    ordenada.head()


    ordenada.drop (["periodo", "mes", "codigoDepartamento", "nombreDepartamento", "codigoMunicipio",
                "municipio", "nombreComercial", "direccion", "precio",
                "estado"], axis = 'columns', inplace = True)

    ordenada.to_html ('templates/empresaProducto.html', index = False, justify = "left", border = 3)


def empresaPrecioProducto():
    base = pd.read_csv ("Base.csv", header = None,
                        names = ["periodo", "mes", "codigoDepartamento", "Departamento", "codigoMunicipio",
                                 "municipio", "nombreComercial", "Empresa", "direccion", "Producto", "precio",
                                 "estado"])
    baseModificada = base.drop_duplicates (['Empresa', 'Producto'], keep = 'last')
    ordenada = baseModificada.sort_values ('Departamento')
    ordenada.head ( )

    ordenada.drop (["periodo", "mes", "codigoDepartamento", "codigoMunicipio",
                    "municipio", "nombreComercial", "direccion", "estado"], axis = 'columns', inplace = True)

    ordenada.to_html ('templates/empresaPrecioProducto.html', index = False, justify = "left", border = 3)