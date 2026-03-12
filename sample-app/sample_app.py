import hashlib
import os

from flask import Flask, render_template, request

sample = Flask(__name__)


def token_hash8(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()[:8]


@sample.route("/")
def main():
    student_token = os.getenv("STUDENT_TOKEN", "").strip()
    th8 = token_hash8(student_token) if student_token else "NO_TOKEN"
    return render_template("index.html", client_ip=request.remote_addr, token_hash8=th8)


if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050, debug=False, threaded=False, use_reloader=False)
