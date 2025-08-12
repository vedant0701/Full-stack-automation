# Cloud-Native End-to-End Automation Framework

This project automates:
- UI Testing (Selenium + Behave)
- API Testing (Python Requests)
- Kafka Event Testing (kafka-python)

It is fully containerized (Docker) and orchestrated using Kubernetes, with CI/CD integration.

## Initial Setup
```bash
git clone <your-repo-url>
cd cloud-native-automation-framework
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
