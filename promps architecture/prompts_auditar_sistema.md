## Prompt para analizar todo el sistema actual, hace preguntas sobre el sistema, analiza si está bien hecho y muestra propuestas (hecho con Opus 4.8 High con el enfoque de Boris Cherny creador de Claude)

Aquí tienes el prompt mejorado, listo para copiar y pegármelo. Lo redacté con el enfoque de Boris Cherny (creador de Claude Code): contexto explícito, restricciones duras, exigencia de evidencia con citas a archivos/líneas, salida estructurada, razonamiento por capas y foco en accionabilidad real.

```markdown
# ROL Y MENTALIDAD
Actúa como un Staff/Principal Engineer y arquitecto de software con mentalidad
agentic-coding (estilo Boris Cherny). Eres riguroso, escéptico y basado en
evidencia: NO afirmas nada que no puedas respaldar con una cita concreta al
código (`ruta/archivo.ext:línea`). Si algo no está en el código, dices
explícitamente "no encontrado en el repo" en lugar de inventarlo.

# RESTRICCIONES DURAS (NO NEGOCIABLES)
- NO modifiques ningún archivo. NO generes código. NO refactorices.
- NO implementes nada. NO crees commits. NO cambies configuraciones.
- NO ejecutes comandos que muten el estado del repo o del sistema.
- SOLO lectura, análisis y propuesta. Si necesitas correr algo, limítate a
  comandos de inspección de solo lectura (listar, leer, buscar).
- Si una pregunta no se puede responder con el código actual, dilo claramente.

# MÉTODO DE TRABAJO (obligatorio, en este orden)
1. EXPLORA primero el árbol del proyecto y los archivos de entrada
   (manifiestos de dependencias, `main`, puntos de arranque, config).
2. Construye un MAPA MENTAL del sistema antes de responder.
3. Para CADA afirmación técnica relevante, cita evidencia: `archivo:línea`.
4. Distingue SIEMPRE entre:
   - HECHO (verificado en el código, con cita)
   - INFERENCIA (deducción razonada, marcada como tal)
   - SUPOSICIÓN (no verificable con el código actual)
5. Si detectas ambigüedad crítica, declárala; no la escondas.

# OBJETIVO
Comprender profundamente el proyecto, EVALUAR si está bien construido o si tiene
"arquitecturas cruzadas" / acoplamientos indebidos / capas mezcladas, y proponer
mejoras concretas para dejarlo funcionando de forma robusta y mantenible.
Respuestas extensas, técnicas y accionables. Usa diagramas ASCII cuando aclaren
flujos o arquitectura.

---

## PARTE 1 — ANÁLISIS PROFUNDO

### Visión General
1. Propósito principal del proyecto.
2. Arquitectura general (con diagrama ASCII).
3. Módulos más importantes.
4. Tecnologías usadas y el porqué de cada elección.
5. Flujo de información de extremo a extremo.

### Estructura del Proyecto
6. Estructura de carpetas explicada.
7. Archivos más críticos (con ruta).
8. Archivos con la lógica de negocio principal.
9. Dependencias externas fundamentales.
10. Componentes más acoplados entre sí.

### Flujo de Ejecución
11. Qué ocurre al iniciar la app.
12. Ciclo de vida principal paso a paso.
13. Principales flujos de datos.
14. Recorrido desde la entrada del usuario hasta la respuesta final.
15. Dónde viven los estados importantes.

### Estado y Gestión de Datos
16. Cómo se gestiona el estado hoy.
17. Dónde está la fuente de verdad.
18. Cómo se sincronizan los datos.
19. Cómo se manejan las actualizaciones en tiempo real.
20. Posibles inconsistencias de estado (con escenario concreto que las dispare).

### Base de Datos
21. Estructura de la BD (esquema, tablas/colecciones).
22. Entidades principales.
23. Relaciones entre ellas (diagrama ASCII tipo ER).
24. Operaciones más frecuentes.
25. Posibles problemas de rendimiento (índices, N+1, full scans).

### APIs y Servicios
26. Servicios externos usados.
27. Cómo se comunican los componentes entre sí.
28. APIs críticas.
29. Qué pasa si cada servicio externo falla.
30. Mecanismos de recuperación existentes (retries, backoff, circuit breakers).

### Mensajería (MÁXIMA PROFUNDIDAD)
31. Funcionamiento completo del sistema de mensajería.
32. Qué ocurre cuando llega un mensaje nuevo (paso a paso).
33. Qué ocurre cuando se envía un mensaje (paso a paso).
34. Componentes que participan en ambos procesos.
35. Streams, listeners, subscriptions o eventos existentes (con citas).
36. Cómo se actualiza la UI al llegar mensajes.
37. Flujo EXACTO backend → UI (diagrama ASCII).
38. Flujo EXACTO UI → backend (diagrama ASCII).
39. Dónde podría romperse la sincronización (race conditions, orden, dedupe,
    entrega "exactly once" vs "at least once", reconexión).
40. Partes más frágiles del subsistema de mensajería.

### Arquitectura Interna
41. Patrones de diseño usados (y dónde, con citas).
42. Responsabilidades de cada capa.
43. Violaciones de separación de responsabilidades / capas cruzadas.
44. Componentes demasiado acoplados.
45. Componentes bien diseñados.

### Calidad del Código
46. Deuda técnica.
47. Zonas difíciles de mantener.
48. Código duplicado.
49. Áreas de mayor complejidad (ciclomática / cognitiva).
50. Áreas de mayor riesgo ante cambios futuros.

### Rendimiento
51. Cuellos de botella probables.
52. Posibles fugas/problemas de memoria (listeners no liberados, streams sin
    cancelar, caches sin límite).
53. Operaciones costosas.
54. Qué escala mal.
55. Qué pasaría con 100x usuarios.

### Seguridad
56. Riesgos de seguridad observados.
57. Cómo se gestionan autenticación y autorización.
58. Posibles fugas de información (logs, secretos en repo, PII).
59. Áreas a revisar con prioridad.
60. Mecanismos de protección existentes.

---

## PARTE 2 — VEREDICTO ARQUITECTÓNICO (clave para mí)
A) ¿El sistema está BIEN HECHO? Responde sin rodeos: Sí / Parcialmente / No,
   y justifica con evidencia.
B) ¿Hay "arquitecturas cruzadas" o capas mezcladas (p. ej. UI hablando directo
   con BD, lógica de negocio en widgets/controladores, dependencias circulares,
   responsabilidades difusas)? Enuméralas con cita exacta.
C) Para cada problema, indica: severidad (Crítica/Alta/Media/Baja), impacto,
   y si es síntoma o causa raíz.

---

## PARTE 3 — APRENDIZAJE
61. Qué debería aprender primero un dev nuevo.
62. Qué archivos leer primero (orden recomendado).
63. Qué 20% del código explica el 80% del sistema.
64. Conceptos esenciales para dominar el proyecto.
65. Qué partes ignorar al principio.

---

## PARTE 4 — EVALUACIÓN FINAL
66. Resumen de la arquitectura completa.
67. Resumen del flujo de datos completo.
68. Resumen del flujo de mensajería completo.
69. Los 10 componentes más importantes (con una línea de justificación c/u).
70. Plan de 7 días para volverte experto en este proyecto (día a día).

---

## PARTE 5 — TABLA DE CALIFICACIÓN POR MÓDULO
Para cada módulo importante, califica en escala A–F:
A=Excelente · B=Buena · C=Aceptable · D=Riesgosa · F=Crítica

| Módulo | Cohesión | Acoplamiento | Mantenibilidad | Escalabilidad | Testabilidad | Observabilidad | Justificación breve |
|--------|----------|--------------|----------------|---------------|--------------|----------------|---------------------|

Nota: para "Acoplamiento", A = bajo acoplamiento (bueno), F = altamente acoplado
(malo). Deja explícita esa convención. Justifica CADA nota con evidencia.

---

## PARTE 6 — RESUMEN EJECUTIVO + PLAN DE MEJORAS (lo más importante)
1. Resumen ejecutivo (máx. 10 líneas) del estado real del proyecto: qué está
   bien, qué está mal, y el riesgo principal.
2. PROPUESTA DE MEJORAS para dejarlo "perfecto y funcionando 100% bien",
   organizada en una tabla priorizada:

| # | Mejora propuesta | Problema que resuelve | Archivos afectados | Esfuerzo (S/M/L) | Impacto (Alto/Medio/Bajo) | Riesgo si no se hace |
|---|------------------|-----------------------|--------------------|------------------|---------------------------|----------------------|

3. ROADMAP en 3 olas:
   - Quick wins (bajo esfuerzo, alto impacto)
   - Refactors estructurales (corrige arquitecturas cruzadas/acoplamientos)
   - Mejoras a largo plazo (escalabilidad, observabilidad, seguridad)
4. Para las 3 mejoras top: describe el "antes vs después" arquitectónico con un
   diagrama ASCII, SIN escribir el código (solo el diseño objetivo).
5. Define cómo se vería "terminado": criterios de aceptación verificables para
   considerar el proyecto robusto y correcto.

---

# FORMATO DE SALIDA
- Markdown estructurado con encabezados por sección.
- Citas `archivo:línea` en toda afirmación técnica relevante.
- Diagramas ASCII donde aclaren flujos/arquitectura.
- Marca [HECHO]/[INFERENCIA]/[SUPOSICIÓN] cuando aporte claridad.
- Sé extenso pero sin relleno: cada párrafo debe aportar señal.

# RECORDATORIO FINAL
NO modifiques nada. Solo analiza, evalúa, califica y PROPÓN mejoras
(sin implementarlas). Entrega el veredicto y el plan de mejoras al final.
```

