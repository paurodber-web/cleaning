# Prompt final para aplicar mejoras UI/UX, SEO local, GEO y optimización para LLMs

## Contexto del proyecto

Trabaja sobre la web de **Maid At Home**, una empresa de limpieza residencial que opera en Melbourne.

- Preview actual: `https://paurodber-web.github.io/maidathome/`
- Dominio oficial de producción: `https://maidathome.com.au`
- Framework: Astro
- Servicio principal: limpieza residencial en Melbourne
- Objetivo SEO principal actual: `house cleaning service in Melbourne`
- Nuevo enfoque SEO recomendado: `house cleaning Melbourne`
- Idioma de la web: inglés australiano
- Tono de marca: cercano, profesional, claro, local y fiable
- Evitar expresiones artificiales, exceso de keywords y textos que parezcan generados por IA
- No utilizar “housekeeping” ni “housekeeper”
- No inventar reseñas, cifras, premios, certificaciones, datos operativos ni estadísticas

---

# Instrucciones no negociables

1. **Mantener visibles los seis servicios en la home.**
2. **No añadir una tabla comparativa debajo de los servicios.**
3. **No añadir un botón “View all services”, “More services” o similar.**
4. No eliminar ninguna página de servicio existente.
5. No eliminar la calculadora de precios.
6. Mantener el diseño visual actual como base. Las mejoras deben refinarlo, no rediseñar toda la web desde cero.
7. Mantener la identidad visual azul, gris, blanco y beige.
8. Mantener las tipografías actuales salvo que exista un problema técnico demostrado.
9. Preservar accesibilidad, navegación con teclado, estados `focus-visible`, `prefers-reduced-motion`, ARIA y un único H1 por página.
10. No fabricar información para completar bloques. Cuando falte un dato real, usar una variable de configuración, un comentario `TODO` o no mostrar el elemento.
11. Aplicar los cambios de forma responsive en desktop, tablet y móvil.
12. No introducir contenido duplicado o casi idéntico entre páginas de suburbios.
13. No cambiar precios, políticas, descuentos o condiciones sin reutilizar los datos reales ya presentes en el proyecto.
14. No repetir “Melbourne” en todos los H2 de una misma página.
15. Usar inglés australiano, por ejemplo `organise`, `favourite` y `licence` cuando corresponda.

---

# Objetivo general

Mejorar la web para:

- Posicionar por `house cleaning Melbourne`.
- Reforzar variaciones como `house cleaning services Melbourne` y `house cleaners Melbourne`.
- Mejorar conversión desde tráfico orgánico y local.
- Reforzar confianza y percepción de negocio real.
- Facilitar que Google, ChatGPT y otros motores entiendan, extraigan y citen la información.
- Evitar riesgos de contenido local escalado o doorway pages.
- Preparar la migración de la nueva web al dominio oficial sin perder autoridad ni URLs existentes.
- Mejorar navegación, consistencia de CTAs y experiencia móvil.
- Mantener los seis servicios visibles en la home.

---

# Prioridad 1: cambios SEO principales de la home

## Keyword principal

Usar como keyword principal:

`house cleaning Melbourne`

Variaciones semánticas que deben aparecer de forma natural:

- `house cleaning services Melbourne`
- `house cleaners Melbourne`
- `home cleaning services Melbourne`
- `professional cleaners Melbourne`
- `house cleaning service in Melbourne`

No forzar todas las variaciones en el hero. Distribuirlas entre title, H1, introducción, servicios, FAQs, enlaces internos y contenido secundario.

## Metadata recomendada para la home

### Title

```text
House Cleaning Melbourne | Instant Prices | Maid At Home
```

Mantenerlo si la longitud final es adecuada. Si la herramienta SEO del proyecto marca exceso de longitud, utilizar:

```text
House Cleaning Melbourne | Maid At Home
```

### Meta description

```text
Trusted house cleaning services across Melbourne with clear online pricing, flexible one-off and recurring cleans, and a 24-hour care promise.
```

La descripción debe mantenerse aproximadamente entre 120 y 160 caracteres.

### H1

```text
Trusted house cleaning services in Melbourne
```

### Eyebrow del hero

```text
HOUSE CLEANING MELBOURNE
```

### Mensaje emocional

Mantener:

```text
A cleaner home. A lighter week.
```

### Texto introductorio del hero

