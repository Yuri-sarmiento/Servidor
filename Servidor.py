from flask import Flask, jsonify  # Importa Flask para crear el servidor y jsonify para formatear las respuestas como JSON

app = Flask(_name_)  # Inicializa una aplicación Flask

# Base de datos simulada 
base_datos = {
    "usuarios": [         
    {"id": 1, "nombre": "Juan"},         
    {"id": 2, "nombre": "María"}     
 ] 
}  
# Ruta para obtener los usuarios 
@app.route('/usuarios', methods=['GET']) 
def obtener_usuarios():    
 return jsonify(base_datos["usuarios"])  
# Devuelve la lista de usuarios en formato 
JSON  if _name_ == '_main_':     
app.run(port=5000)  # Ejecuta el servidor en el puerto 5000
