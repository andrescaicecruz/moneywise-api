
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Pais(db.Model):
    __tablename__ = 'pais'
    __table_args__ = {'schema': 'public'}

    id_pais = db.Column(db.String(5), primary_key=True)  # Longitud cambiada a 5 para coincidir con CHAR(5)
    nombre = db.Column(db.String(40), nullable=False)  # VARCHAR(40) coincide con String(40)
    indicativo_telefonico = db.Column(db.Numeric(5, 0), nullable=False)  # Precisión cambiada a 5
    estado = db.Column(db.String(10), nullable=False)  # VARCHAR(10) se refleja como String(10)
    fecha_registro = db.Column(db.DateTime(timezone=True), nullable=True)  # Corregido el typo y cambiado a DateTime
    fecha_actualizacion = db.Column(db.DateTime(timezone=True), nullable=True, onupdate=datetime.utcnow)
    usuario_id = db.Column(db.String(15), nullable=False)  # NOT NULL agregado
    id_address = db.Column(db.Numeric(10, 0), nullable=True)  # Tipo cambiado a Numeric y nullable True

    def __repr__(self):
        return f"<Pais(id_pais='{self.id_pais}', nombre='{self.nombre}', indicativo_telefonico={self.indicativo_telefonico}, estado={self.estado}, fecha_registro='{self.fecha_registro}', fecha_actualizacion='{self.fecha_actualizacion}', id_usuario='{self.id_usuario}', id_address='{self.id_address}')>"
    
    
class Ciudad(db.Model):
    __tablename__ = 'ciudad'
    id_ciudad = db.Column(db.Integer, primary_key=True)
    id_departamento = db.Column(db.Integer, db.ForeignKey('departamento.id_departamento'), nullable=True)
    nombre = db.Column(db.String(40), nullable=False)
    indicativo = db.Column(db.String(4), nullable=False)
    estado = db.Column(db.Boolean, nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<Ciudad(id_ciudad={self.id_ciudad}, id_departamento={self.id_departamento}, nombre='{self.nombre}', indicativo='{self.indicativo}', estado={self.estado}, fecha_registro='{self.fecha_registro}', fecha_actualizacion='{self.fecha_actualizacion}')>"
    

class Credito(db.Model):
    __tablename__ = 'credito'
    __table_args__ = {'schema': 'public'}

    id_credito = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, nullable=True)
    id_tipo_credito = db.Column(db.Integer, nullable=True)
    monto = db.Column(db.Numeric(10, 2), nullable=True)
    fecha_inicio = db.Column(db.Date, nullable=True)
    estado = db.Column(db.String(2), nullable=True)

    def __repr__(self):
        return f"<Credito(id_credito={self.id_credito}, id_cliente={self.id_cliente}, id_tipo_credito={self.id_tipo_credito}, monto={self.monto}, fecha_inicio='{self.fecha_inicio}', estado='{self.estado}')>"



class CreditoIntereses(db.Model):
    __tablename__ = 'credito_intereses'
    __table_args__ = {'schema': 'public'}

    id_credito_intereses = db.Column(db.Numeric(10), primary_key=True)
    interes = db.Column(db.Numeric(10), nullable=True)
    id_credito = db.Column(db.Numeric(10), db.ForeignKey('public.CREDITO.id_credito'), nullable=True)
    id_tipo_interes = db.Column(db.Numeric(10), nullable=True)

    def __repr__(self):
        return f"<CreditoIntereses(id_credito_intereses={self.id_credito_intereses}, interes={self.interes}, id_credito={self.id_credito}, id_tipo_interes={self.id_tipo_interes})>"

class Depto(db.Model):
    __tablename__ = 'depto'
    __table_args__ = {'schema': 'public'}

    id_departamento = db.Column(db.String(3), primary_key=True)
    id_pais = db.Column(db.String(3), db.ForeignKey('public.pais.id_pais'))
    nombre = db.Column(db.String(30), nullable=False)
    indicativo = db.Column(db.String(3), nullable=False)
    fecha_registro = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    estado = db.Column(db.Numeric(1), nullable=False)
    id_usuario = db.Column(db.String(10))
    ip_address = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f"<Depto(id_departamento='{self.id_departamento}', nombre='{self.nombre}', indicativo='{self.indicativo}', fecha_registro='{self.fecha_registro}', fecha_actualizacion='{self.fecha_actualizacion}', estado={self.estado}, id_usuario='{self.id_usuario}', op_address='{self.op_address}')>"



