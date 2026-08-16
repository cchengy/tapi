#!/usr/bin/env python3
"""
Extrai manual.md → docs/manual/lessons.json + docs/manual/pt.json.

Separação esqueleto × tradução:
  - lessons.json: estrutura das lições + todo texto Tapi (literal, único)
  - pt.json:      strings traduzíveis, chaveadas por id estável
  - en/es/zh/ja.json: mesmas chaves, preenchidas por tradução; chave
    ausente cai para pt.json no manual.html

Ids: l{n}.{hash8 do texto pt} — estáveis enquanto o texto PT não mudar
(mudou o texto ⇒ tradução invalida mesmo, então o id novo é correto).

Regras de literal vs traduzível:
  - célula/item que é Tapi puro (só ptkmns/aiu + pontuação) → literal
  - item de lista "`tapi` = tradução" → split: tapi literal, tradução string
  - resto → string traduzível (backticks preservados; tradutor mantém)

Uso:
    python3 tools/gerar_manual_json.py
"""

import hashlib
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
MANUAL = BASE / "manual.md"
OUTDIR = BASE / "docs" / "manual"

RE_TAPI_PURO = re.compile(r"^[`*ptkmnsaiu\s\-–,.…!?:;()\d]+$")
RE_LICAO = re.compile(r"^## (Lição \d+ — .+|Lição \d+.*)$")
RE_ITEM_GLOSS = re.compile(r"^`([^`]+)`\s*=\s*(.+)$")


def eh_tapi_puro(s: str) -> bool:
    s2 = s.strip()
    if s2.strip("`") in set("ptkmnsaiu"):  # letra isolada (tabela de sons)
        return True
    return bool(s2) and bool(RE_TAPI_PURO.match(s2)) and any(c in "aiu" for c in s2)


class Extrator:
    def __init__(self):
        self.strings: dict[str, str] = {}
        self.licao_atual = 0

    def ref(self, texto: str) -> str:
        """Registra string traduzível, retorna id."""
        texto = texto.strip()
        h = hashlib.md5(texto.encode()).hexdigest()[:8]
        sid = f"l{self.licao_atual}.{h}"
        self.strings[sid] = texto
        return sid

    def celula(self, texto: str):
        """Célula de tabela: literal se Tapi puro, senão traduzível."""
        t = texto.strip()
        if eh_tapi_puro(t):
            return {"lit": t.replace("`", "")}  # já renderiza como código
        return {"t": self.ref(t)}

    def item_lista(self, texto: str):
        m = RE_ITEM_GLOSS.match(texto.strip())
        if m and eh_tapi_puro(m.group(1)):
            return {"tapi": m.group(1), "t": self.ref(m.group(2))}
        if eh_tapi_puro(texto):
            return {"lit": texto.strip()}
        return {"t": self.ref(texto)}


def parse():
    ex = Extrator()
    lessons = []
    intro_blocks = []
    licao = None
    secao = None
    linhas = MANUAL.read_text(encoding="utf-8").split("\n")

    def blocos_alvo():
        if secao is not None:
            return secao["blocks"]
        if licao is not None:
            return licao["intro"]
        return intro_blocks

    i = 0
    while i < len(linhas):
        ln = linhas[i]

        if ln.startswith("## "):
            titulo = ln[3:].strip()
            ex.licao_atual = len(lessons) + 1
            licao = {"id": ex.licao_atual, "title": ex.ref(titulo), "intro": [], "sections": []}
            lessons.append(licao)
            secao = None
            i += 1
            continue

        if ln.startswith("### "):
            if licao is None:
                i += 1
                continue
            secao = {"title": ex.ref(ln[4:].strip()), "blocks": []}
            licao["sections"].append(secao)
            i += 1
            continue

        if ln.startswith("| "):
            # tabela: header | separador | linhas
            tab = []
            while i < len(linhas) and linhas[i].startswith("|"):
                tab.append([c.strip() for c in linhas[i].strip("|").split("|")])
                i += 1
            if len(tab) >= 2:
                header = [ex.celula(c) for c in tab[0]]
                rows = [[ex.celula(c) for c in r] for r in tab[2:]]
                blocos_alvo().append({"type": "table", "header": header, "rows": rows})
            continue

        if re.match(r"^- ", ln):
            itens = []
            while i < len(linhas) and re.match(r"^- ", linhas[i]):
                itens.append(ex.item_lista(linhas[i][2:]))
                i += 1
            blocos_alvo().append({"type": "ul", "items": itens})
            continue

        if re.match(r"^\d+\. ", ln):
            itens = []
            while i < len(linhas) and re.match(r"^\d+\. ", linhas[i]):
                itens.append(ex.item_lista(re.sub(r"^\d+\. ", "", linhas[i])))
                i += 1
            blocos_alvo().append({"type": "ol", "items": itens})
            continue

        if ln.strip() and not ln.startswith("#") and ln.strip() != "---":
            # parágrafo (junta linhas contíguas)
            par = [ln.strip()]
            i += 1
            while i < len(linhas) and linhas[i].strip() and not re.match(r"^(\||#|-|\d+\. |---)", linhas[i]):
                par.append(linhas[i].strip())
                i += 1
            texto = " ".join(par)
            if eh_tapi_puro(texto):
                blocos_alvo().append({"type": "p", "lit": texto})
            else:
                blocos_alvo().append({"type": "p", "t": ex.ref(texto)})
            continue

        i += 1

    return {"lessons": lessons}, ex.strings


def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    skel, strings = parse()
    (OUTDIR / "lessons.json").write_text(
        json.dumps(skel, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    (OUTDIR / "pt.json").write_text(
        json.dumps(strings, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")

    # línguas: preserva traduções existentes cujas chaves ainda existem
    for lang in ("en", "es", "zh", "ja"):
        f = OUTDIR / f"{lang}.json"
        antigas = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
        mantidas = {k: v for k, v in antigas.items() if k in strings}
        f.write_text(json.dumps(mantidas, ensure_ascii=False, indent=1, sort_keys=True),
                     encoding="utf-8")
        print(f"{lang}.json: {len(mantidas)}/{len(strings)} traduzidas")

    n_licoes = len(skel["lessons"])
    print(f"lessons.json: {n_licoes} lições · pt.json: {len(strings)} strings")


if __name__ == "__main__":
    main()
