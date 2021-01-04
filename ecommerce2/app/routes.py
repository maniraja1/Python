from flask_restx import Namespace, Resource, reqparse,fields
import app.models.product_model as product_model
from flask import request, jsonify
import app
from app import tasks


product_ns = Namespace('product', description='product related stuff')


''' Be careful how you define routes, arguments defined in the path are treated as positional arguments. 
It doesn't know the difference between id and name if you define routes like /product/<id> /product/<name>. 

You may have to build separate paths(like below) or build an api that can process parameters in query string or 
the request body
/product/productbyid/<id> /product/productbyname/<name> 

Another way to define arguments is by using parameters in query string instead of in paths.

'''
'''Method 1'''
@product_ns.route('')
@product_ns.doc("API related to product")
class product(Resource):
    def get(self):
        app.flask_app.logger.info("GetProduct Success")
        return product_model.Product.getAllProducts()



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
        if id is not None:
            return product_model.Product(product_id=id).getProductByID()
        elif name is not None:
            return product_model.Product(product_name=name).getProductByName()
        else:
            return "Invalid inputs passed"

# This below endpoint accepts parameters in the url path and has both post and get
# This endpoint also show how to deal with arguments passed in the body
# you need to define a model that will be used in the body documentation

# Define parameters in the body here
resource_fields = product_ns.model('Resource', {
    'name': fields.String(description="Product Name.", required=True),
})

@product_ns.route('/GetProductByID/<int:id>', methods=['GET', 'POST'])  # strongly type parameters
@product_ns.doc("Get Product by ID")
@product_ns.doc(params={'id': 'An ID'})
class productById(Resource):

    def get(self, id=None):
        return product_model.Product(id).getProductByID()

    @product_ns.expect(resource_fields, validate=True) # Body documentation
    def post(self, id):
        # Process parameters
        product_name = request.get_json()['name']
        product_model.Product(id, product_name).insertproduct()


@product_ns.route('/GetProductByName/<string:name>', methods=['GET', 'POST'])  # strongly type parameters
@product_ns.doc("Get Product by name")
class productByName(Resource):
    def get(self, name=None):
        p = product_model.Product(product_name=name)
        return p.getProductByName()


    def post(self, name):
        productname = name
        tasks.InsertAsync2.apply_async(args=[productname])
        return "Processing Request Asynchronously"


# Running adhoc SQL
@product_ns.route('/GettopNProduct')
@product_ns.doc("Get Top N Product")
@product_ns.doc(params={'count': 'count'})
class topNProduct(Resource):
    def get(self):
        count = request.args.get("count")
        print(f"Count: {count}")
        return product_model.Product.getTopNProducts(count)