Utilizar una versión equivalente a:

```text
Reliable house cleaners across Melbourne with clear online pricing, flexible one-off and recurring services, and a 24-hour care promise.
```

Debe sonar natural y no repetir de forma excesiva las mismas palabras del H1.

---

# Prioridad 2: jerarquía y consistencia de CTAs

Reducir la cantidad de nombres diferentes para la misma acción.

## Jerarquía recomendada

### CTA principal antes de elegir un servicio

```text
Get an instant price
```

Debe llevar a la calculadora o al paso inicial de estimación.

### CTA secundaria

```text
Explore cleaning services
```

Debe llevar a la sección de servicios o al hub de servicios.

### CTA después de obtener un precio o decidir

```text
Book your clean
```

Debe llevar al formulario de reserva.

## Aplicación

Revisar en toda la web variantes como:

- Book a clean
- Calculate my price
- Get an estimate
- Build my clean
- Estimate now
- Explore services

Unificarlas según la intención de cada punto del recorrido.

No sustituir todos los CTAs automáticamente por el mismo texto. Respetar esta lógica:

1. Antes de calcular: `Get an instant price`
2. Para aprender: `Explore cleaning services`
3. Cuando el usuario ya está preparado: `Book your clean`

Mantener visibles los seis servicios en la home.

---

# Prioridad 3: simplificar la longitud de la home sin eliminar servicios

La home contiene mucha información útil. No eliminar contenido esencial, pero mejorar la sensación de recorrido y reducir fatiga visual.

## Aplicar

- Mantener los seis servicios visibles.
- No añadir tabla comparativa.
- No añadir botón para mostrar más servicios.
- Mantener la sección de servicios completa.
- Mostrar en la home un máximo aproximado de tres FAQs destacadas y un enlace claro a la página completa de FAQs.
- Compactar textos repetitivos en beneficios, proceso y cobertura local.
- Evitar que “How it works” repita información ya explicada en la calculadora.
- Reducir espacios verticales excesivos cuando dos secciones consecutivas contienen poco contenido.
- Mantener suficiente aire visual y no convertir la página en una interfaz densa.
- Asegurar que cada sección tenga una función clara: informar, comparar, generar confianza o convertir.
- Revisar que no existan dos secciones consecutivas con mensajes equivalentes.

---

# Prioridad 4: barra fija de conversión en móvil

Crear una barra inferior fija en móvil.

## Contenido recomendado

Botón principal:

```text
Get instant price
```

Acción secundaria:

- Teléfono o WhatsApp, usando el canal ya priorizado en la web.

## Requisitos

- Solo visible en móvil o pantallas pequeñas.
- No debe aparecer sobre campos activos, modales, calculadora abierta o formulario de reserva.
- Respetar `safe-area-inset-bottom`.
- No tapar contenido.
- Tener altura moderada.
- Ser accesible por teclado.
- Incluir `aria-label` descriptivo en el icono secundario.
- Ocultarse cuando el footer esté visible si produce duplicación visual.
- No crear CLS.
- No utilizar animaciones molestas.
- Mantener contraste WCAG AA.

---

# Prioridad 5: mejoras de la calculadora

La calculadora es una de las ventajas competitivas principales. Mejorarla sin cambiar la lógica real de precios.

## Flujo recomendado

### Paso 1: comprobar cobertura

Solicitar primero:

- Suburb o postcode

Validar si la zona se encuentra dentro de la cobertura configurada.

Si no se cubre:

- Mostrar un mensaje amable.
- Ofrecer contactar con soporte.
- No permitir completar un cálculo que no pueda reservarse.

No almacenar direcciones completas en este punto.

### Paso 2: servicio

Seleccionar el tipo de servicio.

### Paso 3: tamaño o duración

Mostrar los campos correspondientes al servicio:

- Flat rate: bedrooms u otro parámetro real existente.
- Hourly: número de horas.
- Aplicar el mínimo de horas real configurado.

### Paso 4: frecuencia

Mostrar frecuencias y descuentos reales.

### Paso 5: extras

Mostrar extras compatibles con el servicio seleccionado.

## Mejoras visuales y funcionales

