from flask import Flask, request, send_file, abort
import os

app = Flask(__name__)

def bloqueado_por_user_agent():
    user_agent = request.headers.get("User-Agent", "").lower()
    return "mozilla" in user_agent or "chrome" in user_agent or "safari" in user_agent

@app.route("/download")
def descargar_por_defecto():
    nombre_archivo = "test.txt"

    ruta = os.path.join(".", nombre_archivo)
    return send_file(ruta, as_attachment=True)

@app.route("/download/<path:nombre_archivo>")
def descargar_ss(nombre_archivo):
    if bloqueado_por_user_agent():
        return abort(403)

    if nombre_archivo == "requirements.txt" or "main.py":
        return abort(403)
    # Sanitizar el nombre del archivo para evitar rutas peligrosas
    nombre_archivo = os.path.basename(nombre_archivo)

    ruta = os.path.join(".", nombre_archivo)
    if not os.path.abspath(ruta).startswith(os.path.abspath(DOWNLOADS_DIR)):
        return abort(403, description="Access denied.")
    if not os.path.exists(ruta):
        return abort(404, description="File not found.")

    return send_file(ruta, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
