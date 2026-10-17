# Data Contract Design Notes

A contract declares meaning, schema, ownership, validity, and permitted use. Validate actual CSV headers before finalizing any schema.

## Initial logical entities

| Entity | Candidate key/grain | Relationship |
| --- | --- | --- |
| Orders | One row per `order_id` | References customer |
| Order items | Composite (`order_id`, `order_item_id`) | References order, product, seller |
| Customers | `customer_id` in the source customer table | Referenced by order |
| Products | One row per `product_id` | Referenced by order item |
| Sellers | One row per `seller_id` | Referenced by order item |
| Payments | Multiple payments per order; inspect payment sequence | References order |
| Reviews | Inspect whether `review_id` is unique and whether an order has multiple reviews | References order |
| Geolocation | ZIP prefix may repeat | Do **not** treat ZIP prefix as a unique row key |

## Contract fields to document for each dataset

- Source and business owner
- Row grain; natural and surrogate keys
- Column names, types, nullability, ranges, and allowed categories
- Uniqueness and referential-integrity rules
- Timezone/currency assumptions
- Expected data freshness
- Privacy classification and retention
- Versioning and breaking-change policy

## Common pitfalls

- `customer_id` and `customer_unique_id` serve different purposes; confirm the difference before aggregating customers.
- Multiple payments and order items can multiply rows in naive joins.
- Canceled, unavailable, returned, and delivered order statuses affect metric definitions.
- Monetary values from item, freight, and payment tables are not interchangeable.
- Missing delivery timestamp does not necessarily indicate corrupt data.

## Completion criterion

Every chosen source has an approved written contract and a small set of automated checks when you implement Stage 1.