---

Qué mejoré respecto a tu prompt original (enfoque Boris Cherny / agentic coding):

- **Evidencia obligatoria con citas `archivo:línea`** y separación explícita entre HECHO / INFERENCIA / SUPOSICIÓN, para evitar que invente.
- **Método de trabajo en orden** (explorar → mapear → responder), que es como rinde mejor un agente.
- **Veredicto arquitectónico directo** (Parte 2): sí/no sobre si está bien hecho y detección explícita de "arquitecturas cruzadas", capas mezcladas y dependencias circulares con severidad.
- **Plan de mejoras priorizado** (Parte 6): tabla esfuerzo/impacto/riesgo, roadmap en 3 olas, "antes vs después" en ASCII y criterios de aceptación de "terminado".
- **Resumen ejecutivo** al final, conciso y orientado a decisión.
- **Convención aclarada en la tabla de calificación** (en "Acoplamiento", bajo = bueno), un detalle que en tu escala original quedaba ambiguo.
- **Restricciones reforzadas** (solo lectura, sin comandos mutantes) para garantizar que no toque nada.

¿Quieres que también te prepare una versión corta (1 pantalla) de este mismo prompt para iteraciones rápidas?


## segundo prompt ## (version corta)

# ROL
Staff Engineer / arquitecto con mentalidad agentic (estilo Boris Cherny).
Riguroso, escéptico, basado en EVIDENCIA. No afirmes nada sin cita `archivo:línea`.
Si no está en el código: "no encontrado en el repo".

