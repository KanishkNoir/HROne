# Deployment

Live API URL: https://hrone-production.up.railway.app/

## API Endpoints

### Root Endpoint

**GET /**
```bash
curl "https://hrone-production.up.railway.app/"
```

Response:
```json
{"message": "Hello welcome to the backend assignment by HROne submitted by Kanishk Pratap Singh"}
```

## Products API

### Create Product

**POST /api/products/**

```bash
curl -X POST "https://hrone-production.up.railway.app/api/products/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "T-Shirt",
    "price": 25.99,
    "sizes": [
      {"size": "S", "quantity": 10},
      {"size": "M", "quantity": 15},
      {"size": "L", "quantity": 8}
    ]
  }'
```

Response:
```json
{"id": "507f1f77bcf86cd799439011"}
```

### Get Products

**GET /api/products/**

```bash
curl "https://hrone-production.up.railway.app/api/products/"
```

**Get Products with Filters and Pagination:**

```bash
# Filter by name
curl "https://hrone-production.up.railway.app/api/products/?name=T-Shirt"

# Filter by size
curl "https://hrone-production.up.railway.app/api/products/?size=M"

# Pagination using offset (traditional)
curl "https://hrone-production.up.railway.app/api/products/?limit=5&offset=0"

# Pagination using page numbers (easier)
curl "https://hrone-production.up.railway.app/api/products/?limit=5&page=1"
curl "https://hrone-production.up.railway.app/api/products/?limit=5&page=2"

# Combined filters with pagination
curl "https://hrone-production.up.railway.app/api/products/?name=T-Shirt&size=M&limit=10&page=1"
```

Response:
```json
{
  "data": [
    {
      "_id": "507f1f77bcf86cd799439011",
      "name": "T-Shirt",
      "price": 25.99,
      "sizes": [
        {"size": "S", "quantity": 10},
        {"size": "M", "quantity": 15},
        {"size": "L", "quantity": 8}
      ]
    }
  ],
  "page": {
    "next": null,
    "limit": 1,
    "previous": null
  }
}
```

## Orders API

### Create Order

**POST /api/orders/**

```bash
curl -X POST "https://hrone-production.up.railway.app/api/orders/" \
  -H "Content-Type: application/json" \
  -d '{
    "userId": "user123",
    "items": [
      {
        "productId": "507f1f77bcf86cd799439011",
        "qty": 2
      },
      {
        "productId": "507f1f77bcf86cd799439012",
        "qty": 1
      }
    ]
  }'
```

Response:
```json
{"id": "507f1f77bcf86cd799439021"}
```

### Get Orders

**GET /api/orders/**

```bash
curl "https://hrone-production.up.railway.app/api/orders/"
```

**Get Orders with Pagination:**

```bash
# Using offset
curl "https://hrone-production.up.railway.app/api/orders/?limit=5&offset=0"

# Using page numbers
curl "https://hrone-production.up.railway.app/api/orders/?limit=5&page=1"
curl "https://hrone-production.up.railway.app/api/orders/?limit=5&page=2"
```

Response:
```json
{
  "data": [
    {
      "_id": "507f1f77bcf86cd799439021",
      "userId": "user123",
      "items": [
        {
          "productId": "507f1f77bcf86cd799439011",
          "qty": 2
        }
      ]
    }
  ],
  "page": {
    "next": null,
    "limit": 1,
    "previous": null
  }
}
```

## Data Models

### Product Model
```json
{
  "name": "string (required)",
  "price": "number (required)",
  "sizes": [
    {
      "size": "string (required)",
      "quantity": "number (required)"
    }
  ]
}
```

### Order Model
```json
{
  "userId": "string (required)",
  "items": [
    {
      "productId": "string (required)",
      "qty": "number (required)"
    }
  ]
}
```

## Query Parameters

### Products
- `name`: Filter by product name (case-insensitive search)
- `size`: Filter by available size
- `limit`: Number of results to return (default: 10)
- `offset`: Number of results to skip for pagination (default: 0)

### Orders
- `limit`: Number of results to return (default: 10)
- `offset`: Number of results to skip for pagination (default: 0)
- `page`: Page number (alternative to offset, starts from 1)

### Pagination Options
You can use either:
1. **Offset-based**: `?limit=10&offset=20` (traditional)
2. **Page-based**: `?limit=10&page=3` (easier, automatically calculates offset)

## Important Notes

1. All endpoints require trailing slash (/) in the URL
2. POST requests require Content-Type: application/json header
3. Product IDs returned from POST /api/products/ should be used in orders
4. All responses include pagination information in the page object

## Technology Stack

- FastAPI
- MongoDB Atlas
- Motor (async MongoDB driver)
- Pydantic for data validation
- Deployed on Railway 