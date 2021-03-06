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

# Qpid JMS 0.49.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## Bugs fixed

 - [QPIDJMS-485](https://issues.apache.org/jira/browse/QPIDJMS-485) - AmqpJmsBytesMessageFacade does not copy the content-type
 - [QPIDJMS-491](https://issues.apache.org/jira/browse/QPIDJMS-491) - Race on handling protocol level errors can lead to connection close waiting for the full close timeout

## Tasks

 - [QPIDJMS-488](https://issues.apache.org/jira/browse/QPIDJMS-488) - update to Netty 4.1.45
 - [QPIDJMS-489](https://issues.apache.org/jira/browse/QPIDJMS-489) - Update test dependencies
 - [QPIDJMS-490](https://issues.apache.org/jira/browse/QPIDJMS-490) - Update slf4j to latest point release 1.7.30