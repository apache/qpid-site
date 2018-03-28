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

# Qpid JMS 0.31.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-364](https://issues.apache.org/jira/browse/QPIDJMS-364) - dont hide ClassNotFoundException when setting properties via FactoryFinder
 - [QPIDJMS-367](https://issues.apache.org/jira/browse/QPIDJMS-367) - Add support for XOAUTH2 SASL authentication mechanism

## Bugs fixed

 - [QPIDJMS-365](https://issues.apache.org/jira/browse/QPIDJMS-365) - failover.reconnectDelay not applied between attempts if peer remote-closes during connection
 - [QPIDJMS-366](https://issues.apache.org/jira/browse/QPIDJMS-366) - session commit hangs if server remote-closes and failover.maxReconnectAttempts is exhausted
 - [QPIDJMS-368](https://issues.apache.org/jira/browse/QPIDJMS-368) - Connection URL keystore/truststore/user passwords can be reported unmasked as part of client logs
 - [QPIDJMS-369](https://issues.apache.org/jira/browse/QPIDJMS-369) - Failover doesn't apply max reconnect attempts on initial connect when remote is closing on the Open frame