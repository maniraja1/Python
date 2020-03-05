from flask_restplus import Namespace, Resource, reqparse,fields
from models import product as product_model
from flask import request
product_ns = Namespace('product', description='product related stuff')

''' Be careful how you define routes, arguents defined in the path are treated as positional arguments. 
It doesn't know the difference between id and nameif you define routes like /product/<id> /product/<name>. 
It treats the first argument as ID and doesn't know the difference between id and name. 

However if you change to 
/product/productbyid/<id> /product/productbyname/<name> then it knows the difference. see below

Another way to define arguments is by using parameters in query string instead of in paths.

Below you will find examples for defining  arguments in path and in query string
'''


'''Method 1'''
@product_ns.route('')
@product_ns.doc("API related to product")
class product(Resource):
    def get(self):
        return product_model.Product.getProduct()

# This below endpoint can parse query parameter. There are no parameters in the path  will be parsed as a
# query string

@product_ns.route('/GetProductQuerystring')
@product_ns.doc("API related to product")
@product_ns.doc(params={'id': 'An ID'})
@product_ns.doc(params={'name': 'A Name'})
class product(Resource):
    def get(self):
        id = request.args.get("id")
        name = request.args.get("name")
        return product_model.Product.getProduct(id=id, name=name)

# This below endpoint accepts parameters in the url path and has both post and get
# This endpoint also show how to deal with arguments passed in the body

# you nee dto define a model that will be used in the body documentation
resource_fields = product_ns.model('Resource', {
    'name': fields.String(description="Product Name.", required=True),
})
@product_ns.route('/GetProductByID/<int:id>', methods=['GET', 'POST'])  # strongly type parameters
@product_ns.doc("Get Product by ID")
@product_ns.doc(params={'id': 'An ID'})
class productById(Resource):

    def get(self, id=None):
        return product_model.Product.getProduct(id=id)

    @product_ns.expect(resource_fields, validate=True) # Body documentation
    def post(self,id):
        print (f"{request.get_json()}") # Get body Json
        return product_model.Product.getProduct(id=id)

# This below endpoint accepts parameters in the url path
@product_ns.route('/GetProductByName/<string:name>')  # strongly type parameters
@product_ns.doc("Get Product by name")
class productByName(Resource):
    def get(self, name=None):
        return product_model.Product.getProduct(name=name)

'''Method 2'''
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
product_ns.add_resource(productdynamic, '/ZDynamicProductByID',  methods=['GET'])
product_ns.add_resource(productdynamic, '/ZDynamicProductByName/<name>', methods=['GET'])




'''Method3'''
'''
# Define parser and request args
parser = reqparse.RequestParser()
parser.add_argument('id', type=str, required=False, help='Get product by ID')
parser.add_argument('name', type=str, required=False, help='Get product by name')


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