class Cliente(db.Model):
    __tablename__ = 'cliente'
    __table_args__ = {'schema': 'public'}

    id_cliente = db.Column(db.Numeric(10), primary_key=True)
    id_ciudad = db.Column(db.String(255))
    id_cliente_email = db.Column(db.String(255))
    id_direccion = db.Column(db.String(255))
    id_tipo_telefono = db.Column(db.Numeric(10))
    nombre = db.Column(db.String(20), nullable=False)
    apellido = db.Column(db.String(30))
    documento = db.Column(db.String(10))
    fecha_registro = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Cliente(id_cliente={self.id_cliente}, id_ciudad='{self.id_ciudad}', id_cliente_email='{self.id_cliente_email}', id_direccion='{self.id_direccion}', id_tipo_telefono={self.id_tipo_telefono}, nombre='{self.nombre}', apellido='{self.apellido}', documento='{self.documento}', fecha_registro='{self.fecha_registro}')>"


class Usuario(db.Model):
    __tablename__ = 'usuario'
    __table_args__ = {'schema': 'public'}

    id_usuario = db.Column(db.Numeric(10), primary_key=True)
    id_ciudad = db.Column(db.String(255))
    id_tipo_usuario = db.Column(db.String(255))
    id_cliente_email = db.Column(db.String(255))
    usuario_imail = db.Column(db.String(255))
    nombre_usuario = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(20))

    def __repr__(self):
        return f"<Usuario(id_usuario={self.id_usuario}, id_ciudad='{self.id_ciudad}', id_tipo_usuario='{self.id_tipo_usuario}', id_cliente_email='{self.id_cliente_email}', usuario_imail='{self.usuario_imail}', nombre_usuario='{self.nombre_usuario}', nombre='{self.nombre}', apellido='{self.apellido}')>"
    
    
    
class CreditoMovimientos(db.Model):
    __tablename__ = 'credito_movimientos'
    __table_args__ = {'schema': 'public'}

    id_movimientos = db.Column(db.String(25), primary_key=True)
    id_credito = db.Column(db.String(50))
    id_tipo_movimiento = db.Column(db.String(50))
    monto = db.Column(db.Numeric(10, 2))
    fecha_movimiento = db.Column(db.TIMESTAMP(timezone=True))

    def __repr__(self):
        return f"<CreditoMovimientos(id_movimientos='{self.id_movimientos}', id_credito='{self.id_credito}', id_tipo_movimiento='{self.id_tipo_movimiento}', monto={self.monto}, fecha_movimiento='{self.fecha_movimiento}')>"


class TipoCredito(db.Model):
    __tablename__ = 'tipo_credito'
    __table_args__ = {'schema': 'public'}

    id_tipo_credito = db.Column(db.String(50), primary_key=True)
    descripcion = db.Column(db.String(100))

    def __repr__(self):
        return f"<TipoCredito(id_tipo_credito='{self.id_tipo_credito}', descripcion='{self.descripcion}')>"


class CreditoCliente(db.Model):
    __tablename__ = 'credito_clientes'
    __table_args__ = {'schema': 'public'}

    id_credito_cliente = db.Column(db.Numeric(10), primary_key=True)
    id_cliente = db.Column(db.Numeric(10))
    id_credito = db.Column(db.Numeric(10))

    def __repr__(self):
        return f"<CreditoCliente(id_credito_cliente={self.id_credito_cliente}, id_cliente={self.id_cliente}, id_credito={self.id_credito})>"


class CreditoLotePago(db.Model):
    __tablename__ = 'credito_lote_pagos'
    __table_args__ = {'schema': 'public'}

    id_credito_lote_pago = db.Column(db.Numeric(10), primary_key=True)
    id_credito_pago = db.Column(db.Numeric(10))

    def __repr__(self):
        return f"<CreditoLotePago(id_credito_lote_pago={self.id_credito_lote_pago}, id_credito_pago={self.id_credito_pago})>"


class CreditoReporteMora(db.Model):
    __tablename__ = 'credito_reporte_moras'
    __table_args__ = {'schema': 'public'}

    id_credito_reporte_moras = db.Column(db.Numeric(15), primary_key=True)
    id_credito = db.Column(db.Numeric(20))
    monto = db.Column(db.String(50))

    def __repr__(self):
        return f"<CreditoReporteMora(id_credito_reporte_moras={self.id_credito_reporte_moras}, id_credito={self.id_credito}, monto='{self.monto}')>"


