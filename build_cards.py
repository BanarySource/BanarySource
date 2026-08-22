#!/usr/bin/env python3
"""Genera una tarjeta-panel SVG por proyecto: 7 proyectos x 2 idiomas x 2 temas.

GitHub borra todo el CSS de un README, asi que un panel flotante (fondo,
borde redondeado, sombra) no se puede hacer con HTML: hay que dibujarlo. Cada
proyecto se dibuja como su propio SVG y en el README se envuelve en un enlace,
de modo que la tarjeta entera es clicable.

Como en el banner, TODO debe verse terminado sin animacion.

Las siete tarjetas comparten el mismo lienzo (ANCHO x ALTO) a proposito: al
escalarse al ancho de su celda, un lienzo identico da una altura identica y la
rejilla no queda dispareja.
"""
from __future__ import annotations

import pathlib

from proyectos import TARJETAS, acento, stack_de

RAIZ = pathlib.Path(__file__).resolve().parent
ASSETS = RAIZ / "assets" / "cards"

TEMAS = {
    "dark": dict(panel="#1E2126", borde="#2E343C", titulo="#F7F8FA",
                 texto="#A3AAB3", chip="#262A31", chip_borde="#343A43",
                 chip_texto="#C6CED6", sombra="#000000", sombra_op=".45",
                 tile_op=".16"),
    "light": dict(panel="#FFFFFF", borde="#E1E7EC", titulo="#16181C",
                  texto="#5A626B", chip="#F2F5F8", chip_borde="#DFE5EB",
                  chip_texto="#3A424B", sombra="#8C99A6", sombra_op=".28",
                  tile_op=".12"),
}

FUENTE = "'Segoe UI',system-ui,-apple-system,Helvetica,Arial,sans-serif"

# Lienzo compartido por las siete tarjetas.
ANCHO, ALTO = 620, 372
MARGEN = 14                     # aire para que quepa la sombra
PAD = 34                        # relleno interior del panel
TAM_TEXTO, SALTO = 15, 23
MAX_LINEAS = 5
# Franja reservada a la descripcion. El bloque se centra dentro de ella para
# que una tarjeta de 3 lineas no deje un hueco muerto sobre los chips, y que
# las siete se vean equilibradas aunque su texto no mida lo mismo.
DESC_Y0, DESC_ALTO = 126, 142
ANCHO_CARACTER = 0.503          # ancho medio de glifo estimado para esta fuente