- Añadir indicador de progreso.
- Usar progressive disclosure.
- No mostrar todos los controles desde el primer momento.
- Mantener un resumen fijo en desktop.
- Mostrar un resumen compacto y expandible en móvil.
- Guardar temporalmente la selección con `sessionStorage` o una solución equivalente.
- Recuperar la selección si el usuario visita una página de servicio y vuelve.
- Permitir editar cualquier paso desde el resumen.
- Mostrar qué incluye la estimación.
- Diferenciar claramente `Estimated price` de `Final confirmed price`.
- Mostrar descuentos de frecuencia de forma transparente.
- Mostrar los extras incluidos en determinados servicios con una etiqueta visual.
- No cobrar dos veces un extra que ya esté incluido.
- No inventar duración ni número de cleaners.

## Mensaje obligatorio sobre la estimación

Añadir un mensaje equivalente a:

```text
Your online estimate is based on the selections above. We will confirm availability and the final booking details before your service.
```

Si el sistema ya confirma el precio de forma definitiva, adaptar el texto a la operativa real. No introducir incertidumbre falsa.

## Duración y tamaño del equipo

Solo mostrar duración aproximada o número de cleaners si existen reglas reales en el proyecto.

Si no existen datos fiables:

- No inventarlos.
- Preparar el componente para recibirlos en el futuro.
- Mostrar únicamente que la disponibilidad será confirmada.

---

# Prioridad 6: señales de confianza

## Valoración de Google

Junto a la puntuación, mostrar también el número real de reseñas.

Formato recomendado:

```text
5.0 from {reviewCount} Google reviews
```

Requisitos:

- `reviewCount` debe venir de una configuración o dato real.
- No escribir un número manual no verificado.
- Si no existe el dato, mostrar únicamente la puntuación actual o esconder el contador.
- Enlazar el bloque al perfil real de Google.
- Añadir texto accesible.
- No usar `AggregateRating` en schema si no se cumplen las directrices de Google o si las reseñas no se recopilan y muestran correctamente en la web.

## Reforzar la confianza con información verificable

Mostrar de forma coherente:

- Local since 2017
- Insured professionals
- Clear pricing
- 24-hour care promise
- Flexible recurring options

Verificar que estas afirmaciones estén explicadas en páginas interiores y no solo en iconos.

## No duplicar mensajes

No repetir exactamente las mismas cinco señales en hero, trust bar, About y footer. Distribuirlas según contexto.

---

# Prioridad 7: fotografías y contenido real

La web debe depender menos de fotografías con apariencia de stock.

## Preparar espacios para

- Fotografía real de Pau y Stefania.
- Fotografía real del equipo.
- Cleaners reales, con consentimiento.
- Equipamiento real.
- Antes y después.
- Viviendas reales de Melbourne.
- Apartments, terraces, townhouses y family homes.
- Imágenes de trabajos realizados en suburbios prioritarios.

## Implementación

- No inventar imágenes.
- No descargar fotografías aleatorias para presentarlas como trabajos reales.
- Crear slots o componentes preparados para sustituir imágenes.
- Añadir comentarios claros donde falten assets.
- Mantener imágenes actuales como fallback hasta que se proporcionen imágenes reales.
- Usar `width`, `height`, `srcset`, `sizes`, carga diferida y formatos optimizados.
- No aplicar lazy loading a la imagen LCP del hero.
- Usar alt text descriptivo, no keyword stuffing.
- Para fotografías decorativas, usar `alt=""`.

---

# Prioridad 8: páginas de servicios

Cada página de servicio debe tener una intención principal claramente diferenciada.

## Mapa de keywords recomendado

| Página | Keyword principal | Variaciones |
|---|---|---|
| Home | house cleaning Melbourne | house cleaning services Melbourne, house cleaners Melbourne |
| Standard Clean | standard house cleaning Melbourne | regular home cleaning, general house clean |
| Regular Clean | regular house cleaning Melbourne | weekly house cleaner Melbourne, fortnightly cleaning Melbourne |
| Deep Clean | deep cleaning Melbourne | deep house cleaning Melbourne, spring cleaning Melbourne |
| End of Lease | end of lease cleaning Melbourne | vacate cleaning Melbourne, move out cleaning Melbourne |
| Move In | move in cleaning Melbourne | pre move cleaning Melbourne |
| Hourly | hourly cleaner Melbourne | hourly house cleaning Melbourne |
| Carpet | carpet steam cleaning Melbourne | carpet cleaning Melbourne |
| Extras | oven cleaning Melbourne | fridge cleaning, window cleaning, wall cleaning |

