# -*- coding: utf-8 -*-
import datetime; now=datetime.date.today()

db.define_table('categoria',
                Field('nombre',
                     requires=(IS_NOT_EMPTY(),IS_NOT_IN_DB(db,'categoria.nombre'))))


db.define_table('receta',
               Field('nombre',
                    requires=IS_NOT_EMPTY()),
               Field('categoria', db.categoria,
                    requires=IS_IN_DB(db,'categoria.id', 'categoria.nombre')),
               Field('descripcion', lenght=140,
                    requires=IS_NOT_EMPTY()),
               Field('fecha','date',default=now,
                    requires=IS_DATE()),
               Field('instrucciones','text'))
                
                
db.categoria.update_or_insert(nombre='Entrada')
db.categoria.update_or_insert(nombre='Plato Principal')
db.categoria.update_or_insert(nombre='Postre')
db.categoria.update_or_insert(nombre='Desayuno')
