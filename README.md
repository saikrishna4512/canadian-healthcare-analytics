markdown
# 🏥 Canadian Healthcare Analytics Platform

## Problem Statement
Canadian health authorities process millions of records across disconnected systems. This platform unifies hospital wait time data into a single real-time analytics layer — enabling faster, data-driven decisions that directly impact patient care.

## Architecture

Python Producer → Azure Event Hubs → Azure Databricks → Delta Lake
├── Bronze (Raw)
├── Silver (Clean)
└── Gold (Metrics)


## Tech Stack & Why

| Tool | Purpose | Why Chosen |
|------|---------|-----------|
| Azure Event Hubs | Real-time ingestion | Kafka-compatible, Canadian data residency |
| Azure Databricks | Processing engine | Enterprise Spark, Unity Catalog governance |
| Delta Lake | Storage layer | ACID transactions, time travel, schema enforcement |
| PySpark | Transformation | Scalable distributed processing |
| Python | Producer & ETL | Fast development, rich ecosystem |
| GitHub | Version control | CI/CD ready, team collaboration |

## Medallion Architecture

### 🥉 Bronze — Raw Ingestion
- Ingests data exactly as received — no modifications
- Adds metadata: ingestion_timestamp, source_system, processing_date
- Preserves original data for reprocessing
- Table: `healthcare_bronze.wait_times_raw`

### 🥈 Silver — Cleaned & Validated
- Removes null values from critical columns
- Deduplicates records by hospital_id and timestamp
- Validates ranges — wait times 0–72 hours, patients > 0
- Classifies wait severity: LOW (<4hrs) | MEDIUM (4–12hrs) | HIGH (>12hrs)
- Table: `healthcare_silver.wait_times_clean`

### 🥇 Gold — Business Metrics
- Aggregates by city and date
- KPIs: avg/max/min wait times, total hospitals, avg patients waiting
- Business-ready for dashboards and executive reporting
- Table: `healthcare_gold.city_metrics`

## Sample Output

| City | Avg Wait (hrs) | Max Wait | Hospitals |
|------|---------------|----------|-----------|
| Vancouver | 14.24 | 23.16 | 16 |
| Toronto | 13.45 | 23.85 | 22 |
| Calgary | 12.52 | 21.88 | 13 |
| Winnipeg | 12.11 | 23.82 | 25 |
| Halifax | 9.19 | 21.37 | 24 |

## Project Structure

canadian-healthcare-analytics/
├── health_producer.py # Real-time data producer → Event Hubs
├── bronze_ingestion.ipynb # Raw ingestion → Delta Bronze
├── silver_transformation.ipynb # Cleaning & validation → Delta Silver
├── gold_aggregation.ipynb # City KPIs → Delta Gold
├── .gitignore # Protects credentials
└── README.md


## Key Engineering Decisions

**Why Medallion Architecture?**
Separates concerns — raw, clean, and aggregated data serve different consumers. Bronze preserves history. Silver serves data scientists. Gold serves BI tools directly.

**Why Delta Lake over Parquet?**
ACID transactions prevent corrupt writes. Time travel enables auditing and rollback. Schema enforcement rejects bad data at ingestion.

**Why Event Hubs over direct ingestion?**
Decouples producers from consumers. Handles backpressure. Kafka-compatible so existing Kafka skills transfer directly.

## Author
**Sai Krishna Reddy Kaithi** | Data Engineer | Vancouver, BC
- Open Work Permit — available immediately
- linkedin.com/in/saikrishnareddykaithi