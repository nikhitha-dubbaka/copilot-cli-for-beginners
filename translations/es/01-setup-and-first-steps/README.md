<!--
---
id: CopilotCLI-01
title: !translate First Steps
description: !translate Experience GitHub Copilot CLI through hands-on demos, then learn when to use interactive, plan, and programmatic modes.
audience: Developers / Students / Terminal users
slug: first-steps
weight: 2
---
-->

![Capítulo 01: Primeros pasos](../../../01-setup-and-first-steps/assets/chapter-header.png)

> **Observa cómo la IA encuentra errores al instante, explica código confuso y genera scripts funcionales. Después aprende tres formas diferentes de usar GitHub Copilot CLI.**

¡Este capítulo es donde comienza la magia! Experimentarás de primera mano por qué los desarrolladores describen GitHub Copilot CLI como tener a un ingeniero senior en marcación rápida. Verás a la IA encontrar fallos de seguridad en segundos, obtener explicaciones de código complejo en un inglés sencillo y generar scripts funcionales al instante. Luego dominarás los tres modos de interacción (Interactivo, Plan y Programático) para saber exactamente cuál usar en cada tarea.

> ⚠️ **Prerequisites**: Make sure you've completed **[Chapter 00: Quick Start](../00-quick-start/README.md)** first. You'll need GitHub Copilot CLI installed and authenticated before running the demos below.

## 🎯 Objetivos de aprendizaje

Al final de este capítulo, podrás:

- Experimentar el aumento de productividad que proporciona GitHub Copilot CLI mediante demostraciones prácticas
- Elegir el modo adecuado (Interactivo, Plan o Programático) para cualquier tarea
- Usar comandos slash para controlar tus sesiones

> ⏱️ **Estimated Time**: ~45 minutes (15 min reading + 30 min hands-on)

---

# Tu primera experiencia con Copilot CLI

<img src="../../../01-setup-and-first-steps/assets/first-copilot-experience.png" alt="Desarrollador sentado en un escritorio con código en el monitor y partículas brillantes que representan la asistencia de la IA" width="800"/>

Sumérgete y descubre lo que Copilot CLI puede hacer.

---

## Familiarízate: Tus primeros prompts

Antes de sumergirte en las demostraciones impresionantes, comencemos con algunos prompts sencillos que puedes probar ahora mismo. **No se necesita un repositorio de código**! Simplemente abre una terminal y inicia Copilot CLI:

```bash
copilot
```

Prueba estos prompts para principiantes:

```
> Explain what a dataclass is in Python in simple terms

> Write a function that sorts a list of dictionaries by a specific key

> What's the difference between a list and a tuple in Python?

> Give me 5 best practices for writing clean Python code
```

¿No usas Python? ¡No hay problema! Simplemente haz preguntas sobre el lenguaje que prefieras.

Fíjate en lo natural que se siente. Simplemente haz preguntas como lo harías con un colega. Cuando termines de explorar, escribe `/exit` para salir de la sesión.

**La idea clave**: GitHub Copilot CLI es conversacional. No necesitas sintaxis especial para empezar. Simplemente haz preguntas en lenguaje natural.

## Míralo en acción

Ahora veamos por qué los desarrolladores llaman a esto "tener a un ingeniero senior en marcación rápida."

> 📖 **Cómo leer los ejemplos**: Las líneas que comienzan con `>` son prompts que escribes dentro de una sesión interactiva de Copilot CLI. Las líneas sin prefijo `>` son comandos de shell que ejecutas en tu terminal.

> 💡 **Sobre las salidas de ejemplo**: Las salidas de ejemplo que se muestran a lo largo de este curso son ilustrativas. Dado que las respuestas de Copilot CLI varían cada vez, tus resultados diferirán en redacción, formato y detalle. Concéntrate en el *tipo* de información devuelta, no en el texto exacto.

### Demostración 1: Revisión de código en segundos

El curso incluye archivos de ejemplo con problemas de calidad de código intencionados. Si trabajas en tu máquina local y aún no has clonado el repositorio, ejecuta el comando `git clone` que aparece a continuación, navega a la carpeta `copilot-cli-for-beginners` y luego ejecuta el comando `copilot`.

