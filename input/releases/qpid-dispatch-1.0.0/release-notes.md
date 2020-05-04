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

# Qpid Dispatch 1.0.0 Release Notes

Dispatch is a lightweight AMQP 1.0 message router. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-209](https://issues.apache.org/jira/browse/DISPATCH-209) - Three+ router test is needed in the system test suite.
 - [DISPATCH-390](https://issues.apache.org/jira/browse/DISPATCH-390) - New pn_proactor-based IO driver
 - [DISPATCH-525](https://issues.apache.org/jira/browse/DISPATCH-525) - What are proper names and units for protocol configuration settings?
 - [DISPATCH-551](https://issues.apache.org/jira/browse/DISPATCH-551) - disconnect connections that do not complete initial protocol handshake within a given time 
 - [DISPATCH-584](https://issues.apache.org/jira/browse/DISPATCH-584) - Large, highly redundant router networks generate excessive inter-router message traffic
 - [DISPATCH-731](https://issues.apache.org/jira/browse/DISPATCH-731) - Support wildcard tenant vhosts in address prefix configuration
 - [DISPATCH-744](https://issues.apache.org/jira/browse/DISPATCH-744) - Reject unsettled deliveries to multicast addresses by default
 - [DISPATCH-767](https://issues.apache.org/jira/browse/DISPATCH-767) - Message Cut-Through/Streaming for efficient handling of large messages
 - [DISPATCH-770](https://issues.apache.org/jira/browse/DISPATCH-770) - Show error if creating an entity using web console fails
 - [DISPATCH-771](https://issues.apache.org/jira/browse/DISPATCH-771) - Mark mandatory fields when creating a new entity in the web console
 - [DISPATCH-775](https://issues.apache.org/jira/browse/DISPATCH-775) - allow authentication against a remote server
 - [DISPATCH-788](https://issues.apache.org/jira/browse/DISPATCH-788) - Create peer linkage for presettled deliveries so we can use this to handle muticast dispositions
 - [DISPATCH-795](https://issues.apache.org/jira/browse/DISPATCH-795) - Sort entity names on Schema page to make them easier to find
 - [DISPATCH-796](https://issues.apache.org/jira/browse/DISPATCH-796) - The Python and the C management agents do not have an AMQP header in their responses.
 - [DISPATCH-803](https://issues.apache.org/jira/browse/DISPATCH-803) - refuse attach to undefined addresses
 - [DISPATCH-809](https://issues.apache.org/jira/browse/DISPATCH-809) - Add options to enable Sanitizers to CMake build
 - [DISPATCH-813](https://issues.apache.org/jira/browse/DISPATCH-813) - Support wildcard format for link-routes
 - [DISPATCH-818](https://issues.apache.org/jira/browse/DISPATCH-818) - Honor failoverList provided by connected brokers
 - [DISPATCH-827](https://issues.apache.org/jira/browse/DISPATCH-827) - Large message discard buffer too small
 - [DISPATCH-828](https://issues.apache.org/jira/browse/DISPATCH-828) - Discarded message processing does not close callback window
 - [DISPATCH-839](https://issues.apache.org/jira/browse/DISPATCH-839) - Improve the batching of allocated objects
 - [DISPATCH-844](https://issues.apache.org/jira/browse/DISPATCH-844) - Make TLS cipher suites configurable
 - [DISPATCH-858](https://issues.apache.org/jira/browse/DISPATCH-858) - Simplify hard to follow LICENSE file

## Bugs fixed

 - [DISPATCH-421](https://issues.apache.org/jira/browse/DISPATCH-421) - Toasts messages are not logged in the rolldown "logging console"
 - [DISPATCH-430](https://issues.apache.org/jira/browse/DISPATCH-430) - Cursor snaps way above peaks in a rate chart
 - [DISPATCH-571](https://issues.apache.org/jira/browse/DISPATCH-571) - Driver spins when a listener accepts a socket while FDs are all in use
 - [DISPATCH-737](https://issues.apache.org/jira/browse/DISPATCH-737) - qdstat and qdmanage always force sasl exchange
 - [DISPATCH-741](https://issues.apache.org/jira/browse/DISPATCH-741) - Coverity scan reported errors in Qpid Dispatch master
 - [DISPATCH-743](https://issues.apache.org/jira/browse/DISPATCH-743) - Intermittent SSL Failure
 - [DISPATCH-747](https://issues.apache.org/jira/browse/DISPATCH-747) - Console does not handle connection errors well
 - [DISPATCH-748](https://issues.apache.org/jira/browse/DISPATCH-748) - Error message shown when rapidly clicking treeview on left side of hawtio console: Uncaught TypeError: Cannot read property 'height' of null
 - [DISPATCH-749](https://issues.apache.org/jira/browse/DISPATCH-749) - unmapping all link-routing addresses leaves half of addresses mapped
 - [DISPATCH-750](https://issues.apache.org/jira/browse/DISPATCH-750) - Missing icons and bad rendering of dynatree treeviews in Microsoft Edge 14
 - [DISPATCH-752](https://issues.apache.org/jira/browse/DISPATCH-752) - With more than one outbound SSL connections, failure in one affects all others
 - [DISPATCH-753](https://issues.apache.org/jira/browse/DISPATCH-753) - Neither version of console is usable on Internet Explorer 10 or 11
 - [DISPATCH-754](https://issues.apache.org/jira/browse/DISPATCH-754) - Output of qdstat shows authentication on client SSL connections as anonymous (x.509)
 - [DISPATCH-756](https://issues.apache.org/jira/browse/DISPATCH-756) - Fix Fedora and Ubuntu docker files to use libuv and libwebsockets
 - [DISPATCH-757](https://issues.apache.org/jira/browse/DISPATCH-757) - Qpid Dispatch does not compile under Ubuntu
 - [DISPATCH-758](https://issues.apache.org/jira/browse/DISPATCH-758) - test_listen_error() in system_tests_one_router.py and system_tests_http.py hang inside a docker environment 
 - [DISPATCH-759](https://issues.apache.org/jira/browse/DISPATCH-759) - Core thread consumed deleting deliveries
 - [DISPATCH-761](https://issues.apache.org/jira/browse/DISPATCH-761) - Router crash on abrupt close of sender/receiver connections
 - [DISPATCH-762](https://issues.apache.org/jira/browse/DISPATCH-762) - Hawtio console does not show details about a connection whereas stand-alone console does
 - [DISPATCH-763](https://issues.apache.org/jira/browse/DISPATCH-763) - Router crashes when config file defines listener { addr: } instead of { host: }
 - [DISPATCH-765](https://issues.apache.org/jira/browse/DISPATCH-765) - Three unit tests failing under travis on trusty
 - [DISPATCH-766](https://issues.apache.org/jira/browse/DISPATCH-766) - Update Dockerfile-ubuntu to include libwebsockets
 - [DISPATCH-768](https://issues.apache.org/jira/browse/DISPATCH-768) - On topology page, show connections that go to more than one router
 - [DISPATCH-769](https://issues.apache.org/jira/browse/DISPATCH-769) - Links popup on topology page only shows a single link
 - [DISPATCH-772](https://issues.apache.org/jira/browse/DISPATCH-772) - Buttons to Create and Delete entity disappear after navigation in either version of console
 - [DISPATCH-777](https://issues.apache.org/jira/browse/DISPATCH-777) - [system_tests_drain] pn_object_free: corrupted double-linked list
 - [DISPATCH-779](https://issues.apache.org/jira/browse/DISPATCH-779) - Credit is not issued for multicast address when no receiver is connected
 - [DISPATCH-780](https://issues.apache.org/jira/browse/DISPATCH-780) - When link is disallowed due to target/source name it should not return amqp:resource-limit-exceeded
 - [DISPATCH-784](https://issues.apache.org/jira/browse/DISPATCH-784) - Delivery annotations are not propagated by the router
 - [DISPATCH-787](https://issues.apache.org/jira/browse/DISPATCH-787) - c epoll proactor can raise SIGPIPE
 - [DISPATCH-789](https://issues.apache.org/jira/browse/DISPATCH-789) - Console breaks when quickly moving between tabs (both hawtio and stand-alone)
 - [DISPATCH-790](https://issues.apache.org/jira/browse/DISPATCH-790) - The right-mouse-click menu on Topology tab appears off-center in the stand-alone console
 - [DISPATCH-791](https://issues.apache.org/jira/browse/DISPATCH-791) - The node representing Console in Topology tab is not displayed
 - [DISPATCH-792](https://issues.apache.org/jira/browse/DISPATCH-792) - Freezing and moving nodes is somewhat broken (in either version of console)
 - [DISPATCH-794](https://issues.apache.org/jira/browse/DISPATCH-794) - Arrows in topology graph for IE 11 are hollow
 - [DISPATCH-798](https://issues.apache.org/jira/browse/DISPATCH-798) - Policy description in Dispatch Router book seems to be incorrect
 - [DISPATCH-799](https://issues.apache.org/jira/browse/DISPATCH-799) - Using USE_VALGRIND does not invoke valgrind when running tests
 - [DISPATCH-800](https://issues.apache.org/jira/browse/DISPATCH-800) - Hawtio version of the console is unable to connect to a router when running offline
 - [DISPATCH-802](https://issues.apache.org/jira/browse/DISPATCH-802) - refuse transaction coordination links if they can't be routed to a coordinator
 - [DISPATCH-804](https://issues.apache.org/jira/browse/DISPATCH-804) - connectors ignore addr
 - [DISPATCH-805](https://issues.apache.org/jira/browse/DISPATCH-805) - System test system_tests_sasl_plain fails in systems with TLSv1.2
 - [DISPATCH-806](https://issues.apache.org/jira/browse/DISPATCH-806) - Go thru every deprecated entity and make sure a warning is put out when a deprecated entity is used.
 - [DISPATCH-807](https://issues.apache.org/jira/browse/DISPATCH-807) - Message handling requires flow control to limit memory consumption
 - [DISPATCH-808](https://issues.apache.org/jira/browse/DISPATCH-808) - Setting defaultDistribution: unavailable blocks qdmanage
 - [DISPATCH-810](https://issues.apache.org/jira/browse/DISPATCH-810) - auto link fails to trigger
 - [DISPATCH-811](https://issues.apache.org/jira/browse/DISPATCH-811) - Attributes tab label spelled 'Attriutes'
 - [DISPATCH-814](https://issues.apache.org/jira/browse/DISPATCH-814) - Killing qdrouterd process takes a long time
 - [DISPATCH-815](https://issues.apache.org/jira/browse/DISPATCH-815) - shebang python (#!/usr/bin/env python) gets evaluated on make install
 - [DISPATCH-816](https://issues.apache.org/jira/browse/DISPATCH-816) - Router crashes if connection closed while router is processing attach on that connection 
 - [DISPATCH-820](https://issues.apache.org/jira/browse/DISPATCH-820) - double delete of address hash
 - [DISPATCH-821](https://issues.apache.org/jira/browse/DISPATCH-821) - recreating an address immediately after deleting it, results in error
 - [DISPATCH-822](https://issues.apache.org/jira/browse/DISPATCH-822) - loss of SSL connection breaks other SSL connections
 - [DISPATCH-823](https://issues.apache.org/jira/browse/DISPATCH-823) - Improve logging for lost connections
 - [DISPATCH-824](https://issues.apache.org/jira/browse/DISPATCH-824) - Remove deprecated entities and attributes from the router schema.
 - [DISPATCH-826](https://issues.apache.org/jira/browse/DISPATCH-826) - Specifying an invalid host on the connector crashes the router
 - [DISPATCH-829](https://issues.apache.org/jira/browse/DISPATCH-829) - The router does not set the "aborted" indication on truncated, streamed deliveries
 - [DISPATCH-835](https://issues.apache.org/jira/browse/DISPATCH-835) - The DETACH/CLOSE sequence causes a memory leak
 - [DISPATCH-837](https://issues.apache.org/jira/browse/DISPATCH-837) - Coverity scan reported errors in Qpid Dispatch master
 - [DISPATCH-841](https://issues.apache.org/jira/browse/DISPATCH-841) - Decrease default limit of rows returned by qdstat from 1000 to 100
 - [DISPATCH-842](https://issues.apache.org/jira/browse/DISPATCH-842) - Include missing license information in the LICENSE file
 - [DISPATCH-846](https://issues.apache.org/jira/browse/DISPATCH-846) - Memory leaks in ctest with valgrind
 - [DISPATCH-847](https://issues.apache.org/jira/browse/DISPATCH-847) - Fix issues discovered by Coverity
 - [DISPATCH-855](https://issues.apache.org/jira/browse/DISPATCH-855) - Router crash when disconnecting from console
 - [DISPATCH-857](https://issues.apache.org/jira/browse/DISPATCH-857) - Router crash when ctrl-c on router that has a libwebsockets listener connected to a console
 - [DISPATCH-860](https://issues.apache.org/jira/browse/DISPATCH-860) - Link Route tests failing intermittently.
 - [DISPATCH-865](https://issues.apache.org/jira/browse/DISPATCH-865) - Segmentation fault while running 2-node Artemis tests
 - [DISPATCH-867](https://issues.apache.org/jira/browse/DISPATCH-867) - Messages stuck going through link route
 - [DISPATCH-870](https://issues.apache.org/jira/browse/DISPATCH-870) - connection improperly reopened from closed connector
 - [DISPATCH-871](https://issues.apache.org/jira/browse/DISPATCH-871) - Performance issues with large messages
 - [DISPATCH-873](https://issues.apache.org/jira/browse/DISPATCH-873) - new routes calculated wrongly after connector deletion
 - [DISPATCH-924](https://issues.apache.org/jira/browse/DISPATCH-924) - [CVE-2017-15699] Denial of Service Vulnerability when specially crafted frame is sent to the Router

## Tasks

 - [DISPATCH-812](https://issues.apache.org/jira/browse/DISPATCH-812) - Remove the console stress test directories
 - [DISPATCH-832](https://issues.apache.org/jira/browse/DISPATCH-832) - Ensure the hawtio and stand-alone consoles work with deprecated entities removed