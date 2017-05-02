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

# Qpid Dispatch 0.8.0 Release Notes

Dispatch is a lightweight AMQP message router library. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-103](https://issues.apache.org/jira/browse/DISPATCH-103) - Websocket Listeners
 - [DISPATCH-113](https://issues.apache.org/jira/browse/DISPATCH-113) - expose NodeTracker::last_topology_change in management 
 - [DISPATCH-195](https://issues.apache.org/jira/browse/DISPATCH-195) - Add support for transactional messages in the Router
 - [DISPATCH-441](https://issues.apache.org/jira/browse/DISPATCH-441) - Support password environment variable in qdrouter config 
 - [DISPATCH-467](https://issues.apache.org/jira/browse/DISPATCH-467) - Terminus renaming for autoLinks
 - [DISPATCH-529](https://issues.apache.org/jira/browse/DISPATCH-529) - Address annotation for Multi-Tenancy
 - [DISPATCH-542](https://issues.apache.org/jira/browse/DISPATCH-542) - Popup text for clients should indicate if the client is a sender or receiver
 - [DISPATCH-543](https://issues.apache.org/jira/browse/DISPATCH-543) - Initial load of topology page fetches too much information
 - [DISPATCH-544](https://issues.apache.org/jira/browse/DISPATCH-544) - Add ability to hide the info panel on the left of the topology page
 - [DISPATCH-552](https://issues.apache.org/jira/browse/DISPATCH-552) - Allow only one tree node to be expanded if there is a large number of routers 
 - [DISPATCH-553](https://issues.apache.org/jira/browse/DISPATCH-553) - Add statistic counter to the "log" entity to count log events per severity
 - [DISPATCH-559](https://issues.apache.org/jira/browse/DISPATCH-559) - qdstat - Request only the columns that will be used in the display
 - [DISPATCH-561](https://issues.apache.org/jira/browse/DISPATCH-561) - Create python program that returns fake management data
 - [DISPATCH-568](https://issues.apache.org/jira/browse/DISPATCH-568) - Iterator module cleanup
 - [DISPATCH-570](https://issues.apache.org/jira/browse/DISPATCH-570) - Add some counts to qdstat -g
 - [DISPATCH-572](https://issues.apache.org/jira/browse/DISPATCH-572) - Adding log info with proton transport id and related remote IP/port
 - [DISPATCH-576](https://issues.apache.org/jira/browse/DISPATCH-576) - Use new log entity statistic counter in console
 - [DISPATCH-578](https://issues.apache.org/jira/browse/DISPATCH-578) - Dispatch trace logging forces all proton tracing on
 - [DISPATCH-579](https://issues.apache.org/jira/browse/DISPATCH-579) - Expose software version via management
 - [DISPATCH-592](https://issues.apache.org/jira/browse/DISPATCH-592) - Attempt to auto-login to the host:port that served the web page
 - [DISPATCH-597](https://issues.apache.org/jira/browse/DISPATCH-597) - Log enhancements
 - [DISPATCH-600](https://issues.apache.org/jira/browse/DISPATCH-600) - Support secure websockets
 - [DISPATCH-602](https://issues.apache.org/jira/browse/DISPATCH-602) - Add a favicon to the stand-alone router site
 - [DISPATCH-606](https://issues.apache.org/jira/browse/DISPATCH-606) - Default session window is too small, causing performance bottlenecks
 - [DISPATCH-627](https://issues.apache.org/jira/browse/DISPATCH-627) - BatchedSettlement test fails with timeout on slower systems
 - [DISPATCH-629](https://issues.apache.org/jira/browse/DISPATCH-629) - Add a protocol-version to the inter-router protocol to enable backward compatibility
 - [DISPATCH-726](https://issues.apache.org/jira/browse/DISPATCH-726) - Connection Property for Failover Servers

## Bugs fixed

 - [DISPATCH-55](https://issues.apache.org/jira/browse/DISPATCH-55) - Qdrouterd does not exit when service port is unavailable
 - [DISPATCH-216](https://issues.apache.org/jira/browse/DISPATCH-216) - system_tests_protocol_family fails on systems with no IPv6
 - [DISPATCH-296](https://issues.apache.org/jira/browse/DISPATCH-296) - segfault on router startup
 - [DISPATCH-314](https://issues.apache.org/jira/browse/DISPATCH-314) - If a router has a normal listener, show it in a different color on the topology page
 - [DISPATCH-324](https://issues.apache.org/jira/browse/DISPATCH-324) - Improve initial layout of topology node
 - [DISPATCH-344](https://issues.apache.org/jira/browse/DISPATCH-344) - memory growth after repeated calls from qdstat -m
 - [DISPATCH-352](https://issues.apache.org/jira/browse/DISPATCH-352) - Crash with empty configuration file
 - [DISPATCH-355](https://issues.apache.org/jira/browse/DISPATCH-355) - query fails with what seems to be the error of a previous command
 - [DISPATCH-357](https://issues.apache.org/jira/browse/DISPATCH-357) - Address field is empty for link routed links in the qdstat "links" output
 - [DISPATCH-433](https://issues.apache.org/jira/browse/DISPATCH-433) - Navigating to console from bookmark displays empty page with just toolbars
 - [DISPATCH-451](https://issues.apache.org/jira/browse/DISPATCH-451) - [AMQP] Hard coded session capacity should be configurable
 - [DISPATCH-503](https://issues.apache.org/jira/browse/DISPATCH-503) - [display_name] successful test runs  have non-ascii characters in router log
 - [DISPATCH-504](https://issues.apache.org/jira/browse/DISPATCH-504) - [display_name] successful test runs have invalid message errors  in router log
 - [DISPATCH-506](https://issues.apache.org/jira/browse/DISPATCH-506) - Detach with no "error" sent by router on client TCP connection dropped
 - [DISPATCH-516](https://issues.apache.org/jira/browse/DISPATCH-516) - Core dump when displayname IO adapter receives message with no reply-to
 - [DISPATCH-526](https://issues.apache.org/jira/browse/DISPATCH-526) - Coverity scan reported memory leaks in Qpid Dispatch 0.7.0 
 - [DISPATCH-527](https://issues.apache.org/jira/browse/DISPATCH-527) - The $displayname address is currently available. It should not be available to external users
 - [DISPATCH-528](https://issues.apache.org/jira/browse/DISPATCH-528) - Remove workaround for port-in-hostname proton 0.12 bug
 - [DISPATCH-530](https://issues.apache.org/jira/browse/DISPATCH-530) - Cannot connect using Firefox 48+
 - [DISPATCH-534](https://issues.apache.org/jira/browse/DISPATCH-534) - Node selection and location is lost when the topology changes
 - [DISPATCH-536](https://issues.apache.org/jira/browse/DISPATCH-536) - Circular buffer overflow errors occur when there are a large number of routers
 - [DISPATCH-538](https://issues.apache.org/jira/browse/DISPATCH-538) - Highlighted path between routers sometimes doesn't unhighlight
 - [DISPATCH-540](https://issues.apache.org/jira/browse/DISPATCH-540) - Clients with both in and out links are rendered in yellow
 - [DISPATCH-541](https://issues.apache.org/jira/browse/DISPATCH-541) - Highlighted path between routers contains black arrows
 - [DISPATCH-546](https://issues.apache.org/jira/browse/DISPATCH-546) - Crosssection popup position is incorrect
 - [DISPATCH-547](https://issues.apache.org/jira/browse/DISPATCH-547) - Stand-alone version can't download generated config file for new nodes
 - [DISPATCH-549](https://issues.apache.org/jira/browse/DISPATCH-549) - Doc book needs more detailed introduction of system concepts
 - [DISPATCH-554](https://issues.apache.org/jira/browse/DISPATCH-554) - Topology nodes and links are too far apart when there are a large number of routers 
 - [DISPATCH-556](https://issues.apache.org/jira/browse/DISPATCH-556) - qdstat fails at high scale
 - [DISPATCH-557](https://issues.apache.org/jira/browse/DISPATCH-557) - High connection rates cause problems in the Python management agent
 - [DISPATCH-560](https://issues.apache.org/jira/browse/DISPATCH-560) - [console] Only use the color red to indicate a failure/issue.
 - [DISPATCH-563](https://issues.apache.org/jira/browse/DISPATCH-563) - Topology graph flashes and redraws a few seconds after it is 1st drawn 
 - [DISPATCH-564](https://issues.apache.org/jira/browse/DISPATCH-564) - Error when switching routers on Entities page
 - [DISPATCH-565](https://issues.apache.org/jira/browse/DISPATCH-565) - Error fetching log on Entities page
 - [DISPATCH-566](https://issues.apache.org/jira/browse/DISPATCH-566) - Message annotations are not propagated to brokers on a linkRoute
 - [DISPATCH-567](https://issues.apache.org/jira/browse/DISPATCH-567) - Slight but persistent memory leak when running java messenger producer and consumer
 - [DISPATCH-569](https://issues.apache.org/jira/browse/DISPATCH-569) - Dispatch does not compile due to new pn_event_type_t enum values.
 - [DISPATCH-573](https://issues.apache.org/jira/browse/DISPATCH-573) - Memory leaks on shutdown
 - [DISPATCH-574](https://issues.apache.org/jira/browse/DISPATCH-574) - Restore Qpid dispatch docs into man and book folders
 - [DISPATCH-577](https://issues.apache.org/jira/browse/DISPATCH-577) - Server logs show unexpected POLLNVAL errors.
 - [DISPATCH-581](https://issues.apache.org/jira/browse/DISPATCH-581) - detach with closed=false propagated as closed=true on link route
 - [DISPATCH-582](https://issues.apache.org/jira/browse/DISPATCH-582) - Memory Leak with reactor client
 - [DISPATCH-583](https://issues.apache.org/jira/browse/DISPATCH-583) - Random segmentation fault
 - [DISPATCH-585](https://issues.apache.org/jira/browse/DISPATCH-585) - Firefox dropdown and buttons on list page have incorrect padding
 - [DISPATCH-586](https://issues.apache.org/jira/browse/DISPATCH-586) - Dispatch crash on running c sender and receiver
 - [DISPATCH-587](https://issues.apache.org/jira/browse/DISPATCH-587) - Provide feedback when loading log entries
 - [DISPATCH-588](https://issues.apache.org/jira/browse/DISPATCH-588) - Schema is not loaded if auto-login is enabled
 - [DISPATCH-589](https://issues.apache.org/jira/browse/DISPATCH-589) - Missing links on topology page
 - [DISPATCH-594](https://issues.apache.org/jira/browse/DISPATCH-594) - Log file over-written every time the router is restarted
 - [DISPATCH-595](https://issues.apache.org/jira/browse/DISPATCH-595) - dispositions propagated after link detach on link route
 - [DISPATCH-596](https://issues.apache.org/jira/browse/DISPATCH-596) - error is lost from rejected state in relayed disposition
 - [DISPATCH-598](https://issues.apache.org/jira/browse/DISPATCH-598) - Router crash when calling sender and session close methods in onLinkFLow()
 - [DISPATCH-599](https://issues.apache.org/jira/browse/DISPATCH-599) - Link routing : messages is not transferred if sender detach link immediately
 - [DISPATCH-601](https://issues.apache.org/jira/browse/DISPATCH-601) - Valgrind errors in dispatch tests
 - [DISPATCH-603](https://issues.apache.org/jira/browse/DISPATCH-603) - address resource leak
 - [DISPATCH-604](https://issues.apache.org/jira/browse/DISPATCH-604) - Management - Link connection-id does not match identities of connections
 - [DISPATCH-605](https://issues.apache.org/jira/browse/DISPATCH-605) - Memory Leak with multple sender/receivers in one session
 - [DISPATCH-607](https://issues.apache.org/jira/browse/DISPATCH-607) - Handle empty response from GET-MGMT-NODES
 - [DISPATCH-608](https://issues.apache.org/jira/browse/DISPATCH-608) - Links not cleaned up when a close is sent without being preceeded by a detach and end
 - [DISPATCH-609](https://issues.apache.org/jira/browse/DISPATCH-609) - Name attribute is duplicated in QUERY response
 - [DISPATCH-610](https://issues.apache.org/jira/browse/DISPATCH-610) - crash in qdr_link_cleanup_CT
 - [DISPATCH-611](https://issues.apache.org/jira/browse/DISPATCH-611) - Router core dump with old config file
 - [DISPATCH-612](https://issues.apache.org/jira/browse/DISPATCH-612) - Add support for GCC equivalent compiler options
 - [DISPATCH-613](https://issues.apache.org/jira/browse/DISPATCH-613) - Remove semi-colon not needed after function definition
 - [DISPATCH-614](https://issues.apache.org/jira/browse/DISPATCH-614) - strerror_r on Solaris does not return char*
 - [DISPATCH-615](https://issues.apache.org/jira/browse/DISPATCH-615) - SunStudio doesn't convert pointers to bool correctly
 - [DISPATCH-616](https://issues.apache.org/jira/browse/DISPATCH-616) - Arithmetic operations not allowed on void * pointer
 - [DISPATCH-617](https://issues.apache.org/jira/browse/DISPATCH-617) - Define HOST_NAME_MAX on Unix OSes where _POSIX_HOST_NAME_MAX is defined instead
 - [DISPATCH-618](https://issues.apache.org/jira/browse/DISPATCH-618) - Revert eventfd on Solaris
 - [DISPATCH-619](https://issues.apache.org/jira/browse/DISPATCH-619) - Use memalign instead of posix_memalign which is not defined on Solaris
 - [DISPATCH-620](https://issues.apache.org/jira/browse/DISPATCH-620) - no-strict-aliasing is only supported with GCC
 - [DISPATCH-621](https://issues.apache.org/jira/browse/DISPATCH-621) - Add missing string.h include for Solaris compiler
 - [DISPATCH-622](https://issues.apache.org/jira/browse/DISPATCH-622) - use "-lpthread" instead of "-pthread" as compiler error to avoid undefined symbol on Solaris
 - [DISPATCH-623](https://issues.apache.org/jira/browse/DISPATCH-623) - Unreachable code (qd_field_iterator_free after a return statement) detected on Solaris
 - [DISPATCH-624](https://issues.apache.org/jira/browse/DISPATCH-624) - Add Atomic operations support on Solaris
 - [DISPATCH-626](https://issues.apache.org/jira/browse/DISPATCH-626) - Add hints for getaddrinfo on Solaris
 - [DISPATCH-628](https://issues.apache.org/jira/browse/DISPATCH-628) - [PATCH] Multiple connections per autoLink and linkRoute overwrites connection handle
 - [DISPATCH-631](https://issues.apache.org/jira/browse/DISPATCH-631) - Tests should be made conditional to skip tests for SASL features that are not available
 - [DISPATCH-633](https://issues.apache.org/jira/browse/DISPATCH-633) - Creating connectors and addresses returns success codes of two different types.
 - [DISPATCH-634](https://issues.apache.org/jira/browse/DISPATCH-634) - Dynamic Targets are unsupported
 - [DISPATCH-635](https://issues.apache.org/jira/browse/DISPATCH-635) - The Ubuntu CI tests that involve two routers are failing
 - [DISPATCH-636](https://issues.apache.org/jira/browse/DISPATCH-636) - README claims qpid-proton-c-devel &gt;= 0.13 is required; however, cmake complains with 0.14
 - [DISPATCH-637](https://issues.apache.org/jira/browse/DISPATCH-637) - system_tests_sasl_plain and system_tests_deprecated fail when cyrus-sasl-plain is not installed
 - [DISPATCH-640](https://issues.apache.org/jira/browse/DISPATCH-640) - containerId field conflics with the connector name
 - [DISPATCH-642](https://issues.apache.org/jira/browse/DISPATCH-642) - Fix recognition of Artemis broker on topology page
 - [DISPATCH-643](https://issues.apache.org/jira/browse/DISPATCH-643) - Duplicate log messages show up on normal AMQP close
 - [DISPATCH-644](https://issues.apache.org/jira/browse/DISPATCH-644) - Fix qdrouterd generating exit code 1 because of a pipe issue in Daemon mode
 - [DISPATCH-646](https://issues.apache.org/jira/browse/DISPATCH-646) - Link route tests which test the drain feature fail intermittently
 - [DISPATCH-647](https://issues.apache.org/jira/browse/DISPATCH-647) - Coverity scan reported memory leaks in Qpid Dispatch master
 - [DISPATCH-728](https://issues.apache.org/jira/browse/DISPATCH-728) - crash on shutdown with connector
 - [DISPATCH-729](https://issues.apache.org/jira/browse/DISPATCH-729) - password-file option doesn't work correctly
 - [DISPATCH-730](https://issues.apache.org/jira/browse/DISPATCH-730) - Coverity scan reported errors in Qpid Dispatch master
 - [DISPATCH-732](https://issues.apache.org/jira/browse/DISPATCH-732) - CONN_MGR log module is used in connection_manager.c but is missing from log schema
 - [DISPATCH-733](https://issues.apache.org/jira/browse/DISPATCH-733) - First ssl test in system_tests_qdmanage.py fails intermittently
 - [DISPATCH-734](https://issues.apache.org/jira/browse/DISPATCH-734) - Weird class / address name while using url like queue name
 - [DISPATCH-735](https://issues.apache.org/jira/browse/DISPATCH-735) - Crash on startup parsing JSON conf file with "address" entity
 - [DISPATCH-736](https://issues.apache.org/jira/browse/DISPATCH-736) - 3 system tests in the test suite are failing on RHEL 6.4
 - [DISPATCH-740](https://issues.apache.org/jira/browse/DISPATCH-740) - Remove tooltipsy.min.js and code associated with it
 - [DISPATCH-742](https://issues.apache.org/jira/browse/DISPATCH-742) - Assert while passing multicast or presettled anycast msgs across network
 - [DISPATCH-745](https://issues.apache.org/jira/browse/DISPATCH-745) - Hawtio version of console does not connect: app.js?60f4925a5c3d0942:16 Error: Error: Unknown provider: $uibModalProvider &lt;- $uibModal
 - [DISPATCH-746](https://issues.apache.org/jira/browse/DISPATCH-746) - Standalone console does not connect if port is left as default
 - [DISPATCH-751](https://issues.apache.org/jira/browse/DISPATCH-751) - Clicking entities/connector in stand-alone console prints "Error: [ngModel:numfmt] Expected `1` to be a number"

## Tasks

 - [DISPATCH-591](https://issues.apache.org/jira/browse/DISPATCH-591) - Add http listener to example/test router configs in the tests directory
 - [DISPATCH-639](https://issues.apache.org/jira/browse/DISPATCH-639) - Document proper usage of containerId for autoLinks/linkRoutes entities