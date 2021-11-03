from pymodm import connect, MongoModel, fields
import ssl

connect("mongodb+srv://skriss28:Machka28@bme547.tw6yb.mongodb.net/"
        "MongoTestConnect?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)


class User(MongoModel):
    name = fields.CharField()


x = User(name="Stevan")
x.save()


