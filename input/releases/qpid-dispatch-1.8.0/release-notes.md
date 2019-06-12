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

# Qpid Dispatch 1.8.0 Release Notes

Dispatch is a lightweight AMQP message router library. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-1308](https://issues.apache.org/jira/browse/DISPATCH-1308) - Console access to the force-close a connection feature
 - [DISPATCH-1320](https://issues.apache.org/jira/browse/DISPATCH-1320) - Make it easier to use separate logos for upstream and downstream masthead
 - [DISPATCH-1321](https://issues.apache.org/jira/browse/DISPATCH-1321) - Set rpath for qpid-proton (and other dependencies) when they are found in nonstandard location
 - [DISPATCH-1329](https://issues.apache.org/jira/browse/DISPATCH-1329) - Edge router system test needs skip test convenience switches
 - [DISPATCH-1337](https://issues.apache.org/jira/browse/DISPATCH-1337) - Fallback Destination for Unreachable Addresses
 - [DISPATCH-1340](https://issues.apache.org/jira/browse/DISPATCH-1340) - Show settlement rate and delayed deliveries in client popup
 - [DISPATCH-1348](https://issues.apache.org/jira/browse/DISPATCH-1348) - Avoid qdr_error_t allocation if not necessary
 - [DISPATCH-1356](https://issues.apache.org/jira/browse/DISPATCH-1356) - Remove the dotted line around routers that indicates the router is fixed.
 - [DISPATCH-1357](https://issues.apache.org/jira/browse/DISPATCH-1357) - Change the name of the 'Kill' feature to 'Close'

## Bugs fixed

 - [DISPATCH-974](https://issues.apache.org/jira/browse/DISPATCH-974) - Getting connections via the router management protocol causes AMQP framing errors
 - [DISPATCH-1230](https://issues.apache.org/jira/browse/DISPATCH-1230) - System test failing with OpenSSL &gt;= 1.1 - system_tests_ssl
 - [DISPATCH-1312](https://issues.apache.org/jira/browse/DISPATCH-1312) - Remove cmake option USE_MEMORY_POOL
 - [DISPATCH-1317](https://issues.apache.org/jira/browse/DISPATCH-1317) - HTTP system test is failing on python2.6
 - [DISPATCH-1318](https://issues.apache.org/jira/browse/DISPATCH-1318) - edge_router system test failing 
 - [DISPATCH-1322](https://issues.apache.org/jira/browse/DISPATCH-1322) - Edge router drops disposition when remote receiver closes
 - [DISPATCH-1323](https://issues.apache.org/jira/browse/DISPATCH-1323) - Deprecate addr and externalAddr attributes of autoLink entity. Add address and externalAddress instead.
 - [DISPATCH-1324](https://issues.apache.org/jira/browse/DISPATCH-1324) - [tools] Scraper uses deprecated cgi.escape function
 - [DISPATCH-1325](https://issues.apache.org/jira/browse/DISPATCH-1325) - Sender connections to edge router that connect 'too soon' never get credit
 - [DISPATCH-1326](https://issues.apache.org/jira/browse/DISPATCH-1326) - Anonymous messages are released by edge router even if there is a receiver for the messages
 - [DISPATCH-1330](https://issues.apache.org/jira/browse/DISPATCH-1330) - Q2 stall due to incorrect msg buffer ref count decrement on link detach
 - [DISPATCH-1334](https://issues.apache.org/jira/browse/DISPATCH-1334) - Background map on topology page incorrect height
 - [DISPATCH-1335](https://issues.apache.org/jira/browse/DISPATCH-1335) - After adding client, topology page shows new icon in upper-left corner
 - [DISPATCH-1339](https://issues.apache.org/jira/browse/DISPATCH-1339) - Multiple consoles attached to a router are showing as separate icons