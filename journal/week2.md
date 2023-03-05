# Week 2 — Distributed Tracing

- add/test/verify RollBar to Frontend and Backend
- add/test/verify OTEL with honeycomb to Backend
- add/test/verify X-RAY to Backend
- add/test/verify CloudWatch Logs to Backend

## Local testing

```bash
export FRONTEND_URL="*"
export BACKEND_URL="*"
export OTEL_EXPORTER_OTLP_ENDPOINT="https://api.honeycomb.io"
export OTEL_EXPORTER_OTLP_HEADERS="x-honeycomb-team=${HONEYCOMB_API_KEY}"
export OTEL_SERVICE_NAME=gitpod-docker-compose-backend-flask
export FLASK_DEBUG=true
export AWS_REGION="eu-central-1"
python3 -m flask run --host=0.0.0.0 --port=4567
```

## x-ray

```bash
aws xray create-group \
   --group-name "Cruddur" \
   --filter-expression "service(\"backend-flask\") {fault OR error}"
aws xray create-sampling-rule --cli-input-json file://aws/json/xray.json
```
