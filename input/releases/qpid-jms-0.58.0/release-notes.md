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

# Qpid JMS 0.58.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-527](https://issues.apache.org/jira/browse/QPIDJMS-527) - Add support for SCRAM-SHA-512 Sasl Authentication

## Bugs fixed

 - [QPIDJMS-529](https://issues.apache.org/jira/browse/QPIDJMS-529) - Remote link closure when producer send and close race and lead to close blocking forever
 - [QPIDJMS-530](https://issues.apache.org/jira/browse/QPIDJMS-530) - Potential NPE in JmsSession consumerClosed()

## Tasks

 - [QPIDJMS-531](https://issues.apache.org/jira/browse/QPIDJMS-531) - Update Netty to 4.1.63.Final and tcnative to 2.0.38.Final
 - [QPIDJMS-532](https://issues.apache.org/jira/browse/QPIDJMS-532) - Update the slf4j binding for log4j to 2.14.1 release
 - [QPIDJMS-533](https://issues.apache.org/jira/browse/QPIDJMS-533) - Update test dependencies JUnit and Mockito to latest