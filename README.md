markdown
# Canadian Healthcare Analytics Platform

## Overview
End-to-end real-time healthcare data pipeline processing hospital wait times across Canadian cities using Azure Databricks, Delta Lake, and Medallion Architecture.

## Architecture

DATA SOURCE
└── Health Data Simulator (Python Producer)
└── Sends real-time hospital wait times every 5 seconds

INGESTION
└── Azure Event Hubs (Kafka-compatible message bus)

PROCESSING — MEDALLION ARCHITECTURE
├── Bronze Layer — Raw data as received
├── Silver Layer — Cleaned and validated
└── Gold Layer — Aggregated city metrics

INFRASTRUCTURE
├── Azure Event Hubs
├── Azure Databricks + Apache Spark 4.0
└── Delta Lake — ACID compliant storage


## Tech Stack

| Layer | Technology |
|-------|-----------|
| Ingestion | Azure Event Hubs |
| Processing | Azure Databricks + PySpark |
| Storage | Delta Lake |
| Language | Python + PySpark + SQL |
| Version Control | GitHub |

## Project Structure

canadian-healthcare-analytics/
├── health_producer.py
├── bronze_ingestion.ipynb
├── silver_transformation.ipynb
├── gold_aggregation.ipynb
└── README.md


## Cities Covered
Vancouver — Toronto — Calgary — Winnipeg — Halifax

## Author
Sai Krishna Reddy Kaithi | Data Engineer | Vancouver BC