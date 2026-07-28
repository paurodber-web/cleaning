# Auditoría general del proyecto Maid At Home

Fecha: 26 de julio de 2026

## Resumen

Valoración general: buena base, todavía no lista para escalar sin una ronda de control editorial y técnico. SEO orientativo: 76/100, confianza media.

El proyecto está por encima de la media de una web local: arquitectura clara, contenido útil, metadatos, canonicals, sitemap, robots, llms.txt, datos estructurados, páginas legales, 404, imágenes responsive, blog y un sistema prudente para publicar landings locales. El build pasa y valida 35 documentos HTML.

Los principales riesgos no son de indexación, sino de calidad: caracteres corruptos visibles, contradicciones de copy y CTA, señales E-E-A-T genéricas, una frontera confusa entre 70+ áreas operativas y 5 páginas SEO publicadas, exceso de CSS/JS inline y demasiados derivados de imagen.

## Qué está bien

- Astro estático, rutas limpias y HTML renderizado.
- Canonical, robots, Open Graph, Twitter Card, sitemap y JSON-LD centralizados.
- Build con controles de títulos, H1, enlaces rotos, JSON-LD y canonicals.
- Solo cinco landings de suburbio publicadas, con umbrales de longitud y unicidad.
- Arquitectura comercial completa: Home, Servicios, Pricing, Booking, Áreas, FAQ, Contacto, legales y blog.
- Diseño coherente: paleta reconocible, tipografías locales, jerarquía y CTAs claros.
- Blog con nueve artículos, TOC, relacionados, schema BlogPosting, fechas y metadata editorial.
- 404 noindex, booking fuera del sitemap y redirect de una URL antigua.
- llms.txt sobrio y útil.

## Prioridades

### 1. Encoding y coherencia

Hay mojibake visible: `â€œ`, `â€`, `â€“`, `âœ“` y `â˜…` en servicios y blog. Es el problema más urgente porque daña la percepción de calidad y aparece en el HTML final.

También hay CTAs contradictorios. En Deep Clean, un bloque “Choose Standard” termina con “Book Deep Cleaning”. El validador comprueba que la URL exista, pero no que sea semánticamente correcta.

### 2. SEO local

La web comunica más de 70 suburbios operativos, pero solo cinco tienen landing publicada. La prudencia editorial es positiva, pero el mensaje debe distinguir:

- áreas donde se presta servicio;
- guías locales indexables disponibles.

No conviene convertir automáticamente los 70+ nombres en páginas. Las siguientes landings deben elegirse por Search Console, reservas y capacidad real.

### 3. Entidad y E-E-A-T

LocalBusiness es básico y faltan datos verificables como teléfono, horario, perfiles oficiales y un modelo claro de área de servicio.

La autoría del blog es genérica: “Maid At Home” y “Maid At Home service team”. Falta una página de equipo/editorial, responsable de revisión, metodología y experiencia demostrable.

Los claims de Google y reseñas deben enlazar al perfil oficial, con atribución autorizada. No se recomienda marcar ratings autocontrolados.

### 4. Rendimiento

El build genera 647 WebP, 36,1 MB y 645 transformaciones de imagen para 34 rutas. Es una estrategia demasiado expansiva.

Los 35 HTML suman 2,76 MB. Gran parte del CSS y JavaScript se repite inline. Conviene:

- reducir anchos y variantes de imagen;
- reutilizar assets compartidos;
- extraer CSS común;
- deduplicar scripts de menú, FAQ y scroll;
- medir LCP, INP y CLS en producción.

### 5. Blog

Los temas cubren buenas intenciones: costes, horas, inclusiones, frecuencia, standard vs deep, move-in y end-of-lease.

Mejoras:

- crear hubs de costes y planificación, cuidado regular y mudanzas;
- no publicar cinco artículos con la misma fecha;
- añadir experiencia propia, ejemplos y limitaciones reales;
- usar relaciones editoriales explícitas, no solo categoría y fecha;
- conectar cada post con servicio, pricing, otro post y área relevante;
- crear página de autor/equipo.

Temas que faltan: preparación antes de la visita, mascotas, productos y seguridad, apartamento frente a casa, parking/acceso, manchas y límites de alfombra, preparación del horno y cancelación o reprogramación.

### 6. Diseño y UX

La identidad visual está cuidada y no parece una plantilla básica. Hay focus visible, responsive, estados hover y buena jerarquía.

Lo que resta calidad:

- caracteres corruptos;
- repetición excesiva de hero, cards, how-it-works, FAQ y CTA fotográfica;
- mucho HTML/CSS construido como strings;
- dependencia de fotos de stock;
- falta de pruebas visuales automatizadas.

Las fotos propias del equipo, equipamiento y trabajo real aportarían más confianza que Unsplash.

## Qué incluiría

1. Perfil empresarial verificable: teléfono, horario, área de servicio y perfiles oficiales.
2. Página “Our cleaning standards”: selección, seguros, productos, checklist e incidencias.
3. Página de equipo/editorial y política de actualización.
4. Galería real antes/después con consentimiento.
5. Hubs temáticos del blog.
6. Una matriz comparativa única Standard, Deep, Hourly y Moving.
7. Tests de encoding, accesibilidad, anchors, schema y presupuesto de tamaño.
8. Medición de GA4, Search Console y conversiones de booking, teléfono, email y WhatsApp.

## Puntuación orientativa

| Categoría | Nota |
|---|---:|
| SEO técnico | 82 |
| Contenido | 78 |
| On-page | 80 |
| Schema y entidad | 70 |
| Rendimiento potencial | 66 |
| Imágenes | 78 |
| GEO e IA | 72 |
| Diseño y UX | 78 |
| Coherencia editorial | 64 |

## Limitaciones

- Sin Search Console, GA4, reservas, rankings, backlinks ni CTR.
- Sin CrUX/PageSpeed real ni headers del despliegue.
- Sin validación del Google Business Profile o consentimiento de reseñas.
- La inspección visual interactiva local quedó bloqueada por ACL; el análisis visual se basa en el código.
