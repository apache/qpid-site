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

# Qpid JMS 0.44.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-460](https://issues.apache.org/jira/browse/QPIDJMS-460) - expand accepted types for delivery time annotation on received messages
 - [QPIDJMS-461](https://issues.apache.org/jira/browse/QPIDJMS-461) - JmsMessageIDBuilder::createMessageID can save StringBuilder allocations
 - [QPIDJMS-462](https://issues.apache.org/jira/browse/QPIDJMS-462) - isolate native transport class usage, allow excluding related dependencies.

## Bugs fixed

 - [QPIDJMS-464](https://issues.apache.org/jira/browse/QPIDJMS-464) - zero prefetch receive can hang if timeout reached whilst message is partially transferred

## Tasks

 - [QPIDJMS-463](https://issues.apache.org/jira/browse/QPIDJMS-463) - update surefire and jacoco plugins