def escapar(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def ancho_texto(s: str, tam: float) -> float:
    return len(s) * tam * ANCHO_CARACTER


def repartir(texto: str, ancho_max: float, tam: float) -> list[str]:
    """Corta el texto en lineas que quepan: SVG no sabe hacer saltos solo."""
    lineas: list[str] = []
    actual = ""
    for palabra in texto.split():
        prueba = f"{actual} {palabra}".strip()
        if ancho_texto(prueba, tam) <= ancho_max:
            actual = prueba
        else:
            if actual:
                lineas.append(actual)
            actual = palabra
    if actual:
        lineas.append(actual)
    return lineas


def construir(t: dict, idioma: str, tema: str) -> str:
    c, d = TEMAS[tema], t[idioma]
    a = acento(t["acento"], tema)
    px, py = MARGEN, MARGEN - 4
    pw, ph = ANCHO - MARGEN * 2, ALTO - MARGEN * 2
    x0 = px + PAD

    lineas = repartir(d["texto"], pw - PAD * 2, TAM_TEXTO)
    if len(lineas) > MAX_LINEAS:                     # el texto no cabe: avisar
        raise ValueError(
            f"{t['archivo']} ({idioma}): {len(lineas)} líneas, caben {MAX_LINEAS}. "
            f"Acorta el texto en proyectos.py."
        )
    arranque = DESC_Y0 + (DESC_ALTO - len(lineas) * SALTO) / 2 + TAM_TEXTO
    desc = "".join(
        f'<text x="{x0}" y="{arranque + i * SALTO:.1f}" font-family="{FUENTE}"'
        f' font-size="{TAM_TEXTO}" fill="{c["texto"]}">{escapar(ln)}</text>'
        for i, ln in enumerate(lineas)
    )

    chips, cx = [], x0
    for etiqueta in stack_de(t, idioma):
        w = ancho_texto(etiqueta, 13) + 26
        chips.append(
            f'<rect x="{cx:.1f}" y="282" width="{w:.1f}" height="27" rx="13.5"'
            f' fill="{c["chip"]}" stroke="{c["chip_borde"]}"/>'
            f'<text x="{cx + w / 2:.1f}" y="300" font-family="{FUENTE}"'
            f' font-size="13" fill="{c["chip_texto"]}" text-anchor="middle">'
            f'{escapar(etiqueta)}</text>'
        )
        cx += w + 7
    if cx > ANCHO - MARGEN - PAD:
        raise ValueError(f"{t['archivo']} ({idioma}): los chips no caben en la fila.")

    pie = (
        f'<circle cx="{x0 + 5}" cy="336" r="5" fill="{t["color_estado"]}"/>'
        f'<text x="{x0 + 18}" y="341" font-family="{FUENTE}" font-size="13.5"'
        f' font-weight="600" fill="{c["titulo"]}">{escapar(d["estado"])}</text>'
        f'<text x="{x0 + 26 + ancho_texto(d["estado"], 13.5)}" y="341"'
        f' font-family="{FUENTE}" font-size="13.5" fill="{a}">'
        f'— {escapar(d["enlace"])}</text>'
    )

    tam_sigla = 17 if len(t["sigla"]) < 3 else 14
    etiqueta = escapar(f'{d["titulo"]} — {d["lema"]}')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ANCHO} {ALTO}" width="{ANCHO}" height="{ALTO}" role="img" aria-label="{etiqueta}">
  <title>{etiqueta}</title>
  <defs>
    <filter id="sombra" x="-20%" y="-20%" width="140%" height="150%">
      <feDropShadow dx="0" dy="6" stdDeviation="9"
                    flood-color="{c['sombra']}" flood-opacity="{c['sombra_op']}"/>
    </filter>
    <clipPath id="recorte">
      <rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="18"/>
    </clipPath>
  </defs>

  <!-- Panel flotante -->
  <rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="18"
        fill="{c['panel']}" stroke="{c['borde']}" filter="url(#sombra)"/>
  <!-- Filo de color del proyecto, recortado a la esquina redondeada -->
  <g clip-path="url(#recorte)">
    <rect x="{px}" y="{py}" width="7" height="{ph}" fill="{a}"/>
  </g>

  <!-- Placa con la sigla -->
  <rect x="{x0}" y="42" width="48" height="48" rx="13"
        fill="{a}" fill-opacity="{c['tile_op']}" stroke="{a}" stroke-opacity=".5"/>
  <text x="{x0 + 24}" y="{73 if len(t['sigla']) < 3 else 72}" font-family="{FUENTE}"
        font-size="{tam_sigla}" font-weight="700" fill="{a}"
        text-anchor="middle">{t['sigla']}</text>

  <text x="{x0 + 64}" y="65" font-family="{FUENTE}" font-size="25"
        font-weight="700" fill="{c['titulo']}">{escapar(d['titulo'])}</text>
  <text x="{x0 + 64}" y="87" font-family="{FUENTE}" font-size="14.5"
        font-weight="600" fill="{a}">{escapar(d['lema'])}</text>

  {desc}
  {"".join(chips)}
  {pie}
</svg>
'''


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    n = 0
    for t in TARJETAS:
        for idioma in ("es", "en"):
            for tema in TEMAS:
                destino = ASSETS / f"{t['archivo']}-{idioma}-{tema}.svg"
                destino.write_text(construir(t, idioma, tema), encoding="utf-8")
                n += 1
    print(f"{n} tarjetas generadas en assets/cards/")


if __name__ == "__main__":
    main()
