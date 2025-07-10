from elasticsearch import Elasticsearch, helpers
import csv
import time

# Elasticsearch connection (default: localhost:9200)
es = Elasticsearch(hosts=["http://localhost:9200"])

# Index name and CSV file path
index = "healthcare"
filePath = "hcpc.csv"
bulk_size = 500  # Number of records per batch

def read_csv(file_path):
    """
    Reads the CSV file and returns an iterator over dictionaries (one dict per row).
    """
    with open(file_path, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

def compose_documents(rows):
    """
    Yields Elasticsearch actions for each row in the CSV file.
    """
    for row in rows:
        yield {
            "_index": index,
            "_source": {
                'HCPC': row['HCPC'],
                'SEQNUM': row['SEQNUM'],
                'RECID': row['RECID'],
                'LONG_DESCRIPTION': row['LONG_DESCRIPTION'],
                'SHORT_DESCRIPTION': row['SHORT_DESCRIPTION']
            }
        }

def bulk_index_with_batches(actions, batch_size):
    """
    Processes actions in batches and bulk indexes each batch.
    """
    batch = []
    total_indexed = 0
    for action in actions:
        batch.append(action)
        if len(batch) == batch_size:
            helpers.bulk(es, batch)
            total_indexed += len(batch)
            print(f"Indexed {total_indexed} documents")
            batch = []
    # Index any remaining documents
    if batch:
        helpers.bulk(es, batch)
        total_indexed += len(batch)
        print(f"Indexed {total_indexed} documents (final batch)")

if __name__ == "__main__":
    # Start timing before processing
    start = time.time()
    
    # Read and compose documents from CSV
    csv_rows = read_csv(filePath)
    actions = compose_documents(csv_rows)
    
    # Bulk index documents in batches
    bulk_index_with_batches(actions, bulk_size)
    
    # End timing after processing
    end = time.time()
    print(f"Total time taken: {end - start:.2f} seconds")
