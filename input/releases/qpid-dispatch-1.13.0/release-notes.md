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

# Qpid Dispatch 1.13.0 Release Notes

Dispatch is a lightweight AMQP 1.0 message router. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-1568](https://issues.apache.org/jira/browse/DISPATCH-1568) - Add unittest framework for testing C code
 - [DISPATCH-1633](https://issues.apache.org/jira/browse/DISPATCH-1633) - system_tests_sasl_plain intermittent test failure
 - [DISPATCH-1636](https://issues.apache.org/jira/browse/DISPATCH-1636) - Extract the version advertized in the Open performative by the peer router 
 - [DISPATCH-1642](https://issues.apache.org/jira/browse/DISPATCH-1642) - Avoid extra search when adding address configs to parse tree
 - [DISPATCH-1646](https://issues.apache.org/jira/browse/DISPATCH-1646) - Unable to delete listener with http enabled
 - [DISPATCH-1656](https://issues.apache.org/jira/browse/DISPATCH-1656) - Allow user-configured connection properties in the Open performative
 - [DISPATCH-1667](https://issues.apache.org/jira/browse/DISPATCH-1667) - Increase minimum required LibWebSockets version from 2.1.0 to 2.4.2
 - [DISPATCH-1668](https://issues.apache.org/jira/browse/DISPATCH-1668) - Dockerfile instructions show how to use router debug core dump files
 - [DISPATCH-1675](https://issues.apache.org/jira/browse/DISPATCH-1675) - system_tests_stuck_deliveries failure with AttributeError: 'DelayedSettlementTest' object has no attribute 'proxy'", 
 - [DISPATCH-1685](https://issues.apache.org/jira/browse/DISPATCH-1685) - Provide heap memory allocation wrappers that call abort() on failure to allocate
 - [DISPATCH-1688](https://issues.apache.org/jira/browse/DISPATCH-1688) - Scraper needs a way to inject debug statements into log data web page
 - [DISPATCH-1692](https://issues.apache.org/jira/browse/DISPATCH-1692) - Scraper improvements for sequence diagrams
 - [DISPATCH-1717](https://issues.apache.org/jira/browse/DISPATCH-1717) - Fallback_destination test improvements: mnemonic names, unique msg data and link names
 - [DISPATCH-1726](https://issues.apache.org/jira/browse/DISPATCH-1726) - Upgrade dependencies using dependabot PRs before the 1.13.0 release
 - [DISPATCH-1732](https://issues.apache.org/jira/browse/DISPATCH-1732) - segfault when connecting to multitenant listener with policy but  no hostname in open
 - [DISPATCH-1739](https://issues.apache.org/jira/browse/DISPATCH-1739) - Use GitHub Actions w/ sharding and bubblewrap for some fast CI

## Bugs fixed

 - [DISPATCH-960](https://issues.apache.org/jira/browse/DISPATCH-960) - TCP port randomly assigned when using 'port: amqp' along with 'http: yes' on a listener
 - [DISPATCH-1444](https://issues.apache.org/jira/browse/DISPATCH-1444) - Top level Dockerfile fails to build on centos:latest
 - [DISPATCH-1494](https://issues.apache.org/jira/browse/DISPATCH-1494) - Qdstat heading for a memory display is Types
 - [DISPATCH-1505](https://issues.apache.org/jira/browse/DISPATCH-1505) - [tools] Add policy and vhost information to qdstat
 - [DISPATCH-1545](https://issues.apache.org/jira/browse/DISPATCH-1545) - Streaming deliveries can be delayed by head-of-line blocking on inter-router links
 - [DISPATCH-1637](https://issues.apache.org/jira/browse/DISPATCH-1637) - Adding new config address, autolinks and link routes become slower as more get added 
 - [DISPATCH-1641](https://issues.apache.org/jira/browse/DISPATCH-1641) - If an oversize transfer is rejected then provide details in rejected outcome error field
 - [DISPATCH-1644](https://issues.apache.org/jira/browse/DISPATCH-1644) - Suppress cmake warning about LIBWEBSOCKETS
 - [DISPATCH-1645](https://issues.apache.org/jira/browse/DISPATCH-1645) - Max message size is demoted to INT from UINT64
 - [DISPATCH-1657](https://issues.apache.org/jira/browse/DISPATCH-1657) - system_tests_router_mesh ASAN failure
 - [DISPATCH-1658](https://issues.apache.org/jira/browse/DISPATCH-1658) - Receiver unable to receive messages on waypointed addresses
 - [DISPATCH-1661](https://issues.apache.org/jira/browse/DISPATCH-1661) - system_tests_edge_router fails with ASAN leak
 - [DISPATCH-1662](https://issues.apache.org/jira/browse/DISPATCH-1662) - system_tests_policy_oversize_compound fails with ASAN leak
 - [DISPATCH-1664](https://issues.apache.org/jira/browse/DISPATCH-1664) - test_verify_z_connection_stats failing in system_tests_policy
 - [DISPATCH-1669](https://issues.apache.org/jira/browse/DISPATCH-1669) - Compilation fails on macOS [-Werror,-Wformat]
 - [DISPATCH-1670](https://issues.apache.org/jira/browse/DISPATCH-1670) - system_tests_edge_router.LinkRouteProxyTest.test_50_link_topology reports many objects that remain allocated after test finishes
 - [DISPATCH-1676](https://issues.apache.org/jira/browse/DISPATCH-1676) - system_tests_policy failure on router shutdown
 - [DISPATCH-1682](https://issues.apache.org/jira/browse/DISPATCH-1682) - Optimize the parse tree match algorithm to avoid O(N) lookup
 - [DISPATCH-1690](https://issues.apache.org/jira/browse/DISPATCH-1690) - Pre-delivery messages leak on link close
 - [DISPATCH-1691](https://issues.apache.org/jira/browse/DISPATCH-1691) - Hash symbol in vhost hostname is treated as a comment delimiter
 - [DISPATCH-1693](https://issues.apache.org/jira/browse/DISPATCH-1693) - Edge router closes fallback receiver link when local primary receiver closes
 - [DISPATCH-1694](https://issues.apache.org/jira/browse/DISPATCH-1694) - sys_thread_self() returns NULL pointer if called by main process thread
 - [DISPATCH-1695](https://issues.apache.org/jira/browse/DISPATCH-1695) - Policy vhost groups description error
 - [DISPATCH-1703](https://issues.apache.org/jira/browse/DISPATCH-1703) - router drops TransactionalState on produced messages on link routes
 - [DISPATCH-1707](https://issues.apache.org/jira/browse/DISPATCH-1707) - Policy config file fails with cryptic error if trailing brace on wrong line
 - [DISPATCH-1708](https://issues.apache.org/jira/browse/DISPATCH-1708) - Fallback destination test receives messages on wrong receiver
 - [DISPATCH-1709](https://issues.apache.org/jira/browse/DISPATCH-1709) - Fallback destination rcvr on edge router is unaware that primary rcvr exited
 - [DISPATCH-1715](https://issues.apache.org/jira/browse/DISPATCH-1715) - [clang-10] error: variable length array folded to constant array as an extension
 - [DISPATCH-1716](https://issues.apache.org/jira/browse/DISPATCH-1716) - [clang] -fsanitize=address and -Wl,-z,defs compiler options are incompatible
 - [DISPATCH-1718](https://issues.apache.org/jira/browse/DISPATCH-1718) - Qdstat for policy and vhostgroups not backwards compatible
 - [DISPATCH-1721](https://issues.apache.org/jira/browse/DISPATCH-1721) - Qdstat table for vhostgroupsettings:  too wide; missing default settings
 - [DISPATCH-1722](https://issues.apache.org/jira/browse/DISPATCH-1722) - system_tests_qdstat fails when checking for presence Worker Threads
 - [DISPATCH-1724](https://issues.apache.org/jira/browse/DISPATCH-1724) - Fallback destination fails when primary consumer is on an auto-link
 - [DISPATCH-1727](https://issues.apache.org/jira/browse/DISPATCH-1727) - Dispatch Console mixes usage of `npm` with `yarn`
 - [DISPATCH-1729](https://issues.apache.org/jira/browse/DISPATCH-1729) - Update console test file for DropdownMenu.js to pass required properties.
 - [DISPATCH-1730](https://issues.apache.org/jira/browse/DISPATCH-1730) - Revert console's @testing-library/react from 10.4.7 to 9.5.0
 - [DISPATCH-1733](https://issues.apache.org/jira/browse/DISPATCH-1733) - system_tests_open_properties failure due to qdr_connection_t leak
 - [DISPATCH-1737](https://issues.apache.org/jira/browse/DISPATCH-1737) - Policy config parse errors report wrong line and column numbers 
 - [DISPATCH-1738](https://issues.apache.org/jira/browse/DISPATCH-1738) - system_tests_multicast failing on Ubuntu Focal
 - [DISPATCH-1741](https://issues.apache.org/jira/browse/DISPATCH-1741) - Update console dependency for yargs-parser to avoid security warning

## Tasks

 - [DISPATCH-1624](https://issues.apache.org/jira/browse/DISPATCH-1624) - Doc max message size
 - [DISPATCH-1629](https://issues.apache.org/jira/browse/DISPATCH-1629) - Doc how to enable trace logging for a connection
 - [DISPATCH-1719](https://issues.apache.org/jira/browse/DISPATCH-1719) - Add note about vhost