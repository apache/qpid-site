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

# Qpid JMS 0.38.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-416](https://issues.apache.org/jira/browse/QPIDJMS-416) - Move protocol processing work into the netty event loop thread
 - [QPIDJMS-418](https://issues.apache.org/jira/browse/QPIDJMS-418) - Clean up the usage of Symbol type and conversion to Symbol from String
 - [QPIDJMS-420](https://issues.apache.org/jira/browse/QPIDJMS-420) - Improve performance of MessageConsumer processing
 - [QPIDJMS-421](https://issues.apache.org/jira/browse/QPIDJMS-421) - Improve performance of MessageProducer by caching common annotation encodings
 - [QPIDJMS-423](https://issues.apache.org/jira/browse/QPIDJMS-423) - Log only connection URI in the connection initialized event handler
 - [QPIDJMS-429](https://issues.apache.org/jira/browse/QPIDJMS-429) - Refactor sender and receive code to use newer proton-j APIs 

## Bugs fixed

 - [QPIDJMS-419](https://issues.apache.org/jira/browse/QPIDJMS-419) - JMS Session is sometimes not recovered on failover reconnect

## Tasks

 - [QPIDJMS-415](https://issues.apache.org/jira/browse/QPIDJMS-415) - update test dependencies
 - [QPIDJMS-424](https://issues.apache.org/jira/browse/QPIDJMS-424) - Update to Netty 4.1.31 (and netty-tcnative 2.0.19 test dep)
 - [QPIDJMS-427](https://issues.apache.org/jira/browse/QPIDJMS-427) - update to proton-j 0.30.0