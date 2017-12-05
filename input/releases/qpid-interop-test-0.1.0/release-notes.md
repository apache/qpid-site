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

# Qpid Interop Test 0.1.0 Release Notes

Qpid Interop Test is a suite of AMQP interoperability tests.  More
about [Qpid Interop
Test]({{site_url}}/components/interop-test/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPIDIT-20](https://issues.apache.org/jira/browse/QPIDIT-20) - Add ability to detect broker, skip tests that fail for that broker
 - [QPIDIT-21](https://issues.apache.org/jira/browse/QPIDIT-21) - Add shims for C++ client
 - [QPIDIT-22](https://issues.apache.org/jira/browse/QPIDIT-22) - Add ability to run on Jenkins CI
 - [QPIDIT-32](https://issues.apache.org/jira/browse/QPIDIT-32) - Use Maven to build Java components
 - [QPIDIT-33](https://issues.apache.org/jira/browse/QPIDIT-33) - Add JMS message headers and properties to test suite
 - [QPIDIT-41](https://issues.apache.org/jira/browse/QPIDIT-41) - Rearrange test directory structure to better organize tests and shims
 - [QPIDIT-42](https://issues.apache.org/jira/browse/QPIDIT-42) - Split JMS message test into two separate tests: message bodies, and message headers/properties
 - [QPIDIT-44](https://issues.apache.org/jira/browse/QPIDIT-44) - Add AMQP large content test
 - [QPIDIT-53](https://issues.apache.org/jira/browse/QPIDIT-53) - Eliminate use of authentication when collecting broker connection properties
 - [QPIDIT-84](https://issues.apache.org/jira/browse/QPIDIT-84) - Update README, QUICKSTART, add a users' guide
 - [QPIDIT-96](https://issues.apache.org/jira/browse/QPIDIT-96) - Improvements in Java component management
 - [QPIDIT-98](https://issues.apache.org/jira/browse/QPIDIT-98) - Change Proton C++ Receiver shims to use latest non-deprecated API calls

## Bugs fixed

 - [QPIDIT-24](https://issues.apache.org/jira/browse/QPIDIT-24) - Broker identification failure blocks tests
 - [QPIDIT-34](https://issues.apache.org/jira/browse/QPIDIT-34) - Update to jsoncpp text format has broken test harness for all C++ shims
 - [QPIDIT-38](https://issues.apache.org/jira/browse/QPIDIT-38) - Artemis broker-added properties not handled correctly in python receive shim
 - [QPIDIT-40](https://issues.apache.org/jira/browse/QPIDIT-40) - Sender and Receiver threads don't stop when tests end in some error conditions
 - [QPIDIT-51](https://issues.apache.org/jira/browse/QPIDIT-51) - Method needed to skip sensing broker type
 - [QPIDIT-55](https://issues.apache.org/jira/browse/QPIDIT-55) - Proton install dir is hard coded into cmake
 - [QPIDIT-56](https://issues.apache.org/jira/browse/QPIDIT-56) - Rhea installs to /usr/lib regardless of cmake install dir
 - [QPIDIT-57](https://issues.apache.org/jira/browse/QPIDIT-57) - Cmake installer should check for presence of Node.js and Rhea client
 - [QPIDIT-66](https://issues.apache.org/jira/browse/QPIDIT-66) - Shims should install into a libexec directory, not into the Python site-packages path
 - [QPIDIT-67](https://issues.apache.org/jira/browse/QPIDIT-67) - Compile errors after recent header cleanup in Proton C++ bindings
 - [QPIDIT-69](https://issues.apache.org/jira/browse/QPIDIT-69) - JMS tests fail with "Import Error: no module names jms_types"
 - [QPIDIT-73](https://issues.apache.org/jira/browse/QPIDIT-73) - Rhea shim char type broken by recent updates to Rhea
 - [QPIDIT-82](https://issues.apache.org/jira/browse/QPIDIT-82) - JMS tests fail intermittently with null message
 - [QPIDIT-83](https://issues.apache.org/jira/browse/QPIDIT-83) - JAVA classpath points to maven repository rather than installed location

## Tasks

 - [QPIDIT-1](https://issues.apache.org/jira/browse/QPIDIT-1) - Initial code import
 - [QPIDIT-2](https://issues.apache.org/jira/browse/QPIDIT-2) - Add command-line options to control which shims and/or AMQP type combinations to run
 - [QPIDIT-13](https://issues.apache.org/jira/browse/QPIDIT-13) - Submit patch to Proton for AMQP type support needed by ProtonPython shim
 - [QPIDIT-16](https://issues.apache.org/jira/browse/QPIDIT-16) - Place Qpid JMS shim build management under Maven
 - [QPIDIT-17](https://issues.apache.org/jira/browse/QPIDIT-17) - Add JMS test suite
 - [QPIDIT-18](https://issues.apache.org/jira/browse/QPIDIT-18) - Use existing structured text representation standard for communicating between test and shims
 - [QPIDIT-47](https://issues.apache.org/jira/browse/QPIDIT-47) - Add Rhea javascript shim for AMQP types test
 - [QPIDIT-48](https://issues.apache.org/jira/browse/QPIDIT-48) - Add test options which allow separate addresses for the sender and receiver
 - [QPIDIT-52](https://issues.apache.org/jira/browse/QPIDIT-52) - Make qpid-interop-test installable
 - [QPIDIT-59](https://issues.apache.org/jira/browse/QPIDIT-59) - Create a HOWTO file on writing a new shim
 - [QPIDIT-60](https://issues.apache.org/jira/browse/QPIDIT-60) - Create a HOWTO file on writing a new test