class CreditoPazSalvo(db.Model):
    __tablename__ = 'credito_paz_salvo'
    __table_args__ = {'schema': 'public'}

    id_credito_paz_salvo = db.Column(db.Numeric(15), primary_key=True)
    id_credito = db.Column(db.Numeric(15))
    fecha_paz_salvo = db.Column(db.Date)

    def __repr__(self):
        return f"<CreditoPazSalvo(id_credito_paz_salvo={self.id_credito_paz_salvo}, id_credito={self.id_credito}, fecha_paz_salvo={self.fecha_paz_salvo})>"


class CreditoPago(db.Model):
    __tablename__ = 'credito_pagos'
    __table_args__ = {'schema': 'public'}

    id_credito_pago = db.Column(db.Numeric(10), primary_key=True)
    id_credito = db.Column(db.Numeric(10))
    monto = db.Column(db.DECIMAL(10, 2))
    fecha_pago = db.Column(db.TIMESTAMP(timezone=True))

    def __repr__(self):
        return f"<CreditoPago(id_credito_pago={self.id_credito_pago}, id_credito={self.id_credito}, monto={self.monto}, fecha_pago={self.fecha_pago})>"


class OrganizacionCredito(db.Model):
    __tablename__ = 'organizacion_creditos'
    __table_args__ = {'schema': 'public'}

    id_organizacion_credito = db.Column(db.String(50), primary_key=True)
    id_organizacion = db.Column(db.String(50))
    id_credito = db.Column(db.String(50))

    def __repr__(self):
        return f"<OrganizacionCredito(id_organizacion_credito='{self.id_organizacion_credito}', id_organizacion='{self.id_organizacion}', id_credito='{self.id_credito}')>"

class TipoMovimiento(db.Model):
    __tablename__ = 'tipo_movimiento'
    __table_args__ = {'schema': 'public'}

    id_tipo_movimiento = db.Column(db.String(50), primary_key=True)
    descripcion = db.Column(db.String(50))

    def __repr__(self):
        return f"<TipoMovimiento(id_tipo_movimiento='{self.id_tipo_movimiento}', descripcion='{self.descripcion}')>"


class OrganizacionUsuario(db.Model):
    __tablename__ = 'organizacion_usuarios'
    __table_args__ = {'schema': 'public'}

    id_organizacion_usuario = db.Column(db.String(50), primary_key=True)
    id_organizacion = db.Column(db.String(50))
    id_usuario = db.Column(db.String(50))

    def __repr__(self):
        return f"<OrganizacionUsuario(id_organizacion_usuario='{self.id_organizacion_usuario}', id_organizacion='{self.id_organizacion}', id_usuario='{self.id_usuario}')>"


class Organizacion(db.Model):
    __tablename__ = 'organizacion'
    __table_args__ = {'schema': 'public'}

    id_organizacion = db.Column(db.Numeric(10), primary_key=True)
    nombre = db.Column(db.String(100))

    def __repr__(self):
        return f"<Organizacion(id_organizacion={self.id_organizacion}, nombre='{self.nombre}')>"


class Interes(db.Model):
    __tablename__ = 'interes'
    __table_args__ = {'schema': 'public'}

    id_interes = db.Column(db.Numeric(10), primary_key=True)
    id_tipo_interes = db.Column(db.Numeric(10))
    tasa = db.Column(db.DECIMAL(5, 2))
    descripcion = db.Column(db.String(100))

    def __repr__(self):
        return f"<Interes(id_interes={self.id_interes}, id_tipo_interes={self.id_tipo_interes}, tasa={self.tasa}, descripcion='{self.descripcion}')>"

class TipoInteres(db.Model):
    __tablename__ = 'tipo_interes'
    __table_args__ = {'schema': 'public'}

    id_tipo_interes = db.Column(db.Numeric(10), primary_key=True)
    descripcion = db.Column(db.String(100))

    def __repr__(self):
        return f"<TipoInteres(id_tipo_interes={self.id_tipo_interes}, descripcion='{self.descripcion}')>"


class TipoDocumento(db.Model):
    __tablename__ = 'tipo_documento'
    __table_args__ = {'schema': 'public'}

    id_tipo_documento = db.Column(db.String(5), primary_key=True)
    descripcion = db.Column(db.String(100))

    def __repr__(self):
        return f"<TipoDocumento(id_tipo_documento='{self.id_tipo_documento}', descripcion='{self.descripcion}')>"


