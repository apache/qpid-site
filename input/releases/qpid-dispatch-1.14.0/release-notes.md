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

# Qpid Dispatch 1.14.0 Release Notes

Dispatch is a lightweight AMQP 1.0 message router. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-1759](https://issues.apache.org/jira/browse/DISPATCH-1759) - Update console dependency for react-scripts
 - [DISPATCH-1761](https://issues.apache.org/jira/browse/DISPATCH-1761) - Update console testing library to most recent version

## Bugs fixed

 - [DISPATCH-1752](https://issues.apache.org/jira/browse/DISPATCH-1752) - Router config for policy test creates a log that is not written to a file
 - [DISPATCH-1755](https://issues.apache.org/jira/browse/DISPATCH-1755) - [doc] Policy additions to qdstat are not described in docs
 - [DISPATCH-1760](https://issues.apache.org/jira/browse/DISPATCH-1760) - At boot time config processing should create listeners last
 - [DISPATCH-1762](https://issues.apache.org/jira/browse/DISPATCH-1762) - Connector ssl config errors must prohibit connections
 - [DISPATCH-1764](https://issues.apache.org/jira/browse/DISPATCH-1764) - At boot time config processing should create connectors later
 - [DISPATCH-1765](https://issues.apache.org/jira/browse/DISPATCH-1765) - use connection-capabilities for streaming-links support detection
 - [DISPATCH-1766](https://issues.apache.org/jira/browse/DISPATCH-1766) - Stale code for 'listener trustedCertsFile' should be removed
 - [DISPATCH-1769](https://issues.apache.org/jira/browse/DISPATCH-1769) - Need to fix dispatch use of Proton SASL extension API for Proton 0.33