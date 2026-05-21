# Como Contribuir para o Tapi

Tapi é projeto aberto. Toda contribuição é bem-vinda.

## Tipos de contribuição

### Adicionar palavra ao léxico
1. Confirmar que a palavra **não existe** ainda (busque em `lexico.tsv` e `dicionario_pt_tapi.md`)
2. Verificar fonologia: raiz nova deve ser CVCV (6 cons + 3 vog, sem clusters, sem coda)
3. Verificar **não-colisão** com raízes/partículas existentes
4. Preferir **composição** sobre raiz nova (compostos com hífen são livres)
5. Adicionar linha em `lexico.tsv` com formato: `palavra<TAB>classe<TAB>significado<TAB>notas`
6. Adicionar entrada correspondente em `dicionario_pt_tapi.md`

### Corrigir erro
- Léxico inconsistente: abrir issue ou PR com correção
- Erro na gramática: revisar `gramatica.md` ou `gramatica_avancada.md` e propor fix
- Tradução errada nos textos: corrigir em `exemplos.md` ou `textos.md`

### Adicionar texto traduzido
- Adicionar a `textos.md` com glosa interlinear
- Manter formato: linha 1 = Tapi, linha 2 = análise, linha 3 = tradução

### Propor reforma estrutural (grande)
- Abrir issue antes de qualquer PR
- Justificar mudança com exemplos concretos
- Reformas fonológicas/gramaticais exigem **consenso** (mínimo 3 contribuidores ativos concordando)

### Criar conteúdo cultural
- Provérbios, mitos, festividades em `cultura.md`
- Diálogos, contos, poemas em `textos.md`
- Manter coerência com universo já estabelecido

## Regras gerais

### Sons permitidos
```
Consoantes: p, t, k, m, n, s
Vogais: a, i, u
```
**Qualquer outro som é proibido** em raízes novas.

### Estruturas válidas
- Raízes: CV.CV estrito (ex: `tapi`, `kama`)
- Sufixos: CV (ex: `-ta`, `-ka`) ou C isolado em pluralização (`-n`)
- Partículas: V ou CV (ex: `i`, `pa`, `mu`)
- Compostos: raiz-raiz com hífen (ex: `tunu-puka`)

### Princípio de não-duplicação
Preferir composição. Coine raiz nova **apenas** se conceito não puder ser composto naturalmente.

### Princípio de não-colisão
Toda raiz nova deve ser checada contra `lexico.tsv` antes de adicionar.

## Governança

- Decisões pequenas (palavras, frases): merge livre por mantenedor
- Decisões médias (gramática extensiva): votação simples
- Decisões grandes (fonologia, ortografia): consenso amplo

## Versionamento

Sigo [SemVer](https://semver.org):
- **MAJOR** (1.0.0): mudança fonológica/gramatical incompatível
- **MINOR** (0.X.0): adição de feature gramatical retrocompatível
- **PATCH** (0.0.X): novas palavras, correções de léxico

## Código de Conduta

- Respeite contribuidores
- Critique ideias, não pessoas
- Falantes de qualquer língua nativa bem-vindos

## Setup local

```bash
git clone https://github.com/<você>/tapi.git
cd tapi
# Não há build. Documentação em Markdown.
# Scripts Python para conjugar/traduzir:
python3 conjugador.py ama
python3 tradutor.py pt2tapi "casa"
python3 gerar_anki.py
```

## Contato

(A definir: Discord, GitHub Discussions, etc.)
