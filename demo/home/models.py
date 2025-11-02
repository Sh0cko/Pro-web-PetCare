from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# ==============================
# MODELO: PROPIETARIO
# ==============================
class Propietario(models.Model):
    id_propietario = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.id_propietario})"

# ==============================
# MODELO: PACIENTES
# ==============================
class Paciente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('H', 'Hembra'),
    ]

    id = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=30)
    especie = models.CharField(max_length=30, blank=True, null=True)
    raza = models.CharField(max_length=30, blank=True, null=True)
    nacimiento = models.DateField(blank=True, null=True)
    id_propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, db_column='id_propietario')
    sexo = models.CharField(max_length=10, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.especie} ({self.id})"

# ==============================
# MODELO: DATOS DE CONSULTA
# ==============================
class DatosConsulta(models.Model):
    id_consulta = models.CharField(primary_key=True, max_length=30)
    motivo = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    diagnostico = models.TextField(blank=True, null=True)
    id_mascota = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='id_mascota')
    detalles_paciente = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Consulta {self.id_consulta} - {self.id_mascota.nombre}"

# ==============================
# MODELO: ASEO DE MASCOTAS
# ==============================
class AseoMascota(models.Model):
    TIPO_BANIO_CHOICES = [
        ('BASICO', 'Básico'),
        ('COMPLETO', 'Completo'),
        ('PREMIUM', 'Premium'),
    ]
    
    id_aseo = models.CharField(primary_key=True, max_length=30)
    id_mascota = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='id_mascota')
    id_propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, db_column='id_propietario')
    tipo_banio = models.CharField(max_length=15, choices=TIPO_BANIO_CHOICES, blank=True, null=True)
    es_agresivo = models.BooleanField(default=False)
    fecha_banio = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Aseo {self.id_aseo} - {self.id_mascota.nombre}"

# ==============================
# MODELO: HOTEL
# ==============================
class Hotel(models.Model):
    id_hotel = models.CharField(primary_key=True, max_length=30)
    id_mascota = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='id_mascota')
    fecha_ingreso = models.DateField()
    fecha_egreso = models.DateField()
    habitacion = models.CharField(max_length=30, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Hospedaje {self.id_hotel} - {self.id_mascota.nombre}"

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(fecha_egreso__gte=models.F('fecha_ingreso')),
                name='chk_fechas_hotel'
            )
        ]

# ==============================
# MODELO: VACUNAS
# ==============================
class Vacuna(models.Model):
    id_vacuna = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.id_vacuna})"

# ==============================
# MODELO: VACUNACIÓN
# ==============================
class Vacunacion(models.Model):
    id_vacunacion = models.CharField(primary_key=True, max_length=30)
    id_mascota = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='id_mascota')
    id_vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE, db_column='id_vacuna')
    fecha = models.DateField(blank=True, null=True)
    veterinario = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"Vacunación {self.id_vacunacion} - {self.id_mascota.nombre}"

# ==============================
# MODELO: INVENTARIO
# ==============================
class Inventario(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - Stock: {self.cantidad}"

# ==============================
# MODELO: PRODUCTOS
# ==============================
class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

# ==============================
# MODELO: SERVICIOS
# ==============================
class Servicio(models.Model):
    id_servicio = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - ${self.costo}"

# ==============================
# MODELO: EMPLEADOS
# ==============================
class Empleado(models.Model):
    id_empleado = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    cargo = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"

# ==============================
# MODELO: PAGOS
# ==============================
class Pago(models.Model):
    METODO_PAGO_CHOICES = [
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA', 'Tarjeta'),
        ('TRANSFERENCIA', 'Transferencia'),
    ]
    
    id_pago = models.CharField(primary_key=True, max_length=30)
    id_propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, db_column='id_propietario')
    fecha = models.DateField(blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    metodo = models.CharField(max_length=30, choices=METODO_PAGO_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"Pago {self.id_pago} - ${self.monto}"

# ==============================
# MODELO: FACTURAS
# ==============================
class Factura(models.Model):
    id_factura = models.CharField(primary_key=True, max_length=30)
    id_propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, db_column='id_propietario')
    fecha = models.DateField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Factura {self.id_factura} - ${self.total}"

# ==============================
# MODELO: FACTURA_SERVICIO (TABLA INTERMEDIA)
# ==============================
class FacturaServicio(models.Model):
    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE, db_column='id_factura')
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, db_column='id_servicio')
    cantidad = models.IntegerField(default=1)

    class Meta:
        unique_together = (('id_factura', 'id_servicio'),)

    def __str__(self):
        return f"Factura {self.id_factura} - Servicio {self.id_servicio}"

# ==============================
# MODELO: PAGO_FACTURA (TABLA INTERMEDIA)
# ==============================
class PagoFactura(models.Model):
    id_pago = models.ForeignKey(Pago, on_delete=models.CASCADE, db_column='id_pago')
    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE, db_column='id_factura')

    class Meta:
        unique_together = (('id_pago', 'id_factura'),)

    def __str__(self):
        return f"Pago {self.id_pago} - Factura {self.id_factura}"

# ==============================
# MODELO: HISTORIAL CLÍNICO
# ==============================
class HistorialClinico(models.Model):
    id_historial = models.CharField(primary_key=True, max_length=30)
    id_mascota = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='id_mascota')
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    temperatura = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    antecedentes = models.TextField(blank=True, null=True)
    tratamientos = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Historial {self.id_historial} - {self.id_mascota.nombre}"