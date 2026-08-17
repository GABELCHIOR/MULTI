# MULTI — Johnson & Wichern, Applied Multivariate Statistical Analysis (4ª ed.)

Projeto de estudo autodidata de Análise Multivariada.
Toda a produção é **em português (pt-BR)**.

Este projeto é irmão do `PP_estudo` (Montgomery, DOE): mesma estrutura, mesmo
CSS, mesmo formato de aula. A única diferença de aparência é o tema, que aqui é
**roxo-ametista** em vez de verde-mata.

## O livro

- Arquivo: `Applied Multivariate Statistical Analysis, Fourth Edition.pdf` (16 MB, 828 páginas)
- Johnson, R. A. & Wichern, D. W. — 4ª edição, Prentice Hall, 1998
- 12 capítulos + Apêndice (tabelas) + Data Bank + índices

**Há um segundo PDF na pasta** (6ª edição, 24 MB, 794 páginas). Ele **não serve
para nada aqui**: é um escaneamento puro de TIFF, *sem camada de texto nenhuma*
(`tiff2pdf`), e a paginação é outra. A edição de referência deste caderno
continua sendo a **4ª**, e `extrair.py` prefere explicitamente o arquivo cujo
nome contém "Fourth" — antes ele escolhia o maior arquivo, o que passou a
apontar para a 6ª edição e invalidava todos os offsets.

**É um escaneamento com OCR** (ScanSnap + ClearScan do Acrobat), não um PDF
nativo. Consequências práticas, e as duas importam:

1. A camada de texto reproduz bem a **prosa**, e serve para localizar e ler o
   argumento. Mas **fórmulas, matrizes e índices saem embaralhados**
   (`P-o` para μ₀, `1 1 6` para 116, `LINEA/l` para LINEAR). Nunca copie
   matemática da extração de texto: leia o **recorte de imagem** da página.
2. As figuras não são vetoriais — são os retalhos de bitmap que o OCR não
   reconheceu. `figuras.py` os aglomera, mas o resultado é aproximado; para
   figura importante, recorte à mão com `extrair.py recorte`.

### Offset: NÃO é constante

O escaneamento perdeu duas folhas. O deslocamento cai de 16 para 14 e depois
para 12:

| Páginas do livro | PDF |
|---|---|
| 1 – 174 | livro + 16 |
| **175 – 176** | **ausentes** (meio do cap. 4) |
| 177 – 318 | livro + 14 |
| **319 – 320** | **ausentes** (meio do cap. 6) |
| 321 – 816 | livro + 12 |

Use sempre `livro2pdf()` / `pdf2livro()` de `ferramentas/extrair.py` — nunca uma
constante.

**As quatro páginas foram recuperadas (2026-08-17).** O usuário fotografou a
cópia física; as imagens estão em `paginas-faltantes/livro-175.jpeg`,
`livro-176.jpeg`, `livro-319.jpeg` e `livro-320.jpeg`. A pasta está no
`.gitignore` pela mesma razão do PDF (são páginas inteiras da obra). Leia-as com
a ferramenta Read quando precisar.

- **175–176** (fim da demonstração do Resultado 4.8 e o Exemplo 4.8 inteiro) já
  estão transcritas na seção 3.6 do cap. 4. Nada falta nessa aula.
- **319–320** (tabela ANOVA univariada, Exemplo 6.7 e o início do modelo MANOVA,
  eq. 6-34 e 6-35) esperam o capítulo 6. Já conferidas: legíveis e completas.

## Preferências de estudo definidas

| Item | Decisão |
|---|---|
| Objetivo | Autodidata, base sólida. Percurso **linear do cap. 1 ao 12**, sem prazo. Ênfase em entender de onde vem cada resultado, não em decorar fórmula. |
| Software | **R**. Incluir o código dos exemplos com as funções de base (`cov`, `cor`, `eigen`, `solve`, `cov2cor`) e, quando o assunto pedir, `MASS`, `car`, `psych`, `cluster`. |
| Formato | **Arquivos HTML locais** em `estudo/`. Offline, abertos direto no navegador. Matemática em **MathML nativo** (sem CDN, sem JS). |
| Idioma | Português (pt-BR). Termos técnicos com o original em inglês entre parênteses na primeira ocorrência. |

## Como trabalhar aqui

**Geração sob demanda, capítulo por capítulo.** A cada sessão o usuário escolhe
o próximo capítulo (ou uma seção dele) e eu gero uma página de estudo focada.

Cada página de estudo contém, nesta ordem:

