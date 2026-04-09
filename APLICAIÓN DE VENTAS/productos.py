productos = {
    "1": ("Arroz", 2000),
    "2": ("Leche", 3000)
}

def ver_productos():
    for k, v in productos.items():
        print(k, v[0], "$", v[1])
