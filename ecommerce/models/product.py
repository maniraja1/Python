class Product:

    def getProduct(id=None, name=None):
        print(f"ID: {id}, name: {name}")
        if id is not None:
            return f"This is the product home page ID: {id}"
        elif name is not None:
            return f"This is the product home page Name: {name}"
        else:
            return "This is the product home page"