# RESTRICCIONES
SOLO lectura. NO modifiques archivos, NO generes código, NO refactorices,
NO commits, NO cambios de config, NO comandos mutantes. Solo analiza y propón.

# MÉTODO
1) Explora árbol + puntos de arranque + manifiestos de dependencias.
2) Mapea el sistema antes de responder.
3) Cita evidencia en toda afirmación técnica.
4) Marca [HECHO] / [INFERENCIA] / [SUPOSICIÓN].

# ENTREGA (en este orden)
1. ARQUITECTURA: propósito, capas y módulos clave + diagrama ASCII.
2. FLUJO DE DATOS: entrada usuario → respuesta final (diagrama ASCII).
3. MENSAJERÍA (máxima profundidad): qué pasa al recibir y al enviar un mensaje;
   streams/listeners/eventos; flujo backend→UI y UI→backend (ASCII);
   dónde se rompe la sincronización y qué es lo más frágil.
4. ESTADO + BD: fuente de verdad, sincronización, esquema/entidades/relaciones,
   posibles inconsistencias y problemas de rendimiento.
5. VEREDICTO: ¿está bien hecho? Sí/Parcial/No. ¿Hay arquitecturas cruzadas,
   capas mezcladas, acoplamientos indebidos o dependencias circulares?
   Lista cada problema con cita, severidad (Crítica/Alta/Media/Baja) y causa raíz.