```bash
# Clona el repositorio del curso si estás trabajando localmente y aún no lo has hecho
git clone https://github.com/github/copilot-cli-for-beginners
cd copilot-cli-for-beginners

# Inicia Copilot
copilot
```

Una vez dentro de la sesión interactiva de Copilot CLI, ejecuta lo siguiente:

```
> Review @samples/book-app-project/book_app.py for code quality issues and suggest improvements
```

> 💡 **What's the `@` symbol used for?** The `@` symbol tells Copilot CLI to read a file. You'll learn all about this in Chapter 02. For now, just copy the command exactly as shown.

---

<details>
<summary>🎬 ¡Míralo en acción!</summary>

![Demostración de revisión de código](../../../01-setup-and-first-steps/assets/code-review-demo.gif)

*La salida de la demostración varía. Tu modelo, herramientas y respuestas diferirán de lo que se muestra aquí.*

</details>

---

**La conclusión**: Una revisión de código profesional en segundos. La revisión manual tomaría... bueno... mucho más tiempo que eso.

---

### Demostración 2: Explicar código confuso

¿Alguna vez has mirado código preguntándote qué hace? Prueba esto en tu sesión de Copilot CLI:

```
> Explain what @samples/book-app-project/books.py does in simple terms
```

---

<details>
<summary>🎬 ¡Míralo en acción!</summary>

![Demostración de explicación de código](../../../01-setup-and-first-steps/assets/explain-code-demo.gif)

*La salida de la demostración varía. Tu modelo, herramientas y respuestas diferirán de lo que se muestra aquí.*

</details>

---

**Qué sucede**: (tu salida variará) Copilot CLI lee el archivo, comprende el código y lo explica en lenguaje sencillo.

```
This is a book collection management module using Python dataclasses.

Think of it like a digital bookshelf:
- Book is a dataclass - a simple way to store book information (title, author, year, read status)
- BookCollection manages the entire collection and handles saving/loading

Key components:

1. @dataclass decorator (line 8)
   - Automatically creates __init__, __repr__, etc.
   - Clean way to define data structures in Python

2. BookCollection class (line 16)
   - Maintains a list of Book objects
   - Handles persistence with JSON file I/O
   - load_books() reads from data.json
   - save_books() writes to data.json using asdict()

3. Book operations:
   - add_book() - creates and saves new books
   - find_book_by_title() - searches collection
   - mark_as_read() - updates read status
   - find_by_author() - filters by author name

Common pattern: Read from JSON → Work with Python objects → Write back to JSON
```

**La conclusión**: Código complejo explicado como lo haría un mentor paciente.

---

### Demostración 3: Generar código funcional

¿Necesitas una función para la que normalmente pasarías 15 minutos buscando en Google? Aún en tu sesión:

```
> Write a Python function that takes a list of books and returns statistics: 
  total count, number read, number unread, oldest and newest book
```

---

<details>
<summary>🎬 ¡Míralo en acción!</summary>

![Demostración de generación de código](../../../01-setup-and-first-steps/assets/generate-code-demo.gif)

*La salida de la demostración varía. Tu modelo, herramientas y respuestas diferirán de lo que se muestra aquí.*

</details>

---

**Qué sucede**: Una función completa y funcional en segundos que puedes copiar, pegar y ejecutar.

When you're done exploring, exit the session:

```
> /exit
```

**La conclusión**: Gratificación instantánea y te mantuviste en una única sesión continua todo el tiempo.

---

# Modos y comandos

<img src="../../../01-setup-and-first-steps/assets/modes-and-commands.png" alt="Panel de control futurista con pantallas brillantes, diales y ecualizadores que representan los modos y comandos de Copilot CLI" width="800"/>

Acabas de ver lo que puede hacer Copilot CLI. Ahora entendamos *cómo* usar estas capacidades de manera efectiva. La clave es saber cuál de los tres modos de interacción usar según la situación.

> 💡 **Note**: Copilot CLI also has an **Autopilot** mode where it works through tasks without waiting for your input. It's powerful but requires granting full permissions and uses premium requests autonomously. This course focuses on the three modes below. We'll point you to Autopilot once you're comfortable with the basics.

---