## Respuesta directa al inicio

Añadir debajo del hero o introducción un bloque de respuesta directa de aproximadamente 40 a 80 palabras.

Debe explicar:

- Qué es el servicio.
- Para quién es.
- Qué cubre de forma general.
- Modelo de precio disponible.
- Área atendida.

Ejemplo de estructura, no copiar literalmente en todas las páginas:

```text
Maid At Home provides deep house cleaning across Melbourne for homes needing more than routine maintenance. The service covers detailed kitchen, bathroom and living-area cleaning, with optional extras available. Flat-rate and hourly options are offered depending on the type of clean and the priorities of the home.
```

## Evitar canibalización

- La home debe rankear por la categoría general.
- Cada servicio debe rankear por su intención específica.
- No utilizar el mismo title, H1 o primer párrafo en diferentes páginas.
- Enlazar servicios relacionados con anchor text descriptivo.
- Explicar diferencias entre Standard, Deep, Hourly y End of Lease dentro de las páginas relevantes.
- No repetir el mismo bloque de FAQs en todas las páginas.

## Structured data

Cuando corresponda, añadir:

- `Service`
- `WebPage`
- `BreadcrumbList`
- `FAQPage` solo cuando las preguntas estén visibles en la página
- `Article` o `BlogPosting` para artículos

No añadir schemas que no representen contenido visible.

---

# Prioridad 9: páginas de suburbios

Las páginas locales son una oportunidad, pero también el mayor riesgo SEO.

## Regla principal

No publicar páginas que solo sustituyan el nombre del suburbio dentro de una plantilla.

Cada página indexable debe aportar valor local real.

## Keyword principal

```text
house cleaning {Suburb}
```

Variaciones naturales:

- `house cleaners {Suburb}`
- `cleaning services {Suburb}`
- `deep cleaning {Suburb}`
- `end of lease cleaning {Suburb}`

No intentar posicionar todas las variaciones con la misma intensidad.

## Contenido único recomendado

Cada suburbio prioritario debe incluir al menos tres o cuatro elementos realmente únicos:

- Caso real o tipo de reserva frecuente.
- Reseña real de un cliente de la zona.
- Tipos de propiedad habituales.
- Problemas de acceso, parking, concierge o ascensores.
- Calles, zonas o edificios relevantes cuando sea útil.
- Servicio más reservado.
- Fotografía real.
- FAQ específica.
- Suburbios cercanos enlazados.
- Información sobre apartments, terraces, townhouses o family homes.

## Casos reales

Preparar un bloque opcional:

```text
Recent clean in {Suburb}
```

Contenido ejemplo de estructura:

```text
A fortnightly three-bedroom apartment clean near {local area}, including {real extras or priorities}. Building access was arranged through {real access method}.
```

No inventar casos. Ocultar el bloque hasta que exista información real.

## Priorización

No tratar las más de 60 páginas como si tuvieran la misma prioridad.

Crear un campo de configuración como:

- `priority: primary`
- `priority: secondary`
- `indexable: true/false`
- `hasUniqueLocalEvidence: true/false`

Inicialmente reforzar entre 10 y 15 suburbios con mayor valor:

- Zonas con clientes reales.
- Zonas con reseñas.
- Zonas con reservas recurrentes.
- Zonas con fotografías o casos.
- Zonas operativamente relevantes.

Las páginas con poco contenido diferencial pueden:

- Permanecer sin publicar.
- Usar `noindex,follow`.
- Integrarse dentro del hub de áreas.
- Publicarse más adelante cuando exista evidencia local.

## Detección automática

Ampliar el script de validación de suburbios para detectar:

- Introducciones idénticas.
- Testimonios repetidos.
- FAQs repetidas.
- Demasiado contenido compartido.
- Titles o descriptions duplicadas.
- Páginas sin contenido local mínimo.
- Páginas indexables con menos de un umbral configurable de contenido único.

No medir únicamente número de caracteres. Comprobar diversidad semántica y campos locales completados.

---

# Prioridad 10: página About y entidad empresarial

La página About debe reforzar que Maid At Home es un negocio local real y reconocible.

## Mostrar cuando los datos existan

