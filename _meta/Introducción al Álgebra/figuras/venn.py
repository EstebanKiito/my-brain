#!/usr/bin/env python3
"""Genera los diagramas de Venn del tema Conjuntos y operaciones.

Las clases usan diagramas de Venn dibujados como gráficos vectoriales (no hay
imágenes incrustadas), así que se regeneran aquí en SVG y se rasterizan a PNG
con ImageMagick. Los números del diagrama del problema de los deportistas
corresponden al Ejemplo 22 de la clase de la semana 3:

    S = salto alto (24), P = 100 m planos, G = salto con garrocha (25), |U| = 44
    S ∩ P ∩ G = 7 (e), S∩P sin G = 6 (b), S∩G sin P = 2 (d), P∩G sin S = 5 (f)
    solo S = 9 (a), solo P = 3 (c), solo G = 11 (g), ninguno = 1 (h)
"""
import hashlib
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]  # repo (script vive en _meta/<Ramo>/figuras/)
DEST = RAIZ / "Introducción al Álgebra" / "03-Conjuntos y operaciones" / "adjuntos"

TEXTO = 'font-family="Helvetica, Arial, sans-serif" text-anchor="middle"'


def _circulo(cx, cy, r, fill, stroke):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
            f'fill-opacity="0.55" stroke="{stroke}" stroke-width="2"/>')


def _texto(x, y, s, size=20, fill="#1a202c", peso=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" {TEXTO} {peso}>{s}</text>'


def _svg(w, h, cuerpo):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}">\n'
            f'<rect width="{w}" height="{h}" fill="#ffffff"/>\n{cuerpo}\n</svg>')


def dos_conjuntos():
    cuerpo = (
        '<rect x="24" y="24" width="352" height="312" fill="#ffffff" stroke="#888888" stroke-width="2"/>'
        + _circulo(150, 180, 95, "#bee3f8", "#2b6cb0")
        + _circulo(250, 180, 95, "#fefcbf", "#b7791f")
        + _texto(40, 44, "U", 22)
        + _texto(108, 186, "A", 24)
        + _texto(200, 186, "A ∩ B", 20)
        + _texto(292, 186, "B", 24)
    )
    return _svg(400, 360, cuerpo)


def deportistas():
    # S arriba, P abajo-izquierda, G abajo-derecha
    cuerpo = (
        '<rect x="24" y="24" width="352" height="312" fill="#ffffff" stroke="#888888" stroke-width="2"/>'
        + _circulo(200, 105, 95, "#bee3f8", "#2b6cb0")    # S (salto alto)
        + _circulo(135, 217, 95, "#fefcbf", "#b7791f")    # P (100 m)
        + _circulo(265, 217, 95, "#c6f6d5", "#276749")    # G (garrocha)
        + _texto(40, 44, "U", 22)
        + _texto(200, 78, "S", 24)
        + _texto(95, 250, "P", 24)
        + _texto(305, 250, "G", 24)
        + _texto(200, 50, "9", 20)
        + _texto(135, 150, "6", 20)
        + _texto(265, 150, "2", 20)
        + _texto(200, 186, "7", 22, "#c53030", 'font-weight="bold"')
        + _texto(95, 292, "3", 20)
        + _texto(305, 292, "11", 20)
        + _texto(200, 268, "5", 20)
        + _texto(360, 48, "1", 20)
    )
    return _svg(400, 360, cuerpo)


def guardar(nombre, svg):
    DEST.mkdir(parents=True, exist_ok=True)
    svg_tmp = DEST / (nombre + ".svg")
    png = DEST / (nombre + ".png")
    svg_tmp.write_text(svg, encoding="utf-8")
    subprocess.run(["magick", "convert", str(svg_tmp), str(png)], check=True, capture_output=True)
    svg_tmp.unlink()
    h = hashlib.sha256(png.read_bytes()).hexdigest()
    print(f"{png.relative_to(RAIZ)}  sha256={h}")


if __name__ == "__main__":
    guardar("diagrama de Venn de dos conjuntos", dos_conjuntos())
    guardar("diagrama de Venn del problema de los deportistas", deportistas())