## 🧩 Analogía del mundo real: salir a comer

Piensa en usar GitHub Copilot CLI como salir a comer. Desde planear el viaje hasta hacer el pedido, diferentes situaciones requieren distintos enfoques:

| Modo | Analogía | Cuándo usar |
|------|----------------|-------------|
| **Plan** | Ruta GPS al restaurante | Tareas complejas: traza la ruta, revisa las paradas, acuerda el plan y luego ejecútalo |
| **Interactivo** | Hablar con el camarero | Exploración e iteración - haz preguntas, personaliza, obtén retroalimentación en tiempo real |
| **Programático** | Pedido en el autoservicio | Tareas rápidas y específicas - permanece en tu entorno y obtén un resultado rápido |

Al igual que al salir a comer, aprenderás de forma natural cuándo cada enfoque es el adecuado.

<img src="../../../01-setup-and-first-steps/assets/ordering-food-analogy.png" alt="Tres maneras de usar GitHub Copilot CLI - Modo Plan (ruta GPS al restaurante), Modo Interactivo (hablar con el camarero), Modo Programático (autoservicio)" width="800"/>

*Elige tu modo según la tarea: Plan para trazarlo primero, Interactivo para colaboración de ida y vuelta, Programático para resultados rápidos de una sola vez*

### ¿Con qué modo debería comenzar?

**Comienza con el modo Interactivo.** 
- Puedes experimentar y hacer preguntas de seguimiento
- El contexto se construye de forma natural mediante la conversación
- Los errores se corrigen fácilmente con `/clear`

Una vez que te sientas cómodo, prueba:
- **Modo Programático** (`copilot -p "<your prompt>"`) para preguntas rápidas y puntuales
- **Modo Plan** (`/plan`) cuando necesites planificar con más detalle antes de codificar

---

## Los tres modos

### Modo 1: Modo Interactivo (comienza aquí)

<img src="../../../01-setup-and-first-steps/assets/interactive-mode.png" alt="Modo Interactivo - Como hablar con un camarero que puede responder preguntas y ajustar el pedido" width="250"/>

**Ideal para**: Exploración, iteración, conversaciones de múltiples turnos. Como hablar con un camarero que puede responder preguntas, recibir feedback y ajustar el pedido al instante.

Inicia una sesión interactiva:

```bash
copilot
```

Como has visto hasta ahora, verás un indicador donde puedes escribir de forma natural. Para obtener ayuda sobre los comandos disponibles, simplemente escribe:

```
> /help
```

**Idea clave**: El modo Interactivo mantiene el contexto. Cada mensaje se basa en los anteriores, como en una conversación real.

#### Ejemplo de modo interactivo

```bash
copilot

> Review @samples/book-app-project/utils.py and suggest improvements

> Add type hints to all functions

> Make the error handling more robust

> /exit
```

Fíjate en cómo cada prompt se basa en la respuesta anterior. Estás manteniendo una conversación, no empezando de cero cada vez.

---

### Modo 2: Modo Plan

<img src="../../../01-setup-and-first-steps/assets/plan-mode.png" alt="Modo Plan - Como planear una ruta antes de un viaje usando GPS" width="250"/>

**Ideal para**: Tareas complejas donde quieres revisar el enfoque antes de ejecutarlo. Similar a planear una ruta antes de un viaje usando GPS.

El modo Plan te ayuda a crear un plan paso a paso antes de escribir código. Usa el comando `/plan`, presiona **Shift+Tab** para cambiar al modo Plan:

```bash
copilot

> /plan Add a "mark as read" command to the book app
```

> 💡 **Consejo**: **Shift+Tab** cambia entre modos: Interactivo → Plan → Autopilot. Púlsalo en cualquier momento durante una sesión interactiva para cambiar de modo sin escribir un comando.

También puedes iniciar Copilot CLI directamente en modo Plan usando la bandera `--plan`:

```bash
copilot --plan
```

**Salida del modo Plan:** (tu salida puede variar)

