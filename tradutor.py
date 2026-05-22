#!/usr/bin/env python3
"""
Tradutor Tapi ↔ Português baseado em léxico + regras gramaticais básicas.

Reconhece:
- Sufixos verbais: -ta (passado), -ka (futuro), -sa (habitual), -ma (progressivo), -pa (perfectivo)
- Evidenciais: -ni (inferido), -ni-ni (reportado), -ni-ku (duvidoso)
- Imperativo: -ti
- Voz média/reflexiva: -ku
- Plural: -n
- Negação: partícula `pa` antes do verbo
- Posse: partícula `ni` entre nomes
- Pergunta: `ku?` no fim
- Compostos: tenta forma inteira; se falhar, divide por hífen
- Recompõe palavras desconhecidas via composição de raízes

Uso:
    python3 tradutor.py pt2tapi "casa do pai"
    python3 tradutor.py tapi2pt "kama ni papi"
    python3 tradutor.py tapi2pt "mi manita kasi pa"
"""

import csv
import re
import sys
from pathlib import Path

LEXICO_PATH = Path(__file__).parent / "lexico.tsv"

TEMPO_SUF = {"ta": "passado", "ka": "futuro"}
ASPECTO_SUF = {"sa": "habitual", "ma": "progressivo", "pa": "perfectivo"}
EVID_SUF = [
    ("-ni-ku", "duvidoso"),
    ("-ni-ni", "reportado"),
    ("-ni", "inferido"),
]
ESPECIAL_SUF = {"-ti": "imperativo", "-ku": "voz_media"}


def carregar_lexico() -> tuple[dict, dict, set]:
    """Retorna (tapi→pt, pt→tapi, raizes_verbais)."""
    tapi2pt: dict[str, list[str]] = {}
    pt2tapi: dict[str, list[str]] = {}
    raizes_verbais: set = set()

    with LEXICO_PATH.open(encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader, None)  # header
        for linha in reader:
            if not linha or len(linha) < 3:
                continue
            tapi = linha[0].strip()
            classe = linha[1].strip()
            significado = linha[2].strip()
            if not tapi or not significado:
                continue
            tapi2pt.setdefault(tapi, []).append(significado)
            chave_pt = significado.split(" (")[0].strip().lower()
            pt2tapi.setdefault(chave_pt, []).append(tapi)
            if classe == "verbo":
                raizes_verbais.add(tapi)

    return tapi2pt, pt2tapi, raizes_verbais


def analisar_tapi(palavra: str, tapi2pt: dict, raizes_verbais: set) -> dict:
    """Decompõe palavra Tapi em raiz + sufixos detectados."""
    p = palavra.lower().strip(".,!?;:")
    analise = {"original": palavra, "raiz": None, "marcas": [], "gloss": None}

    # 1) tenta forma exata
    if p in tapi2pt:
        analise["raiz"] = p
        analise["gloss"] = "/".join(tapi2pt[p])
        return analise

    # 2) tenta evidenciais (mais longos primeiro)
    for suf, nome in EVID_SUF:
        if p.endswith(suf):
            core = p[: -len(suf)]
            analise["marcas"].append(nome)
            p = core
            break

    # 3) tenta sufixos especiais (-ti imperativo, -ku voz média)
    for suf, nome in ESPECIAL_SUF.items():
        if p.endswith(suf):
            core = p[: -len(suf)]
            if core in raizes_verbais or core in tapi2pt:
                analise["marcas"].insert(0, nome)
                p = core
                break

    # 4) tenta plural -n (só se base existir)
    if p.endswith("n") and len(p) >= 5:
        base = p[:-1]
        if base in tapi2pt:
            analise["marcas"].insert(0, "plural")
            p = base

    # 5) tenta tempo + aspecto
    # ordem: raiz + (tempo) + (aspecto)
    for asp_suf, asp_nome in ASPECTO_SUF.items():
        if p.endswith(asp_suf):
            sem_asp = p[: -len(asp_suf)]
            for t_suf, t_nome in TEMPO_SUF.items():
                if sem_asp.endswith(t_suf):
                    raiz = sem_asp[: -len(t_suf)]
                    if raiz in raizes_verbais:
                        analise["marcas"].insert(0, asp_nome)
                        analise["marcas"].insert(0, t_nome)
                        p = raiz
                        break
            else:
                if sem_asp in raizes_verbais:
                    analise["marcas"].insert(0, asp_nome)
                    p = sem_asp
            break

    # 6) só tempo (sem aspecto)
    if p not in tapi2pt:
        for t_suf, t_nome in TEMPO_SUF.items():
            if p.endswith(t_suf):
                raiz = p[: -len(t_suf)]
                if raiz in raizes_verbais:
                    analise["marcas"].insert(0, t_nome)
                    p = raiz
                    break

    # 7) confirma raiz
    if p in tapi2pt:
        analise["raiz"] = p
        analise["gloss"] = "/".join(tapi2pt[p])
        return analise

    # 8) tenta composição (divide em raízes conhecidas)
    if "-" in palavra:
        partes = palavra.lower().strip(".,!?;:").split("-")
        glosses = []
        for parte in partes:
            if parte in tapi2pt:
                glosses.append(tapi2pt[parte][0])
            else:
                glosses.append(f"?{parte}")
        analise["raiz"] = palavra
        analise["gloss"] = "+".join(glosses) + " (composto)"
        return analise

    analise["gloss"] = f"?{palavra}"
    return analise


def traduzir_tapi2pt(texto: str, tapi2pt: dict, raizes_verbais: set) -> str:
    """Traduz Tapi → PT com análise morfológica."""
    palavras = texto.split()
    saida = []
    for palavra in palavras:
        a = analisar_tapi(palavra, tapi2pt, raizes_verbais)
        if a["marcas"]:
            saida.append(f"[{a['gloss']}.{'.'.join(a['marcas'])}]")
        else:
            saida.append(f"[{a['gloss']}]")
    return " ".join(saida)


def traduzir_pt2tapi(texto: str, pt2tapi: dict) -> str:
    """Traduz PT → Tapi palavra-a-palavra."""
    palavras = texto.split()
    saida = []
    for palavra in palavras:
        chave = palavra.lower().strip(".,!?;:")
        if chave in pt2tapi:
            saida.append("/".join(pt2tapi[chave]))
        else:
            saida.append(f"⟨?{palavra}⟩")
    return " ".join(saida)


def main() -> None:
    if len(sys.argv) < 3:
        print("Uso: python3 tradutor.py pt2tapi|tapi2pt \"texto\"")
        sys.exit(1)

    modo = sys.argv[1]
    texto = " ".join(sys.argv[2:])
    tapi2pt, pt2tapi, raizes_verbais = carregar_lexico()

    if modo == "pt2tapi":
        print(traduzir_pt2tapi(texto, pt2tapi))
    elif modo == "tapi2pt":
        print(traduzir_tapi2pt(texto, tapi2pt, raizes_verbais))
    else:
        print(f"Modo desconhecido: {modo}")
        sys.exit(1)


if __name__ == "__main__":
    main()
