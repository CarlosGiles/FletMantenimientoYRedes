![portadatech](https://github.com/user-attachments/assets/70b9f5d1-36c1-47c8-84aa-0c22263297c4)

[LinkedIn](https://www.linkedin.com/in/carlosgilesing/)

# FletMantenimientoYRedes

Aplicación de escritorio desarrollada con [Flet](https://docs.flet.dev/) en Python, diseñada para **automatizar tareas de mantenimiento y configuración de red en Windows**. Provee una **interfaz gráfica** sencilla para:

- Eliminar archivos temporales
- Configurar IP dinámica por DHCP
- Asignar IP estática (hogar u oficina)
- Vaciar la papelera de reciclaje

Todo ello usando comandos nativos de Windows (`netsh`, `ipconfig`, PowerShell, etc.).

---

## Tabla de Contenido

1. [Requisitos y dependencias](#️-requisitos-y-dependencias)  
2. [Estructura de archivos](#-estructura-de-archivos)  
3. [Cómo clonar y ejecutar el proyecto](#-cómo-clonar-y-ejecutar-el-proyecto)  
4. [Uso de la aplicación](#️-uso-de-la-aplicación)  
5. [Empaquetar la app (opcional)](#-empaquetar-la-app-opcional)  
6. [Run the app](#run-the-app)  
7. [Referencias técnicas](#-referencias-técnicas)
8. [Consideraciones finales](#consideraciones-finales)
8. [Licencia](#-licencia)

---

## ⚙️ Requisitos y dependencias

1. **Python 3.9+** (recomendado) instalado en el sistema.
2. **Biblioteca Flet**: Para la interfaz gráfica.
3. **Sistema operativo Windows** con acceso a:
   - `netsh` (para configurar la red)
   - `ipconfig` (para liberar y renovar IP)
   - `powershell` (para vaciar la papelera)

---

## 📂 Estructura de archivos

```
FletMantenimientoYRedes/
│
├─ src/
│  ├─ mantenimiento.py     # Lógica de mantenimiento (elimina temp, asigna IP, etc.)
│  ├─ interfaz.py          # Interfaz Flet (UI)
│  ├─ main.py              # Punto de entrada (ejecuta la app)
│  └─ assets/
│       └─ tech.png        # Imagen usada en la UI
│
├─ README.md               # Este archivo
├─ .gitignore              # Ignora env, __pycache__, etc.
└─ ...
```

---

## 🚀 Cómo clonar y ejecutar el proyecto

1. **Clonar este repositorio**:
   ```bash
   git clone https://github.com/CarlosGiles/FletMantenimientoYRedes.git
   cd FletMantenimientoYRedes
   ```
2. **Crear y/o activar un entorno virtual** (opcional pero recomendado):
   ```bash
   python -m venv env
   source env/bin/activate  # En Linux/Mac
   # o en Windows:
   .\env\Scripts\activate
   ```
3. **Instalar dependencias**:
   ```bash
   pip install flet
   ```
4. **Ejecutar la aplicación**:
   ```bash
   python src/main.py
   ```
5. Se abrirá una **ventana de escritorio** en modo oscuro con todas las opciones de mantenimiento.

> **Nota**: Si en vez de la ventana nativa te abre el navegador, asegúrate de estar ejecutando `python src/main.py` y no `flet run`. De esta forma se fuerza el modo de escritorio.

---

## 🖥️ Uso de la aplicación

Una vez iniciada, verás el menú principal con botones para:

1. **Eliminar archivos temporales (C:\Windows\Temp)**
2. **Eliminar archivos temporales locales (%LOCALAPPDATA%\Temp)**
3. **Configurar IP dinámica (DHCP)**
4. **Asignar IP estática - Hogar** (192.168.1.200)
5. **Asignar IP estática - Oficina** (192.168.100.200)
6. **Vaciar Papelera de reciclaje**

Al presionar cada botón, la aplicación ejecuta la acción en un **hilo de fondo**, para que la interfaz no se congele. El resultado se muestra en la parte inferior (texto de `resultado_text`).

---

## 📦 Empaquetar la app (opcional)

Si deseas **distribuir** la aplicación sin requerir que los usuarios instalen Python y Flet manualmente, puedes:

### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).

---

## Run the app

### uv

Run as a desktop app:

```
uv run flet run
```

Run as a web app:

```
uv run flet run --web
```

### Poetry

Install dependencies from `pyproject.toml`:

```
poetry install
```

Run as a desktop app:

```
poetry run flet run
```

Run as a web app:

```
poetry run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/getting-started/).

---

## 🔧 Referencias técnicas

- **Flet**: [Documentación oficial](https://docs.flet.dev/)
- **netsh**: [Documentación Microsoft](https://docs.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh)
- **ipconfig**: Para liberar y renovar direcciones IP.
- **PowerShell**: Para vaciar la papelera (`Clear-RecycleBin`).

---

## Consideraciones Finales
- **Rutas Largas en Windows**: Al compilar, ten en cuenta activar el Modo Desarrollador y minimizar la profundidad de las rutas.
- **Dependencias**: Asegúrate de incluir en el `pyproject.toml` cada librería externa (p. ej. `yt_dlp`) para que se empaquete correctamente.
- **Escalabilidad**: Dado que Flet usa `Flutter` por debajo, se pueden añadir animaciones, más UI, y adaptarlo a web, escritorio, y móvil.

---

## 📝 Licencia

>MIT License
Copyright (c) 2025 Carlos Giles
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

**¡Gracias por usar FletMantenimientoYRedes!**

Siéntete libre de hacer *fork*, proponer cambios o mejoras en *pull requests*.  

