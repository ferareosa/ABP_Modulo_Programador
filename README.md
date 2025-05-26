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
3. **Venta**
4. **Pasajero**
5. **Detalle de Venta**

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

#### 3. Venta

- `id_venta` (Texto) → **Clave primaria**
- `cuit_cliente` (Texto) → **Clave foránea a Cliente**
- `fecha_venta` (Fecha)

#### 4. Pasajero

- `dni` (Texto) → **Clave primaria**
- `nombre` (Texto)
- `apellido` (Texto)

#### 5. Detalle de Venta

- `id_detalle` (Texto) → **Clave primaria**
- `id_venta` (Texto) → **Clave foránea a Venta**
- `dni_pasajero` (Texto) → **Clave foránea a Pasajero**
- `id_destino` (Texto) → **Clave foránea a Destino**

---

### 🔗 Relaciones entre Entidades

- **Cliente** 🧍‍♂️ 🔁 **Venta**

  - Relación: **Uno a Muchos**
  - Un cliente puede tener muchas ventas, pero una venta pertenece a un solo cliente.

- **Venta** 🧾 🔁 **Detalle de Venta**

  - Relación: **Uno a Muchos**
  - Cada venta puede tener múltiples detalles (pasajes vendidos).

- **Detalle de Venta** 🔁 **Destino**

  - Relación: **Muchos a Uno**
  - Cada pasaje (detalle de venta) está asociado a un único destino.

- **Detalle de Venta** 🔁 **Pasajero**
  - Relación: **Muchos a Uno**
  - Cada pasaje corresponde a un único pasajero, pero un pasajero puede tener múltiples pasajes.

---

### 🔑 Claves Primarias y Foráneas

| Entidad          | Clave Primaria | Claves Foráneas                                                                                                |
| ---------------- | -------------- | -------------------------------------------------------------------------------------------------------------- |
| Cliente          | `cuit`         | —                                                                                                              |
| Destino          | `id_destino`   | —                                                                                                              |
| Venta            | `id_venta`     | `cuit_cliente` → Cliente(`cuit`)                                                                               |
| Pasajero         | `dni`          | —                                                                                                              |
| Detalle de Venta | `id_detalle`   | `id_venta` → Venta(`id_venta`) <br> `dni_pasajero` → Pasajero(`dni`) <br> `id_destino` → Destino(`id_destino`) |

---

## 📂 Diagrama Entidad–Relación

> A continuación se presenta el modelo E/R utilizado en el desarrollo del sistema:

<img src="./assets/SkyRoute.drawio.svg" alt="Diagrama Entidad-Relación" style="max-width: 100%;">

## 📌 Notas

Este proyecto corresponde al desarrollo integrador del módulo **Programador** en la **Tecnicatura Superior en Ciencias de Datos e Inteligencia Artificial** (ISPC – 2025).
