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

# Qpid Proton 0.18.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-749](https://issues.apache.org/jira/browse/PROTON-749) - Refactor Proton C transport code
 - [PROTON-1175](https://issues.apache.org/jira/browse/PROTON-1175) - Document BlockingConnection resource cleanup
 - [PROTON-1339](https://issues.apache.org/jira/browse/PROTON-1339) - Event_loop injection is very slow to trigger the events
 - [PROTON-1347](https://issues.apache.org/jira/browse/PROTON-1347) - Container prints to stderr on connection timed out
 - [PROTON-1369](https://issues.apache.org/jira/browse/PROTON-1369) - Add deprecation warnings to the C++ binding
 - [PROTON-1400](https://issues.apache.org/jira/browse/PROTON-1400) - Use the Proactor API for the IO/Event implementation
 - [PROTON-1401](https://issues.apache.org/jira/browse/PROTON-1401) - Improve pn_handle_t constness
 - [PROTON-1402](https://issues.apache.org/jira/browse/PROTON-1402) - Simplify access to object contexts 
 - [PROTON-1416](https://issues.apache.org/jira/browse/PROTON-1416) - Reconnect when receiving connection close with amqp:connection:forced condition
 - [PROTON-1419](https://issues.apache.org/jira/browse/PROTON-1419) - c libuv proactor log all events
 - [PROTON-1421](https://issues.apache.org/jira/browse/PROTON-1421) - c proactor to take a connection URL string rather than host, port
 - [PROTON-1423](https://issues.apache.org/jira/browse/PROTON-1423) - Python reconnect on amqp:connection:forced 
 - [PROTON-1437](https://issues.apache.org/jira/browse/PROTON-1437) - c proactor address info
 - [PROTON-1438](https://issues.apache.org/jira/browse/PROTON-1438) - c proactor listening behavior
 - [PROTON-1440](https://issues.apache.org/jira/browse/PROTON-1440) - pn_connection_wake to return bool status
 - [PROTON-1445](https://issues.apache.org/jira/browse/PROTON-1445) - Change proactor ownership model
 - [PROTON-1450](https://issues.apache.org/jira/browse/PROTON-1450) - Add Filter LinkOption to Electron API
 - [PROTON-1452](https://issues.apache.org/jira/browse/PROTON-1452) - add pn_proactor_disconnect
 - [PROTON-1460](https://issues.apache.org/jira/browse/PROTON-1460) - C "proactor" epoll implementation
 - [PROTON-1471](https://issues.apache.org/jira/browse/PROTON-1471) - Implement platform independent timestamp
 - [PROTON-1472](https://issues.apache.org/jira/browse/PROTON-1472) - travis test for libuv proactor
 - [PROTON-1476](https://issues.apache.org/jira/browse/PROTON-1476) - C tests strict aliasing error on gcc 4.4.7
 - [PROTON-1479](https://issues.apache.org/jira/browse/PROTON-1479) - C++ scheduled_send examples send in an unsafe context
 - [PROTON-1481](https://issues.apache.org/jira/browse/PROTON-1481) - Improve the capability to inject work into serialised contexts
 - [PROTON-1482](https://issues.apache.org/jira/browse/PROTON-1482) - Add capability to schedule work to happen later on work queues
 - [PROTON-1488](https://issues.apache.org/jira/browse/PROTON-1488) - Making Python server example more configurable
 - [PROTON-1500](https://issues.apache.org/jira/browse/PROTON-1500) - Allow plugin SASL implementations
 - [PROTON-1502](https://issues.apache.org/jira/browse/PROTON-1502) - always encode empty proprty maps as missing properties, not empty maps
 - [PROTON-1506](https://issues.apache.org/jira/browse/PROTON-1506) - Expose max frame size
 - [PROTON-1512](https://issues.apache.org/jira/browse/PROTON-1512) - Expose the "aborted" flag for transferred deliveries
 - [PROTON-1520](https://issues.apache.org/jira/browse/PROTON-1520) - C epoll proactor delayed socket writes
 - [PROTON-1536](https://issues.apache.org/jira/browse/PROTON-1536) - There is no way using the C++ binding connection_driver API to either send heartbeat frames, or recognise heartbeat timeouts
 - [PROTON-1540](https://issues.apache.org/jira/browse/PROTON-1540) - Add options to enable Sanitizers to CMake build
 - [PROTON-1543](https://issues.apache.org/jira/browse/PROTON-1543) - Various improvements to the docs and examples
 - [PROTON-1553](https://issues.apache.org/jira/browse/PROTON-1553) - c++ add support for wake() with MT example
 - [PROTON-1554](https://issues.apache.org/jira/browse/PROTON-1554) - c++: remove thread_safe and returned templates
 - [PROTON-1566](https://issues.apache.org/jira/browse/PROTON-1566) - Implement reconnect
 - [PROTON-1567](https://issues.apache.org/jira/browse/PROTON-1567) - Implement Failover
 - [PROTON-1576](https://issues.apache.org/jira/browse/PROTON-1576) - c++: remove link_namer from public API
 - [PROTON-1584](https://issues.apache.org/jira/browse/PROTON-1584) - ruby: remove examples for deprecated Messenger API
 - [PROTON-1605](https://issues.apache.org/jira/browse/PROTON-1605) - Use a mutex instead of atomics for broader platform support
 - [PROTON-1609](https://issues.apache.org/jira/browse/PROTON-1609) - build C examples with c90 flag for older compilers
 - [PROTON-1617](https://issues.apache.org/jira/browse/PROTON-1617) - Expose the "aborted" flag for deliveries in the Python binding
 - [PROTON-1618](https://issues.apache.org/jira/browse/PROTON-1618) - Give unambiguous indication when server listen operation succeeds or fails
 - [PROTON-1621](https://issues.apache.org/jira/browse/PROTON-1621) - Enable C++11 example testing for C++11 build environments

## Bugs fixed

 - [PROTON-785](https://issues.apache.org/jira/browse/PROTON-785) - pn_code is missing one error code
 - [PROTON-876](https://issues.apache.org/jira/browse/PROTON-876) - python examples installed under share are not executable
 - [PROTON-1043](https://issues.apache.org/jira/browse/PROTON-1043) - Possible typo in messenger.c
 - [PROTON-1278](https://issues.apache.org/jira/browse/PROTON-1278) - [Proton-c] Closing connection in proton::handler puts connection in TIME_WAIT state
 - [PROTON-1288](https://issues.apache.org/jira/browse/PROTON-1288) - c++ provide access to message maps as proton::value
 - [PROTON-1326](https://issues.apache.org/jira/browse/PROTON-1326) - Compilation failures against OpenSSL v1.1.0
 - [PROTON-1340](https://issues.apache.org/jira/browse/PROTON-1340) - [Visual Studio 2013] Event_loop injection triggers an exception when the container is being destroyed
 - [PROTON-1345](https://issues.apache.org/jira/browse/PROTON-1345) - [python] Avoid hardcoding the list of C files to be compiled in setup.py
 - [PROTON-1357](https://issues.apache.org/jira/browse/PROTON-1357) - Example C clients do not disconnect on protocol errors
 - [PROTON-1358](https://issues.apache.org/jira/browse/PROTON-1358) - Memory leak in proactor receiver example if I add a timeout
 - [PROTON-1359](https://issues.apache.org/jira/browse/PROTON-1359) - heap-buffer-overflow in pn_decoder_readf32 when invoking pn_message_decode
 - [PROTON-1360](https://issues.apache.org/jira/browse/PROTON-1360) - pn_strndup (util.c:150) Invalid write of size 1
 - [PROTON-1381](https://issues.apache.org/jira/browse/PROTON-1381) - Compiler errors: dereferencing pointer to incomplete type DH {aka struct dh_st}
 - [PROTON-1394](https://issues.apache.org/jira/browse/PROTON-1394) - Creating a Container leaks two file descriptors
 - [PROTON-1403](https://issues.apache.org/jira/browse/PROTON-1403) - c proactor library
 - [PROTON-1407](https://issues.apache.org/jira/browse/PROTON-1407) - pn_collector_next and pn_collector_peek are inconsistent
 - [PROTON-1408](https://issues.apache.org/jira/browse/PROTON-1408) - long-lived connections suffer large performance hit after many messages
 - [PROTON-1413](https://issues.apache.org/jira/browse/PROTON-1413) - [proactor] Assertion `ps-&gt;next == &amp;UNLISTED' failed
 - [PROTON-1415](https://issues.apache.org/jira/browse/PROTON-1415) - go binding does not create durable subscriber
 - [PROTON-1417](https://issues.apache.org/jira/browse/PROTON-1417) - [python] TypeError on listener when handling address already in use
 - [PROTON-1418](https://issues.apache.org/jira/browse/PROTON-1418) - c pn_logf() leaks memory one each call
 - [PROTON-1422](https://issues.apache.org/jira/browse/PROTON-1422) - c libuv proactor should not require extras library
 - [PROTON-1439](https://issues.apache.org/jira/browse/PROTON-1439) - messenger tests fail sporadically with interrupt error 
 - [PROTON-1443](https://issues.apache.org/jira/browse/PROTON-1443) - c proactor - change timeout(0) to mean immediate
 - [PROTON-1453](https://issues.apache.org/jira/browse/PROTON-1453) - pn_ssl_get_{protocol|cypher}_name() may segfault when called by bindings
 - [PROTON-1454](https://issues.apache.org/jira/browse/PROTON-1454) - C proactor API doc overhaul, minor API improvements.
 - [PROTON-1456](https://issues.apache.org/jira/browse/PROTON-1456) - [go] Add AMQP described type support
 - [PROTON-1457](https://issues.apache.org/jira/browse/PROTON-1457) - Ruby tests fail when dependencies are missing
 - [PROTON-1463](https://issues.apache.org/jira/browse/PROTON-1463) - Golang AMQP URL incompatable with Qpid Cpp Broker.  Node not found: /address when using Qpid C++ Broker
 - [PROTON-1466](https://issues.apache.org/jira/browse/PROTON-1466) - Container.create_receiver() does not create all receivers with certain names
 - [PROTON-1469](https://issues.apache.org/jira/browse/PROTON-1469) - c libuv proactor on_write called after transport close
 - [PROTON-1470](https://issues.apache.org/jira/browse/PROTON-1470) - proactor api - flexible, parse-free addressing
 - [PROTON-1474](https://issues.apache.org/jira/browse/PROTON-1474) - C examples no longer compile independently
 - [PROTON-1480](https://issues.apache.org/jira/browse/PROTON-1480) - hello_world_direct example calls listener::stop twice
 - [PROTON-1483](https://issues.apache.org/jira/browse/PROTON-1483) - proactor/epoll.c:181: ptimer_callback: Assertion
 - [PROTON-1490](https://issues.apache.org/jira/browse/PROTON-1490) - c-proactor-test sporadic failures
 - [PROTON-1491](https://issues.apache.org/jira/browse/PROTON-1491) - C epoll proactor has straggling callback after connection teardown
 - [PROTON-1493](https://issues.apache.org/jira/browse/PROTON-1493) - c-proactor make pn_proactor_interrupt async-signal-safe
 - [PROTON-1494](https://issues.apache.org/jira/browse/PROTON-1494) - PN_PROACTOR_INACTIVE event does not behave as documented
 - [PROTON-1495](https://issues.apache.org/jira/browse/PROTON-1495) - c proactor handling file descriptor shortage
 - [PROTON-1498](https://issues.apache.org/jira/browse/PROTON-1498) - [C++ binding] Message annotation_map works as value, but not as ref
 - [PROTON-1501](https://issues.apache.org/jira/browse/PROTON-1501) - c epoll proactor can raise SIGPIPE
 - [PROTON-1503](https://issues.apache.org/jira/browse/PROTON-1503) - Using Python os.tempfile is not guaranteed to work on Windows
 - [PROTON-1504](https://issues.apache.org/jira/browse/PROTON-1504) - epoll proactor: no PN_LISTENER_ACCEPT events if no FDs available
 - [PROTON-1519](https://issues.apache.org/jira/browse/PROTON-1519) - qpid_proton 0.17.0 Ruby gem does not work with Ruby 2.4.1
 - [PROTON-1524](https://issues.apache.org/jira/browse/PROTON-1524) - Libuv proactor does not correctly count active timeouts
 - [PROTON-1526](https://issues.apache.org/jira/browse/PROTON-1526) - make install fails on Fedora
 - [PROTON-1527](https://issues.apache.org/jira/browse/PROTON-1527) - Compile C++ binding with C++11 if it is available
 - [PROTON-1528](https://issues.apache.org/jira/browse/PROTON-1528) - [C++ binding] AMQP open sent with container ID as empty string
 - [PROTON-1529](https://issues.apache.org/jira/browse/PROTON-1529) - Fix Omitted null checks in openssl code
 - [PROTON-1530](https://issues.apache.org/jira/browse/PROTON-1530) - python client does not delegate unhandled events on txn controller link
 - [PROTON-1532](https://issues.apache.org/jira/browse/PROTON-1532) - Undefined method "plain" for SASL in Ruby binding
 - [PROTON-1533](https://issues.apache.org/jira/browse/PROTON-1533) - Swig deprecation warnings with recent versions of cmake
 - [PROTON-1534](https://issues.apache.org/jira/browse/PROTON-1534) - Python client BlockingConnection fails cleanup on LinkDetached exception with socket in close_wait and straggling pipe
 - [PROTON-1535](https://issues.apache.org/jira/browse/PROTON-1535) - Can't set hostname on SASL-INIT through sasl plugin interface
 - [PROTON-1538](https://issues.apache.org/jira/browse/PROTON-1538) - Epoll proactor unguarded memory access
 - [PROTON-1539](https://issues.apache.org/jira/browse/PROTON-1539) - Kerberos SASL exchange results in malformed SASL response frame
 - [PROTON-1548](https://issues.apache.org/jira/browse/PROTON-1548) - C++ proactor_container_impl deadlock in schedule
 - [PROTON-1560](https://issues.apache.org/jira/browse/PROTON-1560) - Cannot install qpid_proton-0.18.0.gem
 - [PROTON-1562](https://issues.apache.org/jira/browse/PROTON-1562) - Executing ssl_client_cert example results in core on centos distro
 - [PROTON-1563](https://issues.apache.org/jira/browse/PROTON-1563) - examples/c/proactor/broker.c does not compile on centos 7
 - [PROTON-1564](https://issues.apache.org/jira/browse/PROTON-1564) - epoll proactor pn_proactor_release_connection reconnect bugs
 - [PROTON-1568](https://issues.apache.org/jira/browse/PROTON-1568) - add helgrind race detection to tests, fix all issues discovered
 - [PROTON-1570](https://issues.apache.org/jira/browse/PROTON-1570) - SASL auth with GSSAPI fails: client isn't sending correct AMQP header even though SASL is explicitly enabled
 - [PROTON-1571](https://issues.apache.org/jira/browse/PROTON-1571) - The ssl C++ example appears leaky, proton::listener does not have a destructor
 - [PROTON-1572](https://issues.apache.org/jira/browse/PROTON-1572) - CppCheck 1.8 warnings
 - [PROTON-1573](https://issues.apache.org/jira/browse/PROTON-1573) - Undefined behavior in some calls to memmove in Proton
 - [PROTON-1574](https://issues.apache.org/jira/browse/PROTON-1574) - WARNING: ThreadSanitizer: lock-order-inversion (potential deadlock) due to missing unlock in stop_polling()
 - [PROTON-1579](https://issues.apache.org/jira/browse/PROTON-1579) - go: restore testing with -race
 - [PROTON-1580](https://issues.apache.org/jira/browse/PROTON-1580) - go: example tests failing in URL parser
 - [PROTON-1586](https://issues.apache.org/jira/browse/PROTON-1586) - [proton-c] examples send core dumps on specifying invalid host
 - [PROTON-1587](https://issues.apache.org/jira/browse/PROTON-1587) - failure on one SSL connection causes error:140E0197:SSL routines:SSL_shutdown:shutdown while in init
 - [PROTON-1588](https://issues.apache.org/jira/browse/PROTON-1588) - c++ libuv proactor release_connection bug
 - [PROTON-1590](https://issues.apache.org/jira/browse/PROTON-1590) - Segfaults when compiling C++03 clients with a C++11 compiled proton-cpp library
 - [PROTON-1591](https://issues.apache.org/jira/browse/PROTON-1591) - [proton-cpp] Scheduling task from a scheduled task will deadlock
 - [PROTON-1601](https://issues.apache.org/jira/browse/PROTON-1601) - windows proactor fails ipv6 target ":::5672"
 - [PROTON-1602](https://issues.apache.org/jira/browse/PROTON-1602) - [Ruby] Possible memory leak in Ruby bindings?
 - [PROTON-1604](https://issues.apache.org/jira/browse/PROTON-1604) - Windows C++ prefers std::endl to newlines
 - [PROTON-1607](https://issues.apache.org/jira/browse/PROTON-1607) - Some C examples can't be compiled using Visual Studio 2010
 - [PROTON-1608](https://issues.apache.org/jira/browse/PROTON-1608) - Logic for checking channel_max is wrong (checking against wrong protocol field)
 - [PROTON-1610](https://issues.apache.org/jira/browse/PROTON-1610) - Intermittent self test fails
 - [PROTON-1611](https://issues.apache.org/jira/browse/PROTON-1611) - cmake fails if g++ not installed
 - [PROTON-1616](https://issues.apache.org/jira/browse/PROTON-1616) - Review and fix Coverity issues for Proton
 - [PROTON-1623](https://issues.apache.org/jira/browse/PROTON-1623) - [c, examples] receiver overwrites existing message with subsequent transfer
 - [PROTON-1624](https://issues.apache.org/jira/browse/PROTON-1624) - [c, examples] Send core dumps sending string longer than 128 bytes
 - [PROTON-1630](https://issues.apache.org/jira/browse/PROTON-1630) - #include "proton/default_container.hpp" does not compile
 - [PROTON-1633](https://issues.apache.org/jira/browse/PROTON-1633) - Windows Link warnings due to unnecessary command line flags
 - [PROTON-1635](https://issues.apache.org/jira/browse/PROTON-1635) - Does not build with gcc 4.4.7

## Tasks

 - [PROTON-209](https://issues.apache.org/jira/browse/PROTON-209) - Update README file(s) to more specific about required versions of tools
 - [PROTON-1368](https://issues.apache.org/jira/browse/PROTON-1368) - Remove parser from the public API
 - [PROTON-1397](https://issues.apache.org/jira/browse/PROTON-1397) - 0.18.0 release tasks
 - [PROTON-1619](https://issues.apache.org/jira/browse/PROTON-1619) - C and C++ API clean up