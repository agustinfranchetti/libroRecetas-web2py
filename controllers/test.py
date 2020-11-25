# -*- coding: utf-8 -*-
# intente algo como

def recetas():
    records=db(db.receta.categoria==request.vars.categoria).select(orderby=db.receta.nombre)
    form=SQLFORM(db.receta, fields=['categoria'])
    return dict(form=form, records=records)

def new_receta():
    form=SQLFORM(db.receta, fields=['nombre','categoria','descripcion','instrucciones'])
    if form.accepts(request,session):
                   redirect(URL('recetas'))
    return dict(form=form)

def mostrar():
    id=request.vars.id
    recetas=db(db.receta.id==id).select()
    if not len(recetas):
        redirect(URL('recetas'))
    return dict(receta=recetas[0])
