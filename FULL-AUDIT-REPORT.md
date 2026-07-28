# Auditoría SEO de la landing principal

Fecha: 26 de julio de 2026  
Página: `https://maidathome.com.au/`  
Fuente: `src/pages/index.astro`, layout global y `dist/index.html`.  
Alcance: página única (on-page, contenido, indexabilidad, schema, imágenes, rendimiento potencial y GEO).

## A) Resumen

**Puntuación orientativa: 78/100 — Buena, con mejoras importantes.**  
**Confianza: media.** Se verificó el HTML local de producción, pero no hay datos de Search Console, CrUX/PageSpeed ni del servidor desplegado.

| Área | Nota | Diagnóstico |
|---|---:|---|
| SEO técnico | 75 | Buena indexación y metadata; falta validación en producción |
| Contenido | 90 | Amplio, localizado y útil |
| On-page | 78 | Metadata fuerte; hero y un enlace necesitan corrección |
| Schema | 72 | Válido, pero poco específico para negocio local |
| Rendimiento potencial | 68 | Imágenes optimizadas; documento inicial voluminoso |
| Imágenes | 90 | Alt, dimensiones, WebP, srcset y lazy loading |
| GEO / IA | 50 | Contenido citable, sin política explícita ni `llms.txt` |

La nota ponderada refleja una base sólida, penalizada por la jerarquía semántica del hero, un enlace incorrecto, schema local incompleto, peso inicial y CWV aún sin medir.

### Problemas prioritarios

1. El mensaje grande del hero (`A cleaner home. A lighter week.`) es un `<div aria-hidden="true">`; el H1 es una etiqueta visual secundaria.
2. La tarjeta “Move in clean” enlaza a `/services/regular-house-cleaning` en vez de `/services/move-in-clean`.
3. El HTML pesa 164,4 KB: 76,9 KB de CSS inline y 22 KB de JavaScript inline.

### Oportunidades principales

1. Convertir el hero en una proposición de búsqueda y conversión más clara con una sola H1 visible.
2. Reforzar la entidad con `LocalBusiness` o subtipo adecuado, solo con datos verificables.
3. Crear enlaces contextuales directos hacia cada servicio y las páginas locales publicadas.

## B) Hallazgos

| Área | Severidad | Confianza | Hallazgo y evidencia | Impacto | Corrección |
|---|---|---|---|---|---|
| Indexabilidad | Pass | Confirmed | `robots=index,follow...`, canonical `https://maidathome.com.au/`; `robots.txt` permite rastreo y declara sitemap | Facilita rastreo y evita duplicidad | Mantener y validar en Search Console |
| Metadata | Pass | Confirmed | Title de 48 caracteres y description de 149, alineados con “house cleaning Melbourne” | Buena relevancia y potencial de CTR | Probar variantes solo con datos de CTR |
| H1 / hero | Warning | Confirmed | H1: “House cleaning service in Melbourne”; el titular visual es un `div` oculto semánticamente | Diluye jerarquía, accesibilidad y proposición temática | Integrar mensaje e intención local en un H1 visible; convertir la eyebrow en `<p>` |
| Enlazado | Warning | Confirmed | “Move in clean” usa `href="/services/regular-house-cleaning"` | Señales contradictorias y mala UX | Cambiar a `/services/move-in-clean` |
| Enlazado | Warning | Confirmed | Hourly y Regular priorizan `#price-calculator` en el markup fuente | Reduce enlaces contextuales a páginas que deben posicionar | Enlazar tarjeta/título a la página y conservar CTA separado al calculador |
| Contenido | Pass | Confirmed | Aproximadamente 1.611 palabras visibles; 11 H2; servicios, precios, proceso, áreas, testimonios y FAQs | Profundidad temática y cobertura de intención | Revisar trimestralmente precios, áreas y claims |
| SEO local | Pass | Confirmed | Melbourne aparece en title, description, H1 y headings de servicios, proceso y zonas | Refuerza intención local naturalmente | Enlazar a suburbios publicados donde sea relevante |
| E-E-A-T | Warning | Confirmed | Hay historia, año y reseñas, pero las firmas dicen “Verified customer” y enlazan a una búsqueda genérica | Menor verificabilidad | Añadir datos autorizados y enlazar al perfil oficial |
| Schema | Pass | Confirmed | JSON-LD válido con Organization, WebPage y WebSite conectados por IDs | Buena comprensión básica de entidad | Mantener IDs estables |
| Schema local | Warning | Confirmed | Faltan `telephone`, `address`, `contactPoint` y `sameAs`; solo hay email y `areaServed` | Desambiguación local limitada | Usar subtipo `LocalBusiness` con datos reales |
| Ratings | Info | Confirmed | No se marca `Review` ni `AggregateRating` | Evita marcado autocontrolado potencialmente inelegible | No añadir sin confirmar elegibilidad y fuente |
| Social | Pass | Confirmed | Open Graph y Twitter Card completos | Mejora previews sociales | Probar y preferir raster 1200×630 frente al SVG genérico |
| Imágenes | Pass | Confirmed | 13 imágenes; 10 lazy; hero eager/high; alt, dimensiones y WebP responsivo | Reduce CLS y ancho de banda | Mantener QA visual de recortes |
| LCP | Info | Likely | Hero WebP observado de 181,7 KB con preload/fetchpriority; fuente original de 2,49 MB | Solo CWV real confirma el resultado | Medir LCP móvil antes de reducir calidad |
| HTML/CSS/JS | Warning | Confirmed | HTML 164,4 KB; CSS inline 76,9 KB; JS inline 22 KB | Más transferencia y trabajo de parseo | Extraer CSS no crítico, eliminar duplicados y diferir JS |
| Navegación | Pass | Confirmed | 59 enlaces internos en el HTML | Buen descubrimiento interno | Corregir destinos inconsistentes |
| GEO / IA | Warning | Confirmed | No existe `public/llms.txt`; robots sin reglas para crawlers de IA | La política para sistemas de IA no está expresada | Definir política; `llms.txt` es experimental |
| FAQ | Pass | Confirmed | Seis preguntas/respuestas presentes en HTML | Cubre lenguaje natural | No recomendar FAQ schema comercial restringido |

## C) Evidencia de puntuación

Señales positivas: canonical/robots/sitemap y social completos; una H1 y jerarquía H1→H2→H3; 1.611 palabras; JSON-LD válido; imágenes correctamente optimizadas.

Déficits: el titular visual no es heading; un enlace conduce al servicio equivocado; schema local limitado; documento inicial voluminoso; confianza verificable y preparación GEO mejorables.

## D) Desconocidos y seguimiento

- LCP, INP y CLS reales en móvil/escritorio.
- Indexación, consultas, CTR y canibalización en Search Console.
- Respuestas HTTP, redirecciones, caché y headers del dominio.
- Compatibilidad del OG SVG en plataformas sociales.
- Fuente y consentimiento de testimonios.
- Datos empresariales necesarios para completar schema local.
- Backlinks y competidores, fuera del alcance de página.

## Limitaciones del entorno

El build y validador SEO propio pasaron: 35 HTML sin errores bloqueantes. Las utilidades externas de parsing/readability no pudieron leer archivos por restricciones ACL. No se ejecutó PageSpeed/CrUX contra producción; las observaciones de rendimiento son potenciales hasta medirlas.

