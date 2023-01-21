
import os
from mongo import mongo

data={
        "url": "http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode?p=33210531487473012103650020000035461870027213|2|1|2|976181ee8ae063994e3b2cbe76ef387838fc9e4f"
    }

result = mongo.safe_save(
    uri=os.getenv("MONGODB_CONNSTRING"),
    database=os.getenv("MONGODB_DATABASE"),
    collection=os.getenv("MONGODB_COLLECTION"),
    data=data
)
print(result)