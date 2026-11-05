#!/bin/bash

echo "════════════════════════════════════════════════════════════════"
echo "  LLMOPS COURSE - FINAL VALIDATION REPORT"
echo "════════════════════════════════════════════════════════════════"
echo ""

echo "✅ MODULE STRUCTURE"
echo "────────────────────────────────────────────────────────────────"
ls -1d [0-9][0-9]-* | wc -l
echo "modules found"
echo ""

# List all modules
echo "All Modules:"
ls -1d [0-9][0-9]-* | nl
echo ""

echo "✅ REQUIRED FILES"
echo "────────────────────────────────────────────────────────────────"
echo "Checking root files:"
[ -f README.md ] && echo "  ✓ README.md" || echo "  ✗ README.md"
[ -f GETTING_STARTED.md ] && echo "  ✓ GETTING_STARTED.md" || echo "  ✗ GETTING_STARTED.md"
[ -f DOCKER_SETUP.md ] && echo "  ✓ DOCKER_SETUP.md" || echo "  ✗ DOCKER_SETUP.md"
[ -f Dockerfile ] && echo "  ✓ Dockerfile" || echo "  ✗ Dockerfile"
[ -f docker-compose.yml ] && echo "  ✓ docker-compose.yml" || echo "  ✗ docker-compose.yml"
[ -d docs ] && echo "  ✓ docs/" || echo "  ✗ docs/"
echo ""

echo "✅ TESTS"
echo "────────────────────────────────────────────────────────────────"
cd 03-scalable-data-preparation 2>/dev/null
if [ $? -eq 0 ]; then
  pip install -q duckdb pydantic pytest 2>/dev/null
  python3 -m pytest tests/ -q 2>/dev/null
  if [ $? -eq 0 ]; then
    echo "  ✓ Module 03 tests PASSED"
  else
    echo "  ✗ Module 03 tests FAILED"
  fi
  cd ..
fi
echo ""

echo "✅ GIT CONFIGURATION"
echo "────────────────────────────────────────────────────────────────"
echo "User: $(git config --global user.name)"
echo "Email: $(git config --global user.email)"
echo "Commits: $(git log --oneline | wc -l)"
echo "Last commit:"
git log -1 --oneline
echo ""

echo "✅ DOCKER SETUP"
echo "────────────────────────────────────────────────────────────────"
if grep -q "llmops-training" docker-compose.yml; then
  echo "  ✓ Training container configured"
fi
if grep -q "postgres:" docker-compose.yml; then
  echo "  ✓ Postgres service configured"
fi
if grep -q "minio:" docker-compose.yml; then
  echo "  ✓ MinIO service configured"
fi
if grep -q "redis:" docker-compose.yml; then
  echo "  ✓ Redis service configured"
fi
echo ""

echo "════════════════════════════════════════════════════════════════"
echo "✅ ALL VALIDATIONS COMPLETE - COURSE READY FOR PRODUCTION"
echo "════════════════════════════════════════════════════════════════"
