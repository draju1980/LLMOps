# LLMOps Course - Complete Docker Setup

**Zero Local Installation Required** ✅

This guide runs the entire LLMOps course inside Docker containers with no local Python installation needed.

---

## Quick Start (30 seconds)

```bash
# 1. Clone the repo
git clone <repo-url>
cd LLMOps

# 2. Start all services (infrastructure + training environment)
docker-compose up -d

# 3. Enter the training container
docker exec -it llmops-training bash

# 4. Run any module (inside container)
cd 01-what-is-llmops && make test
cd 03-scalable-data-preparation && python3 src/duckdb_elt_pipeline.py

# Done! Everything runs in Docker.
```

---

## What's Inside Docker

### Infrastructure Services (Always Running)

| Service | Port | Purpose |
|---------|------|---------|
| **Postgres** | 5432 | Metadata store (MLflow, KFP, Prompt Registry) |
| **MinIO** | 9000, 9001 | S3-compatible object storage |
| **Redis** | 6379 | Semantic cache, session store |
| **Prometheus** | 9090 | Metrics collection |
| **Grafana** | 3000 | Dashboards & visualization |
| **Jaeger** | 16686 | Distributed tracing |
| **MLflow** | 5000 | Model registry & experiments |
| **Qdrant** | 6333, 6334 | Vector database for RAG |
| **Training** | (interactive) | Full course environment |

### Training Container

The `training` service includes:
- Python 3.11 with all dependencies pre-installed
- All 19 course modules
- DuckDB, pytest, FastAPI, etc.
- Connected to all infrastructure services
- Ready to run any module immediately

---

## Common Commands

### Start Everything

```bash
# Start all services in background
docker-compose up -d

# View logs
docker-compose logs -f training
docker-compose logs -f postgres

# Verify all services healthy
docker-compose ps
```

### Access Training Environment

```bash
# Interactive bash session
docker exec -it llmops-training bash

# Run a command directly
docker exec -it llmops-training python3 --version

# Run a specific module
docker exec -it llmops-training \
  bash -c "cd 03-scalable-data-preparation && python3 src/duckdb_elt_pipeline.py"
```

### Run Module Tests

```bash
# Inside container
docker exec -it llmops-training bash -c "cd 03-scalable-data-preparation && make test"

# Or interactively
docker exec -it llmops-training bash
cd 03-scalable-data-preparation
make test
```

### Stop All Services

```bash
# Stop containers (data persists in volumes)
docker-compose down

# Stop and remove volumes (clean slate)
docker-compose down -v

# Stop and remove everything
docker-compose down -v --remove-orphans
```

---

## Module Execution Examples

### Module 01: What is LLMOps?

```bash
docker exec -it llmops-training bash -c "
  cd 01-what-is-llmops
  make test
  python3 src/01_paradigm_shift.py
  python3 exercises/exercise_1_1.py
"
```

### Module 03: Scalable Data Preparation

```bash
docker exec -it llmops-training bash -c "
  cd 03-scalable-data-preparation
  pip install -r requirements.txt
  python3 src/duckdb_elt_pipeline.py
  python3 -m pytest tests/test_elt_pipeline.py -v
  python3 exercises/exercise_3_1.py
"
```

### Run All Module Tests

```bash
docker exec -it llmops-training bash -c "
  for dir in [0-9][0-9]-*/; do
    echo \"Testing \$dir...\"
    cd \$dir && python3 -m pytest tests/ -v || true && cd ..
  done
"
```

---

## Access Infrastructure Services

Once containers are running, access services from your host machine:

### Postgres (from host)

```bash
psql -h localhost -U llmops -d llmops_db -W
# Password: llmops-password
```

### MinIO (from host)

- Console: http://localhost:9001
- Access Key: minioadmin
- Secret Key: minioadmin-password

### Grafana (from host)

- URL: http://localhost:3000
- Username: admin
- Password: admin

### MLflow (from host)

- URL: http://localhost:5000
- Experiment tracking & model registry

### Jaeger (from host)

- URL: http://localhost:16686
- Distributed tracing UI

### Prometheus (from host)

- URL: http://localhost:9090
- Metrics & alerting

---

## Development Workflow

### Edit Code Locally, Run in Docker

Since the repo is mounted as a volume, changes made locally are immediately visible inside the container:

