#!/usr/bin/env python3
"""
Gera áudio web (m4a/AAC) em docs/audio/ + manifest.json.

Cobre: 9 fonemas, 18 sílabas CV, 50 palavras-amostra do léxico e todo
token Tapi que aparece nas lições do manual (docs/manual/lessons.json).
O manual.html usa manifest.json para tornar palavras clicáveis (play).

Requer macOS (`say`). Voz padrão: Luciana (pt-BR).

Uso:
    python3 tools/gerar_audio_web.py [--voice Luciana]
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "docs" / "audio"
LESSONS = ROOT / "docs" / "manual" / "lessons.json"

FONEMAS = ["a", "i", "u", "p", "t", "k", "m", "n", "s"]
SILABAS = [c + v for c in "ptkmns" for v in "aiu"]
RE_TOKEN = re.compile(r"^[ptkmnsaiu]+(-[ptkmnsaiu]+)*$")


def say(texto: str, saida: Path, voz: str) -> None:
    # hífen de composto vira pausa curta demais no `say`; espaço soa melhor?
    # Não: manter a palavra junta preserva o acento penúltimo por raiz.
    falado = texto.replace("-", " ")
    subprocess.run(["say", "-v", voz, "-o", str(saida), falado],
                   check=True, capture_output=True)


def tokens_do_manual() -> set[str]:
    """Todo texto Tapi literal das lições (células, itens, parágrafos)."""
    if not LESSONS.exists():
        return set()
    data = json.loads(LESSONS.read_text(encoding="utf-8"))
    tokens: set[str] = set()

    def visita(obj):
        if isinstance(obj, dict):
            for chave in ("lit", "tapi"):
                v = obj.get(chave)
                if isinstance(v, str):
                    t = v.strip().strip(".,!?;:").lower()
                    if RE_TOKEN.match(t):
                        tokens.add(t)
            for v in obj.values():
                visita(v)
        elif isinstance(obj, list):
            for v in obj:
                visita(v)

    visita(data)
    return tokens


def palavras_amostra(n: int = 50) -> list[str]:
    import csv
    out = []
    with (ROOT / "lexico.tsv").open(encoding="utf-8") as f:
        r = csv.reader(f, delimiter="\t")
        next(r, None)
        for linha in r:
            if len(linha) >= 3 and "-" not in linha[0] and len(linha[0]) == 4 \
               and linha[1].strip() not in ("part", "suf", "pref"):
                out.append(linha[0].strip())
    passo = max(1, len(out) // n)
    return out[::passo][:n]


def main() -> None:
    voz = "Luciana"
    if "--voice" in sys.argv:
        voz = sys.argv[sys.argv.index("--voice") + 1]

    OUTDIR.mkdir(parents=True, exist_ok=True)
    todos = sorted(set(FONEMAS) | set(SILABAS) | set(palavras_amostra())
                   | tokens_do_manual())

    manifest = {}
    novos = 0
    for tok in todos:
        nome = tok.replace("-", "_") + ".m4a"
        destino = OUTDIR / nome
        if not destino.exists():
            try:
                say(tok, destino, voz)
                novos += 1
            except subprocess.CalledProcessError as e:
                print(f"AVISO: falhou '{tok}': {e}", file=sys.stderr)
                continue
        manifest[tok] = "audio/" + nome

    (OUTDIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, separators=(",", ":"), sort_keys=True),
        encoding="utf-8")
    print(f"{len(manifest)} tokens no manifest ({novos} gerados agora) → {OUTDIR}/")


if __name__ == "__main__":
    main()