1. **Objetivo da aula** — o que se deve saber fazer ao final
2. **Conceito** em português, com a derivação matemática em MathML
3. **Figuras** recortadas do PDF
4. **Exemplos do livro resolvidos passo a passo**, com o código em R e a saída comentada
5. **Cartões de recall ativo** — pergunta com resposta escondida (`<details>`)
6. **Exercícios selecionados** do fim do capítulo, com gabarito comentado

**Tom das aulas:** professor dando aula, não resumo. O usuário está aprendendo a
matéria do zero — explicar o *porquê* de cada resultado, mostrar as derivações,
antecipar as armadilhas profissionais e ligar cada conceito a onde ele reaparece
nos capítulos seguintes. Nunca comprimir a ponto de virar lista de fórmulas.

**Regra dos números:** todo resultado numérico das resoluções deve ser
*calculado* (numpy/scipy no scratchpad), nunca copiado de memória. Conferir
contra o livro quando houver valor publicado. As saídas de R nas páginas também
precisam bater com o cálculo — **R não está instalado no PATH**, então elas são
escritas à mão a partir dos números conferidos em Python; mantenha-as simples e
com poucas casas para não inventar formatação.

**Ganchos já plantados.** O capítulo 1 termina prometendo que a seção 2.3
responde "quando é que x'Ax > 0?", e o capítulo 2 paga essa dívida
explicitamente. Vários outros ganchos apontam para frente e devem ser retomados
quando o capítulo chegar:

- ~~cos(θ) = r entre colunas centradas → **cap. 3**~~ (pago na seção 2.4 do cap. 3)
- distância de Mahalanobis, (x−μ)'Σ⁻¹(x−μ) como expoente da densidade → **cap. 4**
- Σ⁻¹/² como padronização multivariada; elipses de confiança → **cap. 4 e 5**
- decomposição espectral de S = componentes principais; λ₁ como máximo de x'Sx
  na esfera unitária → **cap. 8**
- autovalores próximos ⇒ autovetores instáveis (Exemplo 2.10) → **cap. 8**
- lema de maximização ⇒ função discriminante de Fisher, x ∝ B⁻¹(μ₁−μ₂) → **cap. 11**
- os quatro axiomas de distância, para julgar medidas de similaridade → **cap. 12**
- Σ₁₂ e o complemento de Schur → **cap. 10**

Ganchos que o **capítulo 4** pagou (2026-08-17):

- ~~distância de Mahalanobis, `(x−μ)'Σ⁻¹(x−μ)` como expoente da densidade~~
  (seção 2.1 do cap. 4)
- ~~`Σ⁻¹/²` como padronização multivariada~~ (seção 3.5, no Resultado 4.7)
- ~~a elipsoide com `c² = χ²ₚ(α)`~~ (seção 2.5)
- ~~`Cov(X̄) = Σ/n` como base do `T²`~~ (seções 3.6 e 5)
- ~~`Σ₁₂` e o complemento de Schur~~ (seção 3.4, no Resultado 4.6) — mas o
  **cap. 10** ainda vai usar a mesma estrutura para a correlação canônica

Ganchos novos, plantados pelo capítulo 4:

- `T²` de Hotelling: a estatística que substitui `Σ` por `S` em
  `n(X̄−μ)'Σ⁻¹(X̄−μ)`, e cuja distribuição exata deixa de ser `χ²` → **cap. 5**
- a média condicional `μ₁ + Σ₁₂Σ₂₂⁻¹(x₂−μ₂)` **é** a regressão linear múltipla,
  e a homocedasticidade sai de graça → **cap. 7**
- plotar `e₁'xⱼ` (maior autovalor de `S`) como diagnóstico de normalidade →
  **cap. 8**
- a Wishart soma graus de liberdade (propriedade 1 de 4-24) — é o que permite
  juntar grupos → **cap. 6**
- a normalidade das observações *individuais* importa em classificação, e o
  limite central não salva → **cap. 11**
- a estrutura de `Σ` (e não só a média) é o objeto da análise fatorial, e aí
  não normalidade dói mesmo com `n` grande → **cap. 9**

Ganchos ainda pendentes, plantados pelo capítulo 3:

- Cov(X̄) = Σ/n é o σ²/n multivariado, e entra no T² de Hotelling → **cap. 5**
- a elipsoide (x−x̄)'S⁻¹(x−x̄) ≤ c², com semi-eixos c√λᵢ nas direções eᵢ de S,
  e c² = χ²ₚ(α) → **cap. 4 e 5**
