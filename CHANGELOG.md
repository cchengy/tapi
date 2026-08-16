# Changelog Tapi

Formato: [versão] - data - mudanças.

## [v0.7.2] - 2026-08-16

### Adicionado
- Site em produção: `tapilang.com` no Server 2 via Docker/Traefik (`Dockerfile`, `infra/`, `deploy.sh`; stack Portainer `tapilang`). Redirect apex → www. GitHub Pages descontinuado (`docs/CNAME` removido).
- `tools/validar_lexico.py`: validador do `lexico.tsv` — fonologia, forma CV.CV, duplicatas, compostos com raiz órfã, colunas. Exit 1 em erro; `--strict` promove avisos.
- Manual multilíngue no site (`docs/manual.html`): 20 lições navegáveis, esqueleto/tradução separados (`docs/manual/lessons.json` + `{pt,en,es,zh,ja}.json`, texto Tapi único no esqueleto). Extractor: `tools/gerar_manual_json.py`. Traduções en/es/zh/ja pendentes (fallback pt).
- `tradutor.py` pt2tapi: ignora artigos, resolve contrações (do→de, na→em…), lematiza verbos conjugados com marca de tempo (`falou`→`takata`), plural PT -s → Tapi -n, chaves PT alternativas separadas por `/`.
- Manual traduzido: `en.json` e `es.json` completos (512 strings cada; zh/ja pendentes). Exemplos de som da Lição 1 localizados por idioma.
- **Reforma numeral**: `pakuna`→`kuna` (cem, raiz CV.CV) e `tikuna`→`kuna-nuna` (mil = cem-dez, padrão multiplicativo X-Y = X×Y). Elimina a exceção trissilábica: raiz fora de CV.CV agora não existe (sobram só os 5 verbos V.CV). Regra: precisou de mais sílabas → composto com hífen.

