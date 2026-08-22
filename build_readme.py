#!/usr/bin/env python3
"""Genera README.md (español) y README.en.md (inglés).

Los dos salen de los mismos datos (proyectos.py) a proposito: escribirlos a
mano seria garantizar que tarde o temprano digan cosas distintas.

Un README no puede tener un selector de idioma de verdad —es markdown
estatico, sin JavaScript—, asi que el selector es un enlace al otro archivo.
Cada version esta en UN solo idioma, sin lineas mezcladas.

Las imagenes van por URL absoluta de raw.githubusercontent: en la pagina de
perfil (github.com/BanarySource) un path relativo NO resuelve contra el repo
y las imagenes salen en blanco. Verificado.
"""
from __future__ import annotations

import pathlib
import re
import sys
import xml.etree.ElementTree as ET

from proyectos import CONTACTOS, IDIOMAS, TARJETAS

RAIZ = pathlib.Path(__file__).resolve().parent
BASE = "https://raw.githubusercontent.com/BanarySource/BanarySource/main/assets"

ARCHIVOS = {"es": "README.md", "en": "README.en.md"}

def escapar(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def alternativo(t: dict, idioma: str) -> str:
    """El texto de la tarjeta es imagen, asi que el alt lleva el contenido
    completo: es lo unico que puede leer un lector de pantalla."""
    from proyectos import stack_de
    d = t[idioma]
    tec = "Tecnologías" if idioma == "es" else "Technologies"
    est = "Estado" if idioma == "es" else "Status"
    return (f"{d['titulo']} — {d['lema']}. {d['texto']} "
            f"{tec}: {', '.join(stack_de(t, idioma))}. "
            f"{est}: {d['estado']}. {d['enlace']}.")


def icono_titulo(nombre: str) -> str:
    """Icono de un título de sección. Sustituye a un emoji: el emoji lo pinta
    el sistema de quien mira, asi que cambia de forma segun la plataforma."""
    return (f'<img src="{BASE}/icons/{nombre}.svg" width="21" align="top"'
            f' alt="">')


def imagen(ruta: str, alt: str, ancho: str = "100%") -> str:
    return (f'<picture>'
            f'<source media="(prefers-color-scheme: dark)" srcset="{BASE}/{ruta}-dark.svg">'
            f'<source media="(prefers-color-scheme: light)" srcset="{BASE}/{ruta}-light.svg">'
            f'<img src="{BASE}/{ruta}-dark.svg" width="{ancho}" alt="{escapar(alt)}">'
            f'</picture>')


def panel_contacto(c_: dict, idioma: str) -> str:
    d = c_[idioma]
    alt = f'{d["nombre"]}: {d["dato"]}. {d["nota"]}.'
    img = imagen(f"contacto/{c_['archivo']}-{idioma}", alt)
    return f'<a href="{c_["url"]}">{img}</a>'


def fila_contacto(contactos: list[dict], idioma: str) -> str:
    """Una tabla por grupo: las celdas de una misma tabla comparten ancho, y
    mezclar paneles anchos y estrechos en una sola los descuadraria."""
    ancho = f"{100 // len(contactos)}%"
    celdas = "".join(f'<td width="{ancho}" valign="top">'
                     f'{panel_contacto(c_, idioma)}</td>' for c_ in contactos)
    return f'''<table>
<tr>{celdas}</tr>
</table>'''


def rejilla(tarjetas: list[dict], idioma: str) -> str:
    filas = ["<table>"]
    for i in range(0, len(tarjetas), 2):
        pareja = tarjetas[i:i + 2]
        filas.append("<tr>")
        for t in pareja:
            medio = imagen(f"cards/{t['archivo']}-{idioma}", alternativo(t, idioma))
            if t["url"]:
                medio = f'<a href="{t["url"]}">{medio}</a>'
            filas.append(f'<td width="50%" valign="top">{medio}</td>')
        if len(pareja) == 1:                 # celda vacía para cuadrar la fila
            filas.append('<td width="50%"></td>')
        filas.append("</tr>")
    filas.append("</table>")
    return "\n".join(filas)


def construir(idioma: str) -> str:
    t = IDIOMAS[idioma]

    # Selector de idioma: el actual en negritas, el otro como enlace.
    otro = f'<a href="{t["archivo_otro"]}">{t["otro"]}</a>'
    selector = f'<b>{t["nombre"]}</b> &nbsp;·&nbsp; {otro}'

    return f'''<div align="center">

{imagen(f"banner-{idioma}", t["alt_banner"])}

<p>{selector}</p>

</div>

---

### {t["titular"]}

{t["intro"]}

---

## {t["h_proyectos"]}

### {icono_titulo("codigo")} {t["h_software"]}

{rejilla(TARJETAS[:4], idioma)}

### {icono_titulo("robot")} {t["h_hardware"]}

{rejilla(TARJETAS[4:], idioma)}

---

## {t["h_stack"]}

<div align="center">
{imagen(f"stack-{idioma}", t["alt_stack"])}
</div>

---

## {t["h_contacto"]}

{fila_contacto(CONTACTOS[:2], idioma)}

{fila_contacto(CONTACTOS[2:], idioma)}

<div align="center">
<sub>{t["pie_1"]}<br>
{t["pie_2"]}</sub>
<br><br>
<sub>{t["pie_3"].replace("**", "")}</sub>
</div>
'''


def vista_previa(md: str) -> str:
    """preview.html: el mismo README apuntando a los SVG locales, en los dos
    temas. Sirve para ver contraste y desbordes ANTES de publicar, que es
    donde salen los problemas."""
    cuerpo = md.replace(BASE, "assets")
    cuerpo = re.sub(r"^#{2,3} (.+)$", r"<h3></h3>", cuerpo, flags=re.M)
    cuerpo = re.sub(r"\*\*(.+?)\*\*", r"<b></b>", cuerpo)
    cuerpo = cuerpo.replace("---", "<hr>")
    return f"""<!doctype html><meta charset="utf-8"><title>Vista previa del perfil</title>
<style>
 body{{margin:0;background:#0d1117;color:#e6edf3;font:15px/1.6 system-ui}}
 .hoja{{max-width:900px;margin:0 auto;padding:28px}}
 img{{max-width:100%}} table{{border-collapse:separate;border-spacing:8px;width:100%}}
 td{{width:50%;vertical-align:top}} hr{{border:0;border-top:1px solid #30363d;margin:24px 0}}
 a{{color:#58a6ff}} h3{{margin:26px 0 12px}}
 .claro{{background:#fff;color:#1f2328}} .claro a{{color:#0969da}}
 .barra{{font:600 12px system-ui;color:#8b949e;padding:10px 28px;background:#010409}}
</style>
<div class="barra">TEMA OSCURO</div><div class="hoja">{cuerpo}</div>
<div class="claro"><div class="barra" style="background:#f6f8fa;color:#57606a">TEMA CLARO</div>
<div class="hoja">{cuerpo.replace("-dark.svg", "-light.svg")}</div></div>
"""


def validar_svg() -> None:
    """Un SVG mal formado no falla al escribirse: falla al cargarse, y ahi ya
    esta publicado. Paso el 22-ago con "DATA & INFRA": el "&" sin escapar
    rompia el XML y la imagen no aparecia. Se valida antes de publicar.
    """
    archivos = sorted((RAIZ / "assets").rglob("*.svg"))
    rotos = []
    for f in archivos:
        try:
            ET.parse(f)
        except ET.ParseError as e:
            rotos.append(f"{f.relative_to(RAIZ)}: {e}")
    if rotos:
        print("SVG mal formados, NO publiques:", file=sys.stderr)
        for r in rotos:
            print(f"  {r}", file=sys.stderr)
        raise SystemExit(1)
    print(f"{len(archivos)} SVG validados")


def main() -> None:
    validar_svg()
    for idioma, nombre in ARCHIVOS.items():
        destino = RAIZ / nombre
        md = construir(idioma)
        destino.write_text(md, encoding="utf-8")
        print(f"{nombre}: {destino.stat().st_size:,} bytes")
        if idioma == "es":
            (RAIZ / "preview.html").write_text(vista_previa(md), encoding="utf-8")
            print("preview.html: vista previa en tema claro y oscuro")


if __name__ == "__main__":
    main()
