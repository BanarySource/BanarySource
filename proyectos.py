#!/usr/bin/env python3
"""Los datos de los siete proyectos, en español y en inglés.

Vive aparte de los generadores para que cambiar un texto sea tocar UN sitio y
que las dos versiones del perfil no se puedan desincronizar.

Los colores de acento salen del CSS en producción de banarysource.org, salvo
el violeta de Docentia Digital, que es el suyo propio.
"""
from __future__ import annotations

VERDE, AZUL, GRIS = "#2FD69B", "#22C7F5", "#8A939C"

TARJETAS = [
    dict(
        archivo="banary-source", sigla="BS", acento="#22C7F5",
        stack=["React", "TypeScript", "PostgreSQL", "Prisma"],
        color_estado=VERDE, url="https://banarysource.org",
        es=dict(
            titulo="Banary Source", lema="Aula y club de robótica",
            texto="Nuestra plataforma. Las materias que impartimos y el club de "
                  "robótica en un solo lugar, con rangos, experiencia y evidencias "
                  "por alumno. La usan nuestros estudiantes todos los días.",
            estado="En producción", enlace="banarysource.org",
        ),
        en=dict(
            titulo="Banary Source", lema="Classroom and robotics club",
            texto="Our own platform. The courses we teach and the robotics club "
                  "in one place, with ranks, experience points and per-student "
                  "evidence. Our students use it every day.",
            estado="Live", enlace="banarysource.org",
        ),
    ),
    dict(
        archivo="docentia-digital", sigla="DD", acento="#7C3AED",
        stack=["Next.js", "TypeScript", "Supabase", "IA"],
        color_estado=VERDE, url="https://docentiadigital.com",
        es=dict(
            titulo="Docentia Digital", lema="Gestión académica inteligente",
            texto="Calificaciones, rúbricas y evaluación asistida por IA para "
                  "docentes. La IA elige un nivel declarado de la rúbrica y "
                  "justifica la nota en los términos del propio profesor.",
            estado="En producción", enlace="docentiadigital.com",
        ),
        en=dict(
            titulo="Docentia Digital", lema="Smart academic management",
            texto="Grading, rubrics and AI-assisted assessment for teachers. The "
                  "AI picks a level declared in the rubric and justifies the mark "
                  "in the teacher's own terms.",
            estado="Live", enlace="docentiadigital.com",
        ),
    ),
    dict(
        archivo="delfino", sigla="DF", acento="#2FD69B",
        stack=["Cloudflare Workers", "Supabase", "Stripe"],
        color_estado=VERDE, url="https://delfino.app",
        es=dict(
            titulo="Delfino", lema="Suéltalo y yo lo acomodo",
            texto="Secretario personal: le cuentas el día en lenguaje natural y él "
                  "lo convierte en tareas, plazos y un solo foco. Trae diario "
                  "personal y suscripción activa.",
            estado="En producción", enlace="delfino.app",
        ),
        en=dict(
            titulo="Delfino", lema="Just say it, I'll sort it out",
            texto="A personal secretary: tell it about your day in plain language "
                  "and it turns that into tasks, deadlines and a single focus. "
                  "Includes a personal journal and an active subscription.",
            estado="Live", enlace="delfino.app",
        ),
    ),
    dict(
        archivo="print-cost-manager", sigla="PC", acento="#FFC24F",
        stack=["React", "TypeScript", "Vite"],
        color_estado=VERDE, url="https://printcostmanager.vercel.app",
        es=dict(
            titulo="Print Cost Manager", lema="Lo que de verdad cuesta imprimir",
            texto="Calcula el costo real de una impresión 3D —filamento, energía, "
                  "desgaste y tiempo— en vez de estimarlo a ojo. Gratis y sin "
                  "registro.",
            estado="En línea", enlace="printcostmanager.vercel.app",
        ),
        en=dict(
            titulo="Print Cost Manager", lema="What a 3D print really costs",
            texto="Works out the true cost of a 3D print —filament, power, wear "
                  "and time— instead of guessing at it. Free, no sign-up.",
            estado="Live", enlace="printcostmanager.vercel.app",
        ),
    ),
    dict(
        archivo="robotbuscador", sigla="RB", acento="#FF7A5C",
        stack=["ESP32-S3", "C++", "Visión artificial"],
        stack_en=["ESP32-S3", "C++", "Computer vision"],
        color_estado=AZUL, url=None,
        es=dict(
            titulo="RobotBuscador", lema="InnoBótica 2026 · InnovaTecNM",
            texto="Robot 100 % autónomo de 14 cm que busca y desaloja 12 conos de "
                  "un tablero de 122×244 cm en cinco minutos. Resuelve primero la "
                  "localización: cambiar de estrategia es cambiar código, no "
                  "rediseñar el robot.",
            estado="En competencia", enlace="Etapa regional · septiembre 2026",
        ),
        en=dict(
            titulo="RobotBuscador", lema="InnoBótica 2026 · InnovaTecNM",
            texto="A fully autonomous 14 cm robot that finds and pushes 12 cones "
                  "off a 122×244 cm board in five minutes. Localization is solved "
                  "first: changing strategy means changing code, not redesigning "
                  "the robot.",
            estado="In competition", enlace="Regional stage · September 2026",
        ),
    ),
    dict(
        archivo="micromouse", sigla="MM", acento="#B98CFF",
        stack=["RP2040", "C++", "Open source"],
        color_estado=GRIS,
        url="https://github.com/BanarySource/Micromouse-RP2040-Zero",
        es=dict(
            titulo="Micromouse RP2040", lema="Hardware abierto",
            texto="Firmware de prueba para cada periférico del micromouse basado "
                  "en RP2040-Zero. Verifica el hardware pieza por pieza y arranca "
                  "el prototipo sin pelearse con todo a la vez.",
            estado="Código abierto", enlace="ver el repositorio",
        ),
        en=dict(
            titulo="Micromouse RP2040", lema="Open hardware",
            texto="Test firmware for every peripheral of the RP2040-Zero based "
                  "micromouse. Check the hardware piece by piece and bring the "
                  "prototype up without fighting everything at once.",
            estado="Open source", enlace="view the repository",
        ),
    ),
    dict(
        archivo="entrenadora-pic", sigla="PIC", acento="#22C7F5",
        stack=["PIC18F4550", "Electrónica", "PCB"],
        stack_en=["PIC18F4550", "Electronics", "PCB"],
        color_estado=VERDE, url="https://www.youtube.com/c/banarysource",
        es=dict(
            titulo="Entrenadora PIC18F4550", lema="Para prácticas de laboratorio",
            texto="Diseños e impresos de la tarjeta entrenadora con la que se hacen "
                  "las prácticas del canal. Pensada para que un estudiante la arme "
                  "y la use, no para mirarla.",
            estado="En uso", enlace="las prácticas, en el canal",
        ),
        en=dict(
            titulo="PIC18F4550 Trainer", lema="For hands-on lab practice",
            texto="Designs and layouts for the trainer board used in the channel's "
                  "lab sessions. Built so a student can assemble it and use it, "
                  "not just look at it.",
            estado="In use", enlace="the lab sessions, on the channel",
        ),
    ),
]


