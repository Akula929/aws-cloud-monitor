# AWS Cloud Cost Monitor

AWS Cloud Cost Monitor — S3 auditing, EC2 monitoring, and automated cost reporting with Python and Boto3.

---

## Overview

This tool monitors your AWS environment for:
- S3 bucket security issues (public access, versioning, encryption)
- EC2 instance idle detection (low CPU usage)
- Automated CSV and HTML cost reports

---

## Project Structure

```
aws-cloud-monitor/
├── src/
│   ├── s3_auditor.py      # Audit S3 buckets for security & cost hygiene
│   └── reporter.py        # Generate CSV and HTML cost reports
├── config/
│   └── config.yaml        # AWS region and alert settings
├── requirements.txt
└── README.md
```

---

## Features

- **S3 Auditor**: Checks public access blocks, versioning, and encryption on all S3 buckets
- **Reporter**: Generates timestamped CSV and HTML reports with cost summaries and EC2 inventory
- Color-coded HTML dashboard with dark theme

---

## Setup

```bash
git clone https://github.com/Akula929/aws-cloud-monitor
cd aws-cloud-monitor
pip install -r requirements.txt

# Configure AWS credentials
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1

# Run S3 audit
python src/s3_auditor.py
```

---

## Tech Stack

- Python 3.10
- Boto3 (AWS SDK)
- PyYAML
- AWS S3, EC2, CloudWatch

---

## What I Learned

- Working with AWS Boto3 SDK for real-time cloud resource inspection
- Building automated security and cost hygiene pipelines
- Generating multi-format reports (CSV + HTML) from live cloud data
