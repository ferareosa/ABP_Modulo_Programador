# 🧠 Tecnicatura Superior en Ciencias de Datos e Inteligencia Artificial

### 💻 Módulo Programador – Cohorte 2025

---

## 👥 Integrantes del Grupo

- **Annone, Ariel Gastón** – DNI: 29.449.852
- **Areosa, Fernando** – DNI: 36.131.545
- **Krenz, Catalina** – DNI: 35.964.865
- **Muñoz Brizuela, Fátima Belén** – DNI: 39.824.821
- **Varela, Mario** – DNI: 31.401.019

---

## ⚙️ Instrucciones de Uso

1. Clonar o descargar este repositorio.

2. Instalar las dependencias necesarias ejecutando el siguiente comando en la terminal:

   ```bash
   pip install .
   ```

3. Ejecutar el programa principal:

   ```bash
   python main.py
   ```

---

## ✅ Requisitos

- Python 3.10 o superior
- `pip` instalado
- Sistema operativo compatible (Windows, Linux o macOS)

---

## 🧱 Modelo de Datos – Sistema de Gestión de Pasajes

### 🔹 Entidades Principales

1. **Cliente**
2. **Destino**
3. **Pasaje**

---

### 🧾 Atributos y Tipos de Datos

#### 1. Cliente

- `cuit` (Texto) → **Clave primaria**
- `razon_social` (Texto)
- `email` (Texto)

#### 2. Destino

- `id_destino` (Texto) → **Clave primaria**
- `ciudad` (Texto)
- `pais` (Texto)
- `costo_base` (Número decimal)
- `disponible` (Booleano)

#### 3. Pasaje

- `id_venta` (Texto) → **Clave primaria**
- `cuit` (Texto) → **Clave foránea a Cliente**
- `id_destino` (Texto) → **Clave foránea a Destino**
- `fecha_venta` (Texto)
- `estado` (Booleano)
- `costo_total` (Número decimal)

---

### 🔗 Relaciones entre Entidades

- **Cliente** 🧍‍♂️ 🔁 **Pasaje**

  - Relación: **Uno a Muchos**
  - Un cliente puede tener muchos pasajes, pero un pasaje pertenece a un solo cliente.

- **Destino** 🔁🧾 **Pasaje**

  - Relación: **Uno a Muchos**
  - Un Destino puede tener muchos pasajes asociados, pero un pasaje pertenece a un solo Destino.

---

### 🔑 Claves Primarias y Foráneas

| Entidad | Clave Primaria | Claves Foráneas                                                    |
| ------- | -------------- | ------------------------------------------------------------------ |
| Cliente | `cuit`         | —                                                                  |
| Destino | `id_destino`   | —                                                                  |
| Pasaje  | `id_venta`     | `cuit` → Cliente(`cuit`) <br> `id_destino` → Destino(`id_destino`) |

---

## 📂 Diagrama Entidad–Relación

> A continuación se presenta el modelo E/R utilizado en el desarrollo del sistema:

<img src="./assets/SkyRoute.drawio.svg" alt="Diagrama Entidad-Relación" style="max-width: 100%;">

---

# 🧑‍💻 Aspectos Legales del Proyecto

> 📚 Este proyecto fue desarrollado en un contexto educativo, pero contempla consideraciones legales reales para fomentar el aprendizaje profesional.

---

## ⚖️ 1. ¿Qué figura legal tendrá el grupo?

Nuestro grupo está formado por estudiantes, por lo tanto **no contamos con una figura legal formal** como empresa o sociedad.  
En un escenario real, lo ideal sería:

- 📌 Formarnos como una **sociedad de hecho**, o
- 📌 Inscribirnos como **monotributistas individuales**.

Esto permitiría trabajar formalmente, **firmar contratos**, **emitir facturas** y **asumir responsabilidades legales**.

---

## 🤝 2. Relación legal con SkyRoute S.R.L.

La relación con SkyRoute sería similar a una **contratación de servicios** y no a una relación laboral en dependencia.  
En un caso real, se debería:

- ✍️ Firmar un contrato que aclare que somos **prestadores independientes**.
- ✅ Dejar claros los derechos y obligaciones de ambas partes.

---

## 🔁 3. ¿Qué pasa si SkyRoute cambia de grupo?

Si SkyRoute decide contratar a otro grupo:

- 📦 Debemos **entregar todo el trabajo realizado** hasta ese momento.
- 🔐 **No conservar ni reutilizar datos personales ni código**.
- 🤝 Actuar con **profesionalismo y respeto por la confidencialidad** según la **Ley 25.326**.

---

## 📊 4. ¿De quién son los datos?

Los datos (clientes, ventas, etc.):

- Son **propiedad de las personas que los brindan** y de SkyRoute como titular del sistema.
- Nosotros **solo los organizamos técnicamente**.
- Debemos respetar su privacidad de acuerdo con la **Ley 25.326**.

---

## 💻 5. ¿De quién es el código desarrollado?

El código es propiedad del grupo que lo desarrolló **salvo que haya contrato de cesión**.

- 📜 Si no se firma un contrato, **los derechos son nuestros** como autores.
- 🧠 Esto está respaldado por la **Ley de Propiedad Intelectual (Ley 11.723)**.

---

## 🛑 6. Botón de Arrepentimiento

Este botón permite a los usuarios **cancelar una compra dentro de los 60 días hábiles**.  
Es una herramienta que protege al consumidor según la:

- 🛡️ **Ley de Defensa del Consumidor (Ley 24.240)**.
- Obligatoria en **todas las plataformas de venta online**.

---

## 🧾 7. Fundamentación legal de cada punto

| Tema                        | Ley Aplicable              | Detalle Clave                                                     |
| --------------------------- | -------------------------- | ----------------------------------------------------------------- |
| Relación laboral            | Código Civil y Comercial   | Si no hay contrato laboral, somos prestadores independientes.     |
| Cambio de grupo             | Ley 25.326                 | Prohíbe el uso indebido o la retención de datos personales.       |
| Propiedad de los datos      | Ley 25.326                 | Los datos son de quienes los brindan, no de quienes los procesan. |
| Propiedad del código fuente | Ley 11.723                 | El software es propiedad de su autor, salvo acuerdo de cesión.    |
| Botón de arrepentimiento    | Ley 24.240                 | Derecho a cancelar compras digitales.                             |
| Otros aspectos clave        | Ley 27.590, 25.506, 26.388 | Grooming, firma digital y delitos informáticos.                   |

---

## 📌 Consideraciones Finales

Aunque este proyecto es parte de una práctica académica, **nos esforzamos por aplicar criterios legales reales** para:

- 🧠 Formar criterios profesionales.
- 🛠️ Trabajar con responsabilidad.
- 📃 Incorporar buenas prácticas desde el comienzo.

---

## 📌 Notas

Este proyecto corresponde al desarrollo integrador del módulo **Programador** en la **Tecnicatura Superior en Ciencias de Datos e Inteligencia Artificial** (ISPC – 2025).
