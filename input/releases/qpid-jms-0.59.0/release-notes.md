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

# Qpid JMS 0.59.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-528](https://issues.apache.org/jira/browse/QPIDJMS-528) - Improve logging of connection interruption and failure
 - [QPIDJMS-536](https://issues.apache.org/jira/browse/QPIDJMS-536) - Failover URIs should not be deduplicated based on name resolution

## Bugs fixed

 - [QPIDJMS-514](https://issues.apache.org/jira/browse/QPIDJMS-514) - thread for reconnecting a session is blocked forever
 - [QPIDJMS-534](https://issues.apache.org/jira/browse/QPIDJMS-534) - BalancedProviderFuture.sync stuck forever during connection recovery
 - [QPIDJMS-537](https://issues.apache.org/jira/browse/QPIDJMS-537) - replace Float/Double constructor usage marked deprecated for-removal

## Tasks

 - [QPIDJMS-538](https://issues.apache.org/jira/browse/QPIDJMS-538) - Update netty tcnative and mockito to latest releases