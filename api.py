#!/usr/bin/env python3
"""
API REST mínima para Tapi. Stdlib apenas.

Endpoints:
  GET /conjugate?raiz=ama
  GET /lookup?word=kama
  GET /translate?direction=tapi2pt&text=mi+manita+kasi
  GET /translate?direction=pt2tapi&text=casa+do+pai
  GET /health

Uso:
    python3 api.py [porta]      # padrão: 8080
    curl http://localhost:8080/conjugate?raiz=ama
"""

import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from conjugador import conjugar, conjugar_evid
from tradutor import (
    analisar_tapi,
    carregar_lexico,
    traduzir_pt2tapi,
    traduzir_tapi2pt,
)

TAPI2PT, PT2TAPI, RAIZES_VERBAIS = carregar_lexico()


class TapiHandler(BaseHTTPRequestHandler):
    def _send(self, code: int, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _err(self, code: int, msg: str) -> None:
        self._send(code, {"error": msg})

    def log_message(self, fmt, *args):
        sys.stderr.write(f"[api] {self.address_string()} - {fmt % args}\n")

    def do_GET(self) -> None:
        url = urlparse(self.path)
        qs = parse_qs(url.query)

        if url.path == "/health":
            return self._send(200, {
                "status": "ok",
                "entradas_lexico": len(TAPI2PT),
                "raizes_verbais": len(RAIZES_VERBAIS),
            })

        if url.path == "/conjugate":
            raiz = (qs.get("raiz", [""])[0] or "").strip().lower()
            if not raiz:
                return self._err(400, "param 'raiz' obrigatório")
            formas = conjugar(raiz)
            evid = conjugar_evid(formas["passado.simples"])
            return self._send(200, {
                "raiz": raiz,
                "formas": formas,
                "evidenciais_sobre_passado": evid,
            })

        if url.path == "/lookup":
            word = (qs.get("word", [""])[0] or "").strip()
            if not word:
                return self._err(400, "param 'word' obrigatório")
            chave = word.lower()
            resultado = {"word": word, "tapi2pt": None, "pt2tapi": None, "analise": None}
            if chave in TAPI2PT:
                resultado["tapi2pt"] = TAPI2PT[chave]
            if chave in PT2TAPI:
                resultado["pt2tapi"] = PT2TAPI[chave]
            resultado["analise"] = analisar_tapi(word, TAPI2PT, RAIZES_VERBAIS)
            return self._send(200, resultado)

        if url.path == "/translate":
            direction = (qs.get("direction", [""])[0] or "").strip()
            text = (qs.get("text", [""])[0] or "").strip()
            if direction not in ("tapi2pt", "pt2tapi"):
                return self._err(400, "direction deve ser 'tapi2pt' ou 'pt2tapi'")
            if not text:
                return self._err(400, "param 'text' obrigatório")
            if direction == "tapi2pt":
                out = traduzir_tapi2pt(text, TAPI2PT, RAIZES_VERBAIS)
            else:
                out = traduzir_pt2tapi(text, PT2TAPI)
            return self._send(200, {"direction": direction, "input": text, "output": out})

        return self._err(404, f"rota desconhecida: {url.path}")


def main() -> None:
    porta = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    host = sys.argv[2] if len(sys.argv) > 2 else "127.0.0.1"
    server = HTTPServer((host, porta), TapiHandler)
    print(f"API Tapi rodando em http://{host}:{porta}")
    print("Rotas: /health /conjugate?raiz=X /lookup?word=X /translate?direction=Y&text=Z")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nencerrando")
        server.server_close()


if __name__ == "__main__":
    main()
