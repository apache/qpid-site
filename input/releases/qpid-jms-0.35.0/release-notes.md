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

# Qpid JMS 0.35.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-399](https://issues.apache.org/jira/browse/QPIDJMS-399) - Add ability to split a write and flush on the Transport into two operations
 - [QPIDJMS-401](https://issues.apache.org/jira/browse/QPIDJMS-401) - Minor code cleanups and performance improvements

## Bugs fixed

 - [QPIDJMS-403](https://issues.apache.org/jira/browse/QPIDJMS-403) - Failover handler doesn't release pending tasks that could complete on connection drop
 - [QPIDJMS-404](https://issues.apache.org/jira/browse/QPIDJMS-404) - Performance regressions on some platforms using new ProviderFuture implementation

## Tasks

 - [QPIDJMS-397](https://issues.apache.org/jira/browse/QPIDJMS-397) - Update to the current v19 apache parent pom
 - [QPIDJMS-398](https://issues.apache.org/jira/browse/QPIDJMS-398) - Update testing dependencies and bundle plugin to latest
 - [QPIDJMS-405](https://issues.apache.org/jira/browse/QPIDJMS-405) - update to proton-j 0.28.0
 - [QPIDJMS-406](https://issues.apache.org/jira/browse/QPIDJMS-406) - update to Netty 4.1.27