- Nombre comercial.
- Año de fundación: 2017.
- Fundadores: Pau y Stefania.
- Función de cada fundador.
- Área de servicio.
- Teléfono.
- Correo.
- ABN, solo si se proporciona el dato real.
- Información sobre seguro, solo si se puede verificar.
- Proceso de selección o comprobación de cleaners.
- Cómo funciona la atención al cliente.
- Enlaces oficiales a Google e Instagram.

## Coherencia

Los datos de About, footer, schema, Google Business Profile y directorios deben coincidir.

No utilizar biografías genéricas. Explicar experiencia, responsabilidades y forma de trabajar.

## Schema

Mantener y revisar:

- `Organization`
- `LocalBusiness`
- `founder`
- `contactPoint`
- `areaServed`
- `sameAs`

Añadir `Person` para cada fundador cuando sea útil.

No añadir dirección física pública si el negocio funciona como service-area business y no atiende clientes en una ubicación abierta.

---

# Prioridad 11: contenido para GEO y LLMs

## Bloques fáciles de extraer

Cada página comercial debe incluir respuestas claras y autosuficientes.

Usar:

- Párrafos iniciales directos.
- Listas cortas.
- Encabezados descriptivos.
- Tablas solo cuando realmente ayuden. No añadir la tabla comparativa debajo de servicios.
- Definiciones claras.
- Precios y políticas con contexto.
- Fechas de actualización.
- Enlaces internos hacia la fuente completa.

## Autoría

Cada artículo del blog debe incluir:

- Autor real.
- Cargo o experiencia.
- Fecha de publicación.
- Fecha de última revisión.
- Fuentes cuando corresponda.
- Revisor cuando el tema lo requiera.

## Contenido original prioritario

Preparar una guía basada en datos reales:

```text
Melbourne House Cleaning Cost Guide 2026
```

Posibles datos, únicamente si son auténticos y anonimizados:

- Precio medio por tamaño de vivienda.
- Duración media.
- Extras más solicitados.
- Diferencias entre apartment y house.
- Frecuencia más contratada.
- Coste medio de End of Lease.
- Porcentaje de reservas recurrentes.
- Problemas habituales encontrados.

## Metodología

Si se publican datos:

- Explicar periodo analizado.
- Número de reservas.
- Exclusiones.
- Si los precios incluyen GST.
- Cómo se trataron descuentos y extras.
- Fecha de actualización.

No publicar `500+ homes` o cualquier cifra si no se puede demostrar.

---

# Prioridad 12: estrategia de blog

## Keywords informativas prioritarias

- how much does house cleaning cost in Melbourne
- house cleaning prices Melbourne
- how many hours of cleaning does my home need
- standard cleaning vs deep cleaning
- end of lease cleaning checklist Victoria
- how to prepare for a house cleaner
- weekly vs fortnightly house cleaning
- what does a standard house clean include
- do house cleaners bring their own equipment
- how often should you deep clean your home
- apartment cleaning cost Melbourne
- how long does an end of lease clean take

## Requisitos editoriales

- No crear artículos solo para insertar keywords.
- Incluir una respuesta directa en las primeras 100 palabras.
- Añadir índice cuando el artículo sea largo.
- Usar ejemplos de Melbourne o Victoria.
- Enlazar servicios relevantes.
- Enlazar fuentes oficiales cuando se mencionen obligaciones legales, alquileres, bond o normativa.
- Añadir fecha de revisión.
- Evitar introducciones largas y genéricas.
- No repetir el mismo CTA en todos los artículos.
- Incluir un CTA contextual relacionado con la intención del artículo.

---

# Prioridad 13: indexación, canonical y preview

## Producción

Todas las páginas indexables deben usar canonical absoluto en:

```text
https://maidathome.com.au/
```

Mantener la lógica actual de `Astro.site`.

## GitHub Pages preview

La preview de GitHub Pages debe usar:

```html
<meta name="robots" content="noindex,follow">
```

Aplicarlo de forma condicional según entorno o dominio.

Requisitos:

- No aplicar `noindex` al dominio de producción.
- Mantener canonical hacia producción.
- No incluir la preview en sitemaps públicos.
- No bloquear la preview completamente con robots.txt si eso impide que Google lea el canonical. Preferir `noindex,follow` en HTML.
- Evitar indexación duplicada del subdirectorio `/maidathome/`.

## Booking y páginas internas

Mantener `noindex` para páginas que no deben aparecer en buscadores, como:

