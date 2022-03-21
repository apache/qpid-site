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

# Qpid Proton 0.37.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2308](https://issues.apache.org/jira/browse/PROTON-2308) - [cpp] Add support for setting Dynamic Node Properties
 - [PROTON-2447](https://issues.apache.org/jira/browse/PROTON-2447) - Add new internal API pn_buffer_free_memory to get direct access to unused memory in buffer
 - [PROTON-2448](https://issues.apache.org/jira/browse/PROTON-2448) - Implement a dumping AMQP values without using pn_data_t
 - [PROTON-2449](https://issues.apache.org/jira/browse/PROTON-2449) - Remove unnecessary scratch string from pn_transport_t
 - [PROTON-2450](https://issues.apache.org/jira/browse/PROTON-2450) - Generate correct relocatable pc files
 - [PROTON-2451](https://issues.apache.org/jira/browse/PROTON-2451) - Reduce (ultimately eliminate) all use of the pn_data_t data structure in AMQP frame processing
 - [PROTON-2453](https://issues.apache.org/jira/browse/PROTON-2453) - [proton-python] Fix socket.socket type annotations inconsistency found by MyPy
 - [PROTON-2479](https://issues.apache.org/jira/browse/PROTON-2479) - Improve proactor read performance by actually resizing input buffer
 - [PROTON-2481](https://issues.apache.org/jira/browse/PROTON-2481) - [cpp] Improve constructor syntax for maps
 - [PROTON-2485](https://issues.apache.org/jira/browse/PROTON-2485) - [C++] More work to use C++11 features now that we can

## Bugs fixed

 - [PROTON-2112](https://issues.apache.org/jira/browse/PROTON-2112) - segfault in epoll proactor shutdown
 - [PROTON-2362](https://issues.apache.org/jira/browse/PROTON-2362) - c-threaderciser timed out on 32-core machine.
 - [PROTON-2396](https://issues.apache.org/jira/browse/PROTON-2396) - [cpp] Seed in uuid.cpp can lead to duplicates
 - [PROTON-2406](https://issues.apache.org/jira/browse/PROTON-2406) - [cpp] Use of reconnect_options::failover_urls triggers -Wdeprecated-declarations in examples/cpp/reconnect_client.cpp
 - [PROTON-2436](https://issues.apache.org/jira/browse/PROTON-2436) - TSAN race in epoll.c post_event with raw connection
 - [PROTON-2441](https://issues.apache.org/jira/browse/PROTON-2441) - [cpp] Crash upon reconnect when user passed empty vector to connection_options::failover_urls
 - [PROTON-2455](https://issues.apache.org/jira/browse/PROTON-2455) - Workaround for bad use of pn_buffer_append in messenger library
 - [PROTON-2456](https://issues.apache.org/jira/browse/PROTON-2456) - Bad example code was introduced in PROTON-2427
 - [PROTON-2457](https://issues.apache.org/jira/browse/PROTON-2457) - Bugs found by os-fuzzer
 - [PROTON-2468](https://issues.apache.org/jira/browse/PROTON-2468) - Fix some undefined behaviour found by ubsan
 - [PROTON-2472](https://issues.apache.org/jira/browse/PROTON-2472) - assert epoll.c:2519: poller_do_epoll: Assertion `!p-&gt;sched_ready_first' failed.
 - [PROTON-2482](https://issues.apache.org/jira/browse/PROTON-2482) - Proactor can seem to read nonsense
 - [PROTON-2483](https://issues.apache.org/jira/browse/PROTON-2483) - TSAN reported potential deadlock in epoll proactor when run via Qpid Dispatch router.
 - [PROTON-2484](https://issues.apache.org/jira/browse/PROTON-2484) - epoll proactor memory use after free
 - [PROTON-2488](https://issues.apache.org/jira/browse/PROTON-2488) - [python] When tracing is active receiving a message with annotations fails
 - [PROTON-2492](https://issues.apache.org/jira/browse/PROTON-2492) - Python module linking on recent macOS fails with clang unable to find -lssl
 - [PROTON-2498](https://issues.apache.org/jira/browse/PROTON-2498) - Ruby binding fails to test with ruby 3.1
 - [PROTON-2503](https://issues.apache.org/jira/browse/PROTON-2503) - [c] Memory leak found by fuzzing
 - [PROTON-2511](https://issues.apache.org/jira/browse/PROTON-2511) - [python] Fatal Python error: deallocating None
 - [PROTON-2514](https://issues.apache.org/jira/browse/PROTON-2514) - Error in decoding disposition frames
 - [PROTON-2517](https://issues.apache.org/jira/browse/PROTON-2517) - The new C codec can misinterpret pn_data_t values resulting in unintended wire data.