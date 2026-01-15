# DATA-PIPELINE-DEVELOPMENT

###  PERSONAL INFORMATION
* **Company:** CODTECH IT SOLUTIONS
* **Name:** Vipin Nishad
* **Intern ID:** CTIS2391
* **Domain:** Data Science
* **Batch Duration:** 6 Weeks
* **Mentor:** Neela Santosh

---

###  PROJECT DESCRIPTION
This project focuses on the development of a production-grade industrial data pipeline designed to handle environmental sensor data. In modern industrial settings, data integrity is paramount. This pipeline implements a "Data Quality Gate" strategy, which is a professional standard in data engineering to ensure that downstream analytics or machine learning models are not fed "garbage" data.

The system begins by generating synthetic air quality data, including metrics for Temperature, Humidity, and CO2 levels. However, real-world sensors often malfunction due to hardware failure or environmental stress. To simulate this, the pipeline intentionally injects anomalous data points, such as impossible temperatures (500°C) or negative humidity levels.

The core logic of the task is the **Validation Gate**. Instead of simple cleaning, the pipeline performs a multi-step audit:
1. **Validation:** It checks every incoming record against defined physical boundaries (e.g., -10°C to 60°C).
2. **Segregation:** Records that fail these checks are not deleted; instead, they are routed to a specialized `sensor_errors_log.csv`. This provides an audit trail for maintenance teams to identify faulty sensors.
3. **Transformation:** Clean records are enhanced with "Air Quality" status labels based on CO2 thresholds, turning raw data into actionable business intelligence.
4. **Reporting:** The pipeline automatically generates a `pipeline_summary.json` providing statistical health checks and a `data_trends.png` visualization to monitor sensor stability over time.

This modular approach ensures the data remains reliable, traceable, and ready for high-level analytical tasks.

###  TOOLS & TECHNOLOGIES
* **Language:** Python 3.10
* **Libraries:** Pandas (Data manipulation), NumPy (Numerical processing), Matplotlib (Visualization)
* **Editor:** VS Code


###  OUTPUT
[IMAGE_OF_YOUR_TASK1_TREND_GRAPH_HERE]