- |S| = λ₁⋯λₚ; reportar os autovalores separados em vez do produto → **cap. 8**
- autovetor de autovalor nulo denuncia a dependência linear → **cap. 8**
- n ≤ p ⇒ |S| = 0 sempre (Resultado 3.3): o problema de alta dimensão
- traço, e não determinante, na "proporção de variância explicada" → **cap. 8**
- H = I − (1/n)11′, simétrica e idempotente, é a projeção residual → **cap. 7**
- ASA′ para q combinações lineares → **cap. 5, 6, 8 e 11**
- dados composicionais (colunas que somam constante) ⇒ S singular (Exerc. 3.8)

## Ferramentas

`ferramentas/extrair.py` — localiza o PDF sozinho na raiz da pasta (dando
prioridade ao nome que contém "Fourth", e só então ao maior arquivo) e converte
a numeração com `livro2pdf`/`pdf2livro`. Redirecionar a saída de `texto` para
arquivo quebra no Windows (`cp1252`): use `PYTHONIOENCODING=utf-8`.
`ferramentas/figuras.py` — detecta e recorta figuras (aglomera os retalhos de
bitmap, descartando o cisco do OCR com o filtro `minimo`).

```bash
python ferramentas/figuras.py listar 36          # candidatos a figura na página
python ferramentas/figuras.py salvar 36 fig.png  # salva o maior candidato
```

```bash
python ferramentas/extrair.py texto --livro 49 68     # texto pela numeração do livro
python ferramentas/extrair.py texto 65 84             # texto pela numeração do PDF
python ferramentas/extrair.py pagina 65 out.png       # página inteira em PNG 200dpi
python ferramentas/extrair.py recorte 65 100 200 500 400 fig.png   # recorte 300dpi
python ferramentas/extrair.py imagens 65 pasta/       # imagens embutidas
python ferramentas/extrair.py buscar "eigenvalue"     # localiza um termo
```

Dependências: `pymupdf` (instalado). Python 3.13.

**Fluxo que funcionou bem para as figuras:** rodar `figuras.py listar` na página,
pegar a caixa `[0]` sem expansão, folgar 10–15 pontos em cada lado, recortar em
lote com um arquivo de lista (`nome pdf x0 y0 x1 y1`) e **conferir cada PNG
visualmente** — a legenda "Figure N.M" quase sempre invade a borda direita ou
inferior e precisa ser aparada.

## Convenção de nomes

Tudo ordena alfabeticamente na ordem do livro e o nome do arquivo sozinho já diz
de onde veio. **Números sempre com dois dígitos**, minúsculas, sem acento, hífen
entre palavras.

| O quê | Padrão | Exemplo |
|---|---|---|
| Pasta do capítulo | `capNN/` | `cap03/` |
| Página de uma seção | `NN-SS-titulo-kebab.html` | `cap03/03-02-geometria-da-amostra.html` |
| Página do capítulo inteiro | `NN-00-titulo.html` (`00` = visão geral) | `cap01/01-00-aspectos-da-analise-multivariada.html` |
| Figura | `img/fig-NN-MM.png` | `cap02/img/fig-02-06.png` |
| Tabela recortada | `img/tab-NN-MM.png` | `cap01/img/tab-01-02.png` |

Ao criar uma aula nova, acrescentar o link em **três** lugares de
`estudo/index.html`: a lista da barra lateral (trocar o `<li class="adiante">`
daquele capítulo por um `<li>` com link), o cartão em "Aulas disponíveis" e a
linha da tabela da seção **"Menu"** (`<h2 id="menu">`). E acertar o
`.nav-rodape` (anterior/próxima) da aula vizinha.

O link de volta ao `index.html` chama-se **"Menu"** — nos três lugares da aula:
`.extras` da barra lateral, a `.migalha` do cabeçalho e o `.nav-rodape`
("← Menu"). Não escrever "Percurso" nesses rótulos.

## Layout das páginas

O CSS está separado em dois arquivos e essa separação é para valer:

- `estudo/assets/tema.css` — **única** fonte de cores, fontes e medidas, tudo em
  variáveis CSS, com bloco `@media (prefers-color-scheme: dark)`. É o arquivo
  que o usuário troca ao mudar de tema. Tema atual: **roxo-ametista**.

  **Regra do tema, obrigatória:** as superfícies são **neutras** — nenhum fundo
  tingido de cor. Roxo (e petróleo, oliva, âmbar) só em **tipografia e filetes**:
  títulos, links, rótulos, borda esquerda das caixas. Fundo de caixa, cabeçalho
  de tabela e hover usam `--fundo-suave`, que é cinza.
