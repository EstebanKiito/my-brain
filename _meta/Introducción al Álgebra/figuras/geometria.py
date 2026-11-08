#!/usr/bin/env python3
"""Genera la figura de la circunferencia (tema Geometría analítica).

La clase la dibuja como gráfico vectorial; se regenera en SVG y se rasteriza
con ImageMagick.
"""
import hashlib
import math
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
DEST = RAIZ / "Introducción al Álgebra" / "10-Geometría analítica: distancia, circunferencia y división de segmentos" / "adjuntos"


def _svg(w, h, cuerpo):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="#ffffff"/>{cuerpo}</svg>')


def _texto(x, y, s, size=18, fill="#1a202c", anchor="middle"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-family="Helvetica, Arial, sans-serif">{s}</text>'


def circunferencia():
    C = (200, 165)
    r = 95
    P = (C[0] + r * math.cos(0.9), C[1] - r * math.sin(0.9))
    cuerpo = (
        '<line x1="60" y1="165" x2="340" y2="165" stroke="#cccccc" stroke-width="1.5"/>'
        '<line x1="200" y1="30" x2="200" y2="300" stroke="#cccccc" stroke-width="1.5"/>'
        f'<circle cx="{C[0]}" cy="{C[1]}" r="{r}" fill="#bee3f8" fill-opacity="0.4" stroke="#2b6cb0" stroke-width="2.5"/>'
        f'<line x1="{C[0]}" y1="{C[1]}" x2="{P[0]:.0f}" y2="{P[1]:.0f}" stroke="#c53030" stroke-width="2.5"/>'
        f'<circle cx="{C[0]}" cy="{C[1]}" r="4" fill="#1a202c"/>'
        f'<circle cx="{P[0]:.0f}" cy="{P[1]:.0f}" r="4" fill="#c53030"/>'
        + _texto(C[0], C[1] + 20, "C(h, k)", 18)
        + _texto(P[0] + 22, P[1] - 8, "P(x, y)", 18, "#c53030")
        + _texto((C[0] + P[0]) / 2, (C[1] + P[1]) / 2 - 12, "r", 18, "#c53030")
    )
    return _svg(400, 330, cuerpo)


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
    guardar("circunferencia de centro C y radio r", circunferencia())
