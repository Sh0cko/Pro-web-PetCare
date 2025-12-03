-- ==========================================================
-- INSERTS COMPLETOS PARA PET CARE
-- ==========================================================

-- 1. PROPIETARIO
INSERT INTO propietario (id_propietario, nombre, telefono, email, direccion) VALUES
('PROP001', 'María González', '555-123-4567', 'maria.gonzalez@email.com', 'Av. Reforma 123, CDMX'),
('PROP002', 'Carlos Rodríguez', '555-987-6543', 'carlos.rodriguez@email.com', 'Calle Juárez 456, Guadalajara'),
('PROP003', 'Ana Martínez', '555-456-7890', 'ana.martinez@email.com', 'Blvd. López Mateos 789, Monterrey');

-- 2. PACIENTES
INSERT INTO pacientes (id, nombre, especie, raza, nacimiento, id_propietario) VALUES
('MASC001', 'Max', 'Perro', 'Labrador Retriever', '2020-03-15', 'PROP001'),
('MASC002', 'Luna', 'Gato', 'Siamés', '2021-07-22', 'PROP002'),
('MASC003', 'Rocky', 'Perro', 'Bulldog Francés', '2019-11-10', 'PROP003'),
('MASC004', 'Mimi', 'Gato', 'Persa', '2022-01-30', 'PROP001'),
('MASC005', 'Piolín', 'Ave', 'Canario', '2023-03-10', 'PROP002'),
('MASC006', 'Nemo', 'Pez', 'Pez Dorado', '2023-08-15', 'PROP003');

-- 3. VACUNA
INSERT INTO vacuna (id_vacuna, nombre, descripcion) VALUES
('VAC001', 'Rabia', 'Vacuna contra la rabia, aplicación anual'),
('VAC002', 'Múltiple Canina', 'Protección contra moquillo, hepatitis, parvovirus, etc.'),
('VAC003', 'Trivalente Felina', 'Protección contra panleucopenia, calicivirus, rinotraqueitis');

-- 4. SERVICIO
INSERT INTO servicio (id_servicio, nombre, descripcion, costo) VALUES
('SERV001', 'Consulta General', 'Revisión médica general', 300.00),
('SERV002', 'Baño Completo', 'Baño, secado y cepillado', 250.00),
('SERV003', 'Cirugía Menor', 'Procedimientos quirúrgicos básicos', 800.00),
('SERV004', 'Hospitalización', 'Cuidado médico por 24 horas', 450.00);

-- 5. EMPLEADO
INSERT INTO empleado (id_empleado, nombre, cargo, telefono, email) VALUES
('EMP001', 'Dr. Roberto Sánchez', 'Veterinario', '555-111-2233', 'roberto.sanchez@petcare.com'),
('EMP002', 'Laura Mendoza', 'Estilista Canino', '555-444-5566', 'laura.mendoza@petcare.com'),
('EMP003', 'Dra. Elena Torres', 'Veterinaria', '555-777-8899', 'elena.torres@petcare.com');

-- 6. INVENTARIO
INSERT INTO inventario (id_producto, nombre, descripcion, cantidad, precio) VALUES
('INV001', 'Antipulgas', 'Tratamiento mensual para pulgas y garrapatas', 50, 350.00),
('INV002', 'Alimento Premium', 'Alimento para perros adultos raza grande', 30, 850.00),
('INV003', 'Arena Sanitaria', 'Arena aglomerante para gatos', 40, 120.00);

-- 7. PRODUCTO
INSERT INTO producto (id_producto, nombre, precio, cantidad, descripcion) VALUES
('PROD001', 'Shampoo Hidratante', 120.00, 25, 'Shampoo para piel sensible'),
('PROD002', 'Cepillo Deslanador', 85.50, 15, 'Cepillo para gatos de pelo largo'),
('PROD003', 'Juguete Interactivo', 65.00, 20, 'Juguete para estimulación mental');

-- 8. DATOSCONSULTA
INSERT INTO datosconsulta (id_consulta, motivo, fecha, diagnostico, id_mascota, detalles_paciente) VALUES
('CONS001', 'Control anual y vacunación', '2024-01-15', 'Paciente saludable, se aplicó vacuna múltiple', 'MASC001', 'Temperatura 38.2°C, peso 25kg'),
('CONS002', 'Problemas digestivos', '2024-01-18', 'Gastritis leve, tratamiento con protectores gástricos', 'MASC002', 'Vómitos ocasionales, deshidratación leve'),
('CONS003', 'Revisión de plumas', '2024-01-25', 'Muda normal, suplemento vitamínico recomendado', 'MASC005', 'Plumas en buen estado, canto normal');

