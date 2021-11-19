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

# Qpid Dispatch 1.18.0 Release Notes

Dispatch is a lightweight AMQP 1.0 message router. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-2223](https://issues.apache.org/jira/browse/DISPATCH-2223) - Incorporate pythoncapi_compat.h to keep up with CPython development
 - [DISPATCH-2225](https://issues.apache.org/jira/browse/DISPATCH-2225) - [http2] Remove the qdr_http2_session_data_t object and move its contents to qdr_http2_connection_t
 - [DISPATCH-2236](https://issues.apache.org/jira/browse/DISPATCH-2236) - Avoid freeing delivery state while holding the delivery lock
 - [DISPATCH-2238](https://issues.apache.org/jira/browse/DISPATCH-2238) - Avoid holding the core action lock when waking the core thread
 - [DISPATCH-2247](https://issues.apache.org/jira/browse/DISPATCH-2247) - "Received MAU from an unknown router" error message must include unknown router id
 - [DISPATCH-2250](https://issues.apache.org/jira/browse/DISPATCH-2250) - Add extra poll of pending output work on I/O thread
 - [DISPATCH-2251](https://issues.apache.org/jira/browse/DISPATCH-2251) - optimize qd_compose_insert_string_iterator
 - [DISPATCH-2273](https://issues.apache.org/jira/browse/DISPATCH-2273) - Remove support for Proton &lt; 0.33 SASL extension API

## Bugs fixed

 - [DISPATCH-413](https://issues.apache.org/jira/browse/DISPATCH-413) - Improve the qdmanage man page
 - [DISPATCH-840](https://issues.apache.org/jira/browse/DISPATCH-840) - "schema.adoc" contains invalid asciidoc
 - [DISPATCH-1958](https://issues.apache.org/jira/browse/DISPATCH-1958) - Qdstat throws exception when router compiled with `DQD_MEMORY_STATS=OFF`
 - [DISPATCH-2109](https://issues.apache.org/jira/browse/DISPATCH-2109) - Shutdown crash: member access within null pointer of type 'struct qdr_node_t'
 - [DISPATCH-2218](https://issues.apache.org/jira/browse/DISPATCH-2218) - [http2] Remove use of variable length arrays in snd_data_callback()
 - [DISPATCH-2219](https://issues.apache.org/jira/browse/DISPATCH-2219) - Routing protocol messages can be starved by high priority user traffic
 - [DISPATCH-2222](https://issues.apache.org/jira/browse/DISPATCH-2222) - Avoid cpu-intensive message string-ify of every received AMQP message
 - [DISPATCH-2230](https://issues.apache.org/jira/browse/DISPATCH-2230) - Review callback action functions and fix all those that don't check the `discard` flag
 - [DISPATCH-2232](https://issues.apache.org/jira/browse/DISPATCH-2232) - [http2] http response is fragmented across many TCP packets thus increasing latency
 - [DISPATCH-2240](https://issues.apache.org/jira/browse/DISPATCH-2240) - Properly set default value for message annotation strip flag
 - [DISPATCH-2248](https://issues.apache.org/jira/browse/DISPATCH-2248) - link_work item leak due to improper delivery reference drop
 - [DISPATCH-2262](https://issues.apache.org/jira/browse/DISPATCH-2262) - Edge/Interior connections can half-fail in real multi-cloud environments
 - [DISPATCH-2268](https://issues.apache.org/jira/browse/DISPATCH-2268) - HTTP/1.x: incorrectly logs connection close as an error
 - [DISPATCH-2269](https://issues.apache.org/jira/browse/DISPATCH-2269) - warning: 'PN_VERSON_MINOR' is not defined, evaluates to 0 [-Wundef]
 - [DISPATCH-2274](https://issues.apache.org/jira/browse/DISPATCH-2274) - system_tests_router_mesh: ERROR: AddressSanitizer: use-after-poison in qd_link_pn container.c:1029
 - [DISPATCH-2283](https://issues.apache.org/jira/browse/DISPATCH-2283) - heap-use-after-free in system_tests_policy_oversize_compound during qdrc_endpoint_delivery_CT
 - [DISPATCH-2286](https://issues.apache.org/jira/browse/DISPATCH-2286) - Segfault while running iperf3 tests due to null raw connection pointer
 - [DISPATCH-2289](https://issues.apache.org/jira/browse/DISPATCH-2289) - use-after-free of streaming data causes crash in tcp adaptor

## Tasks

 - [DISPATCH-1966](https://issues.apache.org/jira/browse/DISPATCH-1966) - Update top level Dockerfile to CentOS 8 / CentOS 8 Stream
 - [DISPATCH-2079](https://issues.apache.org/jira/browse/DISPATCH-2079) - Update PatternFly packages for the 1.17.0 release
 - [DISPATCH-2210](https://issues.apache.org/jira/browse/DISPATCH-2210) - clarify router scale in documentation