def stack_de(tarjeta: dict, idioma: str) -> list[str]:
    """El stack solo cambia cuando trae un término traducible."""
    if idioma == "en" and "stack_en" in tarjeta:
        return tarjeta["stack_en"]
    return tarjeta["stack"]


# Textos sueltos de cada versión del perfil.
IDIOMAS = {
    "es": dict(
        nombre="Español", otro="English", archivo_otro="README.en.md",
        lema_grande="Robótica · Software · Educación",
        lema_chico="Tecnología y robótica desde México",
        titular="Construimos robótica, software y educación técnica desde México",
        intro=("Somos una empresa de desarrollo tecnológico. Hacemos el **software** "
               "con el que damos clase, el **hardware** con el que compiten nuestros "
               "estudiantes y las **herramientas** que ponemos en manos de otros "
               "docentes. Lo que ves abajo está en uso hoy, no en una presentación."),
        h_proyectos="Proyectos",
        h_software="Software y plataformas",
        h_hardware="Robótica y hardware",
        h_stack="Con qué lo construimos",
        h_contacto="Hablemos",
        nav_plataforma="Plataforma",
        pie_1="La mayor parte de nuestro trabajo vive en repositorios privados.",
        pie_2="Si te interesa alguno de estos proyectos, escríbenos y lo platicamos.",
        pie_3="**Banary Source** · Robótica · Software · Educación · México",
        alt_banner="Banary Source — Robótica · Software · Educación",
        alt_stack=("Tecnologías que usamos. Software: TypeScript, React, Next.js, "
                   "Node.js, Python, FastAPI, Vite, Electron. Datos e infraestructura: "
                   "PostgreSQL, Supabase, Prisma, Cloudflare Workers, Vercel, Railway, "
                   "Stripe, Docker. Hardware: ESP32, RP2040, Arduino, C++, PIC18F, "
                   "KiCad, impresión 3D, visión artificial."),
        filas_stack=["SOFTWARE", "DATOS E INFRA", "HARDWARE"],
    ),
    "en": dict(
        nombre="English", otro="Español", archivo_otro="README.md",
        lema_grande="Robotics · Software · Education",
        lema_chico="Technology and robotics from Mexico",
        titular="We build robotics, software and technical education from Mexico",
        intro=("We are a technology development company. We build the **software** "
               "we teach with, the **hardware** our students compete with, and the "
               "**tools** we put in other teachers' hands. Everything below is in "
               "use today, not in a pitch deck."),
        h_proyectos="Projects",
        h_software="Software and platforms",
        h_hardware="Robotics and hardware",
        h_stack="What we build with",
        h_contacto="Get in touch",
        nav_plataforma="Platform",
        pie_1="Most of our work lives in private repositories.",
        pie_2="If any of these projects interest you, get in touch and let's talk.",
        pie_3="**Banary Source** · Robotics · Software · Education · Mexico",
        alt_banner="Banary Source — Robotics · Software · Education",
        alt_stack=("Technologies we use. Software: TypeScript, React, Next.js, "
                   "Node.js, Python, FastAPI, Vite, Electron. Data and infrastructure: "
                   "PostgreSQL, Supabase, Prisma, Cloudflare Workers, Vercel, Railway, "
                   "Stripe, Docker. Hardware: ESP32, RP2040, Arduino, C++, PIC18F, "
                   "KiCad, 3D printing, computer vision."),
        filas_stack=["SOFTWARE", "DATA & INFRA", "HARDWARE"],
    ),
}

