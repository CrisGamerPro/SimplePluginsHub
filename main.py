from flask import Flask, request, send_file, abort

app = Flask(__name__)

@app.route("/download")
def download():
    user_agent = request.headers.get("User-Agent", "").lower()
    if "mozilla" in user_agent or "chrome" in user_agent or "safari" in user_agent:
        return abort(403)
    return send_file("archivo.zip", as_attachment=True)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
