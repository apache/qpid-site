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

# Qpid Proton 0.33.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-1496](https://issues.apache.org/jira/browse/PROTON-1496) - epoll proactor - improved timers implementation with single timerfd kernel resource
 - [PROTON-2171](https://issues.apache.org/jira/browse/PROTON-2171) - Option to skip building examples
 - [PROTON-2257](https://issues.apache.org/jira/browse/PROTON-2257) - Tidy up and finalise the SASL plugin API
 - [PROTON-2277](https://issues.apache.org/jira/browse/PROTON-2277) - [c] Epoll proactor debug assistance
 - [PROTON-2291](https://issues.apache.org/jira/browse/PROTON-2291) - [c] Proactor: psocket has an unnecessary back pointer to the proactor

## Bugs fixed

 - [PROTON-2170](https://issues.apache.org/jira/browse/PROTON-2170) - cmake -DBUILD_TESTING=OFF does not disable building all tests
 - [PROTON-2229](https://issues.apache.org/jira/browse/PROTON-2229) - pn_data_t initialization lead to low performance
 - [PROTON-2233](https://issues.apache.org/jira/browse/PROTON-2233) - Problem building c examples with qpid-proton 0.31.0
 - [PROTON-2234](https://issues.apache.org/jira/browse/PROTON-2234) - [c] Need ability to add an authorization id in the SASL exchange
 - [PROTON-2268](https://issues.apache.org/jira/browse/PROTON-2268) - Threadercizer causes warnings on BSD based platforms
 - [PROTON-2270](https://issues.apache.org/jira/browse/PROTON-2270) - Threaderciser test does not honor ctest '--timeout' switch
 - [PROTON-2272](https://issues.apache.org/jira/browse/PROTON-2272) - [c] Threadercizer build causes warnings and hence build failures on 32 bit builds
 - [PROTON-2278](https://issues.apache.org/jira/browse/PROTON-2278) - [c] Raw connection API trying to give back buffers after emitting the PN_RAW_CONNECTION_DISCONNECTED event
 - [PROTON-2288](https://issues.apache.org/jira/browse/PROTON-2288) - [cpp][tests] cpp_connect_config_test fails on Fedora 32 with 'tls_post_process_client_hello:no shared cipher'
 - [PROTON-2290](https://issues.apache.org/jira/browse/PROTON-2290) - [c] Proactor: pn_raw_connection_close() doesn't drain already written buffers
 - [PROTON-2292](https://issues.apache.org/jira/browse/PROTON-2292) - [c] Proactor: TSAN failure in pni_timer_manager
 - [PROTON-2293](https://issues.apache.org/jira/browse/PROTON-2293) - [c] Proactor: Raw connection wakes can crash the application
 - [PROTON-2295](https://issues.apache.org/jira/browse/PROTON-2295) - [go] Go 1.15.3 failure in macOS CI; panic: can't call pointer on a non-pointer Value

## Tasks

 - [PROTON-2298](https://issues.apache.org/jira/browse/PROTON-2298) - Disable running of c-threaderciser test by default