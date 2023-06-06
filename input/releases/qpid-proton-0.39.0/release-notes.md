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

# Qpid Proton 0.39.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2657](https://issues.apache.org/jira/browse/PROTON-2657) - [cpp] Accessors for user data on endpoints and deliveries
 - [PROTON-2663](https://issues.apache.org/jira/browse/PROTON-2663) - class ssl_client_options does not have a constructor for a custom client certificate, and default certificate trust database 
 - [PROTON-2665](https://issues.apache.org/jira/browse/PROTON-2665) - [C++] Make the broker example more idiomatic by using C++11 lambdas
 - [PROTON-2666](https://issues.apache.org/jira/browse/PROTON-2666) - [C++] Allow more python examples to run using the C++ broker example
 - [PROTON-2668](https://issues.apache.org/jira/browse/PROTON-2668) - Change versions of Python used/supported
 - [PROTON-2669](https://issues.apache.org/jira/browse/PROTON-2669) - Change version of cmake supported to 3.16 and up
 - [PROTON-2674](https://issues.apache.org/jira/browse/PROTON-2674) - Remove some deprecated python bindings
 - [PROTON-2675](https://issues.apache.org/jira/browse/PROTON-2675) - Remove unnecessary string conversions
 - [PROTON-2678](https://issues.apache.org/jira/browse/PROTON-2678) - Use Python Limited API and create universal wheel when building Qpid Proton Python client
 - [PROTON-2706](https://issues.apache.org/jira/browse/PROTON-2706) - [Python] Allow setting the container id for containers/connections
 - [PROTON-2708](https://issues.apache.org/jira/browse/PROTON-2708) - New proactor APIs to query event batch for subject
 - [PROTON-2709](https://issues.apache.org/jira/browse/PROTON-2709) - Settle delivered messages in the C sender example

## Bugs fixed

 - [PROTON-2401](https://issues.apache.org/jira/browse/PROTON-2401) - on_link_closed is not called when remote detaches link and locally link is also closed.
 - [PROTON-2643](https://issues.apache.org/jira/browse/PROTON-2643) - SSL connection hanging
 - [PROTON-2653](https://issues.apache.org/jira/browse/PROTON-2653) - [cpp] Can't see tracing documentation on public website.
 - [PROTON-2658](https://issues.apache.org/jira/browse/PROTON-2658) - Proton TLS library - buffer leak on cleanup
 - [PROTON-2664](https://issues.apache.org/jira/browse/PROTON-2664) - Frame dumps get truncated by attempting to output 0 length AMQP strings
 - [PROTON-2667](https://issues.apache.org/jira/browse/PROTON-2667) - Various CI python test failures
 - [PROTON-2673](https://issues.apache.org/jira/browse/PROTON-2673) - Proactor hangs if pn_raw_connection_wake() is called with outstanding connection attempt
 - [PROTON-2676](https://issues.apache.org/jira/browse/PROTON-2676) - Make python server examples use ANONYMOUS-RELAY correctly
 - [PROTON-2677](https://issues.apache.org/jira/browse/PROTON-2677) - cpp-example-container test failure
 - [PROTON-2679](https://issues.apache.org/jira/browse/PROTON-2679) - Parallel build of python bindings occasionally fails
 - [PROTON-2684](https://issues.apache.org/jira/browse/PROTON-2684) - CFFI related TypeError:  '%x format: an integer is required, not _cffi_backend._CDataBase'
 - [PROTON-2690](https://issues.apache.org/jira/browse/PROTON-2690) - [Python] The desired and offered capabilities field in open performative should be symbol array or symbol
 - [PROTON-2691](https://issues.apache.org/jira/browse/PROTON-2691) - Clang compilation error: a function declaration without a prototype is deprecated in all versions of C [-Werror,-Wstrict-prototypes]
 - [PROTON-2695](https://issues.apache.org/jira/browse/PROTON-2695) - Epoll proactor raw connections hang on incomplete batches
 - [PROTON-2699](https://issues.apache.org/jira/browse/PROTON-2699) - Turn off proactor fdlimit test by default
 - [PROTON-2701](https://issues.apache.org/jira/browse/PROTON-2701) - [Python] Make python build respect BUILD_TESTING
 - [PROTON-2704](https://issues.apache.org/jira/browse/PROTON-2704) - [Python] The examples test hangs
 - [PROTON-2712](https://issues.apache.org/jira/browse/PROTON-2712) - [Python] Inconsistencies in binding type mappings
 - [PROTON-2715](https://issues.apache.org/jira/browse/PROTON-2715) - Compilation failure on Fedora 38 with clang, cpp/examples/flow_control.cpp:65:18: error: variable 'i' set but not used [-Werror,-Wunused-but-set-variable]
 - [PROTON-2716](https://issues.apache.org/jira/browse/PROTON-2716) - Warnings from opentelemetry-cpp propagate up and stop a -Werror build on Fedora 38 using vcpkg to get opentelemetry-cpp[jaeger]
 - [PROTON-2736](https://issues.apache.org/jira/browse/PROTON-2736) - TLS OpenSSL library: hang with large application data frames