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

# Qpid Dispatch 1.9.0 Release Notes

Dispatch is a lightweight AMQP 1.0 message router. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-480](https://issues.apache.org/jira/browse/DISPATCH-480) - Default tests timeout is too short for some machines
 - [DISPATCH-1266](https://issues.apache.org/jira/browse/DISPATCH-1266) - Improve router's handling of unsettled multicast deliveries
 - [DISPATCH-1338](https://issues.apache.org/jira/browse/DISPATCH-1338) - Improvements to edge router documentation
 - [DISPATCH-1345](https://issues.apache.org/jira/browse/DISPATCH-1345) - Reduce the number of QDR_LINK_FLOW events by coalescing credit grants
 - [DISPATCH-1346](https://issues.apache.org/jira/browse/DISPATCH-1346) - Create documentation for priority delivery
 - [DISPATCH-1347](https://issues.apache.org/jira/browse/DISPATCH-1347) - Update documentation for Dispatch Router console
 - [DISPATCH-1350](https://issues.apache.org/jira/browse/DISPATCH-1350) - Update logging/monitoring documentation
 - [DISPATCH-1353](https://issues.apache.org/jira/browse/DISPATCH-1353) - Document how to configure access policy control on router-initiated connections
 - [DISPATCH-1354](https://issues.apache.org/jira/browse/DISPATCH-1354) - Interrouter annotation processing uses slow methods
 - [DISPATCH-1370](https://issues.apache.org/jira/browse/DISPATCH-1370) - Move the schema, connect, and entities tabs to the right in the console
 - [DISPATCH-1374](https://issues.apache.org/jira/browse/DISPATCH-1374) - Add qdstat options --all-routers and all-entities which display statistics of all routers and displays all entities
 - [DISPATCH-1376](https://issues.apache.org/jira/browse/DISPATCH-1376) - Make it easier to change the product name in the console
 - [DISPATCH-1379](https://issues.apache.org/jira/browse/DISPATCH-1379) - Message receive performance improvements
 - [DISPATCH-1381](https://issues.apache.org/jira/browse/DISPATCH-1381) - Create documentation for configuring fallback destinations
 - [DISPATCH-1382](https://issues.apache.org/jira/browse/DISPATCH-1382) - Document ability to force-close a connection from the web console
 - [DISPATCH-1388](https://issues.apache.org/jira/browse/DISPATCH-1388) - Authorization doc fails to describe vhost abstraction clearly
 - [DISPATCH-1389](https://issues.apache.org/jira/browse/DISPATCH-1389) - Optimize the parsing of message annotations
 - [DISPATCH-1396](https://issues.apache.org/jira/browse/DISPATCH-1396) - Doc how to start the router
 - [DISPATCH-1402](https://issues.apache.org/jira/browse/DISPATCH-1402) - Document unsettled multicast

## Bugs fixed

 - [DISPATCH-1256](https://issues.apache.org/jira/browse/DISPATCH-1256) - Throughput gets worse as more routers are added
 - [DISPATCH-1359](https://issues.apache.org/jira/browse/DISPATCH-1359) - Set ctest timeout to 300 seconds.
 - [DISPATCH-1361](https://issues.apache.org/jira/browse/DISPATCH-1361) - system_tests_fallback_dest hanging in some cases
 - [DISPATCH-1362](https://issues.apache.org/jira/browse/DISPATCH-1362) - Shutdown crash when trying to clean up fallback addresses
 - [DISPATCH-1365](https://issues.apache.org/jira/browse/DISPATCH-1365) - Table of links with delayed deliveries is showing all endpoint links
 - [DISPATCH-1378](https://issues.apache.org/jira/browse/DISPATCH-1378) - missing lock of connection's links_with_work list
 - [DISPATCH-1380](https://issues.apache.org/jira/browse/DISPATCH-1380) - qdrouterd leaves dangling qd_link_t pointer
 - [DISPATCH-1383](https://issues.apache.org/jira/browse/DISPATCH-1383) - system_tests_policy is timing out
 - [DISPATCH-1387](https://issues.apache.org/jira/browse/DISPATCH-1387) - Coverity issues on master branch
 - [DISPATCH-1391](https://issues.apache.org/jira/browse/DISPATCH-1391) - Proton link reference not cleared on router link objects during session close
 - [DISPATCH-1394](https://issues.apache.org/jira/browse/DISPATCH-1394) - qd_check_message() incorrectly validates partially received messages
 - [DISPATCH-1398](https://issues.apache.org/jira/browse/DISPATCH-1398) - "Expression with no effect" warning for console web
 - [DISPATCH-1404](https://issues.apache.org/jira/browse/DISPATCH-1404) - message annotation parsing incorrectly uses -&gt;remainder for current buffer capacity
 - [DISPATCH-1406](https://issues.apache.org/jira/browse/DISPATCH-1406) - Inter-router link stall on receive client failover
 - [DISPATCH-1407](https://issues.apache.org/jira/browse/DISPATCH-1407) - Memory leak on link policy denial
 - [DISPATCH-1408](https://issues.apache.org/jira/browse/DISPATCH-1408) - system_tests_distribution failing when running under valgrind
 - [DISPATCH-1410](https://issues.apache.org/jira/browse/DISPATCH-1410) - attach of auto-links not logged
 - [DISPATCH-1413](https://issues.apache.org/jira/browse/DISPATCH-1413) - system_tests_two_routers.py failing intermittently on Travis
 - [DISPATCH-1417](https://issues.apache.org/jira/browse/DISPATCH-1417) - Crash when connection_wake ctx points to freed memory