# Roadmap Tapi

## v0.6 — Fechado

### Infraestrutura
- [x] `git init` + repositório GitHub público
- [x] Landing page estática (HTML+CSS, 1 página) em `docs/`
- [x] Logo SVG
- [x] Licença explícita MIT
- [x] Mini-conjugador online (JS)
- [ ] Comprar e ativar tapilang.com (CNAME pronto)
- [ ] Habilitar GitHub Pages em Settings → Pages → main/docs

### Validação
- [x] Revisão linguística automática (dedup, fonologia, V.CV exceção documentada — v0.7)
- [x] Áudio gerado dos 9 fonemas + 18 sílabas + 50 palavras-amostra (via `gerar_audio.py`, TTS)
- [ ] Revisão por linguista humano
- [ ] Teste com 1-2 falantes voluntários
- [ ] Áudio gravado por humano (substitui TTS — qualidade superior)

### Conteúdo
- [x] 3 contos curtos (Kipi i Puka, Sapu i Sani, Kuni-puku i Pinu)
- [x] 10 diálogos cotidianos adicionais
- [x] 20 provérbios novos
- [x] FAQ do idioma (`faq.md`)

### Léxico expansão
- [x] Termos jurídicos, médicos, esportes, internet/redes sociais

## v0.7 — Fechado (2026-05-22)

### Ferramentas
- [x] Conjugador online standalone (`docs/conjugador.html`)
- [x] Gerador automático de `dicionario_pt_tapi.md`
- [x] Gerador automático de `anki_tapi.tsv`
- [x] Tradutor melhorado (`tradutor.py`): detecta sufixos verbais, evidenciais, imperativo, voz média, plural, compostos
- [x] API REST stdlib (`api.py`): `/health`, `/conjugate`, `/lookup`, `/translate`
- [x] Gerador de áudio TTS (`gerar_audio.py`): 9 fonemas + 18 sílabas + 50 palavras-amostra (macOS `say`)
- [ ] Wiki colaborativa (decisão de plataforma)

### Pedagogia
- [x] Manual com 20 lições (causativo, voz, evidencial, honoríficos, subordinação, comparativo, numerais, calendário, conversação, criação de palavras)
- [x] Modo interlíngua (`tapi_basico.md`): 150 raízes core + 8 regras + pivot PT/EN/ES
- [x] Catálogo de palavras intraduzíveis (`palavras_intraduziveis.md`): 30 conceitos resolvidos por composição
- [ ] Audiolivro das lições
- [ ] Vídeo introdutório YouTube (5 min)
- [ ] Deck Anki oficial publicado online

### Linguística
- [x] Exceção V.CV documentada (`fonologia.md`): 5 verbos primários como lista fechada
- [x] Lexicon dedup + glosses padronizados (v0.7)

### Comunidade
- [ ] Discord ou Telegram público
- [ ] r/tapi no Reddit
- [ ] Submeter a Conlang Atlas of Language Structures (CALS)
- [ ] Submeter a Language Creation Society

## v0.8 — Curto prazo (próximos 3 meses)

### Camada IA (prioridade 3 da estratégia)
- [ ] Tradutor LLM PT↔Tapi (usa `lexico.tsv` como contexto)
- [ ] Gerador de compostos: input "conceito" → output composição justificada
- [ ] Validador fonológico CLI (rejeita raízes inválidas)
- [ ] Detector de colisão semântica (avisa quando nova raiz fica perto de existente)
- [ ] Chat tutor no site (`docs/`)
- [ ] Tradutor com regras gramaticais (sem LLM, fallback determinístico)

### Ferramentas dev
- [ ] API REST mínima: `/conjugate`, `/translate`, `/lookup`
- [ ] Exporters: JSON, XML, LIFT (Lexique Pro)
- [ ] Tokenizador / parser de compostos
- [ ] Métricas linguísticas (distribuição de raízes, frequência, entropia)

### Léxico
- [ ] Meta v0.8: 1.500 entradas (atual: 693). Foco em compostos de domínios cotidianos (cozinha, transporte, escritório, emoções)
- [ ] Reverso EN, ES, ZH, JA (atual: só PT)

## v0.9 — Médio prazo (6-12 meses)

### Plataforma
- [ ] Curso interativo online (estilo Duolingo)
- [ ] App mobile básico (Tapi-PT, PT-Tapi)
- [ ] Corpus paralelo Tapi↔PT/EN para treinar modelo

### Conteúdo cultural
- [ ] Romance curto em Tapi (5.000 palavras+)
- [ ] 20 poemas
- [ ] Música original em Tapi
- [ ] Filme curto narrado em Tapi (legendado)

### Linguística avançada
- [ ] Gramática descritiva acadêmica (formato linguistic typology)
- [ ] Tipologia documentada (alinhamento, ordem, marcação)
- [ ] Comparação com famílias linguísticas reais
- [ ] Artigo publicado em revista de conlangs

## v1.0 — Estabilização (12-24 meses)

- [ ] Fonologia e gramática congelados (não muda mais)
- [ ] Léxico ≥ 5.000 entradas
- [ ] Manual definitivo publicado em PDF
- [ ] Site oficial completo
- [ ] Comunidade ativa ≥ 50 pessoas
- [ ] Pelo menos 3 falantes fluentes
- [ ] Material didático abundante

## v2.0+ — Futuro distante (visão)

- [ ] Wikipédia em Tapi
- [ ] Tradução de livro famoso (Pequeno Príncipe, Alice no País das Maravilhas)
- [ ] Eventos físicos (encontros, retreats de imersão)
- [ ] Reconhecimento por órgãos linguísticos (ISO 639-3 code)
- [ ] Uso ficcional em RPG, jogo, filme
- [ ] Material didático para crianças
- [ ] LLM treinado em Tapi (geração nativa)

## Princípios de evolução

1. **Estabilidade no núcleo**: fonologia e gramática essencial não mudam.
2. **Flexibilidade no léxico**: palavras se adicionam livremente.
3. **Composição sobre invenção**: preferir compostos sempre que possível.
4. **Documentação em primeiro lugar**: toda mudança vai ao CHANGELOG.
5. **Comunidade decide**: reformas grandes precisam consenso.
6. **Sem emojis no idioma**: emoji é auxílio pedagógico opcional, nunca palavra.

## Estratégia de prioridades

Ordem ideal recomendada (Maio/2026):

1. **Consolidar idioma** (fonologia, gramática, dedup léxico) — v0.7 ✅
2. **Modo interlíngua** (subset de aprendizado rápido) — v0.7 ✅
3. **Camada IA** (tradutor/gerador/validador LLM) — v0.8 🟡 próximo

## Métricas de sucesso

| Métrica | Atual (v0.7) | Meta v0.8 | Meta v1.0 | Meta v2.0 |
|---------|-------------:|----------:|----------:|----------:|
| Palavras | 693 | 1.500 | 5.000 | 30.000 |
| Textos | ~10 | 25 | 50 | 500 |
| Falantes | 0 | 1 | 3 | 100 |
| Stars GitHub | 0 | 30 | 100 | 1.000 |
| Visitas/mês site | 0 | 200 | 1.000 | 50.000 |