CHIPS_STACK = {
    "es": [
        ["TypeScript", "React", "Next.js", "Node.js", "Python", "FastAPI", "Vite", "Electron"],
        ["PostgreSQL", "Supabase", "Prisma", "Cloudflare Workers", "Vercel", "Railway", "Stripe", "Docker"],
        ["ESP32", "RP2040", "Arduino", "C++", "PIC18F", "KiCad", "Impresión 3D", "Visión artificial"],
    ],
    "en": [
        ["TypeScript", "React", "Next.js", "Node.js", "Python", "FastAPI", "Vite", "Electron"],
        ["PostgreSQL", "Supabase", "Prisma", "Cloudflare Workers", "Vercel", "Railway", "Stripe", "Docker"],
        ["ESP32", "RP2040", "Arduino", "C++", "PIC18F", "KiCad", "3D printing", "Computer vision"],
    ],
}


# --- Contacto -------------------------------------------------------------
# Cada red lleva SU color de marca: es lo que la hace reconocible de un
# vistazo sin usar el logotipo original. `ancho` es el lienzo del panel, y va
# emparejado con cuántos caben por fila en el README (2 anchos o 3 estrechos),
# para que los dos grupos se vean a la misma escala.
#
# `nota` dice QUÉ hay en cada canal. Nunca cifras de seguidores: un README es
# estático y un número escrito hoy se congela.
CONTACTOS = [
    dict(
        archivo="plataforma", icono="globo", color="#22C7F5", ancho=620,
        url="https://banarysource.org",
        es=dict(nombre="Plataforma", dato="banarysource.org",
                nota="El aula y el club de robótica, en línea"),
        en=dict(nombre="Platform", dato="banarysource.org",
                nota="The classroom and the robotics club, online"),
    ),
    dict(
        archivo="correo", icono="correo", color="#FFC24F", ancho=620,
        url="mailto:contacto@banarysource.org",
        es=dict(nombre="Correo", dato="contacto@banarysource.org",
                nota="Escríbenos y te contestamos"),
        en=dict(nombre="Email", dato="contacto@banarysource.org",
                nota="Write to us and we'll get back to you"),
    ),
    dict(
        archivo="youtube", icono="youtube", color="#FF3B30", ancho=400,
        url="https://www.youtube.com/@BanarySource",
        es=dict(nombre="YouTube", dato="@BanarySource",
                nota="Prácticas y proyectos"),
        en=dict(nombre="YouTube", dato="@BanarySource",
                nota="Practice and projects"),
    ),
    dict(
        archivo="instagram", icono="instagram", color="#E1306C", ancho=400,
        url="https://www.instagram.com/banarysource",
        es=dict(nombre="Instagram", dato="@banarysource",
                nota="El día a día del taller"),
        en=dict(nombre="Instagram", dato="@banarysource",
                nota="Day to day in the workshop"),
    ),
    dict(
        archivo="tiktok", icono="tiktok", color="#25F4EE", ancho=400,
        url="https://www.tiktok.com/@banarysource",
        es=dict(nombre="TikTok", dato="@banarysource",
                nota="Robótica en formato corto"),
        en=dict(nombre="TikTok", dato="@banarysource",
                nota="Robotics, short-form"),
    ),
]


# --- Contraste en tema claro ----------------------------------------------
# Los acentos están pensados para fondo oscuro. Sobre blanco, los claros
# (cian, ámbar, verde, coral) se leen mal: gris pálido en vez de color. Aquí
# está la variante oscurecida de cada uno. Varias —#8A5A00, #B4421C,
# #0E7A5A— son las que el propio CSS de banarysource.org ya usa en su tema
# claro, así que no se inventa nada donde la marca ya decidió.
ACENTO_CLARO = {
    "#22C7F5": "#0E7FA8",   # cian de marca
    "#7C3AED": "#6425CE",   # violeta de Docentia
    "#2FD69B": "#0E7A5A",   # verde
    "#FFC24F": "#8A5A00",   # ámbar
    "#FF7A5C": "#B4421C",   # coral
    "#B98CFF": "#6D3BC4",   # violeta claro
    "#8A939C": "#5A626B",   # gris
    "#FF3B30": "#C2261C",   # rojo de YouTube
    "#E1306C": "#B81E55",   # rosa de Instagram
    "#25F4EE": "#0A8C88",   # cian de TikTok
}


def acento(color: str, tema: str) -> str:
    """El acento tal cual en oscuro; su variante legible en claro."""
    if tema != "light":
        return color
    if color not in ACENTO_CLARO:
        raise KeyError(f"{color} no tiene variante clara en ACENTO_CLARO")
    return ACENTO_CLARO[color]
