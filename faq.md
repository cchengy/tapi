# FAQ — Perguntas Frequentes sobre Tapi

## Geral

### O que é o Tapi?
Tapi é um idioma construído (conlang) **bissilábico** e **aglutinante**, projetado do zero para máxima pronunciabilidade universal, composicionalidade e regularidade. Usa apenas 9 sons (6 consoantes + 3 vogais) presentes em mais de 95% das línguas humanas.

### Para que serve o Tapi?
Como qualquer conlang: experimentação linguística, uso ficcional, comunidade hobbyista, estudo de princípios de design de idiomas. Não compete com idiomas naturais — propõe-se como código universal mínimo, fácil de aprender por qualquer pessoa.

### Quem criou o Tapi?
Tapi foi projetado em 2026 por um único autor (cchengy) e publicado como projeto aberto sob licença MIT. A intenção é que a comunidade contribua a partir de v0.6.

### O Tapi é uma língua "natural" ou "artificial"?
**Artificial** (construída). Não tem falantes nativos, não evoluiu organicamente. Toda regra é deliberada e documentada.

### Por que "Tapi"?
`tapi` é uma raiz bissilábica cunhada dentro do próprio sistema fonológico. Significa "este idioma / a fala-nossa" — palavra autorreferente.

---

## Fonologia

### Por que só 9 sons?
Para garantir pronunciabilidade universal. Os 6 consoantes (`p, t, k, m, n, s`) e 3 vogais (`a, i, u`) aparecem em mais de 95% dos idiomas do mundo. Qualquer falante de qualquer língua consegue produzir esses sons com mínimo esforço.

### Tapi tem tons?
**Não.** Sem tons, sem stress fonêmico, sem nasalização vocálica, sem alongamento. Cada sílaba tem o mesmo peso prosódico.

### Por que raízes só CV.CV?
Eliminar clusters consonantais (que travam falantes de línguas como japonês, havaiano, swahili) e codas silábicas (problema para falantes do mandarim, italiano, etc). CV.CV é a estrutura silábica mais comum no mundo.

### Tem `r` ou `l`?
**Não.** /r/ e /l/ são justamente os sons que mais variam entre línguas. Em adaptações fonológicas viram `n` (ex: Maria → `Manina`).

---

## Gramática

### Qual a ordem básica da frase?
**SVO** (sujeito-verbo-objeto), igual ao português e ao inglês.
- `mi ama tu` = eu amo tu

### Como se conjuga um verbo?
Raiz + sufixo de tempo + sufixo de aspecto. Tempos: presente (∅), `-ta` passado, `-ka` futuro. Aspectos: simples (∅), `-sa` habitual, `-ma` progressivo, `-pa` perfectivo. Veja `conjugacao.md`.

### Tapi tem gênero gramatical?
**Não.** Nenhum gênero atribuído a substantivos ou adjetivos. Para distinguir biologicamente: `kuni-papu` (filho-macho), `kuni-mumi` (filho-fêmea).

### Tem artigos?
**Não.** Sem definido/indefinido. Contexto resolve. Para enfatizar: demonstrativos (`mata`, `mati`, `maku`).

### Como se faz plural?
Sufixo `-n` em substantivo ou adjetivo: `mati-mati` → `mati-mati-n` (pessoas).

### Tem casos?
Não no sentido latino. Marcações são feitas por **partículas** independentes: `ni` (posse), `mu` (agente passivo), `mipi` (em), `kami` (com), etc.

---

## Léxico

### Quantas palavras tem o Tapi?
Cerca de **600 entradas** (v0.6). Meta v1.0: 5.000. O léxico cresce principalmente por **composição** (raiz-raiz com hífen), não por novas raízes.

### Como se cria uma palavra nova?
1. Verificar que o conceito não pode ser composto de raízes existentes
2. Se raiz nova for inevitável: deve ser CV.CV com sons válidos
3. Verificar não-colisão com raízes/partículas atuais
4. Adicionar a `lexico.tsv` e a `dicionario_pt_tapi.md` (em lockstep)
5. Veja [CONTRIBUTING.md](CONTRIBUTING.md)

### Por que tantos compostos longos?
Tradeoff consciente: composicionalidade total > brevidade. Em vez de memorizar 30.000 raízes opacas, memoriza-se 500 raízes e regras de composição. Compostos longos podem ser abreviados em uso casual depois.

### Tapi aceita estrangeirismos?
Só após **adaptação fonológica** completa (regras em `cultura.md`). Termos técnicos preferem composição interna. Computador = `kupu-mapu` (não "komputatori").

---

## Aprendizado e uso

### É difícil aprender Tapi?
Provavelmente **mais fácil** do que qualquer idioma natural. Sem irregularidades, sem exceções, sem gênero, sem casos, sem tons, fonologia minimalista. Veja `manual.md` (10 lições) para começar.

### Quanto tempo leva pra falar Tapi básico?
Estimativa: 10-20 horas para nível conversacional (com vocabulário limitado). Comparar com ~600 horas para um falante de português atingir o mesmo nível em mandarim.

### Onde encontro material para estudar?
- `manual.md` — curso introdutório em 10 lições
- `referencia.md` — cartão de referência rápida (1 página)
- `gramatica.md` + `gramatica_avancada.md` — referência completa
- `lexico.tsv` — dicionário Tapi → Português
- `dicionario_pt_tapi.md` — dicionário Português → Tapi
- `anki_tapi.tsv` — deck Anki gerado automaticamente

### Tem áudio?
Ainda não (planejado para v0.7). Por enquanto, leitura segue ortografia 1-para-1 com IPA (`fonologia.md`).

### Tem comunidade?
Em formação. Veja `ROADMAP.md` — Discord/Telegram planejados para v0.7.

---

## Filosofia e política

### Tapi compete com Esperanto / Toki Pona / Lojban?
**Não.** Cada conlang resolve problemas diferentes. Esperanto é europeu-cêntrico, Toki Pona é minimalista filosófico (137 palavras), Lojban é logicamente rigoroso. Tapi prioriza **pronunciabilidade universal + composicionalidade transparente**.

### Tapi é neutro culturalmente?
Tenta. Léxico evita assumir geografia, religião ou tecnologia específicas. Cultura ficcional em `cultura.md` é **opcional** — pode ser ignorada ou substituída.

### Posso usar Tapi comercialmente / em um jogo / num livro?
**Sim**, sob licença MIT:
- Inclua o aviso de copyright e a permissão MIT em cópias substanciais
- Sem garantias; sem restrição a uso comercial; sem obrigação de manter mesma licença em derivados

### Tapi vai mudar?
- **Núcleo (fonologia, ortografia, gramática essencial)**: congelado a partir de v1.0
- **Léxico**: cresce livremente sempre
- Mudanças no núcleo exigem consenso (ver CONTRIBUTING.md)

### Como posso contribuir?
Veja `CONTRIBUTING.md`. Resumo: novas palavras, textos traduzidos, conteúdo cultural, correções, gravação de áudio, tradução do site.

---

## Técnico

### Tem aplicativo / curso interativo?
Ainda não. Planejado para v0.8 (ver ROADMAP).

### O site tapilang.com está no ar?
Em provisionamento. Conteúdo do site em `docs/` (servido via GitHub Pages).

### Onde reportar erros?
Issues no repositório GitHub: github.com/cchengy/tapi/issues

### Tapi tem código ISO 639-3?
Ainda não. Submissão planejada para v2.0+ (requer comunidade ativa).
