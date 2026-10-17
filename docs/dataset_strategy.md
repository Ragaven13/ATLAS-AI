# Dataset Strategy

## Canonical fictional business

Use the Olist Brazilian E-Commerce dataset as the seed for **Atlas Commerce**. It provides related order, customer, product, seller, payment, review, and geographic records. Do not describe synthetic company reports as real Olist internal documents.

## Initial source inventory

Common Olist files include:

| Domain | Source file | Intended analysis |
| --- | --- | --- |
| Orders | `olist_orders_dataset.csv` | Status and timestamps |
| Order items | `olist_order_items_dataset.csv` | Product/seller relationships and order-item values |
| Customers | `olist_customers_dataset.csv` | Customer location and customer identifiers |
| Payments | `olist_order_payments_dataset.csv` | Installments, payment type, and values |
| Reviews | `olist_order_reviews_dataset.csv` | Feedback and review dates |
| Products | `olist_products_dataset.csv` | Product attributes |
| Sellers | `olist_sellers_dataset.csv` | Seller locations |
| Geolocation | `olist_geolocation_dataset.csv` | ZIP prefix and coordinates |
| Category translations | `product_category_name_translation.csv` | Category labels |

Treat this as a planning inventory; verify exact columns, encoding, grain, uniqueness, and file names against the acquired dataset.

## Source acquisition checklist

- Record acquisition date, URL, source version, and license/terms.
- Save checksums and row counts before transforming anything.
- Identify delimiters, encoding, locale, timezone, and expected null representations.
- Decide whether raw data can be published; keep raw copies out of public commits until reviewed.
- Document synthetic data generation methods and any unrealistic assumptions.

## Multi-domain expansion

The IBM Telco Customer Churn dataset can support a separate churn benchmark. **Never join IBM and Olist customer identities as though they represent the same organization.** Prefer a separate tenant or clearly labeled analytical demo.

## Synthetic documents (future)

Derive management reports, shipping policy updates, operational incident summaries, and support notes from traceable records. Each generated document should retain generation metadata and be labeled synthetic.
