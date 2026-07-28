# Plan de acción SEO de la landing principal

Fecha: 26 de julio de 2026

## Prioridad 1 — Quick wins

1. **Corregir “Move in clean”**: cambiar el destino a `/services/move-in-clean`. Impacto alto, esfuerzo mínimo.
2. **Rehacer la jerarquía del hero**: usar un único H1 visible que combine la promesa con “Melbourne house cleaning”; convertir la eyebrow actual en texto auxiliar. Impacto alto, esfuerzo bajo.
3. **Separar información y conversión**: enlazar Hourly y Regular a sus páginas; mantener un CTA secundario al calculador. Impacto medio-alto, esfuerzo bajo.

## Prioridad 2 — Técnica y rendimiento

4. **Medir CWV en producción** con PageSpeed/CrUX/Search Console. Objetivos p75: LCP ≤ 2,5 s, INP ≤ 200 ms y CLS ≤ 0,1.
5. **Reducir el documento inicial**: auditar 76,9 KB de CSS inline y 22 KB de JS; extraer reglas no críticas, eliminar duplicados y diferir código no esencial. Objetivo: reducir el HTML de 164,4 KB al menos un 25%.
6. **Validar el hero como LCP**: comprobar la variante `srcset` por viewport; reducir calidad/dimensiones solo si las métricas fallan.

## Prioridad 3 — Entidad, confianza y CTR

7. **Completar la entidad local** con teléfono, dirección o modelo de área de servicio, horario y perfiles oficiales; implementar un subtipo `LocalBusiness` apropiado sin datos inventados.
8. **Hacer verificables los testimonios**: inicial/nombre autorizado, fecha, suburbio y fuente; usar el perfil oficial de Google.
9. **Crear una imagen social raster** de 1200×630 y probarla en Facebook, LinkedIn y WhatsApp.

## Prioridad 4 — Crecimiento

10. **Enlazar los cinco suburbios publicados** desde la sección local con anchors naturales.
11. **Crear rutas temáticas** entre home, servicios y artículos relacionados; revisar canibalización en Search Console.
12. **Definir política para crawlers de IA** y reflejarla en `robots.txt`; considerar `llms.txt` como señal experimental.

## Validación final

- `npm run build` pasa.
- Hay exactamente una H1 visible y descriptiva.
- No hay enlaces con destino semánticamente incorrecto.
- JSON-LD valida y solo contiene datos verificables.
- PageSpeed/CrUX confirma LCP, INP y CLS.
- Search Console no muestra problemas de indexación o canonicalización.

