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

# Qpid Proton 0.7 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-287](https://issues.apache.org/jira/browse/PROTON-287) - Fix Qpid Proton-C build with MinGW on Fedora
 - [PROTON-343](https://issues.apache.org/jira/browse/PROTON-343) - Add a pluggable Proton logging layer
 - [PROTON-439](https://issues.apache.org/jira/browse/PROTON-439) - Support for dynamic reply-to address in Messenger
 - [PROTON-467](https://issues.apache.org/jira/browse/PROTON-467) - Stop initializing encoder and decoder for each message sent/received
 - [PROTON-476](https://issues.apache.org/jira/browse/PROTON-476) - Support a user-context for SASL and SSL objects.
 - [PROTON-496](https://issues.apache.org/jira/browse/PROTON-496) - [Messenger] Messenger fails to send "end" on shutdown.
 - [PROTON-498](https://issues.apache.org/jira/browse/PROTON-498) - Set VALGRIND environment variable to be compatible with the QPID build
 - [PROTON-502](https://issues.apache.org/jira/browse/PROTON-502) - [proton-j] add UnsignedLong.valueOf(BigInteger)
 - [PROTON-507](https://issues.apache.org/jira/browse/PROTON-507) - [proton-c] Idle time out should advertise half the actual timeout period.
 - [PROTON-515](https://issues.apache.org/jira/browse/PROTON-515) - Port to OpenVMS
 - [PROTON-518](https://issues.apache.org/jira/browse/PROTON-518) - Add SASL hostname getter/setter
 - [PROTON-526](https://issues.apache.org/jira/browse/PROTON-526) - C API-doc is not well organized
 - [PROTON-527](https://issues.apache.org/jira/browse/PROTON-527) - events api for proton-j
 - [PROTON-533](https://issues.apache.org/jira/browse/PROTON-533) - Minor cleanup for 0.7 release
 - [PROTON-536](https://issues.apache.org/jira/browse/PROTON-536) - Make exported cmake files more idiomatic
 - [PROTON-557](https://issues.apache.org/jira/browse/PROTON-557) - Include local endpoint state changes in the engine Event API.
 - [PROTON-565](https://issues.apache.org/jira/browse/PROTON-565) - Modify the Messenger to use the Collector API.

## Bugs fixed

 - [PROTON-417](https://issues.apache.org/jira/browse/PROTON-417) - Remove/optionalize bouncycastle dependency
 - [PROTON-445](https://issues.apache.org/jira/browse/PROTON-445) - Binding installation ignores prefix
 - [PROTON-453](https://issues.apache.org/jira/browse/PROTON-453) - OpenSSL libraries are not Valgrind clean
 - [PROTON-462](https://issues.apache.org/jira/browse/PROTON-462) - Documentation: Add doxygen overview file for Proton C API
 - [PROTON-474](https://issues.apache.org/jira/browse/PROTON-474) - Incorrect mapping of TTL to JMSExpiration in JMS InboundTransformer
 - [PROTON-487](https://issues.apache.org/jira/browse/PROTON-487) - [proton-c] Python binding leaks endpoint and delivery objects
 - [PROTON-488](https://issues.apache.org/jira/browse/PROTON-488) - Windows 7 64-bit VS2010 qpid-proton Crash on Startup with Send / Recv Application
 - [PROTON-489](https://issues.apache.org/jira/browse/PROTON-489) - [proton-c] Segfault when freeing endpoints out-of-order.
 - [PROTON-499](https://issues.apache.org/jira/browse/PROTON-499) - maven build is circularly dependent
 - [PROTON-501](https://issues.apache.org/jira/browse/PROTON-501) - [proton-j] UnsignedLong.valueOf(String) can permit values outside the allowed range
 - [PROTON-506](https://issues.apache.org/jira/browse/PROTON-506) - Queue names with '@' symbol cause incorrect hostname lookup
 - [PROTON-508](https://issues.apache.org/jira/browse/PROTON-508) - Use of Sasl auth results in a large performance hit.
 - [PROTON-509](https://issues.apache.org/jira/browse/PROTON-509) - Proton build fails on OS X 10.9
 - [PROTON-513](https://issues.apache.org/jira/browse/PROTON-513) - [proton-j] ulong values over 2^63-1 are encoded incorrectly
 - [PROTON-514](https://issues.apache.org/jira/browse/PROTON-514) - [proton-j] uint values over 2^31-1 are encoded incorrectly
 - [PROTON-516](https://issues.apache.org/jira/browse/PROTON-516) - [proton-c] Dispatcher frame buffer set to peer's max frame size.
 - [PROTON-519](https://issues.apache.org/jira/browse/PROTON-519) - Fix package specifications in qpid_proton.pm and ExceptionHandling.pm
 - [PROTON-520](https://issues.apache.org/jira/browse/PROTON-520) - Unable to send messages to more than 256 queues
 - [PROTON-521](https://issues.apache.org/jira/browse/PROTON-521) - Replace "proton-project" with "proton" in maven related build files
 - [PROTON-524](https://issues.apache.org/jira/browse/PROTON-524) - [proton-c] C++ build fails on Centos6
 - [PROTON-528](https://issues.apache.org/jira/browse/PROTON-528) - Incorrect limit for the channel number.
 - [PROTON-529](https://issues.apache.org/jira/browse/PROTON-529) - Extending PROTON-525 to Windows platforms
 - [PROTON-532](https://issues.apache.org/jira/browse/PROTON-532) - wrong deadline computed in pn_selector_select
 - [PROTON-535](https://issues.apache.org/jira/browse/PROTON-535) - make docs results in several warnings and an error
 - [PROTON-537](https://issues.apache.org/jira/browse/PROTON-537) - [proton-c] Pointer corruption in SSL buffer handling logic.
 - [PROTON-538](https://issues.apache.org/jira/browse/PROTON-538) - fix install and readme
 - [PROTON-539](https://issues.apache.org/jira/browse/PROTON-539) - Incorrect operator on line 283 of proton.php
 - [PROTON-540](https://issues.apache.org/jira/browse/PROTON-540) - [proton-c] Messenger segfault when shutting down
 - [PROTON-545](https://issues.apache.org/jira/browse/PROTON-545) - C++ warning converting size_t to float, possible loss of data
 - [PROTON-552](https://issues.apache.org/jira/browse/PROTON-552) - Examples fail to build on windows
 - [PROTON-553](https://issues.apache.org/jira/browse/PROTON-553) - Proton-C does not URLdecode password before doing SASL-PLAIN
 - [PROTON-554](https://issues.apache.org/jira/browse/PROTON-554) - pn_data_put_long call fails on 64x Linux 2.6.32-5-amd64
 - [PROTON-559](https://issues.apache.org/jira/browse/PROTON-559) - typo prevents compilation of posix/io.c on OSX
 - [PROTON-560](https://issues.apache.org/jira/browse/PROTON-560) - Failing to transfer messages more than 4kB via AMQPS

## Tasks

 - [PROTON-555](https://issues.apache.org/jira/browse/PROTON-555) - QUESTION: how to decode timestamp? pn_data_get_timestamp returnes resource (_p_long_long)
