# Gramática Tapi

## Tipologia

- **Ordem**: SVO
- **Morfologia**: aglutinante (sufixos curtos em raízes CVCV)
- **Alinhamento**: nominativo-acusativo
- **Marcação**: no núcleo
- **Modificadores pós-nominais** (adjetivo segue substantivo)

## Pronomes pessoais

| Pessoa | Singular | Plural |
|--------|----------|--------|
| 1      | mi       | nupi   |
| 2      | tu       | mupi   |
| 3      | si       | kupi   |

### Reflexivos
Adicionar sufixo `-ku` ao pronome.
- `mi-ku` = a mim mesmo
- `si-ku` = a si mesmo
- `mi tika mi-ku` = "eu me vejo"

### Recíprocos
Partícula `tatu` (lit: "um-outro") antes do verbo.
- `kupi tatu ama` = "eles se amam (mutuamente)"

### Vocativo
Partícula `na` antes do nome, sem flexão.
- `na Chen, una!` = "Chen, venha!"
- `na papi!` = "ó pai!"

## Partículas

| Forma | Função              |
|-------|---------------------|
| ni    | de/posse            |
| mu    | agente (voz passiva) |
| pa    | negação (pré-verbal)|
| ku    | pergunta (fim de frase) |
| na    | vocativo (pré-nominal) |
| i     | e                   |
| a     | ou                  |
| asi   | se (condicional)    |
| miku  | porque              |
| upa   | quando (subord.)    |
| pamu  | enquanto            |
| sa    | mais... que (compar.) |
| sami  | o mais (superlativo) |
| tatu  | recíproco           |
| ta    | relativo (que/qual) |

## Demonstrativos

Sistema tripartite:

| Função  | Próximo (do falante) | Médio (do ouvinte) | Distante |
|---------|----------------------|--------------------|----|
| Objeto  | mata                 | mati               | maku |
| Lugar   | muta                 | muki               | muna |

## Interrogativos

| Palavra  | Significado |
|----------|-------------|
| nima     | quem        |
| nipi     | o que       |
| nika     | onde        |
| niku     | quando      |
| napa     | quanto      |
| nima-pa  | como        |
| nima-tu  | por que     |

In situ + opcional `ku` no fim para reforço.

## Substantivos

### Plural
Sufixo `-n`.
- `kama` → `kaman` (casas)

### Posse
`possuidor ni possuído`.
- `mi ni kama` = minha casa
- `papi ni nimi` = nome do pai

### Distinção contável/incontável
Sem marcação morfológica. Incontáveis usam quantificador (`napa` = muito, `puku` = pouco).
- `napa mina` = muita água
- `puku tama` = poucas palavras

## Verbos

### Slots de sufixo (ordem fixa)

```
RAIZ + TEMPO + ASPECTO
```

Para evitar clusters, vogal epentética `i` insere-se entre dois sufixos consonantais.

| Slot | Sufixos |
|------|---------|
| Tempo    | — (pres), -ta (pass), -ka (fut) |
| Aspecto  | -sa (hab), -ma (prog), -pa (perf) |

Sufixos viraram bissilábicos (CV) para nunca gerar clusters.

### Exemplos

| Forma     | Análise                | Significado          |
|-----------|------------------------|---------------------|
| ama       | RAIZ                   | ama                  |
| amata     | RAIZ-PASS              | amou                 |
| amaka     | RAIZ-FUT               | amará                |
| amasa     | RAIZ-HAB               | costuma amar         |
| amama     | RAIZ-PROG              | está amando          |
| amapa     | RAIZ-PERF              | acabou de amar       |
| amatasa   | RAIZ-PASS-HAB          | costumava amar       |
| amakama   | RAIZ-FUT-PROG          | estará amando        |
| amatapa   | RAIZ-PASS-PERF         | tinha acabado de amar (mais-que-perfeito) |
| amakapa   | RAIZ-FUT-PERF          | terá acabado de amar (futuro perfeito) |

### Modais
Modal precede verbo principal (verbo principal sem flexão).
- `mi puni tika` = posso ver
- `tu mika ina` = deves ir
- `si naki mani` = quer comer

Tempo/aspecto flexionam no modal:
- `mi punita tika` = pude ver
- `tu mikaka ina` = terás de ir

### Negação
`pa` antes do verbo ou modal.
- `mi pa amata tu` = não te amei

### Voz passiva
Inversão O-S-V + `pe` antes do agente:
- Ativa: `mati-mati kuta puka` = pessoa pega fogo
- Passiva: `puka mati-mati mu kutata` = "fogo foi pego pela pessoa"

