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

# Qpid Dispatch 1.11.0 Release Notes

Dispatch is a lightweight AMQP 1.0 message router. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-1415](https://issues.apache.org/jira/browse/DISPATCH-1415) - qdstat does not show process memory usage
 - [DISPATCH-1518](https://issues.apache.org/jira/browse/DISPATCH-1518) - Add ability to turn on router trace logging for a specific connection 
 - [DISPATCH-1524](https://issues.apache.org/jira/browse/DISPATCH-1524) - remove stale hawtio console plugin
 - [DISPATCH-1532](https://issues.apache.org/jira/browse/DISPATCH-1532) - Reimplement mobile-sync as a core module
 - [DISPATCH-1536](https://issues.apache.org/jira/browse/DISPATCH-1536) - Tests needs common utility for printing timestamped messages
 - [DISPATCH-1537](https://issues.apache.org/jira/browse/DISPATCH-1537) - [tools] Scraper could help make transfer output more legible
 - [DISPATCH-1538](https://issues.apache.org/jira/browse/DISPATCH-1538) - [tools] Scraper transfer and link nicknames not created in time order
 - [DISPATCH-1544](https://issues.apache.org/jira/browse/DISPATCH-1544) - Coverity false positive use-after-free error
 - [DISPATCH-1546](https://issues.apache.org/jira/browse/DISPATCH-1546) - Augment the existing tests in system_tests_delivery_counts to use large messages
 - [DISPATCH-1548](https://issues.apache.org/jira/browse/DISPATCH-1548) - Modularize Dispatch Router Doc
 - [DISPATCH-1553](https://issues.apache.org/jira/browse/DISPATCH-1553) - Router ID text name is not restricted
 - [DISPATCH-1555](https://issues.apache.org/jira/browse/DISPATCH-1555) - Update documentation for console UI changes
 - [DISPATCH-1556](https://issues.apache.org/jira/browse/DISPATCH-1556) - Doc should specify correct ownership/permission on sasldb file
 - [DISPATCH-1558](https://issues.apache.org/jira/browse/DISPATCH-1558) - Add a new logging module called PROTOCOL 
 - [DISPATCH-1561](https://issues.apache.org/jira/browse/DISPATCH-1561) - Write system test to test writing different log modules to different output files
 - [DISPATCH-1562](https://issues.apache.org/jira/browse/DISPATCH-1562) - Make attribute names provided to Prometheus more router specific
 - [DISPATCH-1567](https://issues.apache.org/jira/browse/DISPATCH-1567) - Compilation errors on s390x platform
 - [DISPATCH-1569](https://issues.apache.org/jira/browse/DISPATCH-1569) - Add total memory usage to router management entity
 - [DISPATCH-1580](https://issues.apache.org/jira/browse/DISPATCH-1580) - Add a --edge-router option to qdstat and qdmanage to enable directly connecting to edge routers
 - [DISPATCH-1582](https://issues.apache.org/jira/browse/DISPATCH-1582) - Prepare Routing Protocol for Backward Compatibility
 - [DISPATCH-1583](https://issues.apache.org/jira/browse/DISPATCH-1583) - Scraper top level Disposition could show settled t/f and state
 - [DISPATCH-1592](https://issues.apache.org/jira/browse/DISPATCH-1592) - Show dropped routers in grey instead of displaying popup error message

## Bugs fixed

 - [DISPATCH-1459](https://issues.apache.org/jira/browse/DISPATCH-1459) - Python3: exception thrown when processing MAUs
 - [DISPATCH-1508](https://issues.apache.org/jira/browse/DISPATCH-1508) - Leak of qd_listener_t's on shutdown
 - [DISPATCH-1509](https://issues.apache.org/jira/browse/DISPATCH-1509) - Leak of core agent timer
 - [DISPATCH-1510](https://issues.apache.org/jira/browse/DISPATCH-1510) - Leak of qdr_error_t in system_tests_link_route_credit
 - [DISPATCH-1511](https://issues.apache.org/jira/browse/DISPATCH-1511) - Leak reported by coverity static analysis 
 - [DISPATCH-1513](https://issues.apache.org/jira/browse/DISPATCH-1513) - system_tests_http failing with libwebsockets 3.2 on Fedora 31
 - [DISPATCH-1526](https://issues.apache.org/jira/browse/DISPATCH-1526) - Local temp address credit growing unpectedly, edge and interior
 - [DISPATCH-1527](https://issues.apache.org/jira/browse/DISPATCH-1527) - Mobile address lookup server grants insufficient credit
 - [DISPATCH-1528](https://issues.apache.org/jira/browse/DISPATCH-1528) - CMake script to find tox tool is broken
 - [DISPATCH-1529](https://issues.apache.org/jira/browse/DISPATCH-1529) - New python-checker warnings fail the unit tests
 - [DISPATCH-1534](https://issues.apache.org/jira/browse/DISPATCH-1534) - python unit tests does not validate qdstat or qdmanage
 - [DISPATCH-1540](https://issues.apache.org/jira/browse/DISPATCH-1540) - multiframe presettled messages not included in presettled count on downstream router 
 - [DISPATCH-1541](https://issues.apache.org/jira/browse/DISPATCH-1541) - released and modified counters can get incremented for presettled deliveries
 - [DISPATCH-1549](https://issues.apache.org/jira/browse/DISPATCH-1549) - Leak of qdr_terminus_t in system_tests_one_router::test_34_reject_coordinator
 - [DISPATCH-1550](https://issues.apache.org/jira/browse/DISPATCH-1550) - [tools] Scraper fails to parse ROUTER_LS costs
 - [DISPATCH-1551](https://issues.apache.org/jira/browse/DISPATCH-1551) - Mobile addresses can get out of sync (DISPATCH-1532 regression)
 - [DISPATCH-1552](https://issues.apache.org/jira/browse/DISPATCH-1552) - Qpid Dispatch Dockerfile for CentOS 7 is broken
 - [DISPATCH-1557](https://issues.apache.org/jira/browse/DISPATCH-1557) - Router crash due to pn_link double free
 - [DISPATCH-1559](https://issues.apache.org/jira/browse/DISPATCH-1559) - Delivery_abort test fails by streaming multiple messages into one
 - [DISPATCH-1560](https://issues.apache.org/jira/browse/DISPATCH-1560) - Compilation error on Fedora 32 (fedora rawhide)
 - [DISPATCH-1564](https://issues.apache.org/jira/browse/DISPATCH-1564) - Two system tests fail on Fedora 32(fedora:rawhide)
 - [DISPATCH-1566](https://issues.apache.org/jira/browse/DISPATCH-1566) - safe_snpritf is not safe.
 - [DISPATCH-1575](https://issues.apache.org/jira/browse/DISPATCH-1575) - Core thread logs to ROUTER module instead of ROUTER_CORE module
 - [DISPATCH-1579](https://issues.apache.org/jira/browse/DISPATCH-1579) - Traffic hangs when multiple large messages are sent using different priorities
 - [DISPATCH-1584](https://issues.apache.org/jira/browse/DISPATCH-1584) - Scraper fails to parse transfers when the delivery-id is absent
 - [DISPATCH-1587](https://issues.apache.org/jira/browse/DISPATCH-1587) - Special characters in container ids cause traffic animation and message flow to not work 
 - [DISPATCH-1588](https://issues.apache.org/jira/browse/DISPATCH-1588) - Message traffic animation may appear to originate from the wrong router.
 - [DISPATCH-1590](https://issues.apache.org/jira/browse/DISPATCH-1590) - Routed link stall when partial received message is &lt; default buffer size
 - [DISPATCH-1596](https://issues.apache.org/jira/browse/DISPATCH-1596) - Console system tests are failing
 - [DISPATCH-1600](https://issues.apache.org/jira/browse/DISPATCH-1600) - Console crashes if background map is enabled and topology is redisplayed
 - [DISPATCH-1601](https://issues.apache.org/jira/browse/DISPATCH-1601) - Console doesn't display multi-cast address correctly
 - [DISPATCH-1602](https://issues.apache.org/jira/browse/DISPATCH-1602) - Link utilization on console's topology page is displayed incorrectly
 - [DISPATCH-1604](https://issues.apache.org/jira/browse/DISPATCH-1604) - After logging in to the qpid-dispatch-console, using sasl plain authentication, the username (on the top menu) is shown as "anonymous"