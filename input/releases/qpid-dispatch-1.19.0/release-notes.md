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

# Qpid Dispatch 1.19.0 Release Notes

Dispatch is a lightweight AMQP 1.0 message router. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-1403](https://issues.apache.org/jira/browse/DISPATCH-1403) - Consolidate chained qd_buffer_t field handling code
 - [DISPATCH-1487](https://issues.apache.org/jira/browse/DISPATCH-1487) - Improve the parsing of message annotations
 - [DISPATCH-2103](https://issues.apache.org/jira/browse/DISPATCH-2103) - Log the actual HTTP websocket listener port when 0 was specified in config
 - [DISPATCH-2310](https://issues.apache.org/jira/browse/DISPATCH-2310) - Enforce a limit to the length of a router's id
 - [DISPATCH-2317](https://issues.apache.org/jira/browse/DISPATCH-2317) - Router per-message annotations version negotiation

## Bugs fixed

 - [DISPATCH-2036](https://issues.apache.org/jira/browse/DISPATCH-2036) - TCP adaptor deliveries reported as "stuck" by delayed delivery detection
 - [DISPATCH-2085](https://issues.apache.org/jira/browse/DISPATCH-2085) - system_tests_fallback_dest failure - addr_proxy.c:323: on_conn_event: Assertion `addr-&gt;edge_outlink == 0' failed
 - [DISPATCH-2132](https://issues.apache.org/jira/browse/DISPATCH-2132) - core-&gt;uptime_ticks races
 - [DISPATCH-2144](https://issues.apache.org/jira/browse/DISPATCH-2144) - Fatal Python error: _PyMem_DebugMalloc: Python memory allocator called without holding the GIL
 - [DISPATCH-2301](https://issues.apache.org/jira/browse/DISPATCH-2301) - Protocol adaptors do not annotate AMQP messages
 - [DISPATCH-2305](https://issues.apache.org/jira/browse/DISPATCH-2305) - policy code overrides configured connection settings by default
 - [DISPATCH-2308](https://issues.apache.org/jira/browse/DISPATCH-2308) - temporary address generation infinite loop if router id &gt; 200 characters
 - [DISPATCH-2309](https://issues.apache.org/jira/browse/DISPATCH-2309) - Message body validation can succeed without validating the actual message body
 - [DISPATCH-2314](https://issues.apache.org/jira/browse/DISPATCH-2314) - TSAN data race when setting the presettled flag
 - [DISPATCH-2316](https://issues.apache.org/jira/browse/DISPATCH-2316) - Py_True/Py_False is not increfed, causing crash in policy tests with libpythond (debug python library)
 - [DISPATCH-2318](https://issues.apache.org/jira/browse/DISPATCH-2318) - Double free of subscription on shutdown
 - [DISPATCH-2319](https://issues.apache.org/jira/browse/DISPATCH-2319) - system_tests_one_router.test_43_dropped_presettled_receiver_stops fails
 - [DISPATCH-2327](https://issues.apache.org/jira/browse/DISPATCH-2327) - system_tests_multi_tenancy flaky link route test failures
 - [DISPATCH-2333](https://issues.apache.org/jira/browse/DISPATCH-2333) - Fix assert that is always true (detected by Coverity Scan)

## Tasks

 - [DISPATCH-2234](https://issues.apache.org/jira/browse/DISPATCH-2234) - Update JavaScript console packages for the 1.19.0 release
 - [DISPATCH-2312](https://issues.apache.org/jira/browse/DISPATCH-2312) - Remove test system_tests_one_router.py::test_07_unsettled_undeliverable
 - [DISPATCH-2326](https://issues.apache.org/jira/browse/DISPATCH-2326) - Remove HTTP1/HTTP2/TCP Adaptors from the source code. 
 - [DISPATCH-2328](https://issues.apache.org/jira/browse/DISPATCH-2328) - c_unittests failing on RHEL 7