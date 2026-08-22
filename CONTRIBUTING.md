# Cómo se mantiene este perfil

Este repositorio genera la portada de <https://github.com/BanarySource>.
GitHub muestra el `README.md` de un repo que se llame igual que la cuenta.

## Nada se edita a mano

Ni los `README`, ni los SVG. Todo el contenido vive en **`proyectos.py`** y de
ahí salen las dos versiones del perfil y las 36 imágenes. Editar un README
directamente se pierde en la siguiente generación.

```bash
python build_banner.py    # 4 banners  (2 idiomas x 2 temas)
python build_stack.py     # 4 tiras de tecnologías
python build_cards.py     # 28 tarjetas (7 proyectos x 2 idiomas x 2 temas)
python build_contact.py   # 20 paneles de contacto + 2 iconos de sección
python build_readme.py    # README.md, README.en.md y preview.html
```

Si tocas `proyectos.py`, corre los cinco. `build_readme.py` va al final: es el
que valida los 58 SVG y arma los archivos que GitHub muestra.

**Para cambiar un texto de proyecto:** su entrada en `TARJETAS`, en las dos
claves `es` y `en`. **Para una red social o el correo:** `CONTACTOS`. **Para
los textos del perfil** (titular, intro, encabezados, pie): el diccionario
`IDIOMAS`. **Para la tira de tecnologías:** `CHIPS_STACK`. **Para colores:**
el diccionario `TEMAS` de cada generador; la paleta sale del CSS en producción
de banarysource.org (cian de marca `#22C7F5` sobre tinta `#16181C`).

**Si añades un color de acento**, mételo también en `ACENTO_CLARO`. Los
acentos están pensados para fondo oscuro y sobre blanco los claros se leen
como gris pálido; ese diccionario tiene la variante oscurecida de cada uno, y
`acento()` **falla a propósito** si le pasas un color que no está.

## Nada de emoji, y nada de cifras de seguidores

**Emoji, no.** Lo pinta el sistema operativo de quien mira: cambia de forma en
Windows, Mac y Android, y los de bandera en Windows ni siquiera salen (se ven
como dos letras). Los iconos se dibujan en `iconos.py`, monolínea sobre una
retícula de 24x24, y se ven igual en todas partes. Los de los títulos de
sección van en el cian de marca y en un solo archivo: ese cian se lee bien
sobre los dos fondos de GitHub, así que no necesitan variante clara/oscura.

**Cifras de seguidores, tampoco.** Un README es estático: un número escrito
hoy se congela y a las pocas semanas hace ver el perfil abandonado. Los
paneles de contacto dicen QUÉ hay en cada canal, que es cierto siempre. Si
algún día se quieren cifras de verdad, la única vía honesta es una GitHub
Action que regenere el SVG cada día — no un número a mano.

## El idioma

Un README no puede tener un selector de idioma de verdad: es markdown
estático, sin JavaScript. El «selector» es un enlace al otro archivo —
`README.md` en español, `README.en.md` en inglés— y **cada versión está en un
solo idioma**, sin líneas mezcladas. Los dos salen de los mismos datos para
que no se puedan desincronizar.

## Cuatro reglas que no hay que romper

1. **Todo debe verse terminado sin animación.** Se comprobó que un SVG
   embebido con `<img>` puede no animar, ni con CSS ni con SMIL. Por eso cada
   elemento animado lleva un valor base que ya se ve bien por sí solo, y el
   `<animate>` solo lo mejora donde sí corre.
2. **Las imágenes van por URL absoluta de `raw.githubusercontent`.** En la
   página de perfil un path relativo NO resuelve contra el repo: las imágenes
   salen en blanco. Comprobado en vivo.
3. **Ningún enlace a repositorio privado.** Casi todo nuestro código es
   privado y un enlace así le da 404 a cualquier visitante. Las tarjetas
   apuntan al sitio, al canal o a la demo. La única excepción es
   `Micromouse-RP2040-Zero`, que sí es público.
4. **El `alt` de cada tarjeta lleva el contenido completo.** El texto de la
   tarjeta es una imagen: ese `alt` es lo único que puede leer un lector de
   pantalla. Lo arma `build_readme.py` solo; no lo recortes.

## Tres estilos de panel, uno por apartado

Para que el perfil no se lea monótono, cada apartado tiene su tratamiento.
Los tres comparten paleta, tipografía y radio de esquina: **cambia el
tratamiento, no el idioma visual**. Si añades un panel, dale el estilo de su
apartado en vez de inventar un cuarto.

| Apartado | Tratamiento |
|---|---|
| **Software** | Cabecera tintada del color del proyecto con divisor limpio debajo, placa cuadrada con las siglas, chips en píldora, punto redondo de estado. Aire de producto. |
| **Hardware** | Aire de plano técnico: banda fina de color arriba, retícula de puntos, marcas de esquina, placa hexagonal (tuerca), chips de esquina recta con marca de color y cuadrado de estado. |
| **Contacto** | El color no va en filo ni banda, sino en un disco relleno detrás del icono, con un subrayado corto bajo el nombre. |

El estilo de cada tarjeta se declara en su entrada de `TARJETAS`, en la clave
`estilo` (`"software"` o `"hardware"`).

Software y hardware **leen los dos de arriba abajo** a propósito: software
tuvo un filo de color a la izquierda y peleaba con la sombra del panel. No se
confunden porque uno es una CABECERA con cuerpo tintado y el otro una BANDA
fina sobre textura de plano.

## Las tarjetas son imágenes, y eso cuesta

GitHub borra todo el CSS de un README, así que un panel flotante (fondo, borde
redondeado, sombra) no se puede hacer con HTML. Por eso cada proyecto se
**dibuja** como su propio SVG. El costo: ese texto no se puede seleccionar ni
copiar, y el buscador de GitHub no lo indexa. Los encabezados y el resto del
README sí siguen siendo texto normal.

Las siete tarjetas comparten el mismo lienzo a propósito: al escalarse al
ancho de su celda, un lienzo idéntico da una altura idéntica y la rejilla no
queda dispareja. `build_cards.py` **falla a propósito** si un texto no cabe en
cinco líneas o si los chips se salen de la fila — si salta ese error, acorta
el texto en `proyectos.py`, no subas el límite.

## Vista previa antes de publicar

```bash
python -m http.server 8777
# y abre http://127.0.0.1:8777/preview.html
```

Muestra el perfil entero en tema claro y oscuro con los SVG locales, que es
donde salen los problemas de contraste y los desbordes.
