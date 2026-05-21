#!/usr/bin/env python3
"""
Gera deck Anki (TSV importável) a partir do léxico Tapi.

Saída: anki_tapi.tsv com colunas:
    Front (português) | Back (Tapi) | Classe | Tags

Uso:
    python3 gerar_anki.py
    (importe anki_tapi.tsv no Anki: File → Import → Field separator: Tab)
"""

import csv
from pathlib import Path

BASE = Path(__file__).parent
LEXICO = BASE / "lexico.tsv"
SAIDA = BASE / "anki_tapi.tsv"


def main() -> None:
    cartoes: list[tuple[str, str, str, str]] = []

    with LEXICO.open(encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        header = next(reader, None)
        for linha in reader:
            if not linha or len(linha) < 3:
                continue
            tapi = linha[0].strip()
            classe = linha[1].strip()
            significado = linha[2].strip()
            if not tapi or not significado or tapi.startswith("-") or tapi.endswith("-"):
                continue

            cartoes.append(
                (
                    significado,
                    tapi,
                    classe,
                    f"tapi {classe}",
                )
            )

    with SAIDA.open("w", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["Front", "Back", "Classe", "Tags"])
        writer.writerows(cartoes)

    print(f"Gerados {len(cartoes)} cartões em {SAIDA}")


if __name__ == "__main__":
    main()
