;;
;; Licensed to the Apache Software Foundation (ASF) under one
;; or more contributor license agreements.  See the NOTICE file
;; distributed with this work for additional information
;; regarding copyright ownership.  The ASF licenses this file
;; to you under the Apache License, Version 2.0 (the
;; "License"); you may not use this file except in compliance
;; with the License.  You may obtain a copy of the License at
;;
;;   http://www.apache.org/licenses/LICENSE-2.0
;;
;; Unless required by applicable law or agreed to in writing,
;; software distributed under the License is distributed on an
;; "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
;; KIND, either express or implied.  See the License for the
;; specific language governing permissions and limitations
;; under the License.
;;

# Qpid Interop Test 0.2.0 Release Notes

Qpid Interop Test is a suite of AMQP interoperability tests.  More
about [Qpid Interop
Test]({{site_url}}/components/interop-test/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPIDIT-65](https://issues.apache.org/jira/browse/QPIDIT-65) - Add command-line controls to JMS_hdrs_props_test to control test more precisely
 - [QPIDIT-93](https://issues.apache.org/jira/browse/QPIDIT-93) - Optionally produce xUnit XML report with test results
 - [QPIDIT-109](https://issues.apache.org/jira/browse/QPIDIT-109) - Add ability to run Proton Python shims under Python 3
 - [QPIDIT-110](https://issues.apache.org/jira/browse/QPIDIT-110) - Add check for failure of Sender shim, if so, kill Receiver shim
 - [QPIDIT-112](https://issues.apache.org/jira/browse/QPIDIT-112) - Change test queue prefix from "jms.queue.qpid_interop" to "qit"
 - [QPIDIT-115](https://issues.apache.org/jira/browse/QPIDIT-115) - Print both stderr and stdout output when stderr output is detected on a shim
 - [QPIDIT-127](https://issues.apache.org/jira/browse/QPIDIT-127) - update to use the current v19 apache parent pom

## Bugs fixed

 - [QPIDIT-79](https://issues.apache.org/jira/browse/QPIDIT-79) - Stopping Python tests using ctrl+c sometimes results in a zombie shim
 - [QPIDIT-85](https://issues.apache.org/jira/browse/QPIDIT-85) - Tests don't limit the number of times it tries to connect to a broker
 - [QPIDIT-106](https://issues.apache.org/jira/browse/QPIDIT-106) - Cmake does not find custom-installed maven
 - [QPIDIT-113](https://issues.apache.org/jira/browse/QPIDIT-113) - AMQP.NetLite shims produce error message on stderr which should be ignored
 - [QPIDIT-114](https://issues.apache.org/jira/browse/QPIDIT-114) - [AMQP.NetLite] AMQP char type is not supported, but is not excluded from test
 - [QPIDIT-128](https://issues.apache.org/jira/browse/QPIDIT-128) - misuse of JAVA_HOME causes tests to error without clear indication why
 - [QPIDIT-129](https://issues.apache.org/jira/browse/QPIDIT-129) - tests reference wrong 'shim' version for Qpid JMS
 - [QPIDIT-130](https://issues.apache.org/jira/browse/QPIDIT-130) - 'utils' module is versioned incorrectly

## Tasks

 - [QPIDIT-37](https://issues.apache.org/jira/browse/QPIDIT-37) - Add test timeout to receiver shims so that when not all expected messages are received, the test does not wait indefinitely
 - [QPIDIT-61](https://issues.apache.org/jira/browse/QPIDIT-61) - Condense common code from the Python tests into a test module.
 - [QPIDIT-107](https://issues.apache.org/jira/browse/QPIDIT-107) - Add support for JMS message properties in ProtonCpp shim
 - [QPIDIT-119](https://issues.apache.org/jira/browse/QPIDIT-119) - Add AMQP complex type test