- `estudo/assets/estilo.css` — só estrutura. **Nunca escrever cor literal aqui**,
  sempre `var(--…)`. Precisa de uma cor nova? Declare-a em `tema.css` (nos dois
  modos) e use a variável. Única exceção tolerada: o `@media print`, que força
  fundo branco.

O `<head>` de toda página de aula é este — os dois CSS nesta ordem, e o
`noindex` obrigatório (as figuras são do livro):

```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Cap. N — Título</title>
<link rel="stylesheet" href="../assets/tema.css?v=1">
<link rel="stylesheet" href="../assets/estilo.css?v=1">
```

`estilo.css` define uma **grade de quebra de coluna**. A prosa fica numa coluna
de 46rem (`--largura-leitura`), e estes elementos avançam para as bordas quando
são filhos diretos de `.pagina`:

`.topo` · `h2` · `h3` · `figure` · `.rolagem` (tabelas) · `pre` · `.cartoes` ·
`.exercicio` · `.nav-rodape`

Os títulos entram nessa lista de propósito: todos nascem na mesma margem
esquerda das figuras e do código, e o filete de cima do `h2` atravessa a largura
inteira em vez de parar na coluna da prosa. `h4` fica de fora — é rótulo curto
colado no parágrafo seguinte.

Os três níveis são roxos, clareando conforme descem: `h2` em `--realce`,
`h3` em `--realce-2`, `h4` em `--realce-3`. A hierarquia se lê pela cor.

Um `h2` logo depois de `</header>` perde o filete pelo seletor
`.pagina > .topo + h2`: o traço do `.topo` já está logo acima.

Numa tabela de números, célula que contém texto leva `class="txt"` para alinhar
à esquerda — o padrão de `td`/`th` é alinhar à direita.

Os nomes das linhas da grade **precisam** terminar em `-start`/`-end` — só assim
o atalho `grid-column: texto` resolve.

Dentro de `.exercicio` há a mesma grade em miniatura: prosa e equações na coluna
de leitura, `pre` e `.rolagem` ocupando a caixa inteira.

**Abertura da aula.** O primeiro `<div class="caixa objetivo">` vem logo depois
de `</header>` e o CSS o trata como continuação do cabeçalho, não como cartão:
perde fundo e moldura, ocupa a coluna `larga` e ganha um filete vertical que
nasce onde começa o traço do `.topo`. **Não mudar essa ordem**: é o seletor
`.topo + .objetivo` que faz a integração. Um `.objetivo` no meio da página
continua sendo cartão normal, que é o certo.

Os tópicos ficam colados no filete e em corpo 0.88rem para **caber um por
linha**. Ao escrever a abertura de uma aula nova, **manter cada objetivo com no
máximo ~125 caracteres**.

**Não existe `.sumario` ("Roteiro da aula")** nem no CSS nem nas páginas: a barra
lateral fica sempre aberta e já traz o índice das seções. Não recriar.

Toda página tem uma **barra lateral fixa** (`<details class="menu-lateral" open>`)
logo depois de `<body>`, com o índice das seções — o atributo `open` é
obrigatório. Acima de 62rem ela é uma coluna permanente de `--largura-menu`
(17rem) colada na borda esquerda, e o CSS esconde o `<summary>`; abaixo de 62rem
volta a ser a aba vertical que abre e fecha. O script no fim do arquivo só
ajusta esse estado conforme a largura.

A primeira coluna da grade reserva `--largura-menu + --desloca-texto`;
`--desloca-texto` (4.5rem) é o que empurra o conteúdo para a direita.

**Seções com subtópicos na barra.** Todo `h3` de primeiro nível (filho direto de
`.pagina`) leva `id="{id-do-h2}-{k}"` — `s8-1`, `s8-2`… — e o `<li>` daquela
seção na barra vira:

```html
<li><details class="sub">
  <summary><a href="#s8">Distância — o conceito central</a></summary>
  <ul class="subitens">
    <li><a href="#s8-1">8.1 A distância euclidiana e por que ela não serve</a></li>
  </ul>
</details></li>
```

Nasce **fechado**. Clicar no título abre a lista *e* salta para a seção; clicar
de novo não fecha (só a setinha fecha). Isso precisa das quatro linhas de JS no
fim do arquivo: o navegador dá prioridade ao `<a>` e **não** alterna o
`<details>` sozinho quando o link está dentro do `<summary>`.

