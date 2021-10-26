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

# Qpid ProtonJ2 1.0.0-M3 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2419](https://issues.apache.org/jira/browse/PROTON-2419) - [ProtonJ2] Use HTTPS where possible in project Maven pom.xml files

## Bugs fixed

 - [PROTON-2390](https://issues.apache.org/jira/browse/PROTON-2390) - wrong direction indicator used for incoming protocol headers
 - [PROTON-2410](https://issues.apache.org/jira/browse/PROTON-2410) - Buffer compare uses incorrect read index for input buffer
 - [PROTON-2428](https://issues.apache.org/jira/browse/PROTON-2428) - [ProtonJ2] Allow ClientOptions to be supplied without requiring container Id

## Tasks

 - [PROTON-2392](https://issues.apache.org/jira/browse/PROTON-2392) - Test Driver TXN declare handler fails when message format is not null
 - [PROTON-2393](https://issues.apache.org/jira/browse/PROTON-2393) - Enhancments to the AMQP Test driver
 - [PROTON-2394](https://issues.apache.org/jira/browse/PROTON-2394) - Javadocs fixs and updates
 - [PROTON-2395](https://issues.apache.org/jira/browse/PROTON-2395) - Update ProtonJ2 test dependencies to latest
 - [PROTON-2398](https://issues.apache.org/jira/browse/PROTON-2398) - Fix some spelling errors in codec API and other minor cleanups
 - [PROTON-2412](https://issues.apache.org/jira/browse/PROTON-2412) - Update Netty dependencies to latest release
 - [PROTON-2418](https://issues.apache.org/jira/browse/PROTON-2418) - [ProtonJ2] Fix tests in Client ReceiverTests not checking correct expectations
 - [PROTON-2420](https://issues.apache.org/jira/browse/PROTON-2420) - Fix some potential code issues found using static analysis tooling
 - [PROTON-2423](https://issues.apache.org/jira/browse/PROTON-2423) - Update slf4j to latest 1.7 release series