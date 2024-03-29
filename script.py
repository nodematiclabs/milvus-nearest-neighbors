from pymilvus import connections
from pymilvus import Collection, FieldSchema, CollectionSchema
from pymilvus.orm.types import DataType

connections.connect(host='localhost', port='19530')

fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=2)
]

schema = CollectionSchema(fields, description="Demonstration Collection")

collection_name = "simple"
collection_2d = Collection(name=collection_name, schema=schema)
collection_2d.load()

insert_result = collection_2d.insert([
    [1, 1],
    [1, -1],
])

index_params = {
    "metric_type": "L2",
    "index_type": "FLAT",
    "params": {}
}
collection_2d.create_index(field_name="vector", index_params=index_params)

query_vectors = [
    [-1, 0]
]
results = collection_2d.search(query_vectors, "vector", search_params, limit=5)