### Corrigido
- `lexico.tsv`: 14 duplicatas consolidadas em linha única (`significado_a/significado_b (notas)`); derivados regenerados.
- Versão exibida no site/README unificada (estava 0.6 em 12 lugares).
- Issue [#1](https://github.com/cchengy/tapi/issues/1) aberta: homofonia sistêmica partícula × sufixo (8 pares) — decisão de reforma antes do teste com falantes.

## [v0.7.1] - 2026-05-22

### Adicionado
- `tradutor.py` melhorado: detecta sufixos verbais (-ta/-ka/-sa/-ma/-pa), evidenciais (-ni, -ni-ni, -ni-ku), imperativo (-ti), voz média (-ku), plural (-n) e decompõe compostos hifenizados. Saída agora marca morfologia: `mi manita kasi` → `[eu] [comer.passado] [comida]`.
- `api.py`: REST mínima em stdlib. Rotas `/health`, `/conjugate?raiz=X`, `/lookup?word=X`, `/translate?direction=Y&text=Z`. Default bind: localhost.
- `gerar_audio.py`: gera amostras TTS via macOS `say`. 9 fonemas + 18 sílabas CV + 50 palavras-amostra distribuídas → `audio/` + `audio/manifest.tsv`.
- `CLAUDE.md`: seção Commands atualizada com os 3 novos scripts.
- `ROADMAP.md`: v0.7 reorganizado, v0.8 redefinido com foco em camada IA, métricas atualizadas, estratégia de prioridades documentada.

## [v0.7] - 2026-05-22

### Adicionado
- `palavras_intraduziveis.md`: catálogo curado de 30 conceitos "intraduzíveis" em vários idiomas (saudade, schadenfreude, komorebi, wabi-sabi, hygge, lagom, nunchi, toska, iktsuarpok, mamihlapinatapai, fernweh, waldeinsamkeit, tsundoku, sisu, cafuné, sobremesa, jugaad, abbiocco, gezellig, shemomedjamo, wanderlust, thalassophilia, mångata, apricity, ya'aburnee, meraki, mokita, dépaysement, utepils, razliubít) resolvidos por composição transparente — sem novas raízes.
- `lexico.tsv`: +30 compostos correspondentes (todos validados: peças = raízes existentes, fonologia CV.CV limpa).
- `manual.md`: expandido de 10 para 20 lições. Novas lições 11-20 cobrem causativo, voz passiva, evidencialidade, honoríficos, subordinação, comparativo, numerais avançados, calendário, conversação, criação de palavras.

### Regenerado
- `anki_tapi.tsv` (690 cartões)
- `dicionario_pt_tapi.md` (719 entradas)

## [v0.6.1] - 2026-05-22

### Adicionado
- `gerar_dicionario_pt.py`: script que regenera `dicionario_pt_tapi.md` automaticamente a partir de `lexico.tsv`. Resolve a sincronização manual que existia. Dicionário reverso passa de 366 entradas hand-maintained para 689 auto-geradas.
- `docs/conjugador.html`: página standalone do conjugador. Adiciona evidenciais (direto, inferido, reportado, duvidoso), botão copiar tudo, click-to-copy por célula, validação CV.CV, suporte a `?r=<raiz>` na URL, link no `docs/index.html`.

### Mudado
- `dicionario_pt_tapi.md` agora é arquivo gerado. **Não editar à mão** — editar `lexico.tsv` e rodar `python3 gerar_dicionario_pt.py`.

### Relicenciado
- Licença mudou de CC-BY-SA 4.0 para **MIT** (mais permissiva; sem cláusula ShareAlike).

## [v0.6] - 2026-05-22

### Adicionado
- LICENSE (MIT) explícito em arquivo
- Landing page estática em `docs/` (HTML + CSS + logo SVG)
- Mini-conjugador online (JS embarcado, sem dependências)
- Site multi-idioma: pt (padrão), en, es, zh, ja — switcher no header, detecção automática via `navigator.language`, persistência em localStorage
- CNAME para tapilang.com (GitHub Pages)
- Repositório publicado em github.com/cchengy/tapi
- CLAUDE.md (instruções para Claude Code)
- Léxico expandido (+119 entradas): termos jurídicos (advogado, juiz, tribunal, sentença, multa, recurso, contrato, etc.), médicos (cirurgia, gripe, câncer, diagnóstico, órgãos internos, especialidades, depressão, etc.), esportes (basquete, vôlei, tênis, boxe, ciclismo, olimpíada, jogador, treino, gol, placar, árbitro, etc.), internet/redes sociais (site, email, post, comentário, curtir, compartilhar, seguidor, senha, app, chat, emoji, fake news, IA, robô, etc.)
- 3 contos curtos novos: "Kipi i Puka" (A flor e o fogo), "Sapu i Sani" (O mar e a montanha), "Kuni-puku i Pinu" (A criança e a lua) — cada um com glosa e moral
- 10 diálogos cotidianos adicionais (diálogos 6-15): telefone, hospital, escola, trabalho, compras online, pedir ajuda na rua, conhecer alguém novo, viagem, conversa pai-filho, despedida informal
- 20 provérbios novos em `cultura.md` (totalizando 26)
- `faq.md` — perguntas frequentes (geral, fonologia, gramática, léxico, aprendizado, filosofia, técnico)
- `anki_tapi.tsv` regenerado: 660 cartões

## [v0.5] - 2026-05-21

### Adicionado
- Gramática avançada: causativo, evidencialidade, honoríficos, classificadores, inclusivo/exclusivo, dual, mirativo, voz média, frequentativo, registros formais, onomatopeias
- Tabela completa de conjugação verbal
- Manual didático em 10 lições
- Universo cultural completo: calendário (12 meses, 7 dias, 4 estações), festividades, saudações, 6 provérbios, eufemismos, 7 onomatopeias, insultos, nomes próprios, mitologia, sistema de moeda, política de empréstimos
- Léxico expandido (+280 entradas): cores estendidas, família estendida, profissões, tech moderno, anatomia detalhada, emoções, cognição, comida, animais, conceitos abstratos, objetos cotidianos, veículos, direções, meteorológicos
- Cartão de referência rápida (1 página)
- Textos: DUDH Art.1, poema original, conto original, 5 diálogos cotidianos, carta formal, letra de música, adivinhação
- Ferramentas: conjugador.py, tradutor.py, gerar_anki.py
- CHANGELOG, CONTRIBUTING, ROADMAP

## [v0.4] - 2026-05-21

### Adicionado
- Léxico Swadesh 207 (100%)
- Babel (Gn 11:1-9) completo
- Pai Nosso completo
- Dicionário reverso pt→Tapi

### Mudado
- Fonologia: adicionado /s/ (6 cons em vez de 5) para destravar léxico
- Substituídas partículas inválidas: `pe` → `mu` (agente), `wa` → `ta` (relativo)

## [v0.3] - 2026-05-21

### Resolvido (críticos)
- Clusters em sufixos combinados: sufixos viraram bissilábicos (-ta, -ka, -sa, -ma, -pa)
- Sobrecarga de `ni`: separado em `ni` (posse) + `mu` (agente passivo)
- Cláusulas relativas: partícula `ta`
- Cópula: verbo dedicado `ipa`

### Adicionado
- Reflexivo (-ku)
- Recíproco (`tatu`)
- Vocativo (`na`)
- Imperativo (-ti)
- Comparativo / superlativo
- Numerais ordinais (ku-)
- Numerais até milhar
- Tempos compostos

## [v0.2] - 2026-05-21

### Resolvido
- Homófonos no léxico (tunu sol≠morrer, muki noite≠sonhar, etc)
- Conflitos numerais ↔ pronomes

### Adicionado
- Demonstrativos (3 níveis × objeto/lugar)
- Interrogativos (7 formas)
- Modais (poder/dever/querer)
- Aspecto verbal (habitual/progressivo/perfectivo)
- Subordinação (se/porque/quando/enquanto)
- Voz passiva

## [v0.1] - 2026-05-20

### Inicial
- Fonologia: 5 cons + 3 vog
- Ortografia: alfabeto latino
- Raízes bissilábicas CVCV estritas
- Gramática básica SVO aglutinante
- Léxico ~100 palavras
- Nome do idioma: **Tapi** (cunhado dentro do próprio sistema)
- Domínio reservado: tapilang.com
