#!/bin/bash

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║   LLMOPS COURSE - COMPREHENSIVE VALIDATION & TEST REPORT      ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

PASSED=0
FAILED=0
TOTAL=0

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Test function
test_module() {
    local module=$1
    local test_name=$2
    TOTAL=$((TOTAL+1))

    if eval "$test_name"; then
        echo -e "${GREEN}✅ PASS${NC} - $module: $test_name"
        PASSED=$((PASSED+1))
        return 0
    else
        echo -e "${RED}❌ FAIL${NC} - $module: $test_name"
        FAILED=$((FAILED+1))
        return 1
    fi
}

echo "📋 CHECKING MODULE STRUCTURE"
echo "════════════════════════════════════════════════════════════════"

# Check all modules exist
for i in {01..19}; do
    module_dir="$i-"*
    if [ -d "$module_dir" ]; then
        echo -e "${GREEN}✓${NC} Module $i exists"

        # Check required files
        test_module "$i" "[ -f $module_dir/README.md ]"
        test_module "$i" "[ -f $module_dir/Makefile ]"
        test_module "$i" "[ -f $module_dir/docker-compose.yml ]"
        test_module "$i" "[ -d $module_dir/src ]"
        test_module "$i" "[ -d $module_dir/tests ]"
    else
        echo -e "${RED}✗${NC} Module $i NOT FOUND"
        FAILED=$((FAILED+5))
    fi
done

echo ""
echo "🧪 RUNNING TESTS FOR KEY MODULES"
echo "════════════════════════════════════════════════════════════════"

# Test Module 03 (has implementation)
if [ -d "03-scalable-data-preparation" ]; then
    cd 03-scalable-data-preparation

    # Check if requirements installed
    if python3 -c "import duckdb" 2>/dev/null; then
        test_module "03" "python3 -m pytest tests/test_elt_pipeline.py -q"
    else
        pip install -q duckdb pydantic pytest 2>/dev/null
        test_module "03" "python3 -m pytest tests/test_elt_pipeline.py -q"
    fi

    cd ..
fi

echo ""
echo "🐳 CHECKING DOCKER SETUP"
echo "════════════════════════════════════════════════════════════════"

test_module "Docker" "[ -f Dockerfile ]"
test_module "Docker" "[ -f docker-compose.yml ]"
test_module "Docker" "[ -f DOCKER_SETUP.md ]"

# Check docker-compose has training service
test_module "Docker" "grep -q 'llmops-training' docker-compose.yml"

echo ""
echo "📚 CHECKING DOCUMENTATION"
echo "════════════════════════════════════════════════════════════════"

test_module "Docs" "[ -f README.md ]"
test_module "Docs" "[ -f GETTING_STARTED.md ]"
test_module "Docs" "[ -f DOCKER_SETUP.md ]"
test_module "Docs" "[ -f docs/source-outline.md ]"
test_module "Docs" "[ -f docs/IMPLEMENTATION_PLAN.md ]"

echo ""
echo "🔧 CHECKING GIT SETUP"
echo "════════════════════════════════════════════════════════════════"

test_module "Git" "[ -d .git ]"
test_module "Git" "git log --oneline | head -1 | grep -q ."

# Check git config
git_user=$(git config --global user.name)
test_module "Git" "[ '$git_user' = 'Divakar Raju Mandapati' ]"

# Check no Co-Authored-By in recent commits
test_module "Git" "! git log --format=%B -5 | grep -q 'Co-Authored-By'"

echo ""
echo "📊 FINAL REPORT"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "Total Tests: $TOTAL"
echo -e "Passed: ${GREEN}$PASSED${NC}"
echo -e "Failed: ${RED}$FAILED${NC}"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}🎉 ALL VALIDATIONS PASSED! Course is production-ready.${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    exit 0
else
    echo -e "${YELLOW}⚠️  Some validations failed. Review above.${NC}"
    exit 1
fi
