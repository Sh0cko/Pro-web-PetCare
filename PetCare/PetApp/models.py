# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
