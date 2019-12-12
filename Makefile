MAJOR?=0
MINOR?=1

VERSION=$(MAJOR).$(MINOR)

BUILD_DATE=$(shell date +%Y%m%d.%H%M%S)

APP_NAME = rosettacode_solutions

# Our docker Hub account name
HUB_NAMESPACE = dockertesteng

# location of Dockerfiles
DOCKER_FILE_DIR = .
DOCKERFILE = ${DOCKER_FILE_DIR}/Dockerfile

IMAGE_NAME = ${APP_NAME}

CUR_DIR = $(shell echo "${PWD}")

# For python format checker. Default is 78
PEP8_MAX_LINE_LENGTH = 85
CODE_STYLE_EXCLUDE = '*.sh,*.md,*.txt,Dockerfile,Makefile,LICENSE,*.swp'
#
SOLUTIONS_DIR = solutions
RUN_SCRIPT = ./run-all.sh

##########################
# Help screen. invoked by any of: 'make', 'make default', 'make help'
##########################
.PHONY: default
default:
	@echo "Please specify a target. The choices are:"
	@echo ""
	@echo "---------------------------------- Run Solutions -----------------------------------"
	@echo "run         : Run all solutions. Halt if any solution fails"
	@echo ""
	@echo "----------------------------------- Development ------------------------------------"
	@echo "pip-freeze  : Run pip freeze and update requirements.txt"
	@echo ""
	@echo "---------------------------------- Unit Testing ------------------------------------"
	@echo "test-all    : Run all static analysis tests"
	@echo "check-fmt   : Run pycodestyle (aka pep8) and report results"
	@echo "test-static : Run static analysis tool: pylint"
	@echo ""
	@echo "------------------------------------ Docker ----------------------------------------"
	@echo "image       : Build image ${IMAGE_NAME}:${VERSION}"
	@echo "clean-image : Run docker rmi ${IMAGE_NAME}:${VERSION}"
	@echo "run-docker  : Build image and run all solutions in a container"
	@echo ""


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
# run targets
.PHONY: run
run:
	@echo "+ $@"
	${RUN_SCRIPT}

#################################
# test targets
#################################
.PHONY: check-fmt
check-fmt:
	@echo "+ $@"
	cd ${SOLUTIONS_DIR}; pycodestyle --filename='*.py' --exclude=${CODE_STYLE_EXCLUDE} --max-line-length=${PEP8_MAX_LINE_LENGTH} *

.PHONY: test-static
test-static:
	@echo "+ $@"
	pylint ${SOLUTIONS_DIR}

.PHONY: test-all
test-all: check-fmt test-static

#################################
# docker
#################################
.PHONY: clean-image
clean-image:
	@echo "+ $@"
	@for img in `docker images ${IMAGE_NAME} --format '{{ .Repository}}:{{ .Tag }}'`; do \
		echo docker rmi $$img; docker rmi $$img;\
	done

.PHONY: image
image:
	@echo "+ $@"
	@docker build  -t ${IMAGE_NAME}:${VERSION} -f ./${DOCKERFILE} .
	@docker tag ${IMAGE_NAME}:${VERSION} ${IMAGE_NAME}:latest
	@echo 'Done.'
	@docker images --format '{{.Repository}}:{{.Tag}}\t\t Built: {{.CreatedSince}}\t\tSize: {{.Size}}' | grep ${IMAGE_NAME}:${VERSION}

.PHONY: run-docker
run-docker: clean-image image
	@echo "+ $@"
	@docker run --rm rosettacode_solutions:latest ./run-all.sh
