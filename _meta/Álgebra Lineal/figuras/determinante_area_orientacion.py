import sys, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
OUT = sys.argv[1]
SQ = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]]).T
F = np.array([[.3,.15],[.3,.85],[.75,.85],[.75,.72],[.43,.72],[.43,.56],[.68,.56],[.68,.43],[.43,.43],[.43,.15],[.3,.15]]).T
AZ, RO, VE, GR, NA = "#2b6cb0", "#c53030", "#2f855a", "#a0aec0", "#dd6b20"
frames = []
ts = np.concatenate([np.linspace(1.5, -1.5, 40), np.full(6, -1.5), np.linspace(-1.5, 1.5, 40), np.full(6, 1.5)])
for t in ts:
    A = np.array([[1, .6], [0, t]])
    fig, ax = plt.subplots(figsize=(3.8, 4.2))
    col = AZ if t >= 0 else NA
    ax.fill(*SQ, color=GR, alpha=.15); ax.plot(*SQ, color=GR, lw=1, ls="--"); ax.fill(*F, color=GR, alpha=.35)
    S2, F2 = A @ SQ, A @ F
    ax.fill(*S2, color=col, alpha=.2); ax.plot(*S2, color=col, lw=1.6); ax.fill(*F2, color=col, alpha=.75)
    for v, c in ((A[:, 0], RO), (A[:, 1], VE)):
        if np.linalg.norm(v) > 1e-9:
            ax.annotate("", xy=v, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=c, lw=2))
    ax.axhline(0, color="k", lw=.6); ax.axvline(0, color="k", lw=.6)
    ax.set_xlim(-1, 2.2); ax.set_ylim(-1.8, 1.8); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(f"A = [[1, 0.6], [0, {t:+.2f}]]", fontsize=9, family="monospace")
    estado = "conserva orientación" if t > 0.02 else ("invierte orientación" if t < -0.02 else "aplasta: no invertible")
    ax.text(.03, .03, f"det A = {t:+.2f}\nárea = |det A| = {abs(t):.2f}\n{estado}", transform=ax.transAxes, fontsize=8.5, va="bottom",
            bbox=dict(facecolor="white", edgecolor="none", alpha=.85, pad=1.5))
    fig.tight_layout(); fig.canvas.draw()
    frames.append(Image.fromarray(np.asarray(fig.canvas.buffer_rgba())).convert("RGB").quantize(64, method=Image.Quantize.MEDIANCUT))
    plt.close(fig)
frames[0].save(f"{OUT}/Determinante como factor de área y orientación.gif", save_all=True, append_images=frames[1:], duration=100, loop=0, optimize=True)
print("ok")