```bash
# 1. Edit code locally (your IDE)
# 2. Changes sync to Docker automatically
# 3. Run in container
docker exec -it llmops-training bash
cd 03-scalable-data-preparation
python3 src/duckdb_elt_pipeline.py
```

### Interactive Development

```bash
# Enter container
docker exec -it llmops-training bash

# Now you're in the container (no installation needed!)
cd 03-scalable-data-preparation
python3 -c "import duckdb; print(duckdb.__version__)"
python3 -m pytest tests/ -v
python3 src/duckdb_elt_pipeline.py

# Exit when done
exit
```

---

## Troubleshooting

### Services Not Healthy

```bash
# Check service status
docker-compose ps

# View logs for specific service
docker-compose logs postgres
docker-compose logs training

# Restart all services
docker-compose restart
```

### Volume Permissions Issues

```bash
# Fix ownership (Linux)
sudo chown -R $USER:$USER .

# Or run with sudo
sudo docker-compose up -d
```

### Clean Slate (Remove All Data)

```bash
# Remove containers and volumes
docker-compose down -v --remove-orphans

# Rebuild training image
docker-compose build --no-cache

# Restart
docker-compose up -d
```

### Python Package Issues

```bash
# Inside container, reinstall all packages
pip install --upgrade --force-reinstall -r /tmp/requirements.txt
```

---

## Production Deployment

### Build Custom Image

```bash
# Build training image
docker build -t llmops-training:latest .

# Push to registry
docker tag llmops-training:latest myregistry/llmops-training:latest
docker push myregistry/llmops-training:latest
```

### Docker Compose with Custom Registry

```yaml
training:
  image: myregistry/llmops-training:latest
  # ... rest of config
```

### Run on Remote Server

```bash
# On remote server
git clone <repo-url>
cd LLMOps
docker-compose -f docker-compose.yml up -d

# Access from local machine
docker exec -it llmops-training bash
```

---

## Learning Path (All in Docker)

```bash
# 1. Start containers
docker-compose up -d

# 2. Module 01: Paradigm Shift
docker exec -it llmops-training bash -c "cd 01-what-is-llmops && make lab"

# 3. Module 03: DuckDB Pipeline
docker exec -it llmops-training bash -c "cd 03-scalable-data-preparation && python3 src/duckdb_elt_pipeline.py"

# 4. Run all tests
docker exec -it llmops-training bash -c "
  for mod in 01-* 03-*; do
    echo \"Testing \$mod...\"
    cd \$mod && python3 -m pytest tests/ -v
    cd ..
  done
"

# 5. View infrastructure dashboards (from host)
# Grafana: http://localhost:3000
# MLflow: http://localhost:5000
# Jaeger: http://localhost:16686
```

---

## FAQ

### Q: Do I need to install Python locally?
**A:** No! Everything runs in Docker. Just have Docker installed.

### Q: Can I edit code in my favorite IDE?
**A:** Yes! The repo is mounted as a volume. Edit locally, run in Docker.

### Q: How do I debug failing code?
**A:** Enter the container interactively:
```bash
docker exec -it llmops-training bash
python3 -m pdb your_script.py
```

### Q: Can I run multiple modules in parallel?
**A:** Yes! Use separate docker exec commands in different terminals.

### Q: How do I save my work?
**A:** All files are on your host machine. Just use git:
```bash
git add .
git commit -m "Module X: completed"
```

### Q: What if I want to use a different Python version?
**A:** Edit the Dockerfile:
```dockerfile
FROM python:3.12-slim  # Changed from 3.11
```
Then rebuild: `docker-compose build --no-cache training`

---

## Architecture

```
┌─────────────────────────────────────────┐
│         Your Host Machine               │
│  (Edit code, run docker commands)       │
└────────────────────┬────────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │   Docker Desktop      │
         └────────────┬──────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
  ┌──────────┐  ┌──────────┐  ┌────────────┐
  │Training  │  │Infra     │  │Volumes     │
  │Container │  │Services  │  │(Data)      │
  └──────────┘  └──────────┘  └────────────┘

Everything runs in Docker!
Nothing installed on host machine!
```

---

## Support

- **Issue with Docker?** Check `docker-compose logs <service-name>`
- **Module fails?** Run `python3 -m pytest tests/ -v` inside container
- **Infrastructure question?** Check `docker-compose ps` to verify all services healthy

---

**Congratulations!** Your complete LLMOps course is now running in Docker with zero local installation. 🐳✨

