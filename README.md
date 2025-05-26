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

## 📌 Notas

Este proyecto corresponde al desarrollo integrador del módulo **Programador** en la **Tecnicatura Superior en Ciencias de Datos e Inteligencia Artificial** (ISPC – 2025).
