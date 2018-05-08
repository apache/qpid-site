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

# Qpid JMS 0.32.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-375](https://issues.apache.org/jira/browse/QPIDJMS-375) - Enable setting of an "Authorization" Header during WebSocket connection handshake.
 - [QPIDJMS-379](https://issues.apache.org/jira/browse/QPIDJMS-379) - Reduce garbage created on input from transport
 - [QPIDJMS-380](https://issues.apache.org/jira/browse/QPIDJMS-380) - Implement ConnectionConsumer to enable use in resource adapters
 - [QPIDJMS-382](https://issues.apache.org/jira/browse/QPIDJMS-382) - limit outgoing frame sizes to configured maxFrameSize
 - [QPIDJMS-383](https://issues.apache.org/jira/browse/QPIDJMS-383) - Utilize new proton-j APIs to eleminate copying delivery buffers
 - [QPIDJMS-384](https://issues.apache.org/jira/browse/QPIDJMS-384) - Add support for user user defined extensions to override client configuration

## Bugs fixed

 - [QPIDJMS-372](https://issues.apache.org/jira/browse/QPIDJMS-372) - [SASL] [XOAUTH2] Access token validation too restrictive
 - [QPIDJMS-374](https://issues.apache.org/jira/browse/QPIDJMS-374) - Double encoded query parameters
 - [QPIDJMS-376](https://issues.apache.org/jira/browse/QPIDJMS-376) - notify the ExceptionListener when a consumer with a MessageListener remotely closes

## Tasks

 - [QPIDJMS-377](https://issues.apache.org/jira/browse/QPIDJMS-377) - Update testing dependencies (ActiveMQ, MiniKDC and Mockito)
 - [QPIDJMS-378](https://issues.apache.org/jira/browse/QPIDJMS-378) - Update Netty to latest 4.1.24.Final
 - [QPIDJMS-381](https://issues.apache.org/jira/browse/QPIDJMS-381) - update to proton-j 0.27.1
