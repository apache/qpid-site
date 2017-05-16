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

# Qpid JMS 0.23.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-291](https://issues.apache.org/jira/browse/QPIDJMS-291) - update to proton-j 0.19.0

## Bugs fixed

 - [QPIDJMS-288](https://issues.apache.org/jira/browse/QPIDJMS-288) - Connection executor is not shutdown on connect failure
 - [QPIDJMS-289](https://issues.apache.org/jira/browse/QPIDJMS-289) - JMSDeliveryTime should be populated even if there isn't a delivery delay during send
 - [QPIDJMS-290](https://issues.apache.org/jira/browse/QPIDJMS-290) - [Websocket] Receiving bytes message with more than 65347 bytes of content fails within the decoder
 - [QPIDJMS-292](https://issues.apache.org/jira/browse/QPIDJMS-292) - consumers may buffer vastly more messages than expected for their 'prefetch' value