-- 9. ASEOMASCOTAS
INSERT INTO aseomascotas (id_aseo, id_mascota, id_propietario, tipo_banio, es_agresivo, fecha_banio) VALUES
('ASEO001', 'MASC001', 'PROP001', 'Completo', FALSE, '2024-01-20'),
('ASEO002', 'MASC003', 'PROP003', 'Básico', TRUE, '2024-01-21'),
('ASEO003', 'MASC004', 'PROP001', 'Completo', FALSE, '2024-01-22');

-- 10. HOTEL
INSERT INTO hotel (id_hotel, id_mascota, fecha_ingreso, fecha_egreso, habitacion, observaciones) VALUES
('HOTEL001', 'MASC001', '2024-02-01', '2024-02-05', 'Suite Premium', 'Paciente tranquilo, dieta especial'),
('HOTEL002', 'MASC004', '2024-02-10', '2024-02-12', 'Habitación Estándar', 'Requiere caja de arena limpia'),
('HOTEL003', 'MASC002', '2024-02-15', '2024-02-20', 'Suite Felina', 'Juguetes interactivos requeridos');

-- 11. VACUNACIÓN
INSERT INTO vacunacion (id_vacunacion, id_mascota, id_vacuna, fecha, veterinario) VALUES
('VACUN001', 'MASC001', 'VAC001', '2024-01-15', 'Dr. Pérez'),
('VACUN002', 'MASC002', 'VAC003', '2024-01-16', 'Dra. López'),
('VACUN003', 'MASC003', 'VAC002', '2024-01-22', 'Dr. Pérez');

-- 12. FACTURA
INSERT INTO factura (id_factura, id_propietario, fecha, total) VALUES
('FACT001', 'PROP001', '2024-01-15', 650.00),
('FACT002', 'PROP002', '2024-01-16', 300.00),
('FACT003', 'PROP003', '2024-01-22', 550.00);

-- 13. PAGO
INSERT INTO pago (id_pago, id_propietario, fecha, monto, metodo) VALUES
('PAGO001', 'PROP001', '2024-01-15', 650.00, 'Tarjeta de Crédito'),
('PAGO002', 'PROP002', '2024-01-16', 300.00, 'Efectivo'),
('PAGO003', 'PROP003', '2024-01-22', 550.00, 'Transferencia');

-- 14. FACTURA_SERVICIO
INSERT INTO factura_servicio (id_factura, id_servicio, cantidad) VALUES
('FACT001', 'SERV001', 1),
('FACT001', 'SERV002', 1),
('FACT002', 'SERV001', 1),
('FACT003', 'SERV001', 1),
('FACT003', 'SERV004', 1);

-- 15. PAGO_FACTURA
INSERT INTO pago_factura (id_pago, id_factura) VALUES
('PAGO001', 'FACT001'),
('PAGO002', 'FACT002'),
('PAGO003', 'FACT003');

-- 16. HISTORIALCLINICO
INSERT INTO historialclinico (id_historial, id_mascota, peso, temperatura, antecedentes, tratamientos, observaciones) VALUES
('HIST001', 'MASC001', 25.5, 38.2, 'Vacunación completa', 'Control de peso anual', 'Paciente en excelente condición'),
('HIST002', 'MASC002', 4.2, 38.5, 'Alergia alimentaria', 'Dieta especial hipoalergénica', 'Mantener dieta estricta'),
('HIST003', 'MASC003', 12.8, 38.1, 'Problemas respiratorios', 'Control de vías respiratorias', 'Evitar ejercicio intenso en días calurosos');

-- ==========================================================
-- VERIFICACIÓN DE DATOS INSERTADOS
-- ==========================================================

-- Ver pacientes y propietarios
SELECT * FROM vista_pacientes_propietarios;

-- Ver todas las consultas
SELECT * FROM datosconsulta;

-- Ver historial clínico
SELECT * FROM historialclinico;

-- Ver servicios y facturas
SELECT f.id_factura, p.nombre as propietario, s.nombre as servicio, fs.cantidad, s.costo
FROM factura f 
JOIN factura_servicio fs ON f.id_factura = fs.id_factura 
JOIN servicio s ON fs.id_servicio = s.id_servicio
JOIN propietario p ON f.id_propietario = p.id_propietario;