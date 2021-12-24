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

# Qpid ProtonJ2 1.0.0-M4 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## Bugs fixed

 - [PROTON-2452](https://issues.apache.org/jira/browse/PROTON-2452) - Connection Dynamic Receiver create API not applying user configuration in all cases
 - [PROTON-2454](https://issues.apache.org/jira/browse/PROTON-2454) - Singular body section not always cleared when bulk adding multiple sections
 - [PROTON-2462](https://issues.apache.org/jira/browse/PROTON-2462) - Incorrect error message in stream receiver message for AMQP value bodies not readable 
 - [PROTON-2463](https://issues.apache.org/jira/browse/PROTON-2463) - Update Netty dependencies to latest release

## Tasks

 - [PROTON-2475](https://issues.apache.org/jira/browse/PROTON-2475) - Update test dependencies to latest releases
 - [PROTON-2478](https://issues.apache.org/jira/browse/PROTON-2478) - Switch to slf4j-simple for logging in tests and examples