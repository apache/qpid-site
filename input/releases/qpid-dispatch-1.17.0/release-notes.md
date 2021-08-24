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

# Qpid Dispatch 1.17.0 Release Notes

Dispatch is a lightweight AMQP 1.0 message router. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-1539](https://issues.apache.org/jira/browse/DISPATCH-1539) - Python 2 has expired. What is the qpid-dispatch strategy going forward?
 - [DISPATCH-2108](https://issues.apache.org/jira/browse/DISPATCH-2108) - TCP adaptor should aggregate statistics for listener and connector
 - [DISPATCH-2142](https://issues.apache.org/jira/browse/DISPATCH-2142) - use dedicated buffers in tcp adaptor
 - [DISPATCH-2178](https://issues.apache.org/jira/browse/DISPATCH-2178) - Do not build separate libqpid-dispatch.so
 - [DISPATCH-2198](https://issues.apache.org/jira/browse/DISPATCH-2198) - [http2] Implement http2 flow control that incorporates q2 blocking/unblocking
 - [DISPATCH-2201](https://issues.apache.org/jira/browse/DISPATCH-2201) - Remove the type_registered global flag in router_node.c
 - [DISPATCH-2211](https://issues.apache.org/jira/browse/DISPATCH-2211) - [http2] system_tests_grpc fails asan with one leaking http2 buffer
 - [DISPATCH-2212](https://issues.apache.org/jira/browse/DISPATCH-2212) - [http2] When creating an AMQP message set its subject field to method (on request) and status (on response)
 - [DISPATCH-2215](https://issues.apache.org/jira/browse/DISPATCH-2215) - [http2] Wrong printf format specifier in read_data_callback 

## Bugs fixed

 - [DISPATCH-1619](https://issues.apache.org/jira/browse/DISPATCH-1619) - System test never closes connections created by wait_router_connected
 - [DISPATCH-1623](https://issues.apache.org/jira/browse/DISPATCH-1623) - Investigate why the console sometimes drops the connection to the router a few seconds after login
 - [DISPATCH-1772](https://issues.apache.org/jira/browse/DISPATCH-1772) - Fallback destination test prints insufficient data when it fails
 - [DISPATCH-1865](https://issues.apache.org/jira/browse/DISPATCH-1865) - [http2] curl client hangs when running multiple clients against HTTP2 adaptor 
 - [DISPATCH-1878](https://issues.apache.org/jira/browse/DISPATCH-1878) - Client app not getting a response through tcpListener
 - [DISPATCH-1896](https://issues.apache.org/jira/browse/DISPATCH-1896) - [http2] GOAWAY frame received from server not propagated to client
 - [DISPATCH-1914](https://issues.apache.org/jira/browse/DISPATCH-1914) - Console Entities view looks to be misformatted
 - [DISPATCH-1963](https://issues.apache.org/jira/browse/DISPATCH-1963) - Memory leak in http1 adaptor
 - [DISPATCH-1975](https://issues.apache.org/jira/browse/DISPATCH-1975) - TCP adaptor sends only 512-byte packets over network
 - [DISPATCH-1976](https://issues.apache.org/jira/browse/DISPATCH-1976) - HTTP1 adaptor must not call proton functions after pn_raw_connection_close
 - [DISPATCH-1977](https://issues.apache.org/jira/browse/DISPATCH-1977) - [http2] adaptor must not call proton functions after pn_raw_connection_close
 - [DISPATCH-1986](https://issues.apache.org/jira/browse/DISPATCH-1986) - [http1] system_tests_http1_adaptor failure due to Address already in use issue
 - [DISPATCH-1995](https://issues.apache.org/jira/browse/DISPATCH-1995) - Dispatch docs build fails if -GNinja is used
 - [DISPATCH-2013](https://issues.apache.org/jira/browse/DISPATCH-2013) - Http1AdaptorManagementTest fails with AssertionError: 0 != 1 : HTTP connection not deleted
 - [DISPATCH-2037](https://issues.apache.org/jira/browse/DISPATCH-2037) - [http2] Thread race accessing qdr_http2_connection_t pings in system_tests_http2
 - [DISPATCH-2041](https://issues.apache.org/jira/browse/DISPATCH-2041) - TSan data race reported from qd_connection_free in system_tests_edge_router
 - [DISPATCH-2055](https://issues.apache.org/jira/browse/DISPATCH-2055) - AddressSanitizer: heap-use-after-free in write_log during system_tests_qdmanage
 - [DISPATCH-2097](https://issues.apache.org/jira/browse/DISPATCH-2097) - [console] GUI displays many connections to pseudo-host egress-dispatch
 - [DISPATCH-2100](https://issues.apache.org/jira/browse/DISPATCH-2100) - TCP adaptor half-closed fix does not have a self test
 - [DISPATCH-2105](https://issues.apache.org/jira/browse/DISPATCH-2105) - [s390s] Compilation failure on Ubuntu Xenial: argument 1 range [18446744071562067968, 18446744073709551615] exceeds maximum object size 9223372036854775807 [-Werror=alloc-size-larger-than=]
 - [DISPATCH-2106](https://issues.apache.org/jira/browse/DISPATCH-2106) - [HTTP2] coverity errors
 - [DISPATCH-2107](https://issues.apache.org/jira/browse/DISPATCH-2107) - [libwebsockets] coverity error
 - [DISPATCH-2110](https://issues.apache.org/jira/browse/DISPATCH-2110) - Qdstat number display formatting problems - need full audit
 - [DISPATCH-2115](https://issues.apache.org/jira/browse/DISPATCH-2115) - Leak of qdr_link_route_t in system_tests_edge_router
 - [DISPATCH-2136](https://issues.apache.org/jira/browse/DISPATCH-2136) - race accessing the aborted message flag
 - [DISPATCH-2154](https://issues.apache.org/jira/browse/DISPATCH-2154) - Message abort flag should never be set false
 - [DISPATCH-2158](https://issues.apache.org/jira/browse/DISPATCH-2158) -  AddressSanitizer: use-after-poison in qdr_core_delete_link_route during system_tests_edge_router
 - [DISPATCH-2161](https://issues.apache.org/jira/browse/DISPATCH-2161) - HTTP/1.x server connection hangs if client disconnects during response message
 - [DISPATCH-2162](https://issues.apache.org/jira/browse/DISPATCH-2162) - HTTP/1.x throughput is abysmal.
 - [DISPATCH-2163](https://issues.apache.org/jira/browse/DISPATCH-2163) - Generated file build/src/config.h does not have include guards
 - [DISPATCH-2166](https://issues.apache.org/jira/browse/DISPATCH-2166) - Race accessing several message content flags and values
 - [DISPATCH-2167](https://issues.apache.org/jira/browse/DISPATCH-2167) - HTTP/1.x server connection hangs if client request is aborted
 - [DISPATCH-2177](https://issues.apache.org/jira/browse/DISPATCH-2177) - [http1] system_tests_http1 failing on test_04_client_request_close
 - [DISPATCH-2184](https://issues.apache.org/jira/browse/DISPATCH-2184) - message receiver is not restarted by qd_message_Q2_holdoff_disable
 - [DISPATCH-2185](https://issues.apache.org/jira/browse/DISPATCH-2185) - HTTP/1.x crash on message content sys_mutex_lock fail
 - [DISPATCH-2186](https://issues.apache.org/jira/browse/DISPATCH-2186) - Pytest runner reports test collection warnings which proved to be misleading to the unwarry
 - [DISPATCH-2189](https://issues.apache.org/jira/browse/DISPATCH-2189) - HTTP/1.x hangs if client sends "Expect: 100-continue" header
 - [DISPATCH-2191](https://issues.apache.org/jira/browse/DISPATCH-2191) - Count only body buffers when considering q2. Do not count header buffers 
 - [DISPATCH-2192](https://issues.apache.org/jira/browse/DISPATCH-2192) - Streaming link leak during TCP + iperf3 testing
 - [DISPATCH-2204](https://issues.apache.org/jira/browse/DISPATCH-2204) - RuntimeError: dictionary changed size during iteration
 - [DISPATCH-2207](https://issues.apache.org/jira/browse/DISPATCH-2207) - Leak of qd_connector_t (coverity)
 - [DISPATCH-2209](https://issues.apache.org/jira/browse/DISPATCH-2209) - HTTP/1.x - fix meta-headers types and values for consistency with HTTP/2

## Tasks

 - [DISPATCH-2120](https://issues.apache.org/jira/browse/DISPATCH-2120) - Create GitHub Actions jobs used for gating incoming pull requests
 - [DISPATCH-2146](https://issues.apache.org/jira/browse/DISPATCH-2146) - TSAN suppression file update