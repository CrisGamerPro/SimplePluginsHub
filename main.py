from flask import Flask, request, send_file, abort
import os

app = Flask(__name__)

def bloqueado_por_user_agent():
    user_agent = request.headers.get("User-Agent", "").lower()
    return "mozilla" in user_agent or "chrome" in user_agent or "safari" in user_agent

@app.route("/download")
def descargar_por_defecto():
    if bloqueado_por_user_agent():
        return abort(403)
    return abort(404, "Not found, Using default route /download, Missing route.")

@app.route("/download/SimpleSpawn.jar")
def descargar_ss(nombre_archivo):
    if bloqueado_por_user_agent():
        return abort(403)

    # Sanitizar el nombre del archivo para evitar rutas peligrosas
    nombre_archivo = os.path.basename(nombre_archivo)

    ruta = os.path.join(".", nombre_archivo)
    if not os.path.exists(ruta):
        return abort(404, description="File not found.")

    return send_file(ruta, as_attachment=True)

@app.route("/download/SimpleSpawn-Legacy.jar")
def descargar_ssl(nombre_archivo):
    if bloqueado_por_user_agent():
        return abort(403)

    # Sanitizar el nombre del archivo para evitar rutas peligrosas
    nombre_archivo = os.path.basename(nombre_archivo)

    ruta = os.path.join(".", nombre_archivo)
    if not os.path.exists(ruta):
        return abort(404, description="File not found.")

    return send_file(ruta, as_attachment=True)

@app.route("/download/SimpleFly.jar")
def descargar_sf(nombre_archivo):
    if bloqueado_por_user_agent():
        return abort(403)

    # Sanitizar el nombre del archivo para evitar rutas peligrosas
    nombre_archivo = os.path.basename(nombre_archivo)

    ruta = os.path.join(".", nombre_archivo)
    if not os.path.exists(ruta):
        return abort(404, description="File not found.")

    return send_file(ruta, as_attachment=True)

@app.route("/download/SimpleJoinEvents.jar")
def descargar_sje(nombre_archivo):
    if bloqueado_por_user_agent():
        return abort(403)

    # Sanitizar el nombre del archivo para evitar rutas peligrosas
    nombre_archivo = os.path.basename(nombre_archivo)

    ruta = os.path.join(".", nombre_archivo)
    if not os.path.exists(ruta):
        return abort(404, description="File not found.")

    return send_file(ruta, as_attachment=True)

@app.route("/download/test.txt")
def test(nombre_archivo):
    nombre_archivo = os.path.basename(nombre_archivo)
    ruta = os.path.join(".", nombre_archivo)
    if not os.path.exists(ruta):
        return abort(404)
    return send_file(ruta, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