```
📋 Implementation Plan

Step 1: Update the command handler in book_app.py
  - Add new elif branch for "mark" command
  - Create handle_mark_as_read() function

Step 2: Implement the handler function
  - Prompt user for book title
  - Call collection.mark_as_read(title)
  - Display success/failure message

Step 3: Update help text
  - Add "mark" to available commands list
  - Document the command usage

Step 4: Test the flow
  - Add a book
  - Mark it as read
  - Verify status changes in list output

Proceed with implementation? [Y/n]
```

**Idea clave**: El modo Plan te permite revisar y modificar el enfoque antes de que se escriba código. Una vez que un plan esté completo, incluso puedes pedirle a Copilot CLI que lo guarde en un archivo para referencia posterior. Por ejemplo, "Save this plan to `mark_as_read_plan.md`" crearía un archivo markdown con los detalles del plan.

> 💡 **¿Quieres algo más complejo?** Prueba: `/plan Add search and filter capabilities to the book app`. El modo Plan escala desde funciones simples hasta aplicaciones completas.

> 📚 **Autopilot mode**: You may have noticed Shift+Tab cycles through a third mode called **Autopilot**. In autopilot mode, Copilot works through an entire plan without waiting for your input after each step — like handing a task to a colleague and saying "let me know when you're finished." The typical workflow is plan → accept → autopilot, which means you need to be good at writing plans first. You can also launch directly into autopilot with `copilot --autopilot`. Get comfortable with Interactive and Plan modes first, then see the [official docs](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot) when you're ready.

---

### Modo 3: Modo Programático

<img src="../../../01-setup-and-first-steps/assets/programmatic-mode.png" alt="Modo Programático - Como usar un autoservicio para un pedido rápido" width="250"/>

**Ideal para**: Automatización, scripts, CI/CD, comandos de una sola ejecución. Como usar un autoservicio para un pedido rápido sin necesidad de hablar con un camarero.

Usa la bandera `-p` para comandos puntuales que no requieren interacción:

```bash
# Generar código
copilot -p "Write a function that checks if a number is even or odd"

# Obtener ayuda rápida
copilot -p "How do I read a JSON file in Python?"
```

**Idea clave**: El modo Programático te da una respuesta rápida y sale. No hay conversación, solo entrada → salida.

<details>
<summary>📚 <strong>Ir más allá: Usar el modo Programático en scripts</strong> (haz clic para expandir)</summary>

Una vez que te sientas cómodo, puedes usar `-p` en scripts de shell:

```bash
#!/bin/bash

# Generar mensajes de confirmación automáticamente
COMMIT_MSG=$(copilot -p "Generate a commit message for: $(git diff --staged)")
git commit -m "$COMMIT_MSG"

# Revisar un archivo
copilot --allow-all -p "Review @myfile.py for issues"
```
> ⚠️ **Acerca de `--allow-all`**: Esta bandera omite todos los avisos de permiso, permitiendo que Copilot CLI lea archivos, ejecute comandos y acceda a URLs sin pedir permiso primero. Esto es necesario para el modo programático (`-p`) ya que no hay una sesión interactiva para aprobar acciones. Usa `--allow-all` solo con prompts que hayas escrito tú mismo y en directorios de confianza. Nunca lo uses con entradas no confiables ni en directorios sensibles.

</details>

---

## Comandos slash esenciales

Estos comandos son estupendos para aprender al empezar con Copilot CLI:

| Comando | Qué hace | Cuándo usar |
|---------|--------------|-------------|
| `/ask` | Haz una pregunta rápida sin que afecte el historial de la conversación | Cuando quieras una respuesta rápida sin desviar tu tarea actual |
| `/clear` | Borrar la conversación y empezar de nuevo | Al cambiar de tema |
| `/help` | Mostrar todos los comandos disponibles | Cuando olvides un comando |
| `/model` | Mostrar o cambiar el modelo de IA | Cuando quieras cambiar el modelo de IA |
| `/plan` | Planificar tu trabajo antes de codificar | Para características más complejas |
| `/research` | Investigación profunda usando GitHub y fuentes web | Cuando necesites investigar un tema antes de codificar |
| `/exit` | Terminar la sesión | Cuando hayas terminado |

> 💡 **`/ask` vs chat normal**: Normalmente cada mensaje que envías forma parte de la conversación en curso y afecta las respuestas futuras. `/ask` es un atajo 'fuera de registro' — perfecto para preguntas puntuales como `/ask What does YAML mean?` sin contaminar el contexto de tu sesión.


