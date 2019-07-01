CUR_DIR = $(shell echo "${PWD}")

# For python format checker. Default is 78
PEP8_MAX_LINE_LENGTH = 85

##########################
# Help screen. invoked by any of: 'make', 'make default', 'make help'
##########################
.PHONY: default
default:
	@echo "Please specify a target. The choices are:"
	@echo ""
	@echo "----------------------------------- Development ------------------------------------"
	@echo "pip-freeze : run pip freeze and update requirements.txt"
	@echo ""
	@echo "---------------------------------- Unit Testing ------------------------------------"
	@echo "test-all      : Run all tests"
	@echo "check-fmt     : Run pycodestyle (aka pep8) and report results"
	@echo "test-static   : Run static analysis tool: pylint"

.PHONY: help
help: default
	@echo ""

#################################
# Install targets
#################################
.PHONY: pip-freeze
pip-freeze:
	@echo "+ $@"
	@pip freeze  > requirements.txt

#################################
# test targets
#################################
.PHONY: check-fmt
check-fmt:
	@echo "+ $@"
	pycodestyle --filename='*.py' --exclude='*.sh,*.md,*.txt,Makefile,*.swp' --max-line-length=${PEP8_MAX_LINE_LENGTH} *

.PHONY: test-static
test-static:
	@echo "+ $@"
	pylint solutions

.PHONY: test-all
test-all: check-fmt test-static
