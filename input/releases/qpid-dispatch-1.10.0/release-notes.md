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

# Qpid Dispatch 1.10.0 Release Notes

Dispatch is a lightweight AMQP message router library. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-1186](https://issues.apache.org/jira/browse/DISPATCH-1186) - qdstat to include csv output format
 - [DISPATCH-1369](https://issues.apache.org/jira/browse/DISPATCH-1369) - Update console dependencies to avoid npm security warnings
 - [DISPATCH-1409](https://issues.apache.org/jira/browse/DISPATCH-1409) - Update qdstat -l output to include the current credit
 - [DISPATCH-1411](https://issues.apache.org/jira/browse/DISPATCH-1411) - Add timestamp and router name to header of qdstat output
 - [DISPATCH-1412](https://issues.apache.org/jira/browse/DISPATCH-1412) - Policy C code performance issue:  reload python module for each call
 - [DISPATCH-1416](https://issues.apache.org/jira/browse/DISPATCH-1416) - Policy log could include denial counts on connection close
 - [DISPATCH-1419](https://issues.apache.org/jira/browse/DISPATCH-1419) - Add status to connector mgmt schema
 - [DISPATCH-1427](https://issues.apache.org/jira/browse/DISPATCH-1427) - Allow policy to define user (group) specific connection limits
 - [DISPATCH-1438](https://issues.apache.org/jira/browse/DISPATCH-1438) - Have ctest parse the routers debug dump files for memory pool leaks
 - [DISPATCH-1439](https://issues.apache.org/jira/browse/DISPATCH-1439) - Expose create time/last transfer time through the Connection management entity
 - [DISPATCH-1440](https://issues.apache.org/jira/browse/DISPATCH-1440) - Deprecate the passwordFile field in sslProfile and consolidate all password scenarios to use  the password field
 - [DISPATCH-1441](https://issues.apache.org/jira/browse/DISPATCH-1441) - optparse python library deprecated, migrate to argparse
 - [DISPATCH-1442](https://issues.apache.org/jira/browse/DISPATCH-1442) - Add a metadata field to the router management entity
 - [DISPATCH-1445](https://issues.apache.org/jira/browse/DISPATCH-1445) - Update saslPassword attribute in connector entity to use openssl style prefixes
 - [DISPATCH-1446](https://issues.apache.org/jira/browse/DISPATCH-1446) - system_tests_qdmanage failing on test_get_log
 - [DISPATCH-1450](https://issues.apache.org/jira/browse/DISPATCH-1450) - Add build option to enable thread sanitizer build
 - [DISPATCH-1454](https://issues.apache.org/jira/browse/DISPATCH-1454) - system_tests_one_router failing due to changes in qpid-proton
 - [DISPATCH-1455](https://issues.apache.org/jira/browse/DISPATCH-1455) - Two system tests failing after optparse to argparse migration
 - [DISPATCH-1463](https://issues.apache.org/jira/browse/DISPATCH-1463) - Detect deliveries that are stuck in the router for a long time
 - [DISPATCH-1465](https://issues.apache.org/jira/browse/DISPATCH-1465) - system_tests_policy.test_verify_z_connection_stats fails 
 - [DISPATCH-1466](https://issues.apache.org/jira/browse/DISPATCH-1466) - flake8 errors in system_test.py
 - [DISPATCH-1467](https://issues.apache.org/jira/browse/DISPATCH-1467) - Add build option to enable Address Sanitizer build (ASAN)
 - [DISPATCH-1471](https://issues.apache.org/jira/browse/DISPATCH-1471) - [test] When string comparison asserts fail the strings are not printed
 - [DISPATCH-1480](https://issues.apache.org/jira/browse/DISPATCH-1480) - Address Sanitizer leak in system_tests_multi_phase
 - [DISPATCH-1491](https://issues.apache.org/jira/browse/DISPATCH-1491) - bottleneck adding or removing addresses in mobile address engine
 - [DISPATCH-1500](https://issues.apache.org/jira/browse/DISPATCH-1500) - inefficiencies in handling large MAU messages
 - [DISPATCH-1516](https://issues.apache.org/jira/browse/DISPATCH-1516) - Trace log the peer delivery id and link id when linking and unlinking peers
 - [DISPATCH-1525](https://issues.apache.org/jira/browse/DISPATCH-1525) - KeyError when executing master branch qdstat -l (links) against 1.9.0 router on Python 3

## Bugs fixed

 - [DISPATCH-1172](https://issues.apache.org/jira/browse/DISPATCH-1172) - Link routes and auto links activated on wrong connections if many route-container conns exist
 - [DISPATCH-1258](https://issues.apache.org/jira/browse/DISPATCH-1258) - Crash executing http test
 - [DISPATCH-1377](https://issues.apache.org/jira/browse/DISPATCH-1377) - system_tests_topology_disposition failing on machine with python3 only
 - [DISPATCH-1418](https://issues.apache.org/jira/browse/DISPATCH-1418) - The default forwarding treatment is not overridden by the treatment in the address configuration
 - [DISPATCH-1421](https://issues.apache.org/jira/browse/DISPATCH-1421) - Attaching link to unavailable address sets source address to null in attach reply
 - [DISPATCH-1423](https://issues.apache.org/jira/browse/DISPATCH-1423) - Multicast sender with no receiver has first 250 messages released
 - [DISPATCH-1426](https://issues.apache.org/jira/browse/DISPATCH-1426) - Repetitive receiver fail over causes memory leak
 - [DISPATCH-1428](https://issues.apache.org/jira/browse/DISPATCH-1428) - route connection not indexed by 'connection' field of connector
 - [DISPATCH-1431](https://issues.apache.org/jira/browse/DISPATCH-1431) - system_tests_one_router_failing on test_19_semantics_multicast
 - [DISPATCH-1433](https://issues.apache.org/jira/browse/DISPATCH-1433) - system_tests_delivery_abort failing due to receiver connecting late
 - [DISPATCH-1443](https://issues.apache.org/jira/browse/DISPATCH-1443) - Unable to run ctest on Centos 8
 - [DISPATCH-1453](https://issues.apache.org/jira/browse/DISPATCH-1453) - Adding "defaultDistribution: unavailable" overrides the regular handling of transaction coordinator link refusal
 - [DISPATCH-1460](https://issues.apache.org/jira/browse/DISPATCH-1460) - Router control messages for local subscribers hang in Q2 holdoff
 - [DISPATCH-1461](https://issues.apache.org/jira/browse/DISPATCH-1461) - Crashed router due to terminus address overflow
 - [DISPATCH-1462](https://issues.apache.org/jira/browse/DISPATCH-1462) - [policy] Test for IPv6 leaves socket open
 - [DISPATCH-1468](https://issues.apache.org/jira/browse/DISPATCH-1468) - out-of-bounds array access in qd_entity_refresh_connector
 - [DISPATCH-1473](https://issues.apache.org/jira/browse/DISPATCH-1473) - [test] test_command fail on python 2.7
 - [DISPATCH-1474](https://issues.apache.org/jira/browse/DISPATCH-1474) - Console message path skips one router hop
 - [DISPATCH-1475](https://issues.apache.org/jira/browse/DISPATCH-1475) - Seg fault in qdr_link_cleanup_CT after 12,400+ connections
 - [DISPATCH-1476](https://issues.apache.org/jira/browse/DISPATCH-1476) - [tools] New proton logging breaks Scraper
 - [DISPATCH-1477](https://issues.apache.org/jira/browse/DISPATCH-1477) - Crash router by deleting authServicePlugin entity through management call
 - [DISPATCH-1481](https://issues.apache.org/jira/browse/DISPATCH-1481) - Multicast producers should block on credit until consumers are present
 - [DISPATCH-1483](https://issues.apache.org/jira/browse/DISPATCH-1483) - Link counters for dispositions are not incremented for outgoing links
 - [DISPATCH-1485](https://issues.apache.org/jira/browse/DISPATCH-1485) - qdstat --limit 0 seems to cause infinit loop
 - [DISPATCH-1488](https://issues.apache.org/jira/browse/DISPATCH-1488) - link-routed transaction coordination broken due to 'declared' state truncation
 - [DISPATCH-1492](https://issues.apache.org/jira/browse/DISPATCH-1492) - Router asserts when client connects to edge listener
 - [DISPATCH-1493](https://issues.apache.org/jira/browse/DISPATCH-1493) - qdstat test_address_priority fails by issuing false positive
 - [DISPATCH-1496](https://issues.apache.org/jira/browse/DISPATCH-1496) - router can grant extra credit during drain of a link-routed receiver
 - [DISPATCH-1498](https://issues.apache.org/jira/browse/DISPATCH-1498) - Skip SASL tests if Cyrus library is not available
 - [DISPATCH-1499](https://issues.apache.org/jira/browse/DISPATCH-1499) - Policy settings objects should be in managed pool
 - [DISPATCH-1512](https://issues.apache.org/jira/browse/DISPATCH-1512) - python checker failing due to wrong variable name
 - [DISPATCH-1514](https://issues.apache.org/jira/browse/DISPATCH-1514) - Dynamically turning on trace logging via qdmanage does not turn proton frame tracing on existing connections
 - [DISPATCH-1517](https://issues.apache.org/jira/browse/DISPATCH-1517) - delivery count is not incremented for undeliverable messages
 - [DISPATCH-1521](https://issues.apache.org/jira/browse/DISPATCH-1521) - qdstat man page -l column header for "dev" is wrong