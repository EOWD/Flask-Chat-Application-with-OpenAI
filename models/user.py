from marshmallow import Schema, fields

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    phoneNumber = fields.Str()
    occupation = fields.Str()
