from elasticsearch import Elasticsearch

# Connect to Elasticsearch (default: localhost:9200)
es = Elasticsearch("http://localhost:9200")

# Sample document (Python dictionary)
doc = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "interests": ["python", "elasticsearch", "data"]
}

# Index name
index_name = "users"

# Index the document (Elasticsearch will auto-assign an ID)
response = es.index(index=index_name, document=doc)

print("Indexed document ID:", response['_id'])