> 💡 **Autocompletado con Tab**: Al escribir un comando con barra, presiona **Tab** para completar automáticamente el nombre del comando o recorrer los subcomandos y argumentos disponibles. Esto es especialmente útil cuando no recuerdas el nombre exacto de un comando.

¡Eso es todo para empezar! A medida que te familiarices, puedes explorar comandos adicionales.

> 📚 **Documentación oficial**: [Referencia de comandos de la CLI](https://docs.github.com/copilot/reference/cli-command-reference) para la lista completa de comandos y opciones.

<details>
<summary>📚 <strong>Comandos adicionales</strong> (haz clic para expandir)</summary>

> 💡 Los comandos esenciales anteriores cubren gran parte de lo que harás en el uso diario. Esta referencia está aquí para cuando estés listo para explorar más.

### Entorno del agente

| Comando | Qué hace |
|---------|--------------|
| `/agent` | Explora y selecciona entre los agentes disponibles |
| `/env` | Muestra los detalles del entorno cargado — qué instrucciones, servidores MCP, skills, agentes y complementos están activos |
| `/init` | Inicializa las instrucciones de Copilot para tu repositorio |
| `/mcp` | Gestiona la configuración del servidor MCP |
| `/settings` | Abre un diálogo interactivo para ver y editar todos los ajustes de usuario en un solo lugar |
| `/skills` | Gestiona las skills para capacidades mejoradas |

> 💡 Los agentes se tratan en [Capítulo 04](../04-agents-custom-instructions/README.md), las skills se tratan en [Capítulo 05](../05-skills/README.md), y los servidores MCP se tratan en [Capítulo 06](../06-mcp-servers/README.md).

### Modelos y subagentes

| Comando | Qué hace |
|---------|--------------|
| `/delegate` | Delegar la tarea al agente en la nube de GitHub Copilot |
| `/fleet` | Divide una tarea compleja en subtareas paralelas para una finalización más rápida |
| `/model` | Mostrar o cambiar el modelo de IA |
| `/tasks` | Ver subagentes en segundo plano y sesiones de shell desconectadas |

### Código

| Comando | Qué hace |
|---------|--------------|
| `/diff` | Revisar los cambios realizados en el directorio actual |
| `/pr` | Trabajar con pull requests de la rama actual |
| `/research` | Realizar una investigación profunda usando GitHub y fuentes web |
| `/review` | Ejecutar el agente de revisión de código para analizar cambios |
| `/terminal-setup` | Habilitar soporte de entrada multilínea (Shift+Enter y Ctrl+Enter) |

### Permisos

| Comando | Qué hace |
|---------|--------------|
| `/add-dir <directory>` | Agregar un directorio a la lista permitida |
| `/allow-all [on\|off\|show]` | Aprobar automáticamente todas las solicitudes de permisos; usa `on` para activar, `off` para desactivar, `show` para comprobar el estado actual |
| `/yolo` | Alias rápido de `/allow-all on` — aprueba automáticamente todas las solicitudes de permisos. |
| `/cwd`, `/cd [directory]` | Ver o cambiar el directorio de trabajo |
| `/list-dirs` | Mostrar todos los directorios permitidos |

> ⚠️ **Usar con precaución**: `/allow-all` y `/yolo` omiten los avisos de confirmación. Genial para proyectos de confianza, pero ten cuidado con código no confiable.

### Sesión

| Comando | Qué hace |
|---------|--------------|
| `/clear` | Abandona la sesión actual (no se guarda el historial) y comienza una conversación nueva |
| `/compact` | Resumir la conversación para reducir el uso de contexto (opcionalmente agrega instrucciones de enfoque, p. ej. `/compact focus on the bug list`) |
| `/context` | Mostrar el uso de tokens de la ventana de contexto y su visualización |
| `/keep-alive` | Evita que tu sistema entre en suspensión mientras Copilot CLI está activo — útil para tareas de larga duración en un portátil |
| `/memory [on\|off\|show]` | Habilitar, deshabilitar o ver la memoria persistente — hechos y preferencias recordados entre todas las sesiones |
| `/new` | Finaliza la sesión actual (guardándola en el historial para búsqueda/reanudación) y comienza una conversación nueva. |
| `/resume` | Cambiar a otra sesión (opcionalmente especifica el ID o nombre de la sesión) |
| `/rename` | Renombrar la sesión actual (omitir el nombre para generarlo automáticamente) |
| `/rewind` | Abrir un selector de línea temporal para retroceder a cualquier punto anterior de la conversación |
| `/usage` | Mostrar métricas y estadísticas de uso de la sesión, incluidas barras de progreso de cuota |
| `/session` | Mostrar información de la sesión y resumen del espacio de trabajo; usa `/session delete`, `/session delete <id>`, o `/session delete-all` para eliminar sesiones |
| `/share` | Exportar la sesión como archivo markdown, gist de GitHub o archivo HTML autocontenido |
| `/every <interval> <prompt>` | Programar un prompt para ejecutarse en intervalos recurrentes (p. ej., `/every 1h summarize new commits`). Usa lenguaje natural para el intervalo. `/loop` es un alias de `/every`. |
| `/after <time> <prompt>` | Programar un prompt para ejecutarse una vez después de un retraso (p. ej., `/after 30m run tests`). Usa lenguaje natural para el tiempo. |

### Visualización

| Comando | Qué hace |
|---------|--------------|
| `/statusline` (or `/footer`) | Personalizar qué elementos aparecen en la barra de estado en la parte inferior de la sesión (directorio, rama, esfuerzo, ventana de contexto, cuota) |
| `/theme` | Ver o establecer el tema del terminal |
| `/voice` | Dicta tu prompt usando reconocimiento de voz local — habla de forma natural en lugar de escribir |

### Ayuda y comentarios

| Comando | Qué hace |
|---------|--------------|
| `/app` | Abrir la aplicación de GitHub (o fallback en el navegador) directamente desde la CLI |
| `/changelog` | Mostrar el registro de cambios de las versiones de la CLI |
| `/feedback` | Enviar comentarios a GitHub |
| `/help` | Mostrar todos los comandos disponibles |

### Comandos rápidos de shell

Ejecuta comandos de shell directamente sin IA anteponiendo `!`:

```bash
copilot

> !git status
# Ejecuta git status directamente, omitiendo la IA

> !python -m pytest tests/
# Ejecuta pytest directamente
```

### Cambio de modelos

Copilot CLI es compatible con múltiples modelos de IA de OpenAI, Anthropic, Google y otros. Los modelos disponibles para ti dependen de tu nivel de suscripción y región. Usa `/model` para ver tus opciones y cambiar entre ellos:

```bash
copilot
> /model

# Muestra los modelos disponibles y te permite elegir uno. Selecciona Sonnet 4.5.
```

> 💡 **Consejo**: Algunos modelos consumen más «premium requests» que otros. Los modelos marcados **1x** (como Claude Sonnet 4.5) son una buena opción por defecto. Son capaces y eficientes. Los modelos con multiplicadores más altos usan tu cuota de solicitudes premium más rápido, así que guárdalos para cuando realmente los necesites.

> 💡 **¿No estás seguro de qué modelo elegir?** Selecciona **`Auto`** en el selector de modelos para permitir que Copilot elija automáticamente el mejor modelo disponible para cada sesión. Es una excelente opción por defecto si recién empiezas y no quieres preocuparte por la selección de modelos.

> 💡 **Atajos por familia de modelos**: También puedes escribir un alias corto de familia — como `opus`, `sonnet`, `haiku`, `gpt` o `gemini` — directamente en el selector `/model` en lugar de desplazarte por la lista completa. Copilot elegirá el mejor modelo disponible de esa familia para ti.

</details>

---

# Práctica

<img src="../../../assets/practice.png" alt="Configuración de escritorio acogedora con monitor mostrando código, lámpara, taza de café y auriculares listos para la práctica" width="800"/>

Es hora de poner en práctica lo que has aprendido.

---

## ▶️ Pruébalo tú mismo

### Exploración interactiva

Inicia Copilot y usa prompts de seguimiento para mejorar iterativamente la aplicación de libros:

```bash
copilot

> Review @samples/book-app-project/book_app.py - what could be improved?

> Refactor the if/elif chain into a more maintainable structure

> Add type hints to all the handler functions

> /exit
```

### Planificar una función

Usa `/plan` para que Copilot CLI trace una implementación antes de escribir código:

```bash
copilot

> /plan Add a search feature to the book app that can find books by title or author

# Revisar el plan
# Aprobar o modificar
# Ver cómo se implementa paso a paso
```

### Automatizar con el modo programático

La bandera `-p` te permite ejecutar Copilot CLI directamente desde tu terminal sin entrar en modo interactivo. Copia y pega el siguiente script en tu terminal (no dentro de Copilot) desde la raíz del repositorio para revisar todos los archivos Python en la aplicación de libros.

```bash
# Revisar todos los archivos Python en la aplicación del libro
for file in samples/book-app-project/*.py; do
  echo "Reviewing $file..."
  copilot --allow-all -p "Quick code quality review of @$file - critical issues only"
done
```

**PowerShell (Windows):**

```powershell
# Revisar todos los archivos Python en la aplicación de libros
Get-ChildItem samples/book-app-project/*.py | ForEach-Object {
  $relativePath = "samples/book-app-project/$($_.Name)";
  Write-Host "Reviewing $relativePath...";
  copilot --allow-all -p "Quick code quality review of @$relativePath - critical issues only" 
}
```

---

Después de completar las demostraciones, prueba estas variaciones:

1. **Desafío interactivo**: Inicia `copilot` y explora la aplicación de libros. Pregunta sobre `@samples/book-app-project/books.py` y solicita mejoras 3 veces seguidas.

2. **Desafío en modo Plan**: Ejecuta `/plan Add rating and review features to the book app`. Lee el plan cuidadosamente. ¿Tiene sentido?

3. **Desafío programático**: Ejecuta `copilot --allow-all -p "List all functions in @samples/book-app-project/book_app.py and describe what each does"`. ¿Funcionó en el primer intento?

---

## 💡 Consejo: Controla tu sesión de CLI desde la web o el móvil

GitHub Copilot CLI admite **sesiones remotas**, lo que te permite monitorizar e interactuar con una sesión CLI en ejecución desde un navegador web (en escritorio o móvil) o la app GitHub Mobile sin estar físicamente en tu terminal.

Inicia una sesión remota con la bandera `--remote`:

```bash
copilot --remote
```

Copilot CLI mostrará un enlace y proporcionará acceso a un código QR. Abre el enlace en tu teléfono o en una pestaña del navegador de escritorio para ver la sesión en tiempo real, enviar prompts de seguimiento, revisar planes y dirigir el agente de forma remota. Las sesiones son específicas del usuario, por lo que solo puedes acceder a tus propias sesiones de Copilot CLI.

También puedes habilitar el acceso remoto desde dentro de una sesión activa en cualquier momento:

```
> /remote
```

Se pueden encontrar detalles adicionales sobre sesiones remotas en la [documentación de Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-cli/steer-remotely).

---

## 📝 Tarea

### Desafío principal: Mejorar las utilidades de la aplicación de libros

Los ejemplos prácticos se centraron en revisar y refactorizar `book_app.py`. Ahora practica las mismas habilidades en un archivo diferente, `utils.py`:

1. Inicia una sesión interactiva: `copilot`
2. Pídele a Copilot CLI que resuma el archivo: "Summarize @samples/book-app-project/utils.py and explain what each function in this file does"
3. Pídele que añada validación de entrada: "Add validation to `get_user_choice()` so it handles empty input and non-numeric entries"
4. Pídele que mejore el manejo de errores: "What happens if `get_book_details()` receives an empty string for the title? Add guards for that."
5. Pídele un docstring: "Add a comprehensive docstring to `get_book_details()` with parameter descriptions and return values"
6. Observa cómo el contexto se mantiene entre prompts. Cada mejora se construye sobre la anterior
7. Sal con `/exit`

**Criterios de éxito**: Deberías tener un `utils.py` mejorado con validación de entrada, manejo de errores y un docstring, todo construido mediante una conversación de múltiples turnos.

<details>
<summary>💡 Sugerencias (haz clic para expandir)</summary>

**Prompts de ejemplo para probar:** 
```bash
> @samples/book-app-project/utils.py What does each function in this file do?
> Add validation to get_user_choice() so it handles empty input and non-numeric entries
> What happens if get_book_details() receives an empty string for the title? Add guards for that.
> Add a comprehensive docstring to get_book_details() with parameter descriptions and return values
```

**Problemas comunes:**
- Si Copilot CLI hace preguntas aclaratorias, respóndelas de forma natural
- El contexto se mantiene, por lo que cada prompt se basa en el anterior
- Usa `/clear` si quieres empezar de nuevo

</details>

### Desafío adicional: Compara los modos

Los ejemplos usaron `/plan` para una función de búsqueda y `-p` para revisiones por lotes. Ahora prueba los tres modos en una sola nueva tarea: agregar un método `list_by_year()` a la clase `BookCollection`:

1. **Interactivo**: `copilot` → pídele que diseñe y construya el método paso a paso
2. **Plan**: `/plan Add a list_by_year(start, end) method to BookCollection that filters books by publication year range`
3. **Programático**: `copilot --allow-all -p "@samples/book-app-project/books.py Add a list_by_year(start, end) method that returns books published between start and end year inclusive"`

**Reflexión**: ¿Qué modo resultó más natural? ¿Cuándo usarías cada uno?

---

<details>
<summary>🔧 <strong>Errores comunes y solución de problemas</strong> (haz clic para expandir)</summary>

### Errores comunes

| Error | Qué ocurre | Solución |
|---------|--------------|-----|
| Escribir `exit` en lugar de `/exit` | Copilot CLI trata "exit" como un prompt, no como un comando | Los comandos con slash siempre empiezan con `/` |
| Usar `-p` para conversaciones de varios turnos | Cada llamada con `-p` está aislada y no tiene memoria de llamadas anteriores | Usa el modo interactivo (`copilot`) para conversaciones que se basan en el contexto |
| Olvidar las comillas alrededor de prompts con `$` o `!` | El shell interpreta caracteres especiales antes de que Copilot CLI los vea | Encierra los prompts entre comillas: `copilot -p "What does $HOME mean?"` |
| Presionar Esc una vez para cancelar una tarea en ejecución | Un solo Esc ya no cancela el trabajo en curso (para evitar accidentes) | Presiona **Esc dos veces** para cancelar mientras Copilot CLI está procesando |

### Solución de problemas

**"Modelo no disponible"** - Tu suscripción puede no incluir todos los modelos. Usa `/model` para ver lo que está disponible.

**"Contexto demasiado largo"** - Tu conversación ha usado toda la ventana de contexto. Usa `/clear` para restablecer, o inicia una nueva sesión.

**"Límite de tasa excedido"** - Espera unos minutos y vuelve a intentarlo. Considera usar el modo programático para operaciones por lotes con retardos.

</details>

---

# Resumen

## 🔑 Puntos clave


1. **modo interactivo** es para exploración e iteración - el contexto se conserva. Es como mantener una conversación con alguien que recuerda lo que has dicho hasta ese momento.
2. **modo de planificación** es normalmente para tareas más complejas. Revisa antes de implementarlo.
3. **modo programático** es para automatización. No se necesita interacción.
4. **Comandos esenciales** (`/ask`, `/help`, `/clear`, `/plan`, `/research`, `/model`, `/exit`) cubren la mayoría del uso diario.

> 📋 **Referencia rápida**: Consulta la [referencia de comandos de GitHub Copilot CLI](https://docs.github.com/en/copilot/reference/cli-command-reference) para una lista completa de comandos y atajos.

---

## ➡️ ¿Qué sigue?

Ahora que entiendes los tres modos, aprendamos cómo darle a Copilot CLI contexto sobre tu código.

En **[Capítulo 02: Contexto y conversaciones](../02-context-conversations/README.md)**, aprenderás:

- La sintaxis `@` para referenciar archivos y directorios
- La gestión de sesiones con `--resume` y `--continue`
- Cómo la gestión del contexto hace que Copilot CLI sea realmente potente

---

**[← Volver al inicio del curso](../README.md)** | **[Continuar al Capítulo 02 →](../02-context-conversations/README.md)**

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->