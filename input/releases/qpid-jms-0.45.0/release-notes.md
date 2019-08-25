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

# Qpid JMS 0.45.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-471](https://issues.apache.org/jira/browse/QPIDJMS-471) - support message tracing using OpenTracing

## Bugs fixed

 - [QPIDJMS-467](https://issues.apache.org/jira/browse/QPIDJMS-467) - Provide consistent stack trace information in client JMS Exceptions
 - [QPIDJMS-468](https://issues.apache.org/jira/browse/QPIDJMS-468) - send dispositions when CLIENT_ACK session closed without calling acknowledge

## Tasks

 - [QPIDJMS-465](https://issues.apache.org/jira/browse/QPIDJMS-465) - update to Netty 4.1.39
 - [QPIDJMS-466](https://issues.apache.org/jira/browse/QPIDJMS-466) - update various test dependencies
 - [QPIDJMS-469](https://issues.apache.org/jira/browse/QPIDJMS-469) - Remove some unused code leftover from previous refactoring
 - [QPIDJMS-470](https://issues.apache.org/jira/browse/QPIDJMS-470) - update to Proton-J 0.33.2