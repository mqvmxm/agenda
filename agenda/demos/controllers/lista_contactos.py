import web 

render = web.template.render('views', base='layout)

class ListaContactos:
    def GET(self):
        return render.lista_contactos()

        