class ClienteDireccion(db.Model):
    __tablename__ = 'cliente_direcciones'
    __table_args__ = {'schema': 'public'}

    id_direcciones = db.Column(db.String(25), primary_key=True)
    id_cliente = db.Column(db.String(25))
    id_direccion = db.Column(db.String(25))
    tip_id_direccion = db.Column(db.String(25))

    def __repr__(self):
        return f"<ClienteDireccion(id_direcciones='{self.id_direcciones}', id_cliente='{self.id_cliente}', id_direccion='{self.id_direccion}', tip_id_direccion='{self.tip_id_direccion}')>"


class TipoCliente(db.Model):
    __tablename__ = 'tipo_cliente'
    __table_args__ = {'schema': 'public'}

    id_tipo_cliente = db.Column(db.String(20), primary_key=True)
    id_cliente = db.Column(db.Numeric(10))
    descripcion = db.Column(db.String(100))

    def __repr__(self):
        return f"<TipoCliente(id_tipo_cliente='{self.id_tipo_cliente}', id_cliente={self.id_cliente}, descripcion='{self.descripcion}')>"


class TipoTelefono(db.Model):
    __tablename__ = 'tipo_telefono'
    __table_args__ = {'schema': 'public'}

    id_tipo_telefono = db.Column(db.String(15), primary_key=True)
    id_cliente_telefono = db.Column(db.String(15))
    descripcion = db.Column(db.String(100))

    def __repr__(self):
        return f"<TipoTelefono(id_tipo_telefono='{self.id_tipo_telefono}', id_cliente_telefono='{self.id_cliente_telefono}', descripcion='{self.descripcion}')>"


class ClienteTelefono(db.Model):
    __tablename__ = 'cliente_telefonos'
    __table_args__ = {'schema': 'public'}

    id_cliente_telefono = db.Column(db.String(10), primary_key=True)
    telefono = db.Column(db.String(10))

    def __repr__(self):
        return f"<ClienteTelefono(id_cliente_telefono='{self.id_cliente_telefono}', telefono='{self.telefono}')>"


class TipoEmail(db.Model):
    __tablename__ = 'tipo_email'
    __table_args__ = {'schema': 'public'}

    id_tipo_email = db.Column(db.String(10), primary_key=True)
    descripcion = db.Column(db.String(50))

    def __repr__(self):
        return f"<TipoEmail(id_tipo_email='{self.id_tipo_email}', descripcion='{self.descripcion}')>"


class ClienteEmail(db.Model):
    __tablename__ = 'cliente_email'
    __table_args__ = {'schema': 'public'}

    id_cliente_email = db.Column(db.String(20), primary_key=True)
    id_tipo_email = db.Column(db.String(20))
    email = db.Column(db.String(25))

    def __repr__(self):
        return f"<ClienteEmail(id_cliente_email='{self.id_cliente_email}', id_tipo_email='{self.id_tipo_email}', email='{self.email}')>"


class OrganizacionCliente(db.Model):
    __tablename__ = 'organizacion_clientes'
    __table_args__ = {'schema': 'public'}

    id_organizacion_cliente = db.Column(db.String(25), primary_key=True)
    id_cliente = db.Column(db.Numeric(10))
    id_organizacion = db.Column(db.Numeric(10))

    def __repr__(self):
        return f"<OrganizacionCliente(id_organizacion_cliente='{self.id_organizacion_cliente}', id_cliente={self.id_cliente}, id_organizacion={self.id_organizacion})>"


class Direccion(db.Model):
    __tablename__ = 'direccion'
    __table_args__ = {'schema': 'public'}

    barrio = db.Column(db.String(20), primary_key=True)
    ciudad = db.Column(db.String(20))
    direccion = db.Column(db.String(20))

    def __repr__(self):
        return f"<Direccion(barrio='{self.barrio}', ciudad='{self.ciudad}', direccion='{self.direccion}')>"


class TipoDireccion(db.Model):
    __tablename__ = 'tipo_direccion'
    __table_args__ = {'schema': 'public'}

    id_direccion = db.Column(db.String(20), primary_key=True)
    pueblo_o_ciudad = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<TipoDireccion(id_direccion='{self.id_direccion}', pueblo_o_ciudad='{self.pueblo_o_ciudad}')>"

# ... Otros modelos si es necesario