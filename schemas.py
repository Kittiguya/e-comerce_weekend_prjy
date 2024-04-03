from marshmallow import Schema, fields





class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    first_name = fields.Str()
    last_name = fields.Str()


class ProductsSchemas(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Integer(required=True)

class CartSchemas(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
    description = fields.Str(dump_only=True)

class UserWithPostsSchemas(UserSchema):
    posts = fields.List(fields.Nested(UserSchema), dump_only=True)

class ProductsWithPostsSchemas(ProductsSchemas):
    posts = fields.List(fields.Nested(ProductsSchemas), dump_only=True)

class CartWithPostsSchemas(CartSchemas):
    posts = fields.List(fields.Nested(CartSchemas), dump_only=True)