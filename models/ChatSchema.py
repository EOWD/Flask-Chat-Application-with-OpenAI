from marshmallow import Schema, fields

class ChatSchema(Schema):
    user_message = fields.Str()
    model_reply = fields.Str()
    timestamp = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    user_id = fields.Int()