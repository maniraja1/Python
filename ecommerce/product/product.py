from flask_restplus import Namespace, Resource, reqparse
from models import product as product_model
product_ns = Namespace('product', description='product related stuff')

'''Method 1'''
@product_ns.route('')
@product_ns.doc("API related to product")
@product_ns.doc(params={'id': 'An ID'})
class product(Resource):
    def get(self, id=None):
        return product_model.Product.getProduct()


@product_ns.route('/GetProductByID/<id>')
@product_ns.doc("Get Product by ID")
@product_ns.doc(params={'id': 'An ID'})
class productById(Resource):
    def get(self, id=None):
        return product_model.Product.getProduct(id=id)


@product_ns.route('/GetProductByName/<name>')
@product_ns.doc("Get Product by name")
class productByName(Resource):
    def get(self, name=None):
        return product_model.Product.getProduct(name=name)

'''Method 2'''
''' Use carefully, it treats arguments as positional arguments. It doesn't know the difference between id and name
if you define routes like /product/<id> /product/<name>. 
It treats the first argument as ID and doesn't know the difference between id and name. 

However if you change to 
/product/productbyid/<id> /product/productbyname/<name> then it knows the difference. see below'''

class productdynamic(Resource):
    def get(self, id=None, name=None):
        print (f"ID: {id}, Name: {name}")
        if id is not None:
            return f"This is the product home page ID: {id}"
        if name is not None:
            return f"This is the product home page name: {name}"
        else:
            return "This is the product home page"


product_ns.add_resource(productdynamic, '/ZDynamicProduct', methods=['GET'])
product_ns.add_resource(productdynamic, '/ZDynamicProductByID/<id>',  methods=['GET'])
product_ns.add_resource(productdynamic, '/ZDynamicProductByName/<name>', methods=['GET'])




'''Method3'''
# Define parser and request args
parser = reqparse.RequestParser()
parser.add_argument('id', type=str, required=False, help='Get product by ID')
parser.add_argument('name', type=str, required=False, help='Get product by name')

'''
class product2(Resource):

    def get(self, id=None, name=None):
        args = parser.parse_args()
        print(args)
        id = args['id']
        name = args['name']
        print (f"ID: {id}, Name: {name}")
        if id is not None:
            return product_model.Product.getProduct(id=id)
        elif name is not None:
            return product_model.Product.getProduct(name=name)
        else:
            return product_model.Product.getProduct()

product_ns.add_resource(product2, '/product2')
product_ns.add_resource(product2, '/product2/<id>')
product_ns.add_resource(product2, '/product2/<name>')
'''



