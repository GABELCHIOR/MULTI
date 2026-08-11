#!/usr/bin/env python
"""
Localiza as regioes de figura numa pagina do PDF do Johnson & Wichern.

Este PDF e um escaneamento passado pelo ClearScan do Acrobat: o texto virou
fonte, mas tudo que o OCR nao reconheceu (linhas de grafico, nuvens de pontos,
chaves de matriz) sobrou como imagem embutida. Isso quer dizer duas coisas:

  * nao ha desenhos vetoriais de verdade -- as figuras sao os retalhos de
    bitmap que sobraram, e eles vem em pedacos que precisam ser aglomerados;
  * ha MUITO cisco: cada sinal de somatorio ou colchete que o OCR falhou em ler
    e um bitmap de 5x6 pixels. Por isso o filtro `minimo` existe.

  python figuras.py listar 36            -> candidatos na pagina 36 do PDF
  python figuras.py salvar 36 saida.png  -> salva o maior candidato

Quando o resultado sair torto (acontece em pagina com muita formula), recorte a
mao com `extrair.py recorte`, que e sempre confiavel.
"""
import re
import sys
import os

import fitz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extrair import abrir, pdf2livro

# Legenda de figura/tabela: neste livro vem escrita normalmente ("Figure 1.3"),
# nao espacada como no Montgomery. Delimita o fim da figura.
LEGENDA = re.compile(r"^\s*(Figure|Table|Panel)\s+\d", re.I)


def caixas(page, margem=8.0, minimo=900.0):
    """Agrupa os retalhos de bitmap em caixas contiguas.

    `minimo` (em pontos²) descarta o cisco do OCR: sem ele, cada fragmento de
    formula entra na lista e a saida fica ilegivel.
    """
    itens = [fitz.Rect(b["bbox"]) for b in page.get_image_info()]
    itens += [d["rect"] for d in page.get_drawings()]
    grupos = []
    for r in itens:
        if r.is_empty or r.width * r.height < minimo:
            continue
        alvo = fitz.Rect(r) + (-margem, -margem, margem, margem)
        juntar = [g for g in grupos if g.intersects(alvo)]
        for g in juntar:
            grupos.remove(g)
            r = fitz.Rect(r) | g
        grupos.append(fitz.Rect(r))
    # repete ate estabilizar
    mudou = True
    while mudou:
        mudou = False
        for i in range(len(grupos)):
            for j in range(i + 1, len(grupos)):
                a = grupos[i] + (-margem, -margem, margem, margem)
                if a.intersects(grupos[j]):
                    grupos[i] |= grupos[j]
                    del grupos[j]
                    mudou = True
                    break
            if mudou:
                break
    return sorted(grupos, key=lambda r: -(r.width * r.height))


def expandir(page, rect, folga=14.0):
    """Cresce a caixa para abarcar os rotulos da figura (eixos, valores).

    Nunca engole a legenda: "Figure N.M" / "Table N.M" marcam o fim.
    """
    r = fitz.Rect(rect)
    mudou = True
    while mudou:
        mudou = False
        for b in page.get_text("blocks"):
            txt = b[4].strip()
            if not txt or LEGENDA.match(txt):
                continue
            tb = fitz.Rect(b[:4])
            # ignora o corpo do texto: blocos largos que atravessam a pagina
            if tb.width > page.rect.width * 0.7:
                continue
            if tb in r:
                continue
            if (r + (-folga, -folga, folga, folga)).intersects(tb):
                r |= tb
                mudou = True
    return r


def legenda_proxima(page, rect):
    """Devolve a legenda (Figure/Table N.M) mais proxima da caixa."""
    melhor, dist = "", 1e9
    for b in page.get_text("blocks"):
        txt = b[4].strip().replace("\n", " ")
        if LEGENDA.match(txt):
            r = fitz.Rect(b[:4])
            d = abs(r.y0 - rect.y1) if r.y0 > rect.y0 else abs(rect.y0 - r.y1)
            if d < dist:
                melhor, dist = txt[:70], d
    return melhor


def cmd_listar(args):
    n = int(args[0])
    doc = abrir()
    page = doc[n - 1]
    print(f"PDF p.{n} (livro p.{pdf2livro(n)})  mediabox={page.rect}")
    for i, r in enumerate(caixas(page)):
        e = expandir(page, r)
        print(f"  [{i}] x0={e.x0:.0f} y0={e.y0:.0f} x1={e.x1:.0f} y1={e.y1:.0f}"
              f"  ({e.width:.0f}x{e.height:.0f})  <- {legenda_proxima(page, e)}")


def cmd_salvar(args):
    n, saida = int(args[0]), args[1]
    idx = int(args[2]) if len(args) > 2 else 0
    doc = abrir()
    page = doc[n - 1]
    cs = caixas(page)
    if not cs:
        raise SystemExit("nenhuma figura encontrada")
    r = expandir(page, cs[idx]) + (-8, -8, 8, 8)
    pix = page.get_pixmap(dpi=300, clip=r)
    pix.save(saida)
    print(f"salvo: {saida}  ({pix.width}x{pix.height})  de {r}")


if __name__ == "__main__":
    cmds = {"listar": cmd_listar, "salvar": cmd_salvar}
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        print(__doc__)
        sys.exit(1)
    cmds[sys.argv[1]](sys.argv[2:])
