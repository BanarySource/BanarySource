#!/usr/bin/env python3
"""Iconos monolinea dibujados a mano, en una retícula de 24x24.

Se dibujan en vez de usar emoji a proposito: el emoji lo pinta el sistema
operativo de quien mira, asi que cambia de forma en Windows, Mac y Android, y
en Windows los de bandera ni siquiera salen (se ven como dos letras). Un
trazo vectorial se ve igual en todas partes.

Cada icono es una lista de elementos SVG con {c} donde va el color, para que
el mismo dibujo sirva en cualquier panel.
"""
from __future__ import annotations

# Trazo comun: monolinea, extremos redondeados, sin relleno.
TRAZO = 'fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'

ICONOS: dict[str, str] = {
    # Globo terráqueo: la plataforma web.
    "globo": f'''<g {TRAZO}>
      <circle cx="12" cy="12" r="9"/>
      <ellipse cx="12" cy="12" rx="4" ry="9"/>
      <path d="M3.2 12h17.6M4.8 6.6h14.4M4.8 17.4h14.4"/>
    </g>''',

    # Sobre: el correo.
    "correo": f'''<g {TRAZO}>
      <rect x="2.5" y="5" width="19" height="14" rx="2.5"/>
      <path d="M3.4 7.2 12 13.4l8.6-6.2"/>
    </g>''',

    # Pantalla con el triangulo de reproducir: YouTube.
    "youtube": f'''<g {TRAZO}>
      <rect x="2" y="5" width="20" height="14" rx="4.5"/>
      <path d="M10.2 9.1 15.6 12l-5.4 2.9z"/>
    </g>''',

    # Cuadro redondeado, objetivo y destello: Instagram.
    "instagram": f'''<g {TRAZO}>
      <rect x="3" y="3" width="18" height="18" rx="5"/>
      <circle cx="12" cy="12" r="4"/>
      <circle cx="16.9" cy="7.1" r=".9" fill="{{c}}"/>
    </g>''',

    # Nota musical con gancho: TikTok.
    "tiktok": f'''<g {TRAZO}>
      <circle cx="8.6" cy="16.4" r="3.9"/>
      <path d="M12.5 16.4V3.6"/>
      <path d="M12.5 3.6c0 3.4 2.6 5.7 6 5.9"/>
    </g>''',

    # Corchetes y barra: la sección de software.
    "codigo": f'''<g {TRAZO}>
      <path d="M8.8 6.6 3.6 12l5.2 5.4M15.2 6.6 20.4 12l-5.2 5.4M13.4 4.6l-2.8 14.8"/>
    </g>''',

    # Cabeza de robot: la sección de hardware.
    "robot": f'''<g {TRAZO}>
      <rect x="3.6" y="8.4" width="16.8" height="11.6" rx="3.4"/>
      <path d="M12 8.4V4.6"/>
      <circle cx="12" cy="3.4" r="1.5"/>
      <path d="M1.6 13.4v3M22.4 13.4v3"/>
      <circle cx="9" cy="13.9" r="1.3" fill="{{c}}" stroke="none"/>
      <circle cx="15" cy="13.9" r="1.3" fill="{{c}}" stroke="none"/>
    </g>''',
}


def icono(nombre: str, color: str, x: float, y: float, tam: float) -> str:
    """Coloca un icono de 24x24 escalado a `tam` con su esquina en (x, y)."""
    k = tam / 24
    return (f'<g transform="translate({x} {y}) scale({k:.4f})">'
            f'{ICONOS[nombre].format(c=color)}</g>')


def suelto(nombre: str, color: str, tam: int = 24) -> str:
    """Icono como archivo SVG independiente, para incrustarlo en un título.

    Va en un solo color (no lleva variante clara/oscura): el cian de marca se
    lee bien sobre los dos fondos de GitHub, asi que un archivo basta.
    """
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
            f'width="{tam}" height="{tam}" role="img" aria-hidden="true">'
            f'{ICONOS[nombre].format(c=color)}</svg>\n')
