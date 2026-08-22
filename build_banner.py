#!/usr/bin/env python3
"""Genera assets/banner-dark.svg y assets/banner-light.svg.

El logo real de Banary Source (engrane abierto + cerebro de circuito) se
incrusta como data URI para que el banner no dependa de ningun host externo.
"""
from __future__ import annotations

import base64
import pathlib

from proyectos import IDIOMAS

RAIZ = pathlib.Path(__file__).resolve().parent
ASSETS = RAIZ / "assets"

# Paleta tomada del CSS en produccion de banarysource.org
TEMAS = {
    "dark": dict(
        bg="#16181C", panel="#1E2126", borde="#262A31",
        marca="#22C7F5", texto="#F7F8FA", tenue="#A3AAB3",
        ambar="#FFC24F", verde="#2FD69B", glow=".55",
    ),
    "light": dict(
        bg="#F7F8FA", panel="#FFFFFF", borde="#E4E8ED",
        marca="#0E9CCF", texto="#16181C", tenue="#5A626B",
        ambar="#B07A00", verde="#0E7A5A", glow=".22",
    ),
}

FUENTE = "'Segoe UI',system-ui,-apple-system,Helvetica,Arial,sans-serif"


def trazos_circuito(c: dict) -> str:
    """Circuito del flanco derecho: pista tenue fija + segmento encendido.

    REGLA DE ESTE ARCHIVO: el dibujo debe quedar terminado SIN animacion.
    Se verifico que el SVG embebido con <img> puede no animar (ni CSS ni
    SMIL), asi que cada elemento animado lleva un valor base que ya se ve
    bien por si solo; el <animate> solo lo mejora donde si corre.

    Por eso el segmento encendido no arranca en el borde: su dashoffset base
    lo deja a media pista, que es como se ve deliberado estando quieto.
    """
    lineas = [
        # (puntos, dashoffset base, retraso del ciclo)
        ("780,182 910,182 940,212 1160,212", -170, "0s"),
        ("780,222 980,222 1010,252 1160,252", -300, "-1.5s"),
        ("780,262 880,262 910,232 1160,232", -95, "-3s"),
    ]
    piezas = []
    for pts, offset, delay in lineas:
        piezas.append(f'<polyline class="pista" points="{pts}"/>')
        piezas.append(
            f'<polyline class="pulso" points="{pts}" stroke-dashoffset="{offset}">'
            f'<animate attributeName="stroke-dashoffset" from="480" to="-70"'
            f' dur="4.5s" begin="{delay}" repeatCount="indefinite"/>'
            f'</polyline>'
        )
        for punto, opacidad in ((pts.split()[0], ".45"), (pts.split()[-1], ".95")):
            x, y = punto.split(",")
            piezas.append(
                f'<circle class="nodo" cx="{x}" cy="{y}" r="4" opacity="{opacidad}">'
                f'<animate attributeName="opacity" values="{opacidad};1;{opacidad}"'
                f' dur="4.5s" begin="{delay}" repeatCount="indefinite"/>'
                f'</circle>'
            )
    return "".join(piezas)


def construir(tema: str, idioma: str, logo_b64: str) -> str:
    c, t = TEMAS[tema], IDIOMAS[idioma]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300" role="img" aria-label="{t['alt_banner']}">
  <title>{t["alt_banner"]}</title>
  <defs>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{c['marca']}" stop-opacity="{c['glow']}"/>
      <stop offset="60%" stop-color="{c['marca']}" stop-opacity=".08"/>
      <stop offset="100%" stop-color="{c['marca']}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="regla" gradientUnits="userSpaceOnUse" x1="322" y1="0" x2="742" y2="0">
      <stop offset="0%" stop-color="{c['marca']}"/>
      <stop offset="70%" stop-color="{c['marca']}" stop-opacity=".35"/>
      <stop offset="100%" stop-color="{c['marca']}" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="marco"><rect x="0" y="0" width="1200" height="300" rx="20"/></clipPath>
  </defs>
  <style>
    .pista  {{ fill:none; stroke:{c['marca']}; stroke-opacity:.16; stroke-width:2;
               stroke-linecap:round; stroke-linejoin:round; }}
    .pulso  {{ fill:none; stroke:{c['marca']}; stroke-opacity:.95; stroke-width:2.5;
               stroke-linecap:round; stroke-linejoin:round; stroke-dasharray:70 410; }}
    .nodo   {{ fill:{c['marca']}; }}
    .subray {{ stroke:url(#regla); stroke-width:3; stroke-linecap:round; fill:none; }}
    .rejilla{{ stroke:{c['marca']}; stroke-opacity:.06; stroke-width:1; fill:none; }}
  </style>

  <g clip-path="url(#marco)">
    <rect width="1200" height="300" fill="{c['bg']}"/>
    <g class="rejilla">
      <path d="M0 75h1200M0 150h1200M0 225h1200"/>
      <path d="M300 0v300M600 0v300M900 0v300"/>
    </g>
    <!-- Trasladado al centro para que el escalado del latido no lo desplace. -->
    <g transform="translate(180 150)">
      <circle cx="0" cy="0" r="150" fill="url(#glow)" opacity=".85">
        <animate attributeName="opacity" values=".85;1;.85" dur="4.5s" repeatCount="indefinite"/>
        <animateTransform attributeName="transform" type="scale"
                          values="1;1.06;1" dur="4.5s" repeatCount="indefinite"/>
      </circle>
    </g>
    {trazos_circuito(c)}
    <image x="105" y="75" width="150" height="150"
           href="data:image/png;base64,{logo_b64}"
           preserveAspectRatio="xMidYMid meet"/>

    <text x="324" y="74" font-family="{FUENTE}" font-size="14" font-weight="600"
          letter-spacing="4.5" fill="{c['tenue']}">EST. 2015 · MÉXICO</text>
    <text x="320" y="136" font-family="{FUENTE}" font-size="60" font-weight="700"
          letter-spacing="7" fill="{c['texto']}">BANARY SOURCE</text>
    <path class="subray" d="M322 160 H742"/>
    <text x="322" y="200" font-family="{FUENTE}" font-size="25" font-weight="600"
          letter-spacing="1.5" fill="{c['marca']}">{t["lema_grande"]}</text>
    <text x="322" y="232" font-family="{FUENTE}" font-size="17" font-weight="400"
          letter-spacing=".8" fill="{c['tenue']}">{t["lema_chico"]}</text>

    <rect x="0" y="292" width="1200" height="8" fill="{c['marca']}" opacity=".9"/>
  </g>
</svg>
'''


def main() -> None:
    logo_b64 = base64.b64encode((ASSETS / "logo.png").read_bytes()).decode("ascii")
    ASSETS.mkdir(exist_ok=True)
    for idioma in IDIOMAS:
        for tema in TEMAS:
            destino = ASSETS / f"banner-{idioma}-{tema}.svg"
            destino.write_text(construir(tema, idioma, logo_b64), encoding="utf-8")
            print(f"{destino.name}: {destino.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
