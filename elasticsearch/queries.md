

## 🧾 **Sample Document (for reference)**

```json
{
  "product_id": "P123",
  "name": "Wireless Bluetooth Headphones",
  "description": "Noise-cancelling over-ear headphones with 30 hours battery life.",
  "price": 2999,
  "brand": "SoundPro",
  "category": "electronics",
  "rating": 4.5,
  "in_stock": true,
  "tags": ["wireless", "bluetooth", "headphones"],
  "created_at": "2024-01-10"
}
```

---

## 🔍 1. `match` — Full-text search (analyzed)

```json
{
  "query": {
    "match": {
      "description": "noise cancelling"
    }
  }
}
```

🔹 *Searches for documents where `description` contains terms like "noise" and "cancelling".*

---

## 🔍 2. `multi_match` — Search multiple fields

```json
{
  "query": {
    "multi_match": {
      "query": "bluetooth headphones",
      "fields": ["name", "description", "tags"]
    }
  }
}
```

🔹 *Search across `name`, `description`, and `tags`.*

---

## 🔍 3. `match_phrase` — Exact phrase match

```json
{
  "query": {
    "match_phrase": {
      "description": "battery life"
    }
  }
}
```

🔹 *Matches the exact phrase “battery life”.*

---

## 🔍 4. `match_phrase_prefix` — Autocomplete-style phrase

```json
{
  "query": {
    "match_phrase_prefix": {
      "name": "wireless bluet"
    }
  }
}
```

🔹 *Good for autosuggestions/search-as-you-type.*

---

## 🔍 5. `query_string` — Lucene-style syntax

```json
{
  "query": {
    "query_string": {
      "query": "bluetooth AND headphones",
      "fields": ["name", "description"]
    }
  }
}
```

🔹 *Useful when giving users control over query syntax.*

---

## 🔍 6. `simple_query_string` — Safe syntax (no errors)

```json
{
  "query": {
    "simple_query_string": {
      "query": "bluetooth +headphones -wired",
      "fields": ["name", "description"]
    }
  }
}
```

---

## 🎯 7. `term` — Exact match (non-analyzed fields)

```json
{
  "query": {
    "term": {
      "category": "electronics"
    }
  }
}
```

---

## 🎯 8. `terms` — Match one of many

```json
{
  "query": {
    "terms": {
      "brand": ["SoundPro", "Bose", "Sony"]
    }
  }
}
```

---

## 🎯 9. `range` — Numeric or date range

```json
{
  "query": {
    "range": {
      "price": {
        "gte": 1000,
        "lte": 5000
      }
    }
  }
}
```

---

## 🎯 10. `exists` — Field existence check

```json
{
  "query": {
    "exists": {
      "field": "rating"
    }
  }
}
```

---

## 🎯 11. `prefix` — Field starts with value

```json
{
  "query": {
    "prefix": {
      "brand": "sou"
    }
  }
}
```

---

## 🎯 12. `wildcard` — Pattern match (slower)

```json
{
  "query": {
    "wildcard": {
      "name": "wire*"
    }
  }
}
```

---

## 🎯 13. `regexp` — Regular expression (very slow)

```json
{
  "query": {
    "regexp": {
      "name": "wire.*less"
    }
  }
}
```

---

## 🧠 14. `bool` — Combine must, should, must\_not

```json
{
  "query": {
    "bool": {
      "must": [
        { "match": { "category": "electronics" } },
        { "range": { "rating": { "gte": 4 } } }
      ],
      "must_not": [
        { "match": { "name": "refurbished" } }
      ]
    }
  }
}
```

---

## 🧠 15. `boosting` — Boost some, demote others

```json
{
  "query": {
    "boosting": {
      "positive": {
        "match": { "tags": "wireless" }
      },
      "negative": {
        "match": { "description": "refurbished" }
      },
      "negative_boost": 0.2
    }
  }
}
```

---

## 🧠 16. `function_score` — Dynamic score adjustment

```json
{
  "query": {
    "function_score": {
      "query": { "match_all": {} },
      "field_value_factor": {
        "field": "rating",
        "factor": 1.2,
        "modifier": "sqrt",
        "missing": 1
      }
    }
  }
}
```

---

## 🧠 17. `constant_score` — Filter with fixed score

```json
{
  "query": {
    "constant_score": {
      "filter": {
        "term": { "category": "electronics" }
      }
    }
  }
}
```

---

## 🧠 18. `script_score` — Custom scoring logic

```json
{
  "query": {
    "script_score": {
      "query": { "match": { "tags": "wireless" } },
      "script": {
        "source": "doc['rating'].value * 2"
      }
    }
  }
}
```

---

## 🧠 19. `dis_max` — Best scoring query wins

```json
{
  "query": {
    "dis_max": {
      "queries": [
        { "match": { "name": "wireless" } },
        { "match": { "description": "wireless" } }
      ],
      "tie_breaker": 0.3
    }
  }
}
```

---

## 🧠 20. `nested` — Query nested fields

```json
{
  "query": {
    "nested": {
      "path": "reviews",
      "query": {
        "bool": {
          "must": [
            { "match": { "reviews.comment": "great" } },
            { "range": { "reviews.rating": { "gte": 4 } } }
          ]
        }
      }
    }
  }
}
```
