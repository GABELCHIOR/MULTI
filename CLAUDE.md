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

Os capítulos 1, 2 e 3 (livro 1–148) estão inteiros na primeira faixa. Use
sempre `livro2pdf()` / `pdf2livro()` de `ferramentas/extrair.py` — nunca uma
constante. Ao chegar nos capítulos 4 e 6, avisar o usuário das lacunas e
decidir se vale conseguir outra cópia do PDF.

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

- cos(θ) = r entre colunas centradas → **cap. 3**
- distância de Mahalanobis, (x−μ)'Σ⁻¹(x−μ) como expoente da densidade → **cap. 4**
- Σ⁻¹/² como padronização multivariada; elipses de confiança → **cap. 4 e 5**
- decomposição espectral de S = componentes principais; λ₁ como máximo de x'Sx
  na esfera unitária → **cap. 8**
- autovalores próximos ⇒ autovetores instáveis (Exemplo 2.10) → **cap. 8**
- lema de maximização ⇒ função discriminante de Fisher, x ∝ B⁻¹(μ₁−μ₂) → **cap. 11**
- os quatro axiomas de distância, para julgar medidas de similaridade → **cap. 12**
- Σ₁₂ e o complemento de Schur → **cap. 10**

## Ferramentas

`ferramentas/extrair.py` — localiza o PDF sozinho (por tamanho, na raiz da pasta)
e converte a numeração com `livro2pdf`/`pdf2livro`.
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

**Ainda não é um repositório git** e ainda **não foi para o GitHub** — o usuário
pediu para segurar. Quando for a hora: `git init`, conferir o `.gitignore`, e só
então publicar.

## Progresso

**Capítulos 1 e 2 prontos** (gerados em 2026-08-10). Próximo: capítulo 3
(Geometria da Amostra e Amostragem Aleatória, livro 116–148, PDF 132–164).

Ao gerar o cap. 3, retomar os ganchos: `cos(θ) = r` entre colunas centradas
(prometido em 1.6 e em 2.2.4), a decomposição de cada coluna em média + desvio,
a variância generalizada `|S|` como produto dos autovalores (prometido em 4.1 do
cap. 2), e a distinção entre as duas geometrias — `n` pontos em `p` dimensões e
`p` pontos em `n` dimensões.

| Cap. | Título | Livro p. | PDF p. | Status |
|---|---|---|---|---|
| 1 | Aspects of Multivariate Analysis | 1 | 17 | ✅ `estudo/cap01/01-00-aspectos-da-analise-multivariada.html` |
| 2 | Matrix Algebra and Random Vectors | 49 | 65 | ✅ `estudo/cap02/02-00-algebra-de-matrizes-e-vetores-aleatorios.html` |
| 3 | Sample Geometry and Random Sampling | 116 | 132 | — |
| 4 | The Multivariate Normal Distribution | 149 | 165 | — |
| 5 | Inferences about a Mean Vector | 222 | 238 | — |
| 6 | Comparisons of Several Multivariate Means | 288 | 304 | — |
| 7 | Multivariate Linear Regression Models | 373 | 389 | — |
| 8 | Principal Components | 454 | 470 | — |
| 9 | Factor Analysis | 510 | 526 | — |
| 10 | Canonical Correlation Analysis | 583 | 599 | — |
| 11 | Discrimination and Classification | 625 | 641 | — |
| 12 | Clustering, Distance Methods, and Ordination | 722 | 738 | — |
