#!/usr/bin/env python3
"""
Gera amostras de áudio para fonemas e palavras Tapi usando `say` (macOS).

Saída em audio/:
  audio/fonemas/01_a.aiff ... 09_s.aiff   (9 fonemas)
  audio/silabas/pa.aiff ... su.aiff       (18 sílabas)
  audio/palavras/<palavra>.aiff           (50 palavras-amostra)
  audio/manifest.tsv                      (índice tab-separated)

Uso:
    python3 gerar_audio.py              # gera tudo
    python3 gerar_audio.py --voice Luciana    # voz pt-BR específica
    python3 gerar_audio.py --list-voices      # lista vozes disponíveis

Vozes recomendadas pt-BR no macOS: Luciana, Felipe.
"""

import csv
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
AUDIO_DIR = ROOT / "audio"
LEXICO = ROOT / "lexico.tsv"

FONEMAS = ["a", "i", "u", "p", "t", "k", "m", "n", "s"]
CONSOANTES = ["p", "t", "k", "m", "n", "s"]
VOGAIS = ["a", "i", "u"]


def vozes_disponiveis() -> list[str]:
    r = subprocess.run(["say", "-v", "?"], capture_output=True, text=True)
    return [l.split()[0] for l in r.stdout.splitlines() if l.strip()]


def say(texto: str, saida: Path, voz: str) -> None:
    saida.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["say", "-v", voz, "-o", str(saida), texto],
        check=True,
        capture_output=True,
    )


def carregar_palavras_amostra(n: int = 50) -> list[tuple[str, str]]:
    """Pega n raízes puras (CV.CV) variadas para cobertura fonética."""
    raizes = []
    with LEXICO.open(encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader, None)
        for linha in reader:
            if not linha or len(linha) < 3:
                continue
            tapi = linha[0].strip()
            sig = linha[2].strip()
            classe = linha[1].strip()
            if "-" in tapi or len(tapi) != 4:
                continue
            if classe in ("part", "suf", "pref"):
                continue
            raizes.append((tapi, sig.split(" (")[0]))
    # pega n distribuídos
    if len(raizes) <= n:
        return raizes
    passo = len(raizes) // n
    return [raizes[i * passo] for i in range(n)]


def main() -> None:
    if "--list-voices" in sys.argv:
        for v in vozes_disponiveis():
            print(v)
        return

    voz = "Luciana"
    if "--voice" in sys.argv:
        idx = sys.argv.index("--voice")
        voz = sys.argv[idx + 1]

    if shutil.which("say") is None:
        sys.exit("Erro: comando `say` indisponível (este script requer macOS)")

    if voz not in vozes_disponiveis():
        sys.exit(f"Erro: voz '{voz}' não encontrada. Use --list-voices.")

    print(f"Gerando áudio com voz: {voz}")

    manifest = []

    # 1) Fonemas
    print("Fonemas...")
    for i, f in enumerate(FONEMAS, 1):
        saida = AUDIO_DIR / "fonemas" / f"{i:02d}_{f}.aiff"
        say(f, saida, voz)
        manifest.append(("fonema", f, str(saida.relative_to(ROOT))))

    # 2) Sílabas (18 CV)
    print("Sílabas...")
    for c in CONSOANTES:
        for v in VOGAIS:
            sil = c + v
            saida = AUDIO_DIR / "silabas" / f"{sil}.aiff"
            say(sil, saida, voz)
            manifest.append(("silaba", sil, str(saida.relative_to(ROOT))))

    # 3) Palavras
    print("Palavras-amostra...")
    palavras = carregar_palavras_amostra(50)
    for tapi, sig in palavras:
        saida = AUDIO_DIR / "palavras" / f"{tapi}.aiff"
        say(tapi, saida, voz)
        manifest.append(("palavra", tapi, str(saida.relative_to(ROOT))))

    # 4) Manifest
    manifest_path = AUDIO_DIR / "manifest.tsv"
    with manifest_path.open("w", encoding="utf-8") as f:
        f.write("tipo\ttoken\tcaminho\n")
        for tipo, tok, caminho in manifest:
            f.write(f"{tipo}\t{tok}\t{caminho}\n")

    print(f"\nGerados {len(manifest)} arquivos em {AUDIO_DIR}/")
    print(f"Manifest: {manifest_path}")
    print("\nConverter para mp3 (opcional, requer ffmpeg):")
    print(f"  find {AUDIO_DIR} -name '*.aiff' -exec sh -c 'ffmpeg -y -i \"$0\" \"${{0%.aiff}}.mp3\"' {{}} \\;")


if __name__ == "__main__":
    main()
