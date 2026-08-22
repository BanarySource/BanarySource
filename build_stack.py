#!/usr/bin/env python3
"""Genera assets/stack-dark.svg y assets/stack-light.svg.

Tira de tecnologias dibujada como SVG propio en vez de badges de shields.io:
un solo archivo en el repo, sin peticiones a terceros que puedan caerse o
quedar bloqueadas. Es decorativa (no lleva enlaces), asi que no pierde nada
por estar embebida con <img>.

Igual que el banner: TODO se ve terminado sin animacion.
"""
from __future__ import annotations

import pathlib

RAIZ = pathlib.Path(__file__).resolve().parent
ASSETS = RAIZ / "assets"

TEMAS = {
    "dark": dict(bg="#16181C", chip="#1E2126", borde="#2E343C",
                 texto="#D2D9E0", titulo="#22C7F5"),
    "light": dict(bg="#F7F8FA", chip="#FFFFFF", borde="#D9E0E7",
                  texto="#3A424B", titulo="#0E9CCF"),
}

FUENTE = "'Segoe UI',system-ui,-apple-system,Helvetica,Arial,sans-serif"

FILAS = [
    ("SOFTWARE", ["TypeScript", "React", "Next.js", "Node.js", "Python",
                  "FastAPI", "Vite", "Electron"]),
    ("DATOS E INFRA", ["PostgreSQL", "Supabase", "Prisma", "Cloudflare Workers",
                       "Vercel", "Railway", "Stripe", "Docker"]),
    ("HARDWARE", ["ESP32", "RP2040", "Arduino", "C++", "PIC18F", "KiCad",
                  "Impresión 3D", "Visión artificial"]),
]

# Geometria
MARGEN_X = 34
ANCHO = 1200
ALTO_CHIP = 34
SALTO_FILA = 78
PAD_CHIP = 17          # relleno horizontal a cada lado del texto
HUECO = 9              # separacion entre chips
TAM_TEXTO = 15
ANCHO_CARACTER = 0.545  # aproximacion del ancho medio de glifo para esta fuente


def ancho_chip(etiqueta: str) -> float:
    return len(etiqueta) * TAM_TEXTO * ANCHO_CARACTER + PAD_CHIP * 2


def construir(tema: str) -> str:
    c = TEMAS[tema]
    cuerpo: list[str] = []
    y = 40

    for titulo, etiquetas in FILAS:
        cuerpo.append(
            f'<text x="{MARGEN_X}" y="{y}" font-family="{FUENTE}" font-size="12"'
            f' font-weight="700" letter-spacing="3" fill="{c["titulo"]}">{titulo}</text>'
        )
        x = MARGEN_X
        fila_y = y + 14
        for etiqueta in etiquetas:
            w = ancho_chip(etiqueta)
            if x + w > ANCHO - MARGEN_X:      # salto de linea si no cabe
                x = MARGEN_X
                fila_y += ALTO_CHIP + HUECO
            cuerpo.append(
                f'<rect x="{x:.1f}" y="{fila_y}" width="{w:.1f}" height="{ALTO_CHIP}"'
                f' rx="{ALTO_CHIP / 2}" fill="{c["chip"]}" stroke="{c["borde"]}"/>'
                f'<text x="{x + w / 2:.1f}" y="{fila_y + 22}" font-family="{FUENTE}"'
                f' font-size="{TAM_TEXTO}" font-weight="500" fill="{c["texto"]}"'
                f' text-anchor="middle">{etiqueta}</text>'
            )
            x += w + HUECO
        y = fila_y + SALTO_FILA

    alto = y - SALTO_FILA + ALTO_CHIP + 34
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ANCHO} {alto}"'
        f' width="{ANCHO}" height="{alto}" role="img"'
        f' aria-label="Tecnologias que usa Banary Source">\n'
        f'  <title>Stack de Banary Source</title>\n'
        f'  <rect width="{ANCHO}" height="{alto}" rx="16" fill="{c["bg"]}"/>\n  '
        + "\n  ".join(cuerpo)
        + "\n</svg>\n"
    )


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    for tema in TEMAS:
        destino = ASSETS / f"stack-{tema}.svg"
        destino.write_text(construir(tema), encoding="utf-8")
        print(f"{destino.name}: {destino.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
