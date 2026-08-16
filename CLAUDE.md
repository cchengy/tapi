# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project nature

This is **not a software project** — it is a constructed language (conlang) called **Tapi**, documented primarily in Markdown and TSV. Most "work" here is editing linguistic data files, not writing code. The three Python scripts are tiny utilities (no dependencies beyond stdlib, no build, no tests, no linter).

Primary user-facing language is **Portuguese** (pt-BR). Keep edits to docs, dictionary glosses, and commit messages consistent with the existing Portuguese voice unless explicitly editing the `docs/` site i18n.

## Commands

No build, no test suite, no package manager. All scripts use Python 3 stdlib only.

```bash
# Conjugate a verbal root (prints full tense × aspect table + evidentials)
python3 conjugador.py <raiz>           # e.g. python3 conjugador.py ama

# Translation against lexico.tsv (with morphological analysis Tapi→PT:
# detects -ta/-ka tense, -sa/-ma/-pa aspect, evidentials -ni/-ni-ni/-ni-ku,
# imperative -ti, voz média -ku, plural -n, and composto decomposition)
python3 tradutor.py pt2tapi "casa do pai"
python3 tradutor.py tapi2pt "mi manita kasi tina"

# REST API (localhost, stdlib only) — endpoints /health /conjugate /lookup /translate
python3 api.py 8080 127.0.0.1
# curl http://localhost:8080/conjugate?raiz=ama
# curl 'http://localhost:8080/translate?direction=tapi2pt&text=mi+manita'

# Generate audio samples via macOS `say` (9 phonemes + 18 syllables + 50 words → audio/)
python3 gerar_audio.py                  # default voice: Luciana (pt-BR)
python3 gerar_audio.py --list-voices    # list available voices
python3 gerar_audio.py --voice Felipe   # use specific voice

# Regenerate anki_tapi.tsv from lexico.tsv (run after lexicon edits)
python3 gerar_anki.py

# Regenerate dicionario_pt_tapi.md from lexico.tsv (run after lexicon edits)
python3 gerar_dicionario_pt.py

# Validate lexico.tsv (phonology, CV.CV shape, duplicates, orphan compound roots)
python3 tools/validar_lexico.py          # exit 1 on error; --strict promotes warnings

# Regenerate docs/manual/{lessons,pt}.json from manual.md (run after manual edits)
python3 tools/gerar_manual_json.py
```

Production deploy of the site (Server 2, Portainer stack `tapilang`, Traefik, tapilang.com):

```bash
./deploy.sh              # build+push image (arm64) + create/update stack
SKIP_BUILD=1 ./deploy.sh # stack only
```

The static site lives in `docs/` and is served as plain HTML/CSS/JS — open `docs/index.html` directly in a browser, or rely on GitHub Pages (`docs/CNAME` = tapilang.com). No build step.

## Architecture

### Two coupled data sources

`lexico.tsv` is the **canonical lexicon**. Columns: `palavra<TAB>classe<TAB>significado<TAB>notas`. Both Python utilities and `dicionario_pt_tapi.md` derive from it:

- `tradutor.py` loads `lexico.tsv` and builds both directions (Tapi↔PT) in memory each run. The PT key is `significado.split(" (")[0].strip().lower()` — anything before a parenthetical gloss.
- `gerar_anki.py` reads `lexico.tsv`, skips entries whose `palavra` starts or ends with `-` (affixes), and writes `anki_tapi.tsv`. Regenerate after every lexicon edit.
- `gerar_dicionario_pt.py` reads `lexico.tsv` and writes `dicionario_pt_tapi.md`. The reverse dictionary is now **auto-generated** — do not edit it by hand. Regenerate after every lexicon edit. Splits Portuguese keys on `/` so a single Tapi entry like `meaning_a / meaning_b` produces two reverse entries.

### Conjugation model (encoded in `conjugador.py`)

Verb forms are root + tense suffix + aspect suffix, optionally followed by evidential clitics:

- Tenses: presente `""`, passado `ta`, futuro `ka`
- Aspects: simples `""`, habitual `sa`, progressivo `ma`, perfectivo `pa`
- Evidentials (appended with `-`): direto `""`, inferido `-ni`, reportado `-ni-ni`, duvidoso `-ni-ku`
- Special forms: imperativo `raiz-ti`, voz média/reflexivo `raiz-ku`

If you change any of these tables in `conjugador.py`, also update `conjugacao.md` and `gramatica.md` so the grammar docs stay authoritative.

### Phonological constraints (hard rules)

Any new root added to `lexico.tsv` MUST satisfy:

- Consonants only from `{p, t, k, m, n, s}`, vowels only from `{a, i, u}`
- Root shape is strict **CV.CV** (no clusters, no codas)
- Suffix shape is CV, or a bare `n` for pluralization; particles are V or CV
- Compounds use `raiz-raiz` with hyphen (free to coin)
- Prefer composition over coining new roots; check non-collision against `lexico.tsv` before adding

Enforced by `tools/validar_lexico.py` (run it after any lexicon edit). Documented exceptions (closed lists): V.CV primary verbs (`ipa`, `ipi`, `ama`, `ina`, `una`) and trisyllabic numerals (`pakuna`, `tikuna`) — see `fonologia.md`.

Polysemy/homonymy lives in ONE line per word: `significado_a/significado_b (notas)` — never two rows with the same `palavra` (the validator rejects duplicates; `gerar_dicionario_pt.py` splits alternatives on `/`, and the parenthetical must come last because reverse keys are cut at the first `(`).

### Doc layout

- Linguistic spec: `fonologia.md`, `ortografia.md`, `gramatica.md`, `gramatica_avancada.md`, `conjugacao.md`, `referencia.md`
- Lexicon: `lexico.tsv` (canonical), `dicionario_pt_tapi.md` (reverse, hand-kept in sync)
- Corpus: `exemplos.md`, `textos.md` — glossed in three lines: Tapi / análise / tradução
- Pedagogy & culture: `manual.md` (10 lessons), `cultura.md`
- Site: `docs/` (static, multi-language via `docs/i18n.js`: pt/en/es/zh/ja). Manual as web pages: `docs/manual.html` renders `docs/manual/lessons.json` (structure + all Tapi text, single source) + `docs/manual/{lang}.json` (translatable strings; missing keys fall back to pt). Generated by `tools/gerar_manual_json.py` — do not edit `docs/manual/lessons.json`/`pt.json` by hand; edit `manual.md` and regenerate. `en/es/zh/ja.json` ARE hand-translated (the generator preserves still-valid keys).
- Meta: `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `ROADMAP.md`

## Editing rules from CONTRIBUTING.md worth surfacing

- Adding a word: verify it doesn't already exist in `lexico.tsv` **and** `dicionario_pt_tapi.md`; verify phonology; check non-collision with existing roots/particles; prefer composition; update both files.
- Fonologia/ortografia changes are **breaking** (MAJOR per SemVer). Grammar extensions are MINOR. Lexicon additions are PATCH.
- Reforms to fonologia/gramática require consensus — open an issue first, do not just edit.
- Texts in `textos.md` / `exemplos.md` keep the three-line interlinear gloss format.

## Licensing

Content is **MIT** (see `LICENSE`). Do not remove or weaken license headers/notices.