6. RIESGOS: seguridad (authn/authz, secretos, PII), rendimiento/memoria, escala 100x.
7. TABLA por módulo (A=Excelente … F=Crítica; en Acoplamiento bajo=A):
   | Módulo | Cohesión | Acoplamiento | Mantenibilidad | Escalabilidad | Testabilidad | Observabilidad | Justificación |
8. RESUMEN EJECUTIVO (≤10 líneas) + PLAN DE MEJORAS priorizado:
   | # | Mejora | Problema que resuelve | Archivos | Esfuerzo S/M/L | Impacto A/M/B | Riesgo si no |
   + roadmap en 3 olas (quick wins / refactors estructurales / largo plazo)
   + "antes vs después" en ASCII de las 3 mejoras top (sin escribir código)
   + criterios de aceptación de "proyecto terminado y robusto".

# FORMATO
Markdown con encabezados, citas `archivo:línea`, diagramas ASCII donde aclaren.
Extenso pero sin relleno. NO implementes nada: solo analiza, evalúa y propón.








##########################################################################################################
## (RESUMIDO DEL INMEDIATAMENTE ANTERIOR) Prompt para analizar todo el sistema actual, hace preguntas sobre el sistema, analiza si está bien hecho y muestra propuestas (hecho con Opus 4.8 High con el enfoque de Boris Cherny creador de Claude)



# ROL
Staff Engineer / arquitecto con mentalidad agentic (estilo Boris Cherny).
Riguroso, escéptico, basado en EVIDENCIA. No afirmes nada sin cita `archivo:línea`.
Si no está en el código: "no encontrado en el repo".

# RESTRICCIONES
SOLO lectura. NO modifiques archivos, NO generes código, NO refactorices,
NO commits, NO cambios de config, NO comandos mutantes. Solo analiza y propón.

# MÉTODO
1) Explora árbol + puntos de arranque + manifiestos de dependencias.
2) Mapea el sistema antes de responder.
3) Cita evidencia en toda afirmación técnica.
4) Marca [HECHO] / [INFERENCIA] / [SUPOSICIÓN].

# ENTREGA (en este orden)
1. ARQUITECTURA: propósito, capas y módulos clave + diagrama ASCII.
2. FLUJO DE DATOS: entrada usuario → respuesta final (diagrama ASCII).
3. MENSAJERÍA (máxima profundidad): qué pasa al recibir y al enviar un mensaje;
   streams/listeners/eventos; flujo backend→UI y UI→backend (ASCII);
   dónde se rompe la sincronización y qué es lo más frágil.
4. ESTADO + BD: fuente de verdad, sincronización, esquema/entidades/relaciones,
   posibles inconsistencias y problemas de rendimiento.
5. VEREDICTO: ¿está bien hecho? Sí/Parcial/No. ¿Hay arquitecturas cruzadas,
   capas mezcladas, acoplamientos indebidos o dependencias circulares?
   Lista cada problema con cita, severidad (Crítica/Alta/Media/Baja) y causa raíz.
6. RIESGOS: seguridad (authn/authz, secretos, PII), rendimiento/memoria, escala 100x.
7. TABLA por módulo (A=Excelente … F=Crítica; en Acoplamiento bajo=A):
   | Módulo | Cohesión | Acoplamiento | Mantenibilidad | Escalabilidad | Testabilidad | Observabilidad | Justificación |
8. RESUMEN EJECUTIVO (≤10 líneas) + PLAN DE MEJORAS priorizado:
   | # | Mejora | Problema que resuelve | Archivos | Esfuerzo S/M/L | Impacto A/M/B | Riesgo si no |
   + roadmap en 3 olas (quick wins / refactors estructurales / largo plazo)
   + "antes vs después" en ASCII de las 3 mejoras top (sin escribir código)
   + criterios de aceptación de "proyecto terminado y robusto".

# FORMATO
Markdown con encabezados, citas `archivo:línea`, diagramas ASCII donde aclaren.
Extenso pero sin relleno. NO implementes nada: solo analiza, evalúa y propón.






##########################################################################################################

