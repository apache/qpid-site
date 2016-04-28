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

# Qpid Proton 0.9 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-471](https://issues.apache.org/jira/browse/PROTON-471) - Expose the Messenger work method in Perl bindings
 - [PROTON-697](https://issues.apache.org/jira/browse/PROTON-697) - SChannel SSL/TLS support for Proton-c on Windows
 - [PROTON-747](https://issues.apache.org/jira/browse/PROTON-747) - Use around wrapper on Messenger methods to raise errors
 - [PROTON-750](https://issues.apache.org/jira/browse/PROTON-750) - Have distinct API to indicate SSL layer is not really implemented
 - [PROTON-753](https://issues.apache.org/jira/browse/PROTON-753) - [proton-j] provide constants for descriptors required to configure source delivery outcomes
 - [PROTON-769](https://issues.apache.org/jira/browse/PROTON-769) - Simplify the trace flag logic by only keeping a single copy
 - [PROTON-770](https://issues.apache.org/jira/browse/PROTON-770) - Refactor Proton C to eliminate the pn_dispatcher_t class
 - [PROTON-805](https://issues.apache.org/jira/browse/PROTON-805) - Add dispatch request-response extension to utils.py
 - [PROTON-812](https://issues.apache.org/jira/browse/PROTON-812) - LinkException needs an attribute that indicates the reason for the exception.
 - [PROTON-816](https://issues.apache.org/jira/browse/PROTON-816) - Add access to dynamic-node-properties in termini
 - [PROTON-819](https://issues.apache.org/jira/browse/PROTON-819) - BlockingLink.__init__() raise LinkDetached instead of LinkException

## Bugs fixed

 - [PROTON-154](https://issues.apache.org/jira/browse/PROTON-154) - proton-j: link attach, detach, attach sequence on single session does not result in a new link for the 2nd attach
 - [PROTON-548](https://issues.apache.org/jira/browse/PROTON-548) - Proton-C driver and URL Parsers don't support AF_INET6 (IPv6)
 - [PROTON-563](https://issues.apache.org/jira/browse/PROTON-563) - Generated Proton.sln doesn't compile
 - [PROTON-578](https://issues.apache.org/jira/browse/PROTON-578) - proton-c: windows/io.c prints "Unknown error" for all winsock errors
 - [PROTON-667](https://issues.apache.org/jira/browse/PROTON-667) - add support for transactional state and enable outgoing transfer frames to specify a txn-id
 - [PROTON-723](https://issues.apache.org/jira/browse/PROTON-723) - Proton-c does not support attaching to the transaction coordinator
 - [PROTON-730](https://issues.apache.org/jira/browse/PROTON-730) - Can't read transactional state set on incoming transfer
 - [PROTON-736](https://issues.apache.org/jira/browse/PROTON-736) - ruby: unable to send binary data?
 - [PROTON-737](https://issues.apache.org/jira/browse/PROTON-737) - [PATCH] ruby: StateError not included in exceptions
 - [PROTON-739](https://issues.apache.org/jira/browse/PROTON-739) - [PATCH] ruby: update messenger#subscribe to accept TTL
 - [PROTON-742](https://issues.apache.org/jira/browse/PROTON-742) - Proton Windows SChannel buffer copy error
 - [PROTON-743](https://issues.apache.org/jira/browse/PROTON-743) - [PATCH] ruby: user doesn't have access to clear messenger error object
 - [PROTON-745](https://issues.apache.org/jira/browse/PROTON-745) - DataImpl cant roundtrip a Symbol array it decoded.
 - [PROTON-746](https://issues.apache.org/jira/browse/PROTON-746) - Qpid::Proton::Messenger fails to encode a Ruby Symbol type.
 - [PROTON-751](https://issues.apache.org/jira/browse/PROTON-751) - [PATCH] proton-c: pn_connect failures aren't exposed via messenger-&gt;error
 - [PROTON-752](https://issues.apache.org/jira/browse/PROTON-752) - Ruby: Cproton calls don't unlock the GIL for blocking / long-running operations
 - [PROTON-757](https://issues.apache.org/jira/browse/PROTON-757) - [PATCH] proton-c: transport errors are output to stderr in 0.8 onwards
 - [PROTON-762](https://issues.apache.org/jira/browse/PROTON-762) - Javascript tests run when emscripten is not installed (and fail)
 - [PROTON-765](https://issues.apache.org/jira/browse/PROTON-765) - 64-bit values are not being properly marshalled in Ruby on 32-bit systems
 - [PROTON-771](https://issues.apache.org/jira/browse/PROTON-771) - AMQP and SASL performatives are not validated against correct frame type
 - [PROTON-775](https://issues.apache.org/jira/browse/PROTON-775) - ruby: message annotations send from a ruby client are invalid
 - [PROTON-779](https://issues.apache.org/jira/browse/PROTON-779) - Building Proton documentation fails due to missing proton.py file
 - [PROTON-784](https://issues.apache.org/jira/browse/PROTON-784) - Settled Deliveries keep piling up, and do not seem to get freed from heap
 - [PROTON-792](https://issues.apache.org/jira/browse/PROTON-792) - [contrib/proton-jms] remove stale support of byte destination type annotation from message transformers
 - [PROTON-794](https://issues.apache.org/jira/browse/PROTON-794) - [Windows] Visual Studio 2008 compile error
 - [PROTON-798](https://issues.apache.org/jira/browse/PROTON-798) - Hang in Windows SSL negotiation
 - [PROTON-800](https://issues.apache.org/jira/browse/PROTON-800) - [Windows C] Reactor test times out
 - [PROTON-804](https://issues.apache.org/jira/browse/PROTON-804) - the transport doesn't always shutdown its output properly
 - [PROTON-807](https://issues.apache.org/jira/browse/PROTON-807) - Proton does not decode AMQP small long encoding correctly and does not use it.
 - [PROTON-809](https://issues.apache.org/jira/browse/PROTON-809) - Changes to build on AIX with IBM XL C
 - [PROTON-811](https://issues.apache.org/jira/browse/PROTON-811) - [PATCH] proton-j: no way to implement idle timeout of a connection
 - [PROTON-814](https://issues.apache.org/jira/browse/PROTON-814) - proton-c: pn_selector_select caches its return code from a previous error
 - [PROTON-815](https://issues.apache.org/jira/browse/PROTON-815) - LinkException on BlockingConnection.create_receiver() leaves things in bad state.
 - [PROTON-817](https://issues.apache.org/jira/browse/PROTON-817) - BlockingConnection doesn't pass options down in create_sender or create_receiver
 - [PROTON-820](https://issues.apache.org/jira/browse/PROTON-820) - Windows build error for perlPERL_wrap.c
 - [PROTON-822](https://issues.apache.org/jira/browse/PROTON-822) - Valgrind errors and problems with dispatch system tests.
 - [PROTON-823](https://issues.apache.org/jira/browse/PROTON-823) - Proton prints some log/trace information to stdout/stderr.
 - [PROTON-825](https://issues.apache.org/jira/browse/PROTON-825) - BlockingReceiver.receive() uses 100% CPU.
 - [PROTON-828](https://issues.apache.org/jira/browse/PROTON-828) - Python binding does not support MODIFIED delivery state
 - [PROTON-831](https://issues.apache.org/jira/browse/PROTON-831) - proton_tests.utils.SyncRequestResponseTest.test_request_response test fails on RHEL 5
 - [PROTON-832](https://issues.apache.org/jira/browse/PROTON-832) - messenger: next_drain is not reset for "manual" link credit mode in messenger
 - [PROTON-833](https://issues.apache.org/jira/browse/PROTON-833) - transport can emit frames with an invalid channel number after local session close
 - [PROTON-835](https://issues.apache.org/jira/browse/PROTON-835) - strncmp in pn_data_lookup doesn't work in some cases
 - [PROTON-836](https://issues.apache.org/jira/browse/PROTON-836) - Missing import SSLUnavailable in reactor.py
 - [PROTON-839](https://issues.apache.org/jira/browse/PROTON-839) - Proton 0.9 RC 2 blocker - proton_tests.utils.SyncRequestResponseTest.test_request_response ........ fail