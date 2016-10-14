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

# Qpid Proton 0.15.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-1224](https://issues.apache.org/jira/browse/PROTON-1224) - [proton-j] use newer versions of BouncyCastle
 - [PROTON-1274](https://issues.apache.org/jira/browse/PROTON-1274) - Performance: avoid referencing 'context' in Event constructor
 - [PROTON-1277](https://issues.apache.org/jira/browse/PROTON-1277) - pn_connection_engine API improvements.
 - [PROTON-1283](https://issues.apache.org/jira/browse/PROTON-1283) - [proton-j] enable the transport impl to accept additional wrapper layers
 - [PROTON-1289](https://issues.apache.org/jira/browse/PROTON-1289) - Add coverage analysis into build system
 - [PROTON-1293](https://issues.apache.org/jira/browse/PROTON-1293) - Support username and password in electron go binding
 - [PROTON-1294](https://issues.apache.org/jira/browse/PROTON-1294) - c++ examples: remove un-necessary 64 bit integers.
 - [PROTON-1301](https://issues.apache.org/jira/browse/PROTON-1301) - add pn_condition_format for formatted descriptions
 - [PROTON-1306](https://issues.apache.org/jira/browse/PROTON-1306) - Go simplified client/server example
 - [PROTON-1308](https://issues.apache.org/jira/browse/PROTON-1308) - Support Idle Timeout setting in electron Transport  

## Bugs fixed

 - [PROTON-1255](https://issues.apache.org/jira/browse/PROTON-1255) - connection_engine support for built-in proton SSL/SASL
 - [PROTON-1275](https://issues.apache.org/jira/browse/PROTON-1275) - [proton-j] [reactor] socket connection interrupt causes unhandled IllegalArgumentException
 - [PROTON-1282](https://issues.apache.org/jira/browse/PROTON-1282) - Seg Fault in Ruby Messenger pn_messenger_free
 - [PROTON-1287](https://issues.apache.org/jira/browse/PROTON-1287) - c++: missing empty() method on message_id and annotation_key
 - [PROTON-1290](https://issues.apache.org/jira/browse/PROTON-1290) - [proton-j] Transport can emit erroneous Flow frame before sending a Detach from a Receiver
 - [PROTON-1291](https://issues.apache.org/jira/browse/PROTON-1291) - [proton-j] calling close again on a closed endpoints marks it modified and emits the related event again
 - [PROTON-1299](https://issues.apache.org/jira/browse/PROTON-1299) - [proton-j] the Link#getRemoteCredit() method return value isn't suitable for sending links
 - [PROTON-1305](https://issues.apache.org/jira/browse/PROTON-1305) - Go sporadic test failure in electron_test
 - [PROTON-1307](https://issues.apache.org/jira/browse/PROTON-1307) - go binding amqp.message does not honor Inferred flag
 - [PROTON-1313](https://issues.apache.org/jira/browse/PROTON-1313) - c++: missing #include &lt;string&gt; in some headers

## Tasks

 - [PROTON-1300](https://issues.apache.org/jira/browse/PROTON-1300) - [proton-j] remove redundant credit update call