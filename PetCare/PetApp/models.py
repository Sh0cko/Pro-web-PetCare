# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings
from django.utils import timezone


class Aseomascotas(models.Model):
    id_aseo = models.CharField(primary_key=True, max_length=30)
    id_mascota = models.ForeignKey('Pacientes', models.DO_NOTHING, db_column='id_mascota', blank=True, null=True)
    id_propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    tipo_banio = models.CharField(max_length=15, blank=True, null=True)
    es_agresivo = models.BooleanField(blank=True, null=True)
    fecha_banio = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aseomascotas'


class Datosconsulta(models.Model):
    id_consulta = models.CharField(primary_key=True, max_length=30)
    motivo = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    diagnostico = models.TextField(blank=True, null=True)
    id_mascota = models.ForeignKey('Pacientes', models.DO_NOTHING, db_column='id_mascota')
    detalles_paciente = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datosconsulta'


class Empleado(models.Model):
    id_empleado = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    cargo = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class Factura(models.Model):
    id_factura = models.CharField(primary_key=True, max_length=30)
    id_propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura'


class FacturaServicio(models.Model):
    pk = models.CompositePrimaryKey('id_factura', 'id_servicio')
    id_factura = models.ForeignKey(Factura, models.DO_NOTHING, db_column='id_factura')
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio')
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura_servicio'


class Historialclinico(models.Model):
    id_historial = models.CharField(primary_key=True, max_length=30)
    id_mascota = models.ForeignKey('Pacientes', models.DO_NOTHING, db_column='id_mascota', blank=True, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    temperatura = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    antecedentes = models.TextField(blank=True, null=True)
    tratamientos = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historialclinico'


class Hotel(models.Model):
    id_hotel = models.CharField(primary_key=True, max_length=30)
    id_mascota = models.ForeignKey('Pacientes', models.DO_NOTHING, db_column='id_mascota', blank=True, null=True)
    fecha_ingreso = models.DateField()
    fecha_egreso = models.DateField()
    habitacion = models.CharField(max_length=30, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel'


class Inventario(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario'


class Pacientes(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=30)
    especie = models.CharField(max_length=30, blank=True, null=True)
    raza = models.CharField(max_length=30, blank=True, null=True)
    nacimiento = models.DateField(blank=True, null=True)
    id_propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pacientes'


class Pago(models.Model):
    id_pago = models.CharField(primary_key=True, max_length=30)
    id_propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    metodo = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pago'


class PagoFactura(models.Model):
    pk = models.CompositePrimaryKey('id_pago', 'id_factura')
    id_pago = models.ForeignKey(Pago, models.DO_NOTHING, db_column='id_pago')
    id_factura = models.ForeignKey(Factura, models.DO_NOTHING, db_column='id_factura')

    class Meta:
        managed = False
        db_table = 'pago_factura'


class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Propietario(models.Model):
    id_propietario = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propietario'


class Servicio(models.Model):
    id_servicio = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio'


class Vacuna(models.Model):
    id_vacuna = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacuna'


class Vacunacion(models.Model):
    id_vacunacion = models.CharField(primary_key=True, max_length=30)
    id_mascota = models.ForeignKey(Pacientes, models.DO_NOTHING, db_column='id_mascota', blank=True, null=True)
    id_vacuna = models.ForeignKey(Vacuna, models.DO_NOTHING, db_column='id_vacuna', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    veterinario = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacunacion'


# ===================== Nuevos modelos gestionados por Django =====================
class ProductMeta(models.Model):
    """Información complementaria del producto (umbral de bajo stock, caducidad)."""
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name='meta')
    low_stock_threshold = models.PositiveIntegerField(default=5, help_text="Cantidad mínima antes de alertar bajo stock")
    expiration_date = models.DateField(blank=True, null=True, help_text="Fecha de caducidad (opcional)")
    notes = models.TextField(blank=True, null=True)

    def is_low_stock(self):
        qty = self.producto.cantidad or 0
        return qty <= self.low_stock_threshold

    def expiration_status(self):
        """Return 'expired', 'soon', 'ok'."""
        if not self.expiration_date:
            return 'ok'
        today = timezone.now().date()
        if self.expiration_date < today:
            return 'expired'
        if (self.expiration_date - today).days <= 30:
            return 'soon'
        return 'ok'

    def __str__(self):
        return f"Meta {self.producto.id_producto}"


class InventoryMovement(models.Model):
    """Historial de movimientos de inventario para productos."""
    TYPE_CHOICES = [
        ('CREACION', 'Creación'),
        ('ACTUALIZACION', 'Actualización'),
        ('VENTA', 'Venta'),
        ('AJUSTE', 'Ajuste'),
        ('DEVOLUCION', 'Devolución'),
    ]
    id = models.BigAutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='movimientos')
    change_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    quantity_change = models.IntegerField(help_text="Cantidad modificada (negativa para reducción)")
    previous_quantity = models.IntegerField()
    new_quantity = models.IntegerField()
    source = models.CharField(max_length=30, blank=True, null=True, help_text="Origen lógico: vista, proceso, etc.")
    note = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Movimiento de Inventario'
        verbose_name_plural = 'Movimientos de Inventario'

    def __str__(self):
        return f"{self.change_type} {self.producto.id_producto} {self.quantity_change}"


class Cita(models.Model):
    """Citas programadas para pacientes con servicios específicos."""
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADA', 'Confirmada'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
        ('NO_ASISTIO', 'No asistió'),
    ]
    
    id = models.BigAutoField(primary_key=True)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE, related_name='citas')
    servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True, blank=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True, help_text="Veterinario o empleado asignado")
    fecha = models.DateField(help_text="Fecha de la cita")
    hora = models.TimeField(help_text="Hora de inicio")
    duracion_minutos = models.PositiveIntegerField(default=30, help_text="Duración estimada en minutos")
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='PENDIENTE')
    motivo = models.TextField(blank=True, null=True, help_text="Motivo o descripción de la cita")
    notas = models.TextField(blank=True, null=True, help_text="Notas adicionales")
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='citas_creadas')
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['fecha', 'hora']
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        indexes = [
            models.Index(fields=['fecha', 'hora']),
            models.Index(fields=['estado']),
        ]

    def __str__(self):
        return f"Cita {self.id} - {self.paciente.nombre} ({self.fecha} {self.hora})"

    @property
    def hora_fin(self):
        """Calcula la hora estimada de finalización."""
        from datetime import datetime, timedelta
        dt = datetime.combine(self.fecha, self.hora) + timedelta(minutes=self.duracion_minutos)
        return dt.time()
