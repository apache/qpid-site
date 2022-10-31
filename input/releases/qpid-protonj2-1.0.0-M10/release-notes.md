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

# Qpid ProtonJ2 1.0.0-M10 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## Bugs fixed

 - [PROTON-2616](https://issues.apache.org/jira/browse/PROTON-2616) - Can't use `receiverOptions.sourceOptions().filters()` to set message selector for Artemis broker
 - [PROTON-2618](https://issues.apache.org/jira/browse/PROTON-2618) - Remote close with [condition = amqp:connection:forced] leads to exception thrown even though reconnect is enabled
 - [PROTON-2627](https://issues.apache.org/jira/browse/PROTON-2627) - [protonj2] Filtered version file in engine jar placed in wrong namespace
 - [PROTON-2628](https://issues.apache.org/jira/browse/PROTON-2628) - [protonj2] WS Connection test can generate OOM in some cases

## Tasks

 - [PROTON-2625](https://issues.apache.org/jira/browse/PROTON-2625) - [protonj2] Update Netty to latest release
 - [PROTON-2626](https://issues.apache.org/jira/browse/PROTON-2626) - [protonj2] Remove bundle packaging from the engine build
 - [PROTON-2630](https://issues.apache.org/jira/browse/PROTON-2630) - [protonj2] Update some javadocs with additional details and fix typos
 - [PROTON-2632](https://issues.apache.org/jira/browse/PROTON-2632) - [protonj2] Update test dependencies to latest releases