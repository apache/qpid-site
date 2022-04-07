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

# Qpid ProtonJ2 1.0.0-M5 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2499](https://issues.apache.org/jira/browse/PROTON-2499) - Reduce overhead of Stream Sender message operations
 - [PROTON-2505](https://issues.apache.org/jira/browse/PROTON-2505) - Improve stream sender reconnect detection for in-progress message streams

## Bugs fixed

 - [PROTON-2490](https://issues.apache.org/jira/browse/PROTON-2490) - SASL to AMQP handoff is unsuccessful in server contexts (e.g. for peer-to-peer)
 - [PROTON-2504](https://issues.apache.org/jira/browse/PROTON-2504) - Message Properties type is not properly filtering for valid CorrelationId types
 - [PROTON-2507](https://issues.apache.org/jira/browse/PROTON-2507) - AMQP Test Peer can select the wrong handle for attach response
 - [PROTON-2510](https://issues.apache.org/jira/browse/PROTON-2510) - Client Transaction recovery can fail if detach response is delayed
 - [PROTON-2513](https://issues.apache.org/jira/browse/PROTON-2513) - Connection and Client CloseAsync are not yet operating asynchronously
 - [PROTON-2524](https://issues.apache.org/jira/browse/PROTON-2524) - protonj2 stream receiver does not always expand the credit window correctly

## Tasks

 - [PROTON-2486](https://issues.apache.org/jira/browse/PROTON-2486) - Update Netty dependencies to latest release
 - [PROTON-2496](https://issues.apache.org/jira/browse/PROTON-2496) - Update slf4j to latest 1.7 release series
 - [PROTON-2515](https://issues.apache.org/jira/browse/PROTON-2515) - Update test dependencies to latest releases