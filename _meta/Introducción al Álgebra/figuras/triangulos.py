#!/usr/bin/env python3
"""Genera las figuras de triángulos del tema Trigonometría: razones.

La clase dibuja los triángulos como gráficos vectoriales (no hay imágenes
incrustadas para el triángulo de las definiciones), así que se regeneran en
SVG y se rasterizan a PNG con ImageMagick.
"""
import hashlib
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]  # repo (script vive en _meta/<Ramo>/figuras/)
DEST = RAIZ / "Introducción al Álgebra" / "07-Trigonometría: razones y resolución de triángulos" / "adjuntos"

TEXTO = 'font-family="Helvetica, Arial, sans-serif" text-anchor="middle"'


def _linea(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#1a202c" stroke-width="3"/>'


def _texto(x, y, s, size=22, fill="#1a202c", peso=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" {TEXTO} {peso}>{s}</text>'


def _svg(w, h, cuerpo):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}">\n'
            f'<rect width="{w}" height="{h}" fill="#ffffff"/>\n{cuerpo}\n</svg>')


def _angulo_recto(x, y, orient):
    # marca del ángulo recto en (x,y); orient: "NE", "NW", "SE", "SW"
    dx, dy = {"NE": (1, -1), "NW": (-1, -1), "SE": (1, 1), "SW": (-1, 1)}[orient]
    s = 14
    return (f'<polyline points="{x},{y + s*dy} {x + s*dx},{y + s*dy} {x + s*dx},{y}" '
            f'fill="none" stroke="#1a202c" stroke-width="2"/>')


def triangulo_rectangulo():
    # A=(0,0) ángulo α, B=(4,0) ángulo recto, C=(4,3). Cateto opuesto a α = a (vertical),
    # adyacente = b (horizontal), hipotenusa = c. Escala ×60.
    A = (60, 300); B = (300, 300); C = (300, 120)
    cuerpo = (
        '<polygon points="60,300 300,300 300,120" fill="#bee3f8" fill-opacity="0.45" stroke="#2b6cb0" stroke-width="3"/>'
        + _angulo_recto(300, 300, "NW")
        + _texto(96, 292, "α", 26)
        + _texto(180, 322, "b (adyacente)", 20)
        + _texto(324, 210, "a (opuesto)", 20)
        + _texto(150, 170, "c (hipotenusa)", 20)
        + _texto(304, 112, "90°", 18)
    )
    return _svg(360, 340, cuerpo)


def triangulo_30_60_90():
    # Triángulo rectángulo 30-60-90: ángulo 60° en A, 30° en C, recto en B.
    # Catetos √3 (horizontal, opuesto a 60°) y 1 (vertical, opuesto a 30°); hipotenusa 2. Escala ×110.
    A = (40, 300); B = (230, 300); C = (230, 190)
    cuerpo = (
        '<polygon points="40,300 230,300 230,190" fill="#fefcbf" fill-opacity="0.5" stroke="#b7791f" stroke-width="3"/>'
        + _angulo_recto(230, 300, "NW")
        + _texto(72, 292, "60°", 22)
        + _texto(246, 182, "30°", 22)
        + _texto(135, 322, "√3", 22)
        + _texto(254, 245, "1", 22)
        + _texto(108, 230, "2", 22)
    )
    return _svg(300, 330, cuerpo)


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
    guardar("triangulo rectangulo de razones trigonometricas", triangulo_rectangulo())
    guardar("triangulo 30-60-90", triangulo_30_60_90())
