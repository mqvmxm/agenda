import web
import sys
import os

# Le enseñamos a Python a mirar las carpetas que están más arriba
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora sí encuentra el controlador sin importar desde dónde lances la terminal
from controllers.lista_contactos import ListaContactos

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