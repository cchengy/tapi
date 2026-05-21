#!/usr/bin/env python3
"""
Tradutor Tapi ↔ Português baseado em léxico.

Tradução palavra-a-palavra. Não cobre gramática completa.

Uso:
    python3 tradutor.py pt2tapi "casa do pai"
    python3 tradutor.py tapi2pt "kama ni papi"
"""

import csv
import sys
from pathlib import Path

LEXICO_PATH = Path(__file__).parent / "lexico.tsv"


def carregar_lexico() -> tuple[dict, dict]:
    """Retorna (tapi→pt, pt→tapi)."""
    tapi2pt: dict[str, list[str]] = {}
    pt2tapi: dict[str, list[str]] = {}

    with LEXICO_PATH.open(encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        header = next(reader, None)
        for linha in reader:
            if not linha or len(linha) < 3:
                continue
            tapi = linha[0].strip()
            significado = linha[2].strip()
            if not tapi or not significado:
                continue

            tapi2pt.setdefault(tapi, []).append(significado)
            chave_pt = significado.split(" (")[0].strip().lower()
            pt2tapi.setdefault(chave_pt, []).append(tapi)

    return tapi2pt, pt2tapi


def traduzir_palavra(palavra: str, dicionario: dict) -> str:
    chave = palavra.lower().strip(".,!?;:")
    if chave in dicionario:
        return f"[{'/'.join(dicionario[chave])}]"
    return f"⟨?{palavra}⟩"


def traduzir(texto: str, dicionario: dict) -> str:
    palavras = texto.split()
    return " ".join(traduzir_palavra(p, dicionario) for p in palavras)


def main() -> None:
    if len(sys.argv) < 3:
        print("Uso: python3 tradutor.py pt2tapi|tapi2pt \"texto\"")
        sys.exit(1)

    modo = sys.argv[1]
    texto = " ".join(sys.argv[2:])
    tapi2pt, pt2tapi = carregar_lexico()

    if modo == "pt2tapi":
        print(traduzir(texto, pt2tapi))
    elif modo == "tapi2pt":
        print(traduzir(texto, tapi2pt))
    else:
        print(f"Modo desconhecido: {modo}")
        sys.exit(1)


if __name__ == "__main__":
    main()
