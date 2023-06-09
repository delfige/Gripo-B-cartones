from flask import Flask, render_template, request
from loteria import generar_cartones_sin_repetir, guardar_cartones_en_csv,cargar_cartones



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
    return render_template('resultado.html', cartones=cartones_cargados)


if __name__ == '__main__':
    app.run()