No `index.html` a barra lista **os 12 capítulos** (os prontos como link, os
demais em `<li class="adiante">`, apagados e sem link).

O tamanho das figuras também sai do tema: `--figura-largura` (34rem) e
`--figura-altura` (52vh) são os tetos de `figure img`.

Ao editar qualquer um dos dois CSS, **incrementar o `?v=` nos dois `<link>` de
todas as páginas**, senão o navegador serve a versão em cache. Estão em `?v=1`.

## Estrutura

```
MULTI/
├── Applied Multivariate Statistical Analysis, Fourth Edition.pdf   (fora do git: .gitignore)
├── paginas-faltantes/      fotos das págs. 175, 176, 319 e 320 (fora do git)
├── index.html              redireciona para estudo/ — serve ao GitHub Pages
├── README.md               documentação pública do repositório
├── CLAUDE.md               este arquivo
├── .gitignore  .gitattributes  robots.txt
├── ferramentas/
│   ├── extrair.py
│   └── figuras.py
└── estudo/
    ├── index.html          painel com o percurso e o progresso
    ├── assets/
    │   ├── tema.css        cores, fontes, medidas (roxo-ametista)
    │   └── estilo.css      estrutura e layout
    └── capNN/
        ├── NN-SS-secao.html
        └── img/fig-NN-MM.png
```

O PDF está no `.gitignore`: é material com direitos autorais. Ao mudar a
estrutura, atualizar `README.md` **e** este arquivo.

O repositório já existe e está publicado em
<https://github.com/GABELCHIOR/MULTI> (remoto `origin`, branch `main`). O PDF
fica de fora pelo `.gitignore`.

## Progresso

**Capítulos 1, 2, 3 e 4 prontos** (1 e 2 em 2026-08-10; 3 em 2026-08-13;
4 em 2026-08-17). Próximo: capítulo 5 (Inferences about a Mean Vector,
livro 224–289, PDF 238–303) — inteiro na terceira faixa do PDF, sem lacunas.

Ao gerar o cap. 5, retomar o que o cap. 4 deixou pronto: `X̄ ~ Nₚ(μ, Σ/n)`,
`(n−1)S ~ Wishart` e **a independência entre os dois** são as três peças de que
o `T²` de Hotelling precisa; a elipsoide `(x̄−μ)'S⁻¹(x̄−μ)` já está construída,
só falta trocar o quantil `χ²` pelo de `T²`; e (4-28) explica por que, com `n`
grande, a diferença entre os dois quantis some.

O capítulo 4 é longo (≈2 000 linhas de HTML, 12 figuras, 20 cartões de recall,
10 exercícios). Foi escrito em quatro passadas com `Edit` acrescentando ao fim
do arquivo — escrever tudo numa chamada de `Write` estoura o limite de saída.

**Numeração do livro corrigida em 2026-08-13.** As páginas de livro dos
capítulos 4 a 12 na tabela abaixo estavam erradas — tinham sido obtidas
aplicando o offset constante `+16`, que só vale até a p. 174. Foram conferidas
uma a uma na página de abertura de cada capítulo. As páginas do **PDF** sempre
estiveram certas.

| Cap. | Título | Livro p. | PDF p. | Status |
|---|---|---|---|---|
| 1 | Aspects of Multivariate Analysis | 1 | 17 | ✅ `estudo/cap01/01-00-aspectos-da-analise-multivariada.html` |
| 2 | Matrix Algebra and Random Vectors | 49 | 65 | ✅ `estudo/cap02/02-00-algebra-de-matrizes-e-vetores-aleatorios.html` |
| 3 | Sample Geometry and Random Sampling | 116 | 132 | ✅ `estudo/cap03/03-00-geometria-da-amostra-e-amostragem-aleatoria.html` |
| 4 | The Multivariate Normal Distribution | 157 | 173 | ✅ `estudo/cap04/04-00-a-distribuicao-normal-multivariada.html` |
| 5 | Inferences about a Mean Vector | 224 | 238 | — |
| 6 | Comparisons of Several Multivariate Means | 290 | 304 | — |
| 7 | Multivariate Linear Regression Models | 377 | 389 | — |
| 8 | Principal Components | 458 | 470 | — |
| 9 | Factor Analysis | 514 | 526 | — |
| 10 | Canonical Correlation Analysis | 587 | 599 | — |
| 11 | Discrimination and Classification | 629 | 641 | — |
| 12 | Clustering, Distance Methods, and Ordination | 726 | 738 | — |
