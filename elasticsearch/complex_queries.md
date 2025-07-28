
# Elasticsearch Query Practice with Kibana Sample eCommerce Dataset

This document contains example Elasticsearch queries you can use to practice with the `kibana_sample_data_ecommerce` dataset.

---

## 🔍 Basic Search Queries

### 1. Match All Documents
```json
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "match_all": {}
  }
}
```

### 2. Match Single Field
```json
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "match": {
     "products.product_name": "dress"
    }
  }
}
```

### 3. Match Phrase
```json
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "match_phrase": {
      "products.product_name": "Party dress"
    }
  }
}
```

### 4. Match Phrase Prefix
```json
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "match_phrase_prefix": {
      "products.product_name": "Cocktail dress"
    }
  }
}
```

---

## 🔗 Boolean Logic and Operators

### 5. Boolean AND (must both match)
```json
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "customer_first_name": "Betty" }},
        { "match": { "day_of_week": "Monday" }}
      ]
    }
  }
}
```

### 6. Boolean OR (should match at least one)
```json
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "bool": {
      "should": [
        { "match": { "customer_first_name": "Betty" }},
        { "match": { "customer_first_name": "Donna" }}
      ],
      "minimum_should_match": 1
    }
  }
}
```

### 7. Boolean NOT (must_not)
```json
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "bool": {
      "must_not": {
        "match": {
          "day_of_week": "Friday"
        }
      }
    }
  }
}
```

---

## 🔎 Query String Queries

### 8. Query String with AND
```json
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "query_string": {
      "default_field": "product_name",
      "query": "Men's AND Jacket"
    }
  }
}
```

### 9. Query String with OR
```json
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "query_string": {
      "default_field": "product_name",
      "query": "Shoes OR Pants"
    }
  }
}
```

---

## 🎯 Filtering Queries

### 10. Range Filter
```json
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "bool": {
      "filter": {
        "range": {
          "taxful_total_price": {
            "gte": 100
          }
        }
      }
    }
  }
}
```

### 11. Term Filter (exact match)
```json
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "term": {
      "day_of_week.keyword": "Monday"
    }
  }
}
```

---

## 📊 Aggregations

### 12. Aggregate by Day of Week
```json
GET kibana_sample_data_ecommerce/_search
{
  "size": 0,
  "aggs": {
    "sales_by_day": {
      "terms": {
        "field": "day_of_week.keyword"
      }
    }
  }
}
```

### 13. Avg Sale per Category
```json
GET kibana_sample_data_ecommerce/_search
{
  "size": 0,
  "aggs": {
    "category_avg_price": {
      "terms": {
        "field": "category.keyword"
      },
      "aggs": {
        "avg_price": {
          "avg": {
            "field": "taxful_total_price"
          }
        }
      }
    }
  }
}
```

### 14. Filtered Aggregation: Avg Sale on Monday
```json
GET kibana_sample_data_ecommerce/_search
{
  "size": 0,
  "query": {
    "term": {
      "day_of_week.keyword": "Monday"
    }
  },
  "aggs": {
    "avg_monday_sales": {
      "avg": {
        "field": "taxful_total_price"
      }
    }
  }
}
```

---

## 🧠 Complex Queries

### 15. Customers who purchased on Saturday AND total sale > 200
```json
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "day_of_week": "Saturday" }}
      ],
      "filter": [
        {
          "range": {
            "taxful_total_price": {
              "gt": 200
            }
          }
        }
      ]
    }
  }
}
```

### 16. Total Sales by Category on Saturday for California
```json
GET kibana_sample_data_ecommerce/_search
{
  "size": 0,
  "query": {
    "bool": {
      "must": [
        { "match": { "geoip.region_name": "California" }},
        { "match": { "day_of_week": "Saturday" }}
      ]
    }
  },
  "aggs": {
    "category_sales": {
      "terms": {
        "field": "category.keyword"
      },
      "aggs": {
        "total_sales": {
          "sum": {
            "field": "taxful_total_price"
          }
        }
      }
    }
  }
}
```

### 17. Top 5 Customers by Total Spending
```json
GET kibana_sample_data_ecommerce/_search
{
  "size": 0,
  "aggs": {
    "top_customers": {
      "terms": {
        "field": "customer_full_name.keyword",
        "size": 5,
        "order": {
          "total_spent": "desc"
        }
      },
      "aggs": {
        "total_spent": {
          "sum": {
            "field": "taxful_total_price"
          }
        }
      }
    }
  }
}
```

---

Happy Querying! 🚀