- Booking si todavía es una página técnica o temporal.
- Plantillas.
- Páginas de prueba.
- Resultados internos.
- Estados de confirmación.
- Páginas de usuario.

---

# Prioridad 14: robots.txt y crawlers de IA

## Robots de producción

Comprobar que:

- Googlebot puede acceder a CSS, JS, imágenes y páginas indexables.
- El sitemap se declara correctamente.
- No se bloquean accidentalmente servicios, blog o suburbios.
- La preview no comparte un robots.txt que afecte al dominio oficial.

## OpenAI

Permitir el crawler utilizado para búsqueda:

```text
User-agent: OAI-SearchBot
Allow: /
```

No cambiar la política de `GPTBot` sin una decisión explícita del propietario.

Si no existe un bloqueo de GPTBot, no es obligatorio añadir ninguna regla.

## llms.txt

Crear un archivo `llms.txt` sencillo como ayuda complementaria, no como sustituto de SEO.

Debe incluir:

- Nombre de la empresa.
- Descripción breve.
- Dominio canónico.
- Servicios principales.
- Áreas atendidas.
- URLs importantes.
- Página de contacto.
- Política de actualización.

No incluir información inventada ni convertirlo en un listado de keywords.

---

# Prioridad 15: migración al dominio oficial

Antes de reemplazar la web actual, crear una migración controlada.

## Proceso obligatorio

1. Obtener todas las URLs actuales del dominio oficial.
2. Obtener URLs desde:
   - Sitemap actual.
   - Search Console.
   - Analytics.
   - Enlaces internos.
   - Backlinks conocidos.
3. Crear un mapa:
   - URL antigua.
   - URL nueva.
   - Tipo de redirección.
4. Aplicar redirecciones 301.
5. No redirigir todas las URLs antiguas a la home.
6. Mantener URLs existentes cuando sean válidas y tengan histórico.
7. Actualizar enlaces internos.
8. Actualizar sitemap.
9. Actualizar canonicals.
10. Verificar 404 y cadenas de redirección.
11. Enviar el sitemap nuevo a Search Console.
12. Supervisar indexación después de publicar.

## Implementación técnica

El método de redirección dependerá del hosting final.

- Si el hosting soporta redirects nativos, usar configuración del proveedor.
- Si es un servidor propio, usar reglas del servidor.
- Si es una plataforma estática, generar archivos o configuración compatibles.
- No confiar en meta refresh para URLs con autoridad.
- Documentar cualquier URL que no pueda redirigirse correctamente.

## Redirecciones existentes

Conservar y revisar las redirecciones ya definidas en `astro.config`.

Comprobar que funcionan realmente en el entorno final, no solo durante desarrollo.

---

# Prioridad 16: rendimiento y Core Web Vitals

No asumir que la web es lenta. Medir primero y optimizar después.

## Medir en producción

- Largest Contentful Paint
- Interaction to Next Paint
- Cumulative Layout Shift
- First Contentful Paint
- Total Blocking Time en laboratorio
- Peso de HTML
- Peso de CSS
- Peso del hero
- JavaScript de calculadora
- Scripts de terceros

## Mejoras recomendadas

- Optimizar la imagen LCP.
- Usar `fetchpriority="high"` en el hero cuando corresponda.
- Preload únicamente de recursos críticos.
- Evitar CSS duplicado entre páginas.
- Extraer estilos compartidos cuando reduzca tamaño total.
- No cargar JavaScript de calculadora en páginas donde no se utiliza.
- Cargar scripts de terceros después de interacción o consentimiento cuando sea posible.
- Reservar dimensiones de imágenes.
- No introducir animaciones costosas.
- Mantener `content-visibility` solo si no produce problemas de accesibilidad, búsqueda interna o medición.
- Revisar el uso de `font-display: optional`; decidir si produce cambios de tipografía no deseados.
- No sacrificar legibilidad por una puntuación artificial.

## Presupuesto orientativo

- Hero optimizado y responsive.
- JavaScript mínimo por página.
- Ningún desplazamiento visible al cargar.
- Interacciones de calculadora inmediatas.
- Evitar bundles globales innecesarios.

---

# Prioridad 17: analítica y medición de conversiones

Configurar eventos sin almacenar información personal innecesaria.

## Eventos recomendados

