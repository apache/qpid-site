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

# Qpid Proton 0.38.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2438](https://issues.apache.org/jira/browse/PROTON-2438) - [cpp] Cancellable tasks
 - [PROTON-2487](https://issues.apache.org/jira/browse/PROTON-2487) - [cpp] Implement distributed tracing
 - [PROTON-2494](https://issues.apache.org/jira/browse/PROTON-2494) - Improve python-qpid-proton wheel build regarding pkgconfig and deps
 - [PROTON-2521](https://issues.apache.org/jira/browse/PROTON-2521) - The new frame codec doesn't omit enough nulls!
 - [PROTON-2527](https://issues.apache.org/jira/browse/PROTON-2527) - Since we produce python packages and ruby gems there is no need to "install" anything if SYSINSTALL_BINDINGS is off
 - [PROTON-2532](https://issues.apache.org/jira/browse/PROTON-2532) - CMake find_package will fail unhelpfully when user asks for component that is not provided
 - [PROTON-2536](https://issues.apache.org/jira/browse/PROTON-2536) - [Python] Modernize package setup
 - [PROTON-2540](https://issues.apache.org/jira/browse/PROTON-2540) - [cpp] Provide a way to query proton::connection for the url it was created with
 - [PROTON-2542](https://issues.apache.org/jira/browse/PROTON-2542) - Simplify and Speed up proton-c object system
 - [PROTON-2555](https://issues.apache.org/jira/browse/PROTON-2555) - Remove internal details from the proton/object.h API header file
 - [PROTON-2562](https://issues.apache.org/jira/browse/PROTON-2562) - Refactor logging so that it doesn't allocate any heap memory
 - [PROTON-2590](https://issues.apache.org/jira/browse/PROTON-2590) - Remove "from __future__ import ..." as they are all the default behaviour for Python 3
 - [PROTON-2633](https://issues.apache.org/jira/browse/PROTON-2633) - Proactor: allow early writes to reduce latency
 - [PROTON-2640](https://issues.apache.org/jira/browse/PROTON-2640) - Set a reasonable default maximum frame size
 - [PROTON-2641](https://issues.apache.org/jira/browse/PROTON-2641) - use consistent socket io cals in epoll proactor

## Bugs fixed

 - [PROTON-2458](https://issues.apache.org/jira/browse/PROTON-2458) - Python Qpid Proton won't compile on Windows with Python 3.10
 - [PROTON-2520](https://issues.apache.org/jira/browse/PROTON-2520) - More error checking for received AMQP frames
 - [PROTON-2525](https://issues.apache.org/jira/browse/PROTON-2525) - Received link handles greater or equal to 2^31 cause proton-c to misbehave
 - [PROTON-2526](https://issues.apache.org/jira/browse/PROTON-2526) - [Python] distutils will soon be removed from Python, we should stop using it
 - [PROTON-2534](https://issues.apache.org/jira/browse/PROTON-2534) - Compilation failure on CentOS 7: error: 'for' loop initial declarations are only allowed in C99 mode
 - [PROTON-2535](https://issues.apache.org/jira/browse/PROTON-2535) - TLS library - false indication of user data in OpenSSL
 - [PROTON-2544](https://issues.apache.org/jira/browse/PROTON-2544) - Build fails on Fedora 36 + Ubuntu 22.04
 - [PROTON-2546](https://issues.apache.org/jira/browse/PROTON-2546) - Leak of raw connection pn_event
 - [PROTON-2567](https://issues.apache.org/jira/browse/PROTON-2567) - Fuzz-proactor-receiver doesn#t work with response file
 - [PROTON-2568](https://issues.apache.org/jira/browse/PROTON-2568) - Leak of addrinfo memory held by raw connection 
 - [PROTON-2578](https://issues.apache.org/jira/browse/PROTON-2578) - Support Python 3.11
 - [PROTON-2583](https://issues.apache.org/jira/browse/PROTON-2583) - [Python/swig] Build warnings from recent versions of CMake
 - [PROTON-2586](https://issues.apache.org/jira/browse/PROTON-2586) - TLS OpenSSL library: incomplete decryption/encryption of staged buffers
 - [PROTON-2612](https://issues.apache.org/jira/browse/PROTON-2612) - TLS OpenSSL library: uninitialized raw buffer size for output buffers
 - [PROTON-2613](https://issues.apache.org/jira/browse/PROTON-2613) - TLS OpenSSL library: write channel not fully configured.
 - [PROTON-2617](https://issues.apache.org/jira/browse/PROTON-2617) - Header file proton/version.h exposes the install prefix
 - [PROTON-2622](https://issues.apache.org/jira/browse/PROTON-2622) - TLS OpenSSL library: ensure capacity values match given capacity
 - [PROTON-2645](https://issues.apache.org/jira/browse/PROTON-2645) - pip install fails on Windows
 - [PROTON-2647](https://issues.apache.org/jira/browse/PROTON-2647) - Fix FLOW event processing in send-abort example.

## Tasks

 - [PROTON-2506](https://issues.apache.org/jira/browse/PROTON-2506) - 0.38.0 release tasks