# Tapi

Idioma construído do zero. Bissilábico, pronunciável universalmente, composicional.

Site: [tapilang.com](https://tapilang.com) (após registro do domínio) — fonte em [docs/](docs/)
Licença: [MIT](LICENSE)
Versão: **v0.6**
Repositório: [github.com/cchengy/tapi](https://github.com/cchengy/tapi)

## Princípios

- **Fonologia mínima**: 6 consoantes (/p, t, k, m, n, s/) + 3 vogais (/a, i, u/)
- **Raízes bissilábicas**: toda raiz = CV.CV
- **Pronunciabilidade 9.5/10**: sons presentes em >95% dos idiomas humanos
- **Sem tons, sem clusters, sem coda em raízes**
- **Gramática aglutinante**: sufixos curtos para tempo, aspecto, plural
- **Composição massiva**: vocabulário cresce combinando raízes

## Arquivos

### Linguística
| Arquivo | Conteúdo |
|---------|----------|
| [fonologia.md](fonologia.md) | Inventário de sons (IPA) |
| [ortografia.md](ortografia.md) | Alfabeto e mapeamento grafema↔fonema |
| [gramatica.md](gramatica.md) | Morfologia, sintaxe básicas |
| [gramatica_avancada.md](gramatica_avancada.md) | Causativo, evidencialidade, honoríficos, etc |
| [conjugacao.md](conjugacao.md) | Tabela completa de conjugação verbal |
| [referencia.md](referencia.md) | Cartão de referência rápida (1 página) |

### Léxico
| Arquivo | Conteúdo |
|---------|----------|
| [lexico.tsv](lexico.tsv) | Dicionário Tapi → Português (~500 entradas) |
| [dicionario_pt_tapi.md](dicionario_pt_tapi.md) | Dicionário Português → Tapi |

### Textos
| Arquivo | Conteúdo |
|---------|----------|
| [exemplos.md](exemplos.md) | Frases (Babel, Pai Nosso) |
| [textos.md](textos.md) | DUDH, poema, conto, diálogos, carta, lullaby, adivinha |

### Pedagogia
| Arquivo | Conteúdo |
|---------|----------|
| [manual.md](manual.md) | Curso introdutório — 10 lições |
| [cultura.md](cultura.md) | Universo cultural (calendário, mitologia, etc) |

### Ferramentas
| Arquivo | Função |
|---------|--------|
| [conjugador.py](conjugador.py) | Gera todas formas verbais de uma raiz |
| [tradutor.py](tradutor.py) | Tradução palavra-a-palavra pt↔Tapi |
| [gerar_anki.py](gerar_anki.py) | Gera deck Anki (TSV) do léxico |

### Meta
| Arquivo | Conteúdo |
|---------|----------|
| [CHANGELOG.md](CHANGELOG.md) | Histórico de versões |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Como contribuir |
| [ROADMAP.md](ROADMAP.md) | Planos futuros |
| [faq.md](faq.md) | Perguntas frequentes |

## Status v0.5

### Núcleo linguístico
- [x] Fonologia (6 cons + 3 vog)
- [x] Ortografia (9 grafemas latinos)
- [x] Gramática essencial (SVO, aglutinante, modais, aspecto, passiva, relativas)
- [x] Gramática avançada (causativo, evidencialidade, honoríficos, classificadores)
- [x] Léxico Swadesh 207 (100%)
- [x] Léxico expandido (~500 entradas via raízes + compostos)
- [x] Cores expandidas (preto, branco, vermelho, verde, amarelo, azul, roxo, laranja, marrom, rosa, dourado, prateado)
- [x] Família estendida (avô, avó, tio, tia, primo, sobrinho, sogro, etc)
- [x] Profissões (médico, professor, agricultor, engenheiro, soldado, artista, etc)
- [x] Tech moderno (computador, internet, telefone, carro, avião, etc)
- [x] Anatomia detalhada (ombro, cotovelo, dedo, costela, etc)
- [x] Emoções (felicidade, tristeza, vergonha, gratidão, etc)
- [x] Cognição (lembrar, esquecer, decidir, duvidar, etc)
- [x] Calendário (12 meses, 7 dias, 4 estações)

### Documentação
- [x] Manual didático (10 lições)
- [x] Tabela completa de conjugação
- [x] Dicionário reverso (pt→Tapi)
- [x] Babel (Gn 11:1-9) completo
- [x] Pai Nosso completo
- [x] Universo cultural (mitologia, festividades, provérbios)
- [x] Sistema de adaptação fonológica de nomes

### Falta (Tier 2/3)
- [ ] Site tapilang.com
- [ ] Conjugador online (script)
- [ ] Tradutor automático básico
- [ ] Mais textos teste (DUDH Art.1, poemas, contos)
- [ ] Audiolivro / pronúncia gravada
- [ ] Repositório git público
- [ ] App mobile / curso interativo

## Nome

**Tapi** = raiz bissilábica dedicada, significando "este idioma / a fala-nossa". Cunhada dentro do próprio sistema fonológico.

## Comparação com outros conlangs

| Idioma | Anos | Palavras | Falantes |
|--------|------|----------|----------|
| Esperanto | 140 | 30.000 | ~2M |
| Klingon | 40 | 3.000 | ~30 |
| Toki Pona | 25 | 137 | ~100 |
| **Tapi** | **2 dias** | **~660** | **0** |

Tapi v0.5 = idioma funcionalmente completo no núcleo. Pronto para uso experimental.
