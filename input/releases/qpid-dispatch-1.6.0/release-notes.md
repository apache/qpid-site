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

# Qpid Dispatch 1.6.0 Release Notes

Dispatch is a lightweight AMQP 1.0 message router. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-1243](https://issues.apache.org/jira/browse/DISPATCH-1243) - Change Valgrind configuration to run only qdrouterd under valgrind
 - [DISPATCH-1251](https://issues.apache.org/jira/browse/DISPATCH-1251) - Allow traffic animations to run simultaneaously on console's topology page. 
 - [DISPATCH-1255](https://issues.apache.org/jira/browse/DISPATCH-1255) - Test execution with python3 modifies files in source directory
 - [DISPATCH-1269](https://issues.apache.org/jira/browse/DISPATCH-1269) - Improve error handling for remote_sasl.c plugin
 - [DISPATCH-1278](https://issues.apache.org/jira/browse/DISPATCH-1278) - Add support for prometheus metrics export
 - [DISPATCH-1281](https://issues.apache.org/jira/browse/DISPATCH-1281) - Performance - Batch the freeing of messages from the core thread
 - [DISPATCH-1289](https://issues.apache.org/jira/browse/DISPATCH-1289) - Logging and Management Enhancements
 - [DISPATCH-1290](https://issues.apache.org/jira/browse/DISPATCH-1290) - expose simple http base health check
 - [DISPATCH-1291](https://issues.apache.org/jira/browse/DISPATCH-1291) - Update console to use router-generated link settlement rates
 - [DISPATCH-1296](https://issues.apache.org/jira/browse/DISPATCH-1296) - Change use of pn_ssl_domain_allow_unsecured_client() to pn_transport_require_encryption()
 - [DISPATCH-1299](https://issues.apache.org/jira/browse/DISPATCH-1299) - Provide API access to the already existing safe-reference capability in alloc-pool

## Bugs fixed

 - [DISPATCH-1242](https://issues.apache.org/jira/browse/DISPATCH-1242) - [tools] Scraper does not highlight incomplete transfers
 - [DISPATCH-1244](https://issues.apache.org/jira/browse/DISPATCH-1244) - New senders/receivers/edge routers first appear too close to router in console 
 - [DISPATCH-1245](https://issues.apache.org/jira/browse/DISPATCH-1245) - Console build generates new warnings about potential vulnerabilities 
 - [DISPATCH-1247](https://issues.apache.org/jira/browse/DISPATCH-1247) - Leak of bitmask during message annotation
 - [DISPATCH-1248](https://issues.apache.org/jira/browse/DISPATCH-1248) - leak of core timers on shutdown
 - [DISPATCH-1252](https://issues.apache.org/jira/browse/DISPATCH-1252) - Display connect page if console is disconnected
 - [DISPATCH-1254](https://issues.apache.org/jira/browse/DISPATCH-1254) - qdstat sometimes raises "TypeError: 'NoneType' object is not iterable"
 - [DISPATCH-1257](https://issues.apache.org/jira/browse/DISPATCH-1257) - qdstat &amp; qdmanage send bad initial response for EXTERNAL if --sasl-mechanisms is specified
 - [DISPATCH-1260](https://issues.apache.org/jira/browse/DISPATCH-1260) - Closing traffic animation doesn't always work
 - [DISPATCH-1261](https://issues.apache.org/jira/browse/DISPATCH-1261) - Builds failing on CentOS7
 - [DISPATCH-1262](https://issues.apache.org/jira/browse/DISPATCH-1262) - GCC 8.2 format-truncation error in router/src/main.c
 - [DISPATCH-1263](https://issues.apache.org/jira/browse/DISPATCH-1263) - Symbol for sender/receiver is incorrect on console's topology page
 - [DISPATCH-1267](https://issues.apache.org/jira/browse/DISPATCH-1267) - Bad_configuration test fails intermittently
 - [DISPATCH-1272](https://issues.apache.org/jira/browse/DISPATCH-1272) - Router crashes when detach from receiver and detach from broker arrive at the same time on a link route
 - [DISPATCH-1273](https://issues.apache.org/jira/browse/DISPATCH-1273) - 'to' field not authorized against valid targets for anonymous sender
 - [DISPATCH-1275](https://issues.apache.org/jira/browse/DISPATCH-1275) - Enable deletion of connections based on connection id
 - [DISPATCH-1276](https://issues.apache.org/jira/browse/DISPATCH-1276) - Spontaneous drop of client connection causes crash on edge router
 - [DISPATCH-1277](https://issues.apache.org/jira/browse/DISPATCH-1277) - max-frame-size defaults to 2147483647 if it is not specified in the policy
 - [DISPATCH-1285](https://issues.apache.org/jira/browse/DISPATCH-1285) - Router crashes occasionally on system_tests_delivery_abort
 - [DISPATCH-1287](https://issues.apache.org/jira/browse/DISPATCH-1287) - router gets confused by clients response to drain and subsequently issue too little credit
 - [DISPATCH-1288](https://issues.apache.org/jira/browse/DISPATCH-1288) - Optionally enforce access policy on connections established by the router
 - [DISPATCH-1292](https://issues.apache.org/jira/browse/DISPATCH-1292) - Coverity issues on master branch
 - [DISPATCH-1293](https://issues.apache.org/jira/browse/DISPATCH-1293) - Show traffic for stand-alone router
 - [DISPATCH-1297](https://issues.apache.org/jira/browse/DISPATCH-1297) - Fix buffer reference counting for multiframe fanout messages
 - [DISPATCH-1301](https://issues.apache.org/jira/browse/DISPATCH-1301) - Management messages lost

## Tasks

 - [DISPATCH-1115](https://issues.apache.org/jira/browse/DISPATCH-1115) - Configure Travis to run Dispatch tests agianst the latest Proton release and Proton master branch