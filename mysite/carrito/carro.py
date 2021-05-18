class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        carro = self.session.get('carro')
        
        if not carro:
             self.carro = self.session['carro'] = {}
        else:
            self.carro = carro
    
    def agregar(self, producto):

        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                'producto_id':producto.id,
                'nombre':producto.nombre,
                'precio': producto.precio,
                'cantidad': 1,
                'imagen': producto.imagen.url
                }

        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    self.carro[key]['cantidad'] = self.carro[key]['cantidad'] + 1
                    break
        
        self.guardar_carro()

    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True
    
    def eliminar(self, producto):

        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar(self, producto, restar = -1):
        for key in self.carro.keys():
            if key == str(producto.id):
                self.carro[key]['cantidad'] = self.carro[key]['cantidad'] - 1
                if self.carro[key]['cantidad'] < 1:
                    del self.carro[key]
                break

        self.guardar_carro()
    
    def vaciar(self):
        self.session['carro'] = {}
        self.session.modified = True


