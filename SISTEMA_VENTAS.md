# 🛒 Sistema de Ventas - PetCare

## Descripción

Sistema completo de ventas y carrito de compras integrado al sistema PetCare. Permite la venta de productos con gestión automática de inventario, facturación y pagos.

## Características Principales

### 🏪 Catálogo de Productos
- Visualización de productos disponibles en formato de tarjetas
- Información detallada: nombre, descripción, precio y stock
- Indicador visual de disponibilidad
- Control de stock en tiempo real

### 🛒 Carrito de Compras
- Sistema de carrito basado en sesiones (sin necesidad de login)
- Agregar productos con cantidad personalizada
- Actualizar cantidades desde el carrito
- Eliminar productos individuales
- Vaciar carrito completo
- Validación automática de stock disponible
- Cálculo automático de subtotales y total

### 💳 Proceso de Pago (Checkout)
- Resumen detallado de la compra
- Selección de cliente (propietario)
- Múltiples métodos de pago:
  - Efectivo 💵
  - Tarjeta de Crédito 💳
  - Tarjeta de Débito 💳
  - Transferencia Bancaria 🏦
  - PayPal 💰

### 📄 Facturación Automática
- Generación automática de facturas con ID único
- Registro de pagos vinculado a facturas
- Actualización automática de inventario
- Reducción de stock al completar compra

### ✅ Confirmación de Compra
- Página de confirmación con detalles de la compra
- Información de factura generada
- Enlaces para seguir comprando o revisar facturas

## Estructura de URLs

```
/tienda/                              → Catálogo de productos
/carrito/                             → Ver carrito de compras
/carrito/agregar/<producto_id>/       → Agregar producto al carrito
/carrito/actualizar/<producto_id>/    → Actualizar cantidad
/carrito/eliminar/<producto_id>/      → Eliminar producto del carrito
/carrito/vaciar/                      → Vaciar todo el carrito
/checkout/                            → Proceso de pago
/procesar-pago/                       → Procesar la compra
/compra-exitosa/<id_factura>/         → Confirmación de compra
```

## Flujo de Compra

1. **Navegación al Catálogo**
   - Usuario accede a la tienda desde el menú o página principal
   - Visualiza productos con stock disponible

2. **Selección de Productos**
   - Selecciona cantidad deseada
   - Agrega productos al carrito
   - Sistema valida disponibilidad de stock

3. **Revisión del Carrito**
   - Usuario revisa productos seleccionados
   - Puede actualizar cantidades o eliminar productos
   - Ve el total a pagar

4. **Checkout**
   - Selecciona el cliente (propietario)
   - Elige método de pago
   - Revisa resumen de compra

5. **Procesamiento**
   - Sistema genera factura automáticamente
   - Crea registro de pago
   - Actualiza inventario (reduce stock)
   - Limpia el carrito

6. **Confirmación**
   - Usuario ve detalles de compra exitosa
   - Recibe número de factura
   - Puede continuar comprando o ver facturas

## Funcionalidades Técnicas

### Gestión de Sesiones
- El carrito se almacena en la sesión del navegador
- Persiste durante la navegación
- Se limpia al completar la compra

### Validaciones
- Stock disponible al agregar productos
- Verificación de stock al actualizar cantidades
- Validación de campos obligatorios en checkout
- Manejo de errores con mensajes informativos

### Actualización de Inventario
- Reducción automática de stock al procesar pago
- Sincronización con tabla de Productos
- Control de disponibilidad en tiempo real

### Integración con Sistema Existente
- Utiliza modelos existentes:
  - **Producto**: Catálogo y stock
  - **Factura**: Registro de ventas
  - **Pago**: Registro de transacciones
  - **Propietario**: Clientes

## Accesos al Sistema

### Desde el Sidebar
- 🛒 **Tienda / Ventas**: Acceso al catálogo
- 🛍️ **Ver Carrito**: Acceso directo al carrito

### Desde la Barra Superior
- Botón flotante del carrito con contador de productos

### Desde la Página Principal
- Sección destacada con accesos rápidos

## Ventajas del Sistema

✅ **Fácil de usar**: Interfaz intuitiva y moderna
✅ **Integrado**: Usa las tablas existentes de la base de datos
✅ **Automático**: Actualización automática de inventario
✅ **Completo**: Desde el catálogo hasta la facturación
✅ **Validado**: Control de stock y errores
✅ **Responsive**: Funciona en móviles y desktop
✅ **Visual**: Indicadores claros de stock y totales

## Ejemplo de Uso

1. Un empleado accede a la **Tienda**
2. Ve un producto "Alimento para Perros" a $25.00
3. Agrega 2 unidades al carrito
4. Va al carrito y revisa su compra (Total: $50.00)
5. Procede al checkout
6. Selecciona al cliente "Juan Pérez"
7. Elige "Efectivo" como método de pago
8. Confirma la compra
9. Sistema genera:
   - Factura: FAC-20251103143022
   - Pago: PAG-20251103143022
   - Actualiza stock: De 10 a 8 unidades
10. Muestra confirmación con todos los detalles

## Archivos Creados

### Vistas (views.py)
- `tienda_productos()` - Catálogo
- `carrito_ver()` - Ver carrito
- `carrito_agregar()` - Agregar al carrito
- `carrito_actualizar()` - Actualizar cantidad
- `carrito_eliminar()` - Eliminar producto
- `carrito_vaciar()` - Vaciar carrito
- `checkout()` - Página de pago
- `procesar_pago()` - Procesar compra
- `compra_exitosa()` - Confirmación

### Templates
- `tienda/catalogo.html` - Catálogo de productos
- `tienda/carrito.html` - Vista del carrito
- `tienda/checkout.html` - Proceso de pago
- `tienda/compra_exitosa.html` - Confirmación

### URLs
- 9 rutas nuevas en `urls.py`

## Próximas Mejoras Posibles

- 📊 Reportes de ventas
- 🔍 Búsqueda y filtros de productos
- 📸 Imágenes de productos
- 📦 Historial de compras por cliente
- 💰 Descuentos y promociones
- 📧 Envío de factura por email
- 🖨️ Impresión de tickets
- 📈 Dashboard de ventas

---

**Sistema desarrollado para PetCare** 🐾
Gestión Veterinaria Integral
