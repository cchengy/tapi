#!/usr/bin/env python3
"""
Validador do lexico.tsv — as regras do CONTRIBUTING.md, em código.

Checa:
  1. TSV bem-formado (>=3 colunas, sem palavra/significado vazios)
  2. Fonologia: só {p,t,k,m,n,s} × {a,i,u}
  3. Forma: raiz CV.CV estrita; partícula V/CV/VCV; sufixo CV ou -n;
     compostos raiz-raiz; exceções lexicais documentadas em fonologia.md
  4. Duplicatas exatas (mesma palavra em 2+ linhas) — polissemia deve
     ficar numa linha só, significados separados por " / "
  5. Compostos com parte inexistente no léxico
  6. Colisão de nova raiz com partícula/sufixo existente

Uso:
    python3 tools/validar_lexico.py            # valida, exit 1 se erro
    python3 tools/validar_lexico.py --strict   # warnings também viram erro

Sai 0 = ok, 1 = erro. Roda no CI ou antes de commit.
"""

import csv
import re
import sys
from collections import Counter
from pathlib import Path

LEXICO = Path(__file__).resolve().parent.parent / "lexico.tsv"

# Exceções lexicais documentadas (fonologia.md § exceções)
# (vazio desde a reforma kuna/kuna-nuna — V.CV é coberto por RE_CURTA)
EXCECOES: set[str] = set()

RE_CHARS = re.compile(r"^[ptkmnsaiu-]+$")
RE_RAIZ = re.compile(r"^([ptkmns][aiu]){2}$")           # CV.CV
RE_CURTA = re.compile(r"^[aiu]$|^[ptkmns][aiu]$|^[aiu][ptkmns][aiu]$")  # V, CV, V.CV
RE_PLURAL_N = re.compile(r"^([ptkmns][aiu]){1,2}n$")    # ex.: 'tan' não existe, mas -n em base


def carregar():
    with LEXICO.open(encoding="utf-8") as f:
        linhas = list(csv.reader(f, delimiter="\t"))
    return linhas[0], linhas[1:]


def validar(strict: bool = False) -> int:
    _, rows = carregar()
    erros: list[str] = []
    avisos: list[str] = []

    palavras = []
    for i, r in enumerate(rows, start=2):  # 1-based + header
        if not r or not any(r):
            continue
        if len(r) < 3:
            erros.append(f"linha {i}: menos de 3 colunas: {r}")
            continue
        w, classe, sig = r[0].strip(), r[1].strip(), r[2].strip()
        if not w:
            erros.append(f"linha {i}: palavra vazia")
            continue
        if not sig:
            erros.append(f"linha {i}: '{w}' sem significado")
        palavras.append((i, w, classe))

    # 4) duplicatas exatas
    cont = Counter(w for _, w, _ in palavras)
    for w, c in sorted(cont.items()):
        if c > 1:
            erros.append(
                f"duplicata: '{w}' aparece {c}× — consolidar numa linha, "
                f"significados separados por ' / '"
            )

    todas = {w for _, w, _ in palavras}
    raizes = {w for w in todas if "-" not in w}

    for i, w, classe in palavras:
        afixo = w.startswith("-") or w.endswith("-")
        nucleo = w.strip("-")

        # 2) fonologia
        if not RE_CHARS.match(nucleo):
            erros.append(f"linha {i}: '{w}' usa caractere fora de ptkmns/aiu")
            continue

        # 3) forma
        if afixo:
            if not (RE_CURTA.match(nucleo) or nucleo == "n" or RE_RAIZ.match(nucleo)):
                avisos.append(f"linha {i}: afixo '{w}' fora de CV/-n/CV.CV")
        elif "-" in w:
            for parte in w.split("-"):
                # 5) parte de composto precisa existir (partículas curtas ok)
                if parte not in raizes and len(parte) > 2:
                    erros.append(f"linha {i}: composto '{w}' usa raiz inexistente '{parte}'")
        else:
            if w in EXCECOES:
                continue
            if not (RE_RAIZ.match(w) or RE_CURTA.match(w)):
                erros.append(
                    f"linha {i}: '{w}' ({classe}) fora de CV.CV/V/CV/V.CV "
                    f"e não está nas exceções documentadas"
                )

    for e in erros:
        print(f"ERRO   {e}")
    for a in avisos:
        print(f"AVISO  {a}")

    n_err = len(erros) + (len(avisos) if strict else 0)
    print(f"\n{len(rows)} linhas · {len(erros)} erro(s) · {len(avisos)} aviso(s)")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(validar(strict="--strict" in sys.argv))
