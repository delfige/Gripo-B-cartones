from flask import Flask, render_template, request,redirect, url_for
from loteria import generar_cartones_sin_repetir, guardar_cartones_en_csv,cargar_cartones
import math


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generar_cartones', methods=['POST'])
def generar_cartones():
    cantidad_cartones = int(request.form.get('cantidad_cartones'))
    cartones_sin_repetir = generar_cartones_sin_repetir(cantidad_cartones)
    nombre_archivo = 'cartones_bingo.csv'
    guardar_cartones_en_csv(cartones_sin_repetir, cantidad_cartones, nombre_archivo)
    cartones_cargados = cargar_cartones(nombre_archivo)
    
    return redirect(url_for('mostrar_cartones', pagina=1))


@app.route('/generar_cartones/<int:pagina>', methods=['GET'])
def mostrar_cartones(pagina):
    nombre_archivo = 'cartones_bingo.csv'
    cartones_cargados = cargar_cartones(nombre_archivo)
    
    indice_inicio = (pagina - 1) * 3
    indice_fin = indice_inicio + 3
    cartones_pagina = cartones_cargados[indice_inicio:indice_fin]
    
    total_paginas = math.ceil(len(cartones_cargados) / 3)  
    
    return render_template('resultado.html', cartones=cartones_pagina, cantidad=len(cartones_cargados), pagina=pagina, total_paginas=total_paginas)




if __name__ == "__main__":
    app.run(debug=True)