import web

urls = (
    '/', 'Index',
    '/contactos', 'ListaContactos',
    '/ver', 'VerContacto',
    '/insertar', 'InsertarContacto',
    '/editar', 'EditarContacto',
    '/borrar', 'BorrarContacto'
)

app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()

class ListaContactos:
    def GET(self):
        return render.lista_contactos()

class VerContacto:
    def GET(self):
        return render.ver_contacto()

class InsertarContacto:
    def GET(self):
        return render.insertar_contacto()
        
    def POST(self):
        raise web.seeother('/contactos')

class EditarContacto:
    def GET(self):
        return render.editar_contacto()
        
    def POST(self):
        raise web.seeother('/contactos')

class BorrarContacto:
    def GET(self):
        return render.borrar_contacto()
        
    def POST(self):
        raise web.seeother('/contactos')

if __name__ == "__main__":
    app.run()