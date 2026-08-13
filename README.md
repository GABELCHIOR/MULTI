# Análise Multivariada — caderno de estudo

Caderno de estudo autodidata de **Análise Multivariada**, em português, montado a
partir de Johnson, R. A. & Wichern, D. W., *Applied Multivariate Statistical
Analysis*, 4ª edição (Prentice Hall, 1998).

São páginas HTML locais, sem dependência de rede: abrem direto no navegador,
funcionam offline, e a matemática é **MathML nativo** — sem CDN, sem JavaScript
de renderização.

👉 **Comece por [`estudo/index.html`](estudo/index.html).**

## O que já existe

| Cap. | Título | Conteúdo |
|---|---|---|
| 1 | [Aspectos da Análise Multivariada](estudo/cap01/01-00-aspectos-da-analise-multivariada.html) | Os cinco objetivos; o arranjo `X`; média, variância, covariância e correlação amostrais; os arranjos `x̄`, `Sₙ` e `R`; as duas geometrias; gráficos, *brushing*, estrelas e faces de Chernoff; e a **distância estatística** — por que a euclidiana não serve e de onde vem a elipse. |
| 2 | [Álgebra de Matrizes e Vetores Aleatórios](estudo/cap02/02-00-algebra-de-matrizes-e-vetores-aleatorios.html) | Comprimento, ângulo e projeção; **decomposição espectral**; matrizes definidas positivas e a resposta à pergunta deixada no cap. 1; elipses por autovalores; a raiz quadrada `A^{1/2}`; `μ`, `Σ` e `ρ`; a regra `CΣC′`; Cauchy–Schwarz e os lemas de maximização. |
| 3 | [Geometria da Amostra e Amostragem Aleatória](estudo/cap03/03-00-geometria-da-amostra-e-amostragem-aleatoria.html) | As duas leituras de `X`; a decomposição `yᵢ = x̄ᵢ1 + dᵢ` como projeção; comprimento = desvio-padrão e **cos(θ) = r**, pagando a dívida do cap. 1; amostra aleatória, `E(X̄) = μ`, `Cov(X̄) = Σ/n` e de onde vem o divisor `n − 1`; **variância generalizada `\|S\|`** como volume, suas duas fraquezas e o diagnóstico de `\|S\| = 0`; `x̄`, `S` e `R` como operações matriciais; `b′Sc` e `ASA′`. |

Cada aula traz o objetivo da seção, o conceito com a derivação completa, figuras
recortadas do livro, os exemplos resolvidos passo a passo com código em **R**,
cartões de recall ativo e uma seleção de exercícios com gabarito comentado.
**Todo resultado numérico foi recalculado**, não copiado.

## Estrutura

```
├── index.html              redireciona para estudo/
├── estudo/
│   ├── index.html          painel do percurso
│   ├── assets/
│   │   ├── tema.css        cores, fontes e medidas (tema roxo-ametista)
│   │   └── estilo.css      estrutura e layout
│   └── capNN/
│       ├── NN-SS-secao.html
│       └── img/            figuras recortadas do PDF
└── ferramentas/
    ├── extrair.py          texto, páginas e recortes do PDF
    └── figuras.py          detecção automática de figuras
```

Trocar de tema é trocar `assets/tema.css`: todas as cores e medidas do site
estão ali, em variáveis CSS, e `estilo.css` nunca traz cor literal. Há suporte a
modo claro e escuro pelo `prefers-color-scheme`.

## Sobre o PDF do livro

O PDF **não** está no repositório — é obra protegida por direitos autorais. As
ferramentas o localizam sozinhas se você colocar a sua própria cópia na raiz da
pasta (preferindo o arquivo cujo nome contém "Fourth", se houver mais de um).

Duas ressalvas sobre o arquivo usado, se você for reproduzir o processo:

- É um **escaneamento com OCR** (ClearScan). A prosa extrai bem; fórmulas e
  matrizes saem embaralhadas. Por isso as figuras aqui são recortes de imagem e
  toda a matemática foi reescrita à mão.
- O **deslocamento entre a numeração do livro e a do PDF não é constante**,
  porque o escaneamento perdeu duas folhas (páginas 175–176 e 319–320 do livro):

  | Páginas do livro | PDF |
  |---|---|
  | 1 – 174 | livro + 16 |
  | 177 – 318 | livro + 14 |
  | 321 – 816 | livro + 12 |

  Use `livro2pdf()` / `pdf2livro()` de `ferramentas/extrair.py`. Os capítulos 1,
  2 e 3 estão inteiros.

## Uso das ferramentas

```bash
python ferramentas/extrair.py texto --livro 49 68            # texto pela numeração do livro
python ferramentas/extrair.py recorte 65 100 200 500 400 fig.png
python ferramentas/extrair.py buscar "eigenvalue"
python ferramentas/figuras.py listar 36
```

Requer Python 3 e `pymupdf`.

## Aviso

Material de estudo pessoal. As páginas reproduzem figuras e trechos da obra
original para fins de estudo; todas trazem `noindex, nofollow` e o repositório
inclui um `robots.txt` restritivo. Não é substituto do livro — é um caderno de
quem está lendo o livro.
