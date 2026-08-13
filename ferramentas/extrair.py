#!/usr/bin/env python
"""
Ferramentas de extracao do PDF do Johnson & Wichern.

O PDF e um escaneamento com OCR (ClearScan): a prosa sai limpa, mas formulas,
matrizes e indices vem embaralhados. Use `texto` para localizar e ler o
argumento; para qualquer coisa com matematica, recorte a imagem da pagina.

Uso:
  python extrair.py texto  19 40           -> imprime o texto das paginas 19..40 (numeracao do PDF)
  python extrair.py texto  --livro 1 22    -> idem, mas usando a numeracao impressa no livro
  python extrair.py pagina 88 saida.png    -> renderiza a pagina inteira como PNG
  python extrair.py recorte 88 100 200 500 400 saida.png   -> recorta uma regiao (x0 y0 x1 y1, em pontos)
  python extrair.py imagens 88 pasta/      -> extrai as imagens embutidas da pagina
  python extrair.py buscar "eigenvalue"    -> lista as paginas onde o termo aparece

ATENCAO -- o offset NAO e constante. Este escaneamento perdeu duas folhas, e o
deslocamento entre a numeracao do livro e a do PDF cai de 16 para 14 e depois
para 12. Use `livro2pdf` / `pdf2livro`, nunca uma constante:

  livro 1-174    -> pdf +16
  livro 175-176  -> AUSENTES do PDF
  livro 177-318  -> pdf +14
  livro 319-320  -> AUSENTES do PDF
  livro 321-816  -> pdf +12

Os capitulos 1, 2 e 3 (livro 1-148) estao inteiros na primeira faixa; as duas
lacunas caem no meio do cap. 4 e do cap. 6.
"""
import sys
import os

import fitz  # PyMuPDF

import glob

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Localiza o PDF sozinho: o nome do arquivo pode mudar, a pasta nao.
# A 4a edicao e a edicao de referencia deste caderno (os offsets abaixo sao dela),
# entao ela tem prioridade sobre qualquer outro PDF que apareca na raiz.
_pdfs = sorted(glob.glob(os.path.join(RAIZ, "*.pdf")), key=os.path.getsize, reverse=True)
if not _pdfs:
    raise SystemExit(f"nenhum PDF encontrado em {RAIZ}")
_quarta = [p for p in _pdfs if "fourth" in os.path.basename(p).lower()]
PDF = (_quarta or _pdfs)[0]

# (primeira pagina do livro na faixa, ultima, offset). Levantado conferindo o
# folio impresso pagina a pagina -- ver ferramentas/offset.py no historico.
FAIXAS = [(1, 174, 16), (177, 318, 14), (321, 816, 12)]
OFFSET = 16          # so vale ate a p.174 do livro; mantido para compatibilidade


def livro2pdf(p):
    """Pagina do livro -> pagina do PDF. Erra alto se a pagina nao foi escaneada."""
    for ini, fim, off in FAIXAS:
        if ini <= p <= fim:
            return p + off
    raise SystemExit(f"pagina {p} do livro nao existe neste PDF (folhas 175-176 e "
                     f"319-320 faltam no escaneamento)")


def pdf2livro(n):
    """Pagina do PDF -> pagina do livro."""
    for ini, fim, off in FAIXAS:
        if ini + off <= n <= fim + off:
            return n - off
    return None


def abrir():
    return fitz.open(PDF)


def cmd_texto(args):
    """Imprime o texto de um intervalo de paginas."""
    if args and args[0] == "--livro":
        args = args[1:]
        ini = livro2pdf(int(args[0]))
        fim = livro2pdf(int(args[1])) if len(args) > 1 else ini
    else:
        ini = int(args[0])
        fim = int(args[1]) if len(args) > 1 else ini
    doc = abrir()
    for n in range(ini, fim + 1):
        print(f"\n{'=' * 70}\n### PDF p.{n}  (livro p.{pdf2livro(n)})\n{'=' * 70}")
        print(doc[n - 1].get_text())


def cmd_pagina(args):
    """Renderiza uma pagina inteira como PNG a 200 dpi."""
    n, saida = int(args[0]), args[1]
    doc = abrir()
    pix = doc[n - 1].get_pixmap(dpi=200)
    pix.save(saida)
    print(f"salvo: {saida}  ({pix.width}x{pix.height})")


def cmd_recorte(args):
    """Recorta uma regiao retangular da pagina em alta resolucao."""
    n = int(args[0])
    x0, y0, x1, y1 = (float(v) for v in args[1:5])
    saida = args[5]
    doc = abrir()
    rect = fitz.Rect(x0, y0, x1, y1)
    pix = doc[n - 1].get_pixmap(dpi=300, clip=rect)
    pix.save(saida)
    print(f"salvo: {saida}  ({pix.width}x{pix.height})")


def cmd_imagens(args):
    """Extrai as imagens embutidas de uma pagina."""
    n, pasta = int(args[0]), args[1]
    os.makedirs(pasta, exist_ok=True)
    doc = abrir()
    for i, info in enumerate(doc[n - 1].get_images(full=True)):
        xref = info[0]
        img = doc.extract_image(xref)
        caminho = os.path.join(pasta, f"p{n}_{i}.{img['ext']}")
        with open(caminho, "wb") as f:
            f.write(img["image"])
        print(f"salvo: {caminho}  ({img['width']}x{img['height']})")


def cmd_buscar(args):
    """Lista as paginas em que um termo aparece."""
    termo = args[0]
    doc = abrir()
    for n, page in enumerate(doc, start=1):
        if page.search_for(termo):
            print(f"PDF p.{n}  (livro p.{pdf2livro(n)})")


COMANDOS = {
    "texto": cmd_texto,
    "pagina": cmd_pagina,
    "recorte": cmd_recorte,
    "imagens": cmd_imagens,
    "buscar": cmd_buscar,
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMANDOS:
        print(__doc__)
        sys.exit(1)
    COMANDOS[sys.argv[1]](sys.argv[2:])
