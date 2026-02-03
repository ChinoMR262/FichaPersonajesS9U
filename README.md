# S9U HELIOS ENGINE DATA v8 🌌

**Motor de Creación y Análisis Psicológico de Personajes para el Universo S9U**

## 📖 Descripción del Proyecto
**S9U Helios Engine** es una herramienta web interactiva diseñada para la creación, gestión y análisis profundo de personajes dentro del lore de *"Seres del Noveno Universo"* (S9U). Combina una interfaz retro-futurista con lógica de análisis local y la potencia de la Inteligencia Artificial (Google Gemini) para generar perfiles psicológicos, morales y narrativos detallados.

## ✨ Características Principales

### 🛠️ Creación de Personajes
- **Base de Datos de Lore**: Selección automática de Universos (U1-U21), Planetas, Razas y Rangos Jerárquicos.
- **Validación en Tiempo Real**: Sistema de progreso que asegura la coherencia del perfil (relaciones, hobbies, rasgos).
- **Personalización Visual**: Configuración detallada de apariencia (cabello, ojos, vestimenta, armas).
- **Animales Divinos**: Selección de compañíeros espirituales con efectos sonoros.

### 🧠 Inteligencia Artificial (Helios AI)
- **Análisis Profundo**: Utiliza la API de **Google Gemini 2.0 Flash** para generar un perfil psicológico complejo basado en los datos ingresados.
- **Modo Villano**: Detecta roles antagónicos y adapta el análisis hacia un perfil oscuro, estratégico y dominante.
- **Sugerencias Inteligentes**: Generación automática de Hobbies, Rasgos y deseos profundos coherentes con el rol y universo.

### ⚡ Motor Local (Fallback)
- Funciona perfectamente sin conexión a internet o sin API Key.
- Genera historias y conclusiones morales basadas en patrones predefinidos y lógica interna del sistema.

### 🖥️ Interfaz & Experiencia
- **Estilo Terminal**: Efectos de escritura tipo máquina ("typewriter"), sonidos de interfaz y animaciones CRT.
- **Panel de Configuración**: Control de audio (Música/SFX), modo de voz (Auto-Speak) y gestión de API Key.
- **Exportación PDF**: Genera una ficha técnica profesional del personaje lista para descargar.

---

## 🚀 Instalación y Uso

1. **Descargar**: Clona este repositorio o descarga los archivos `index.html` y `helios_data.js`.
2. **Ejecutar**: Abre el archivo `index.html` en cualquier navegador web moderno (Chrome, Edge, Firefox).
3. **Splash Screen**: Haz clic en la pantalla inicial para iniciar el sistema y cargar los módulos de audio.

### Configuración de la IA (Opcional)
Para habilitar el análisis avanzado con Helios AI:
1. Abre el panel de configuración (icono de engranaje).
2. Pega tu **Google Gemini API Key** en el campo "Clave API Gemini".
   - *Nota: La clave se almacena solo en la memoria temporal del navegador por seguridad. No se guarda en `localStorage`.*
3. El indicador cambiará a "Clave configurada" y podrás usar las funciones de "Generar con IA".

---

## 📂 Estructura del Proyecto

- `index.html`: Núcleo de la aplicación. Contiene la estructura DOM, estilos CSS y lógica principal JS.
- `helios_data.js`: Base de datos del lore (Universos, Razas, Rangos, Descripciones).
- `README.MD`: Documentación oficial.

---

## 🔒 Seguridad
- **Cero Persistencia de Credenciales**: Las claves API nunca se guardan en cookies ni almacenamiento local.
- **Validación de Entradas**: El sistema sanea las entradas de texto para prevenir inyecciones básicas.

---

## © Créditos y Licencia
**S9U Helios Engine v8.0**
- **Creador y Autor Original**: Jonathan Gabriel Nieto.
- **Derechos**: Todos los derechos reservados sobre el universo narrativo, mitología y personajes de S9U.
- **Año**: 2026.

> *"La autenticidad de S9U reside en la visión única de su autor original, quien posee la titularidad exclusiva sobre este legado literario."*
