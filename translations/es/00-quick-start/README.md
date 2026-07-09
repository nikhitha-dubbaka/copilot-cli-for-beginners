<!--
---
id: CopilotCLI-00
title: !translate Quick Start
description: !translate Install GitHub Copilot CLI, sign in with your GitHub account, and verify that everything works.
audience: Developers / Students / Terminal users
slug: quick-start
weight: 1
---
-->

![Capítulo 00: Inicio rápido](../../../00-quick-start/assets/chapter-header.png)

¡Bienvenido! En este capítulo, instalarás GitHub Copilot CLI (Interfaz de Línea de Comandos), iniciarás sesión con tu cuenta de GitHub y verificarás que todo funciona. Este es un capítulo de configuración rápida. ¡Una vez que estés en funcionamiento, las demostraciones reales comienzan en el Capítulo 01!

## 🎯 Learning Objectives

Al final de este capítulo, habrás:

- Instalado GitHub Copilot CLI
- Iniciado sesión con tu cuenta de GitHub
- Verificado que funciona con una prueba simple

> ⏱️ **Tiempo estimado**: ~10 minutos (5 min lectura + 5 min práctica)

---

## ✅ Prerequisites

- **Cuenta de GitHub** con acceso a Copilot. [Ver opciones de suscripción](https://github.com/features/copilot/plans). Estudiantes/Profesores pueden acceder a Copilot Pro [gratis a través de GitHub Education](https://education.github.com/pack).
- **Conceptos básicos de la terminal**: Familiaridad con comandos como `cd` y `ls`

### Qué "Acceso a Copilot" Significa

GitHub Copilot CLI requiere una suscripción activa a Copilot. Puedes verificar tu estado en [github.com/settings/copilot](https://github.com/settings/copilot). Deberías ver una de las siguientes:

- **Copilot Individual** - Suscripción personal
- **Copilot Business** - A través de tu organización
- **Copilot Enterprise** - A través de tu empresa
- **GitHub Education** - Gratis para estudiantes/profesores verificados

Si ves "You don't have access to GitHub Copilot", necesitarás usar la opción gratuita, suscribirte a un plan o unirte a una organización que proporcione acceso.

---

## Installation

> ⏱️ **Tiempo estimado**: La instalación toma 2-5 minutos. La autenticación añade otros 1-2 minutos.

### GitHub Codespaces (Zero Setup)

Si no quieres instalar ninguno de los requisitos previos, puedes usar GitHub Codespaces, que tiene GitHub Copilot CLI listo para usar (necesitarás iniciar sesión) y preinstala Python y pytest.

1. [Haz un fork de este repositorio](https://github.com/github/copilot-cli-for-beginners/fork) a tu cuenta de GitHub
2. Selecciona **Code** > **Codespaces** > **Create codespace on main**
3. Espera unos minutos a que el contenedor se construya
4. ¡Estás listo! La terminal se abrirá automáticamente en el entorno de Codespace.

> 💡 **Verificar en Codespace**: Ejecuta `cd samples/book-app-project && python book_app.py help` para confirmar que Python y la aplicación de muestra funcionan.

### Local Installation

Sigue estos pasos si quieres ejecutar Copilot CLI en tu máquina local con las muestras del curso.

1. Clona el repositorio para obtener las muestras del curso en tu máquina:

    ```bash
    git clone https://github.com/github/copilot-cli-for-beginners
    cd copilot-cli-for-beginners
    ```

2. Instala Copilot CLI usando una de las siguientes opciones.

    > 💡 **¿No sabes cuál elegir?** Usa `npm` si tienes Node.js instalado. De lo contrario, elige la opción que coincida con tu sistema.

    ### Todas las plataformas (npm)

    ```bash
    # Si tienes Node.js instalado, esta es una forma rápida de obtener la CLI
    npm install -g @github/copilot
    ```

    ### macOS/Linux (Homebrew)

    ```bash
    brew install copilot-cli
    ```

    ### Windows (WinGet)

    ```bash
    winget install GitHub.Copilot
    ```

    ### macOS/Linux (Script de instalación)

    ```bash
    curl -fsSL https://gh.io/copilot-install | bash
    ```

<details>
<summary>Opcional: Habilitar autocompletado con Tab en el shell</summary>

El autocompletado con Tab en el shell te permite presionar **Tab** para completar subcomandos de `copilot`, opciones de comando y algunos valores de opciones. Es opcional, pero puede resultar útil una vez que te sientas cómodo usando la CLI.

Copilot CLI actualmente admite scripts de autocompletado para Bash, Zsh y Fish:

```shell
# Bash, solo para la sesión actual
source <(copilot completion bash)

# Bash, persistente en Linux
copilot completion bash | sudo tee /etc/bash_completion.d/copilot

# Zsh
copilot completion zsh > "${fpath[1]}/_copilot"

# Fish
copilot completion fish > ~/.config/fish/completions/copilot.fish
```

Reinicia tu shell después de añadir el autocompletado persistente. PowerShell es compatible para ejecutar Copilot CLI en Windows, pero `copilot completion` actualmente solo admite Bash, Zsh y Fish.

</details>

---

## Authentication

Abre una ventana de terminal en la raíz del repositorio `copilot-cli-for-beginners`, inicia la CLI y permite el acceso a la carpeta.

```bash
copilot
```

Se te pedirá que confíes en la carpeta que contiene el repositorio (si no lo has hecho ya). Puedes confiar una vez o en todas las sesiones futuras.

<img src="../../../00-quick-start/assets/copilot-trust.png" alt="Confiar en archivos de una carpeta con Copilot CLI" width="800"/>

Después de confiar en la carpeta, puedes iniciar sesión con tu cuenta de GitHub.

```
> /login
```

**Qué sucede a continuación:**

1. Copilot CLI muestra un código de un solo uso (como `ABCD-1234`)
2. Tu navegador se abrirá en la página de autorización de dispositivo de GitHub. Inicia sesión en GitHub si no lo has hecho ya.
3. Introduce el código cuando se te solicite
4. Selecciona "Autorizar" para otorgar acceso a GitHub Copilot CLI
5. Vuelve a tu terminal - ¡ahora has iniciado sesión!

<img src="../../../00-quick-start/assets/auth-device-flow.png" alt="Flujo de autorización del dispositivo - mostrando el proceso de 5 pasos desde el inicio de sesión en la terminal hasta la confirmación" width="800"/>

*El flujo de autorización del dispositivo: tu terminal genera un código, lo verificas en el navegador y Copilot CLI queda autenticado.*

**Consejo**: El inicio de sesión persiste entre sesiones. Solo necesitas hacerlo una vez a menos que tu token caduque o cierres la sesión explícitamente.

---

## Verify It Works

### Step 1: Test Copilot CLI

Ahora que has iniciado sesión, verifiquemos que Copilot CLI funciona para ti. En la terminal, inicia la CLI si no lo has hecho ya:

```bash
> Say hello and tell me what you can help with
```

Después de recibir una respuesta, puedes salir de la CLI:

```bash
> /exit
```

---

<details>
<summary>🎬 ¡Míralo en acción!</summary>

![Demostración 'Hello'](../../../00-quick-start/assets/hello-demo.gif)

*La salida de la demostración puede variar. Tu modelo, herramientas y respuestas serán diferentes de lo mostrado aquí.*

</details>

---

**Salida esperada**: Una respuesta amigable que enumera las capacidades de Copilot CLI.

### Step 2: Run the Sample Book App

El curso proporciona una aplicación de ejemplo que explorarás y mejorarás a lo largo del curso usando la CLI *(Puedes ver el código de esto en /samples/book-app-project)*. Verifica que la *aplicación de terminal de colección de libros en Python* funcione antes de comenzar. Ejecuta `python` o `python3` dependiendo de tu sistema.

> **Nota:** Los ejemplos principales mostrados a lo largo del curso usan Python (`samples/book-app-project`), por lo que necesitarás tener [Python 3.10+](https://www.python.org/downloads/) disponible en tu máquina local si eliges esa opción (el Codespace ya lo tiene instalado). También hay versiones en JavaScript (`samples/book-app-project-js`) y C# (`samples/book-app-project-cs`) si prefieres trabajar con esos lenguajes. Cada muestra tiene un README con instrucciones para ejecutar la aplicación en ese lenguaje.

```bash
cd samples/book-app-project
python book_app.py list
```

**Salida esperada**: Una lista de 5 libros que incluyen "The Hobbit", "1984" y "Dune".

### Step 3: Try Copilot CLI with the Book App

Primero vuelve a la raíz del repositorio (si ejecutaste el Paso 2):

```bash
cd ../..   # Volver a la raíz del repositorio si es necesario
copilot 
> What does @samples/book-app-project/book_app.py do?
```

**Salida esperada**: Un resumen de las funciones principales y comandos de la aplicación de libros.

Si ves un error, consulta la [sección de solución de problemas](#no-tienes-acceso-a-github-copilot) más abajo.

Una vez que termines puedes salir de Copilot CLI:

```bash
> /exit
```

---

## ✅ ¡Estás listo!

Eso es todo por la instalación. La diversión real comienza en el Capítulo 01, donde:

- Ver cómo la IA revisa la aplicación de libros y encuentra problemas de calidad de código al instante
- Aprender tres formas diferentes de usar Copilot CLI
- Generar código funcional a partir de instrucciones en inglés

**[Continuar al Capítulo 01: Primeros pasos →](../01-setup-and-first-steps/README.md)**

---

## Troubleshooting

### "copilot: command not found"

La CLI no está instalada. Prueba otro método de instalación:

```bash
# Si brew falló, intenta con npm:
npm install -g @github/copilot

# O el script de instalación:
curl -fsSL https://gh.io/copilot-install | bash
```

### "No tienes acceso a GitHub Copilot"

1. Verifica que tienes una suscripción a Copilot en [github.com/settings/copilot](https://github.com/settings/copilot)
2. Comprueba que tu organización permite el acceso a la CLI si usas una cuenta de trabajo

### "Autenticación fallida"

Vuelve a autenticarte:

```bash
copilot
> /login
```

### El navegador no se abre automáticamente

Visita manualmente [github.com/login/device](https://github.com/login/device) e introduce el código que se muestra en tu terminal.

### Token caducado

Simplemente ejecuta `/login` de nuevo:

```bash
copilot
> /login
```

### ¿Sigues atascado?

- Consulta la [documentación de GitHub Copilot CLI](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)
- Busca en [GitHub Issues](https://github.com/github/copilot-cli/issues)

---

## 🔑 Puntos clave

1. **Un GitHub Codespace es una forma rápida de comenzar** - Python, pytest y GitHub Copilot CLI vienen todos preinstalados para que puedas entrar directamente en las demostraciones
2. **Múltiples métodos de instalación** - Elige lo que funcione para tu sistema (Homebrew, WinGet, npm o script de instalación)
3. **Autenticación única** - El inicio de sesión persiste hasta que el token caduque
4. **La aplicación de libros funciona** - Usarás `samples/book-app-project` durante todo el curso

> 📚 **Documentación oficial**: [Instalar Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-cli/cli-getting-started) para opciones de instalación y requisitos.

> 📋 **Referencia rápida**: Consulta la [referencia de comandos de GitHub Copilot CLI](https://docs.github.com/en/copilot/reference/cli-command-reference) para una lista completa de comandos y atajos.

---

**[Continuar al Capítulo 01: Primeros pasos →](../01-setup-and-first-steps/README.md)**

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->