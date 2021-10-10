from flask import Flask, render_template
from mesesVSprecios import mesesVSprecios
from preciosProductos import preciosProductos
from tablas import municipio, departamento, empresaProducto, empresaPrecioProducto

app = Flask (__name__)


@app.route('/inicio', methods=["GET", "POST"])
@app.route ('/index', methods=["GET", "POST"])
@app.route ('/', methods=["GET", "POST"])
def inicio():
    return render_template("inicio.html")


@app.route('/mesesVSprecios/gasolina-corriente', methods=["GET", "POST"])
def dibuja_meses_vs_precios_gasolina_corriente ( ):
    mesesVSprecios("GASOLINA CORRIENTE OXIGENADA")
    return render_template("inicio.html")


@app.route('/mesesVSprecios/gasolina-extra', methods=["GET", "POST"])
def dibuja_meses_vs_precios_gasolina_extra ( ):
    mesesVSprecios("GASOLINA EXTRA OXIGENADA")
    return render_template("inicio.html")


@app.route('/mesesVSprecios/biodiesel-extra', methods=["GET", "POST"])
def dibuja_meses_vs_precios_biodiesel_extra ( ):
    mesesVSprecios("BIODIESEL EXTRA")
    return render_template("inicio.html")


@app.route('/mesesVSprecios/acpm-diesel', methods=["GET", "POST"])
def dibuja_meses_vs_precios_acpm_diesel ( ):
    mesesVSprecios("ACPM - DIESEL")
    return render_template("inicio.html")


@app.route('/preciosVSproductos', methods=["GET", "POST"])
def dibuja_precios_vs_productos():
    preciosProductos()
    return render_template("inicio.html")

@app.route('/codigo-departamento')
def dibuja_tabla_departamentos():
    departamento()
    return render_template("codigoDepartamento.html")

@app.route('/codigo-municipio')
def dibuja_tabla_municipios():
    municipio()
    return render_template("codigoMunicipio.html")

@app.route('/empresa-producto')
def dibuja_tabla_empresa_vs_productos():
    empresaProducto()
    return render_template("empresaProducto.html")

@app.route('/empresa-producto-precio')
def dibuja_tabla_empresa_vs_productos_vs_precio():
    empresaPrecioProducto()
    return render_template("empresaPrecioProducto.html")


if __name__ == '__main__':
    app.run (debug = False)
