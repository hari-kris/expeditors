from elasticsearch import Elasticsearch

# Connect to Elasticsearch (default: localhost:9200)
es = Elasticsearch("http://localhost:9200")

# Index name
index_name = "users"

# Document ID to upsert (provide a known ID or a new one)
document_id = "user_001"

# The document fields to update or insert
doc = {
    "name": "John Doe",
    "age": 32,
    "email": "john.doe@upsert.com",
    "interests": ["python", "elasticsearch", "upsert"]
}

# Upsert the document (update if exists, insert if not)
response = es.update(
    index=index_name,
    id=document_id,
    body={
        "doc": doc,
        "doc_as_upsert": True
    }
)

print("Upsert response:", response)
