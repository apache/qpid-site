#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

export PYTHONPATH := python

OUTPUT_DIR := output
SITE_URL := file:$(abspath ${OUTPUT_DIR})

ifdef RELEASE
    ifndef ISSUES_RELEASE
        ISSUES_RELEASE := ${RELEASE}
    endif

    ifndef SOURCE_RELEASE
        SOURCE_RELEASE := ${RELEASE}
    endif
endif

SOURCE_MODULES := broker-j cpp dispatch interop-test jms jms-amqp-0-x proton proton-j protonj2 proton-dotnet python

.PHONY: default
default: render

.PHONY: help
help:
	@echo "[default]       Equivalent to 'make render'"
	@echo "render          Renders input/* to output/"
	@echo "publish         Renders input/* to content/"
	@echo "clean           Removes output/"
	@echo "check-links [INTERNAL=1] [EXTERNAL=0]"
	@echo "                Verify that all links have targets"
	@echo "gen-proton-release RELEASE=\$$VERSION [CHECKOUT_DIR=\$$DIR]"
	@echo "                Generate Qpid Proton release content"
	@echo "gen-proton-j-release RELEASE=\$$VERSION [CHECKOUT_DIR=\$$DIR]"
	@echo "                Generate Qpid Proton-J release content"
	@echo "gen-protonj2-release RELEASE=\$$VERSION [CHECKOUT_DIR=\$$DIR]"
	@echo "                Generate Qpid ProtonJ2 release content"
	@echo "gen-proton-dotnet-release RELEASE=\$$VERSION [CHECKOUT_DIR=\$$DIR]"
	@echo "                Generate Qpid Proton DotNet release content"
	@echo "gen-dispatch-release RELEASE=\$$VERSION [CHECKOUT_DIR=\$$DIR]"
	@echo "                Generate Qpid Dispatch release content"
	@echo "gen-jms-release RELEASE=\$$VERSION [CHECKOUT_DIR=\$$DIR]"
	@echo "                Generate Qpid JMS release content"
	@echo "gen-cpp-release RELEASE=\$$VERSION [CHECKOUT_DIR=\$$DIR]"
	@echo "                Generate Qpid C++ release content"

.PHONY: render
render:
	scripts/render ${SITE_URL} input ${OUTPUT_DIR}
	@echo "See the output in your browser at ${SITE_URL}/index.html"

.PHONY: publish
publish: 
	scripts/render "" input content
	git status input content
	@echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	@echo "NOTICE! One more step remains!"
	@echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	@echo "Use git to commit and push the changes."
	@echo "Keep in mind that you may need to git add new files."
	@echo "Also keep in mind to git rm matching files from content/ that have been removed from input/."

.PHONY: devel-publish
devel-publish: TAG := "head"
devel-publish: OUTPUT_DIR := $(shell mktemp -d --dry-run)
devel-publish: SITE_URL := /~${USER}/qpid-site/${TAG}
devel-publish:
	scripts/render ${SITE_URL} input ${OUTPUT_DIR}
	chmod 755 ${OUTPUT_DIR}
	rsync -av ${OUTPUT_DIR}/ ${USER}@people.apache.org:public_html/qpid-site/${TAG}
	rm -rf ${OUTPUT_DIR}

.PHONY: check-output-files
check-output-files:
	scripts/render "" input content
	scripts/check-output-files ${SITE_URL} input content

.PHONY: check-links
check-links: INTERNAL := 1
check-links: EXTERNAL := 0
check-links:
	scripts/render ${SITE_URL} input ${OUTPUT_DIR}
	scripts/check-links ${SITE_URL} input ${OUTPUT_DIR} ${INTERNAL} ${EXTERNAL}

.PHONY: clean
clean:
	rm -rf ${OUTPUT_DIR}
	find python -name \*.pyc -delete

.PHONY: gen-amqp-type-reference
gen-amqp-type-reference:
	scripts/gen-amqp-type-reference misc/amqp > input/amqp/type-reference.html.in

define RELEASE_TEMPLATE =
.PHONY: gen-${1}-release
gen-${1}-release: gen-${1}-release-page gen-${1}-release-notes gen-${1}-release-docs

.PHONY: gen-${1}-release-%
gen-${1}-release-%: RELEASE_DIR := input/releases/qpid-${1}-$${RELEASE}
gen-${1}-release-%:
	scripts/gen-${1}-release-$$* $${RELEASE} $${ISSUES_RELEASE} $${SOURCE_RELEASE} $${RELEASE_DIR} $${CHECKOUT_DIR}
endef

$(foreach module,${SOURCE_MODULES},$(eval $(call RELEASE_TEMPLATE,${module})))

.PHONY: update-%
update-%:
	curl "https://raw.githubusercontent.com/ssorj/$*/main/python/$*.py" -o python/$*.py
