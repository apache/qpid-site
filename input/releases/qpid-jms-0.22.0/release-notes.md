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

# Qpid JMS 0.22.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-274](https://issues.apache.org/jira/browse/QPIDJMS-274) - Be able to REJECT messages in JmsRedeliveryPolicy
 - [QPIDJMS-278](https://issues.apache.org/jira/browse/QPIDJMS-278) - Add a fast path for the Accepted outcome into the producer
 - [QPIDJMS-279](https://issues.apache.org/jira/browse/QPIDJMS-279) - Add support for Netty Epoll transport
 - [QPIDJMS-281](https://issues.apache.org/jira/browse/QPIDJMS-281) - Add option to the transport to allow for tracing bytes in / out in the logs
 - [QPIDJMS-283](https://issues.apache.org/jira/browse/QPIDJMS-283) - Pipeline the declare that follows a transaction discharge for quicker processing
 - [QPIDJMS-285](https://issues.apache.org/jira/browse/QPIDJMS-285) - Throw a more meaningful exception when commit fails due to connection being down
 - [QPIDJMS-286](https://issues.apache.org/jira/browse/QPIDJMS-286) - Shorten the thread name given to the AmqpProvider executor thread

## Bugs fixed

 - [QPIDJMS-282](https://issues.apache.org/jira/browse/QPIDJMS-282) - creating a Connection can time out if a pipelined Open frame arrives before the client sends its own
 - [QPIDJMS-284](https://issues.apache.org/jira/browse/QPIDJMS-284) - client includes 'global' source capability for some consumers it shouldn't

## Tasks

 - [QPIDJMS-275](https://issues.apache.org/jira/browse/QPIDJMS-275) - Update Netty to latest release
 - [QPIDJMS-276](https://issues.apache.org/jira/browse/QPIDJMS-276) - Update slf4j to latest release