- `calculator_started`
- `coverage_checked`
- `service_selected`
- `frequency_selected`
- `extra_selected`
- `estimate_completed`
- `booking_started`
- `booking_completed`
- `phone_clicked`
- `whatsapp_clicked`
- `contact_submitted`
- `review_link_clicked`
- `suburb_page_viewed`

## Parámetros permitidos

- Tipo de servicio.
- Suburb o postcode general.
- Frecuencia.
- Número de extras.
- Rango de precio.
- Fuente de la conversión.
- Página de entrada.

No enviar a Analytics:

- Nombre.
- Dirección completa.
- Teléfono.
- Correo.
- Datos de tarjeta.
- Notas privadas del cliente.

## Embudo

Crear un funnel para:

1. Landing page.
2. Inicio de calculadora.
3. Estimación.
4. Inicio de booking.
5. Reserva completada.

Permitir comparar por:

- Servicio.
- Suburbio.
- Dispositivo.
- Fuente.
- Landing page.
- Campaña.

---

# Prioridad 18: revisión de navegación y enlaces internos

## Navegación principal

Mantener acceso claro a:

- Services
- Pricing
- Areas We Serve
- About
- Blog
- FAQs
- Contact
- Book

## Enlaces internos

- Home hacia los seis servicios.
- Servicios hacia Pricing.
- Servicios hacia suburbios relevantes.
- Blog hacia servicios relacionados.
- Suburbios hacia servicios.
- Suburbios hacia zonas cercanas.
- FAQs hacia páginas que amplían la respuesta.
- About hacia Contact y booking.
- No usar anchors genéricos como `Learn more` cuando se pueda describir el destino.

Ejemplos:

```text
Explore deep cleaning
View end of lease cleaning
Check house cleaning prices
See cleaning services in Brunswick
```

## Breadcrumbs

Añadir breadcrumbs visibles y schema en:

- Servicios.
- Blog posts.
- Suburbios.
- Páginas informativas profundas.

No añadir breadcrumbs innecesarios en la home.

---

# Prioridad 19: información externa que no puede resolverse solo con código

Crear un archivo de checklist separado o una sección en README con acciones manuales.

## Google Business Profile

Revisar:

- Nombre.
- Categoría principal.
- Categorías secundarias.
- Teléfono.
- Dominio.
- Horarios.
- Áreas servidas.
- Servicios.
- Fotografías.
- Enlace de reserva.
- Descripción.

La categoría principal debe mantenerse enfocada en limpieza residencial.

## Reseñas

Crear un proceso para solicitar feedback sin proporcionar textos exactos para copiar.

Pregunta recomendada:

```text
What service did we help you with, and what did you appreciate most about your cleaner?
```

## Enlaces y colaboraciones

Preparar una lista manual de oportunidades:

- Property managers.
- Real estate agencies.
- Removalists.
- Interior designers.
- Professional organisers.
- Blogs locales.
- Directorios australianos relevantes.
- Asociaciones de negocios locales.

No generar backlinks falsos ni directorios de baja calidad.

---

# Copy recomendado para puntos clave

## Hero

### Eyebrow

```text
HOUSE CLEANING MELBOURNE
```

### H1

```text
Trusted house cleaning services in Melbourne
```

### Supporting line

```text
A cleaner home. A lighter week.
```

### Description

```text
Reliable house cleaners across Melbourne with clear online pricing, flexible one-off and recurring services, and a 24-hour care promise.
```

### CTA principal

```text
Get an instant price
```

### CTA secundaria

```text
Explore cleaning services
```

## Trust review

```text
5.0 from {reviewCount} Google reviews
```

## Calculator disclaimer

```text
Your online estimate is based on the selections above. We will confirm availability and the final booking details before your service.
```

## Calculator out-of-area

```text
We may not currently cover this area online. Contact us and we will check whether we can help.
```

## CTA final

```text
Ready for a cleaner home?
```

Botón:

```text
Book your clean
```

---

# Criterios de aceptación

## SEO

- La home usa `house cleaning Melbourne` como objetivo principal.
- Title y description son únicos y válidos.
- Cada página tiene un único H1.
- Canonicals apuntan a producción.
- GitHub preview usa `noindex,follow`.
- Sitemap no contiene páginas noindex.
- Robots.txt declara el sitemap.
- OAI-SearchBot puede acceder a producción.
- No existen titles duplicados.
- No existen enlaces internos rotos.
- No existen páginas de suburbio indexables sin contenido local mínimo.
- No hay keyword stuffing.
- Las páginas de servicio no compiten entre sí por el mismo objetivo principal.