(`mu` partícula dedicada para agente passivo — `ni` agora exclusivo para posse.)

### Imperativo
Sufixo `-ti` no verbo, sem sujeito.
- `mani-ti` = come!
- `pa mani-ti` = não comas!
- `una-ti muta` = vem aqui!

(Sufixo dedicado resolve ambiguidade com indicativo.)

### Cópula

Verbo dedicado `ipa` (ser/estar).

Predicação adjetival: cópula opcional.
- `kama panu` = casa (é) bela
- `kama ipa panu` = casa é bela (enfático)

Predicação nominal: cópula obrigatória.
- `Chen ipa mati-mati` = "Chen é pessoa"
- `mi ipa tapi-mati-mati` = "eu sou falante de Tapi"

Localização: cópula obrigatória.
- `mi ipa muta` = "estou aqui"
- `kama ipa muna` = "casa está ali"

Flexão normal:
- `ipata` = foi/era
- `ipaka` = será

## Adjetivos

Seguem substantivo. Concordância em número.
- `kama panu` = casa bela
- `kaman panun` = casas belas

### Comparativo
`X [adj] sa Y` = "X é mais [adj] que Y"
- `mi tipi sa tu` = sou maior que você

### Superlativo
`sami [adj]` antes ou `[adj] sami` depois.
- `sami tipi` = o maior
- `kama panu sami` = a casa mais bela

### Intensificadores
- `tipi` (muito) como advérbio antes do adjetivo: `tipi panu` = muito belo
- `puku` (pouco) similar: `puku panu` = pouco belo

## Numerais

### Cardinais (1-10)

| 1   | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9    | 10   |
|-----|----|----|----|----|----|----|----|------|------|
| tani| pi | ti | pu | ka | ma | na | nu | pina | nuna |

### Acima de 10

Composição aditiva (dezena + unidade):
- 11 = `nuna-tani`
- 15 = `nuna-ka`
- 19 = `nuna-pina`

Multiplicativa para múltiplos de 10:
- 20 = `pi-nuna` (dois-dez)
- 30 = `ti-nuna`
- 50 = `ka-nuna`
- 99 = `pina-nuna-pina`

Centena: `pakuna` (raiz nova)
- 100 = `pakuna`
- 200 = `pi-pakuna`
- 250 = `pi-pakuna ka-nuna`

Milhar: `tikuna`
- 1000 = `tikuna`
- 1.234 = `tikuna pi-pakuna ti-nuna-pu`

### Ordinais

Prefixo `ku-` ao cardinal.
- ku-tani = primeiro
- ku-pi = segundo
- ku-nuna = décimo

## Cláusulas relativas

Partícula `ta` introduz a relativa, segue o antecedente.

```
mati-mati  ta  unata
pessoa     REL veio
"a pessoa que veio"
```

```
kama   ta  mi  mipa  muna
casa   REL 1SG morar ali
"a casa onde eu moro ali"
```

```
tama   ta  tu  takata
palavra REL 2SG dizer.PASS
"a palavra que você disse"
```

Sujeito da relativa: `ta` ocupa a posição.
Objeto da relativa: `ta` na posição, resto da oração intacto.
Adjuntos: `ta` + advérbio/preposição interna.

## Conjunções e subordinação

Subordinada após principal:
- `mi ina kama miku puka pini` = vou pra casa porque fogo (está) frio
- `asi tu una, mi naki tika tu` = se vieres, quero te ver
- `mi kima upa tu unata` = sei quando vieste

## Acento

### Raízes
- Penúltima sílaba sempre

### Compostos (raiz + raiz com hífen)
- Acento primário na **última** raiz
- Acento secundário na primeira
- `tunu-puka` → [ˌtu.nu.ˈpu.ka]
- `tapi-mati-mati` → [ˌta.pi.ˌma.ti.ˈma.ti]

### Verbos com sufixo
- Acento mantém-se na penúltima da raiz
- `amata` → [ˈa.ma.ta] (não amata)
- `amatasa` → [ˈa.ma.ta.sa]

## Sintaxe esquemática

```
[VOC?] [Demonstrativo?] [Numeral?] [Sujeito] [Adjetivos]
       [NEG?] [Modal?] [Verbo+TEMPO+ASPECTO]
       [Objeto] [Adjuntos] [Relativa?] [Subordinada?] [Q?]
```

Exemplo completo:
```
na   Chen,   mata   ti    kaman    panun   wa   tu   patuta   ipa   tina-sami   ku
VOC  Chen    estas  três  casa.PL  belo.PL REL  2SG  fazer.PASS COP  bom-SUP    Q
"Chen, estas três casas belas que você fez são as melhores?"
```
