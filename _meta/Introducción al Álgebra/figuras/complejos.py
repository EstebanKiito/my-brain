#!/usr/bin/env python3
"""Genera la figura de la forma polar de un número complejo (tema Números complejos).

La clase la dibuja como gráfico vectorial; se regenera en SVG y se rasteriza
con ImageMagick.
"""
import hashlib
import math
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
DEST = RAIZ / "Introducción al Álgebra" / "09-Números complejos, inversas y ecuaciones trigonométricas" / "adjuntos"

T = 'font-family="Helvetica, Arial, sans-serif"'


def _svg(w, h, cuerpo):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="#ffffff"/>{cuerpo}</svg>')


def _texto(x, y, s, size=18, fill="#1a202c", anchor="middle"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" {T}>{s}</text>'


def forma_polar():
    # z = a + bi con a=2.4, b=1.8; escala 70. Eje real horizontal, imaginario vertical.
    O = (90, 250)
    a, b = 2.4, 1.8
    P = (O[0] + a * 70, O[1] - b * 70)
    r = math.hypot(a, b)
    # ejes
    eje_x = f'<line x1="60" y1="{O[1]}" x2="360" y2="{O[1]}" stroke="#888888" stroke-width="1.5"/>'
    eje_y = f'<line x1="{O[0]}" y1="300" x2="{O[0]}" y2="60" stroke="#888888" stroke-width="1.5"/>'
    # flechas de los ejes
    flechas = (
        f'<polygon points="360,{O[1]} 352,{O[1]-5} 352,{O[1]+5}" fill="#888888"/>'
        f'<polygon points="{O[0]},60 {O[0]-5},68 {O[0]+5},68" fill="#888888"/>'
    )
    # radio
    radio = f'<line x1="{O[0]}" y1="{O[1]}" x2="{P[0]}" y2="{P[1]}" stroke="#2b6cb0" stroke-width="2.5"/>'
    # arco del argumento
    t0 = math.atan2(b, a)
    x_arc = O[0] + 45 * math.cos(t0)
    y_arc = O[1] - 45 * math.sin(t0)
    arco = (f'<path d="M {O[0]+45},{O[1]} A 45,45 0 0 0 {x_arc:.0f},{y_arc:.0f}" '
            f'fill="none" stroke="#c53030" stroke-width="2"/>')
    punto = f'<circle cx="{P[0]}" cy="{P[1]}" r="4.5" fill="#c53030"/>'
    cuerpo = (
        eje_x + eje_y + flechas + radio + arco + punto
        + _texto(370, O[1] + 4, "Re", 18)
        + _texto(O[0], 52, "Im", 18)
        + _texto(P[0] + 16, P[1] - 10, "z = a + bi", 18, "#c53030")
        + _texto((O[0] + P[0]) / 2, (O[1] + P[1]) / 2 - 10, "r", 20, "#2b6cb0")
        + _texto(O[0] + 62, O[1] - 30, "θ", 20, "#c53030")
        + _texto(O[0] + 45, O[1] + 22, "a", 18)
        + _texto(P[0] + 12, (O[1] + P[1]) / 2, "b", 18)
    )
    return _svg(420, 320, cuerpo)


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
    guardar("forma polar de un numero complejo", forma_polar())
