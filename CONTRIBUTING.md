# Cómo se mantiene este perfil

Este repositorio genera la portada de <https://github.com/BanarySource>.
GitHub muestra el `README.md` de un repo que se llame igual que la cuenta.

## Los SVG no se editan a mano

`assets/banner-*.svg` y `assets/stack-*.svg` los generan dos scripts:

```bash
python build_banner.py    # banner con el logo real incrustado
python build_stack.py     # tira de tecnologías
```

Para cambiar una tecnología de la tira, edita la lista `FILAS` en
`build_stack.py` y vuelve a correrlo. Para tocar colores, edita `TEMAS` en
cualquiera de los dos: la paleta sale del CSS en producción de
banarysource.org (cian de marca `#22C7F5` sobre tinta `#16181C`).

## Dos reglas que no hay que romper

1. **Todo debe verse terminado sin animación.** Se comprobó que un SVG
   embebido con `<img>` puede no animar (ni con CSS ni con SMIL, según el
   navegador). Por eso cada elemento animado lleva un valor base que ya se ve
   bien por sí solo, y el `<animate>` solo lo mejora donde sí corre.
2. **Ningún enlace a repositorio privado.** Casi todo nuestro código es
   privado: un enlace así le da 404 a cualquier visitante. Las tarjetas
   apuntan al sitio, al canal o a la demo. La única excepción es
   `Micromouse-RP2040-Zero`, que sí es público.

## Vista previa antes de publicar

```bash
python -m http.server 8777
# y abre http://127.0.0.1:8777/preview.html
```

Muestra el banner y la tira en tema claro y oscuro, que es donde salen los
problemas de contraste.