## UI/UX

- Los seis servicios siguen visibles en la home.
- No existe tabla comparativa debajo de servicios.
- No existe botón para mostrar más servicios.
- Los CTAs utilizan una jerarquía consistente.
- La barra móvil no tapa contenido.
- La calculadora valida cobertura.
- La calculadora muestra progreso y resumen.
- La selección se conserva durante la sesión.
- La diferencia entre estimate y final price es clara.
- La home se siente más compacta sin perder contenido importante.

## Confianza

- El contador de reseñas solo aparece con un dato real.
- El enlace de Google funciona.
- No se inventan casos, fotografías o cifras.
- About y schema contienen datos consistentes.
- Las afirmaciones sobre seguro, experiencia y garantía están explicadas.

## Accesibilidad

- Navegación completa con teclado.
- Focus visible.
- Contraste suficiente.
- Etiquetas accesibles.
- Menú móvil gestionado correctamente.
- `prefers-reduced-motion` respetado.
- La barra móvil no atrapa el foco.
- Los acordeones mantienen ARIA correcto.

## Rendimiento

- No hay CLS visible.
- La imagen del hero está optimizada.
- JavaScript de calculadora solo se carga donde se necesita.
- No se introducen scripts globales innecesarios.
- Los estilos compartidos no se duplican de forma excesiva.

## Calidad del código

- Reutilizar componentes.
- Centralizar precios, servicios, descuentos y datos de confianza.
- No duplicar copy en múltiples archivos si puede venir de configuración.
- Añadir validaciones de build.
- Documentar variables nuevas.
- Mantener TypeScript válido.
- Ejecutar:
  - `npm run check`
  - `npm run build`
  - `npm run check:seo`
  - `npm run check:suburbs`
- Corregir errores antes de finalizar.

---

# Entregables requeridos

1. Cambios completos en el código.
2. Resumen de archivos modificados.
3. Lista de decisiones de SEO aplicadas.
4. Lista de elementos pendientes por falta de datos reales:
   - Número de reseñas.
   - Fotografías.
   - ABN.
   - Casos locales.
   - Estadísticas.
5. Mapa de redirecciones propuesto.
6. Lista de páginas con `noindex`.
7. Lista de suburbios prioritarios.
8. Informe de validación:
   - Build.
   - SEO checks.
   - Enlaces rotos.
   - Schema.
   - Responsive.
   - Accesibilidad básica.
9. Checklist manual para Google Business Profile, reseñas y backlinks.
10. No dejar placeholders visibles para usuarios finales. Los datos pendientes deben quedar ocultos o controlados por configuración.

---

# Orden recomendado de implementación

## Fase 1

- Metadata y H1.
- Canonicals y noindex de preview.
- Jerarquía de CTAs.
- Review count configurable.
- Barra móvil.
- Validaciones de build.

## Fase 2

- Mejoras de calculadora.
- Resumen y persistencia.
- Validación de cobertura.
- Analítica del funnel.

## Fase 3

- Respuestas directas en servicios.
- Schema por tipo de página.
- Refuerzo de About.
- Autoría y fechas del blog.
- `llms.txt`.

## Fase 4

- Auditoría de suburbios.
- Priorización de 10 a 15 páginas.
- Campos de contenido local.
- Casos reales opcionales.
- Noindex para páginas insuficientes.

## Fase 5

- Rendimiento.
- Migración y redirecciones.
- Revisión final del dominio oficial.
- Envío de sitemap y supervisión post-lanzamiento.

---

# Restricciones finales

- No rediseñar toda la web.
- No eliminar los seis servicios de la home.
- No añadir tabla de comparación de servicios.
- No añadir botón para ocultar o desplegar servicios.
- No inventar datos.
- No publicar páginas locales débiles solo para aumentar el número de URLs.
- No depender de `llms.txt` como estrategia principal.
- No bloquear OAI-SearchBot.
- No poner `noindex` en producción.
- No redirigir todas las URLs antiguas a la home.
- No introducir claims que no puedan verificarse.
- No sacrificar conversión o legibilidad para repetir keywords.
