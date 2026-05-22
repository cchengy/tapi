#!/usr/bin/env python3
"""
Gera dicionario_pt_tapi.md a partir de lexico.tsv.

Saída: dicionario_pt_tapi.md (Markdown, ordenado por português, agrupado por letra).
Uma palavra portuguesa pode mapear pra múltiplas formas Tapi (separadas por " / ").

Uso:
    python3 gerar_dicionario_pt.py
"""

import csv
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).parent
LEXICO = BASE / "lexico.tsv"
SAIDA = BASE / "dicionario_pt_tapi.md"


def chave_pt(significado: str) -> str:
    """Extrai chave portuguesa: primeira parte antes de '(', barras viram separadores."""
    primeira = significado.split("(")[0].strip()
    return primeira.rstrip(".,;:").strip()


def primeira_letra(texto: str) -> str:
    """Letra inicial sem acentos, em maiúscula. '#' para não-letras."""
    if not texto:
        return "#"
    c = unicodedata.normalize("NFD", texto[0])[0].upper()
    return c if c.isalpha() else "#"


def main() -> None:
    entradas: dict[str, list[tuple[str, str]]] = defaultdict(list)

    with LEXICO.open(encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader, None)
        for linha in reader:
            if not linha or len(linha) < 3:
                continue
            tapi = linha[0].strip()
            classe = linha[1].strip()
            significado = linha[2].strip()
            if not tapi or not significado:
                continue

            partes = re.split(r"\s*[/]\s*", chave_pt(significado))
            for parte in partes:
                if parte:
                    entradas[parte.lower()].append((tapi, classe))

    consolidado: dict[str, dict[str, list[tuple[str, str]]]] = defaultdict(dict)
    for pt, pares in entradas.items():
        letra = primeira_letra(pt)
        vistos = []
        for tapi, classe in pares:
            if (tapi, classe) not in vistos:
                vistos.append((tapi, classe))
        consolidado[letra][pt] = vistos

    linhas = [
        "# Dicionário Português → Tapi",
        "",
        "Gerado automaticamente de `lexico.tsv` por `gerar_dicionario_pt.py`. **Não editar à mão.**",
        "",
        "Para atualizar: edite `lexico.tsv` e rode `python3 gerar_dicionario_pt.py`.",
        "",
    ]

    for letra in sorted(consolidado.keys()):
        linhas.append(f"## {letra}")
        linhas.append("")
        linhas.append("| Português | Tapi | Classe |")
        linhas.append("|-----------|------|--------|")
        for pt in sorted(consolidado[letra].keys()):
            tapis = " / ".join(t for t, _ in consolidado[letra][pt])
            classes = ", ".join(sorted({c for _, c in consolidado[letra][pt]}))
            linhas.append(f"| {pt} | {tapis} | {classes} |")
        linhas.append("")

    SAIDA.write_text("\n".join(linhas), encoding="utf-8")
    total = sum(len(v) for v in consolidado.values())
    print(f"Gerado {SAIDA} com {total} entradas portuguesas em {len(consolidado)} letras.")


if __name__ == "__main__":
    main()
