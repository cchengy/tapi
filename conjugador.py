#!/usr/bin/env python3
"""
Conjugador Tapi.

Uso:
    python3 conjugador.py <raiz_verbal>
    python3 conjugador.py ama
    python3 conjugador.py tika
"""

import sys

TEMPOS = {
    "presente": "",
    "passado": "ta",
    "futuro": "ka",
}

ASPECTOS = {
    "simples": "",
    "habitual": "sa",
    "progressivo": "ma",
    "perfectivo": "pa",
}

EVIDENCIAIS = {
    "direto": "",
    "inferido": "-ni",
    "reportado": "-ni-ni",
    "duvidoso": "-ni-ku",
}


def conjugar(raiz: str) -> dict:
    """Gera todas as formas conjugadas de uma raiz verbal."""
    formas = {}
    for nome_tempo, suf_t in TEMPOS.items():
        for nome_asp, suf_a in ASPECTOS.items():
            chave = f"{nome_tempo}.{nome_asp}"
            formas[chave] = raiz + suf_t + suf_a
    formas["imperativo"] = raiz + "-ti"
    formas["reflexivo_v_media"] = raiz + "-ku"
    return formas


def conjugar_evid(forma: str) -> dict:
    """Adiciona evidencialidade a uma forma conjugada."""
    return {nome: forma + suf for nome, suf in EVIDENCIAIS.items()}


def imprimir_tabela(raiz: str) -> None:
    print(f"\n=== Conjugação de '{raiz}' ===\n")
    formas = conjugar(raiz)

    print("TEMPO × ASPECTO:")
    print(f"  {'Tempo':<10} | {'Simples':<10} | {'Habitual':<12} | {'Progress.':<12} | {'Perf.':<10}")
    print("  " + "-" * 70)
    for tempo in TEMPOS:
        linha = [
            formas[f"{tempo}.simples"],
            formas[f"{tempo}.habitual"],
            formas[f"{tempo}.progressivo"],
            formas[f"{tempo}.perfectivo"],
        ]
        print(f"  {tempo:<10} | {linha[0]:<10} | {linha[1]:<12} | {linha[2]:<12} | {linha[3]:<10}")

    print(f"\nIMPERATIVO:   {formas['imperativo']}")
    print(f"VOZ MÉDIA:    {formas['reflexivo_v_media']}")

    print("\nEVIDENCIAIS (sobre passado simples):")
    evid = conjugar_evid(formas["passado.simples"])
    for nome, forma in evid.items():
        print(f"  {nome:<12} {forma}")

    print()


def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python3 conjugador.py <raiz_verbal>")
        print("Exemplo: python3 conjugador.py ama")
        sys.exit(1)
    raiz = sys.argv[1].strip().lower()
    imprimir_tabela(raiz)


if __name__ == "__main__":
    main()
