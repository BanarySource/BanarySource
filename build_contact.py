#!/usr/bin/env python3
"""Genera los paneles de contacto y los iconos de los títulos de sección.

Los paneles son SVG por el mismo motivo que las tarjetas: GitHub borra el CSS
de un README, asi que un panel con fondo, borde y sombra hay que dibujarlo.
Cada uno se envuelve en un enlace, asi que el panel entero es clicable.

Cada red lleva SU color de marca en el filo y el icono: es lo que hace que se
reconozca de un vistazo sin depender del logotipo original.

NADA de cifras de seguidores. Un README es estatico: un numero escrito hoy se
queda congelado y a las pocas semanas hace ver el perfil abandonado. Los
paneles dicen que hay en cada canal, que es cierto siempre.
"""
from __future__ import annotations

import pathlib

from iconos import icono, suelto
from proyectos import CONTACTOS, IDIOMAS, acento

RAIZ = pathlib.Path(__file__).resolve().parent
ASSETS = RAIZ / "assets" / "contacto"
ICONOS_DIR = RAIZ / "assets" / "icons"

MARCA = "#22C7F5"

TEMAS = {
    "dark": dict(panel="#1E2126", borde="#2E343C", titulo="#F7F8FA",
                 texto="#A3AAB3", sombra="#000000", sombra_op=".45"),
    "light": dict(panel="#FFFFFF", borde="#E1E7EC", titulo="#16181C",
                  texto="#5A626B", sombra="#8C99A6", sombra_op=".28"),
}

FUENTE = "'Segoe UI',system-ui,-apple-system,Helvetica,Arial,sans-serif"

ALTO = 148
MARGEN = 10
PAD = 26
ANCHO_CARACTER = 0.503


def escapar(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def ancho_texto(s: str, tam: float) -> float:
    return len(s) * tam * ANCHO_CARACTER


def construir(c_: dict, idioma: str, tema: str) -> str:
    """`c_` es una entrada de CONTACTOS; `ancho` viene en la propia entrada."""
    t = TEMAS[tema]
    d = c_[idioma]
    a = acento(c_["color"], tema)
    ancho = c_["ancho"]
    px, py = MARGEN, MARGEN - 4
    pw, ph = ancho - MARGEN * 2, ALTO - MARGEN * 2
    x0 = px + PAD

    for campo, tam, limite in ((d["nombre"], 23, ancho - MARGEN - PAD - 66),
                               (d["dato"], 16, ancho - MARGEN - PAD - 66),
                               (d["nota"], 16, ancho - MARGEN - PAD * 2)):
        if ancho_texto(campo, tam) > limite:
            raise ValueError(f"{c_['archivo']} ({idioma}): «{campo}» no cabe. "
                             f"Acórtalo en proyectos.py.")

    etiqueta = escapar(f'{d["nombre"]} — {d["dato"]}')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {ALTO}" width="{ancho}" height="{ALTO}" role="img" aria-label="{etiqueta}">
  <title>{etiqueta}</title>
  <defs>
    <filter id="s" x="-20%" y="-20%" width="140%" height="150%">
      <feDropShadow dx="0" dy="5" stdDeviation="8"
                    flood-color="{t['sombra']}" flood-opacity="{t['sombra_op']}"/>
    </filter>
    <clipPath id="r"><rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="16"/></clipPath>
  </defs>

  <rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="16"
        fill="{t['panel']}" stroke="{t['borde']}" filter="url(#s)"/>
  <g clip-path="url(#r)"><rect x="{px}" y="{py}" width="6" height="{ph}" fill="{a}"/></g>

  {icono(c_["icono"], a, x0, 30, 34)}

  <text x="{x0 + 50}" y="47" font-family="{FUENTE}" font-size="23"
        font-weight="700" fill="{t['titulo']}">{escapar(d["nombre"])}</text>
  <text x="{x0 + 50}" y="70" font-family="{FUENTE}" font-size="16"
        font-weight="600" fill="{a}">{escapar(d["dato"])}</text>
  <text x="{x0}" y="112" font-family="{FUENTE}" font-size="16"
        fill="{t['texto']}">{escapar(d["nota"])}</text>
</svg>
'''


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    ICONOS_DIR.mkdir(parents=True, exist_ok=True)

    n = 0
    for c_ in CONTACTOS:
        for idioma in IDIOMAS:
            for tema in TEMAS:
                destino = ASSETS / f"{c_['archivo']}-{idioma}-{tema}.svg"
                destino.write_text(construir(c_, idioma, tema), encoding="utf-8")
                n += 1
    print(f"{n} paneles de contacto")

    # Iconos de los títulos de sección, en el cian de marca.
    for nombre in ("codigo", "robot"):
        (ICONOS_DIR / f"{nombre}.svg").write_text(suelto(nombre, MARCA),
                                                  encoding="utf-8")
    print("2 iconos de sección para los títulos (sustituyen a los emoji)")


if __name__ == "__main__":
    main()
