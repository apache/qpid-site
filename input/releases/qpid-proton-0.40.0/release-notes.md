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

# Qpid Proton 0.40.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2594](https://issues.apache.org/jira/browse/PROTON-2594) - Use of HSM for crypto opterations with the private key of a TLS certificate
 - [PROTON-2724](https://issues.apache.org/jira/browse/PROTON-2724) - Cannot disable building binaries in c/tools
 - [PROTON-2751](https://issues.apache.org/jira/browse/PROTON-2751) - Reduce use of pn_buffer_t when not needed
 - [PROTON-2752](https://issues.apache.org/jira/browse/PROTON-2752) - Use pn_string_t/pn_bytes_t instead of raw char*
 - [PROTON-2753](https://issues.apache.org/jira/browse/PROTON-2753) - Split util.h to separate the C++ safe parts out of the C99 but not C++ parts
 - [PROTON-2755](https://issues.apache.org/jira/browse/PROTON-2755) - [Python] Make python code and binding work with python 3.12
 - [PROTON-2756](https://issues.apache.org/jira/browse/PROTON-2756) - [Python] There is no way to run python tests except by building a virtual environment
 - [PROTON-2772](https://issues.apache.org/jira/browse/PROTON-2772) - [c] Add parameter safety annotations for printf format strings
 - [PROTON-2773](https://issues.apache.org/jira/browse/PROTON-2773) - [c] Add various compiler diagnostic helper macros
 - [PROTON-2774](https://issues.apache.org/jira/browse/PROTON-2774) - Support composite CMake builds
 - [PROTON-2790](https://issues.apache.org/jira/browse/PROTON-2790) - Improve session flow control
 - [PROTON-2791](https://issues.apache.org/jira/browse/PROTON-2791) - Add MSG_MORE performance boost to raw connections
 - [PROTON-2813](https://issues.apache.org/jira/browse/PROTON-2813) - [Python] Make the python code pep8 clean
 - [PROTON-2824](https://issues.apache.org/jira/browse/PROTON-2824) - C example broker doesn't respond well if the client tries to use transactions
 - [PROTON-2838](https://issues.apache.org/jira/browse/PROTON-2838) - Remove all operations using the pn_data_t structure from the frame decode path
 - [PROTON-2844](https://issues.apache.org/jira/browse/PROTON-2844) - Modernize python code
 - [PROTON-2848](https://issues.apache.org/jira/browse/PROTON-2848) - [python] Add py.typed marker to officially support typing and be compliant with PEP 561
 - [PROTON-2854](https://issues.apache.org/jira/browse/PROTON-2854) - Make it easier to build with AFL fuzzer manually
 - [PROTON-2856](https://issues.apache.org/jira/browse/PROTON-2856) - Provide TLS support for intermediate CA certificates as trust anchors  in OpenSSL
 - [PROTON-2861](https://issues.apache.org/jira/browse/PROTON-2861) - Use C++ raw string now that we can

## Bugs fixed

 - [PROTON-2322](https://issues.apache.org/jira/browse/PROTON-2322) - Fix and remove ignores in flake8 configuration
 - [PROTON-2714](https://issues.apache.org/jira/browse/PROTON-2714) - logger.c:204:41: error: format ‘%x’ expects argument of type ‘unsigned int’, but argument 4 has type ‘size_t’ {aka ‘long unsigned int’} [-Werror=format=]
 - [PROTON-2742](https://issues.apache.org/jira/browse/PROTON-2742) - The python binding installation instructions in python/PACKAGING.txt are wrong
 - [PROTON-2743](https://issues.apache.org/jira/browse/PROTON-2743) - Logging raw frames only log outgoing frames not incoming frames
 - [PROTON-2746](https://issues.apache.org/jira/browse/PROTON-2746) - pn_value_dump can access uninitialised memory
 - [PROTON-2748](https://issues.apache.org/jira/browse/PROTON-2748) - Raw connections do not always complete close operations
 - [PROTON-2754](https://issues.apache.org/jira/browse/PROTON-2754) - Python example broker supports ANONYMOUS-RELAY but doesn't offer the capability
 - [PROTON-2759](https://issues.apache.org/jira/browse/PROTON-2759) - [python docs] auto_accept doc in TransactionalClientHandler is incorrect
 - [PROTON-2760](https://issues.apache.org/jira/browse/PROTON-2760) - Ruby Some unit tests fail as they use MiniTest which is no longer an alias for Minitest
 - [PROTON-2761](https://issues.apache.org/jira/browse/PROTON-2761) - The ruby unittests give deprecation warnings 
 - [PROTON-2762](https://issues.apache.org/jira/browse/PROTON-2762) - [C++, tracing] Binding does not compile with opentracing
 - [PROTON-2763](https://issues.apache.org/jira/browse/PROTON-2763) - Two final disconnect events possible from a raw connection
 - [PROTON-2764](https://issues.apache.org/jira/browse/PROTON-2764) - Zombie raw connections
 - [PROTON-2765](https://issues.apache.org/jira/browse/PROTON-2765) - [go] Go compilation fails with go 1.21
 - [PROTON-2785](https://issues.apache.org/jira/browse/PROTON-2785) - [Go] Message of certain size fail to be marshalled by amqp module
 - [PROTON-2786](https://issues.apache.org/jira/browse/PROTON-2786) - Cannot cross-compile proton-c using the `zig c++` compiler
 - [PROTON-2787](https://issues.apache.org/jira/browse/PROTON-2787) - Compilation failure with `zig cc` (equivalent to clang 16)
 - [PROTON-2788](https://issues.apache.org/jira/browse/PROTON-2788) - Static build of the Proton TLS library fails when openssl is located outside of default system include directories
 - [PROTON-2792](https://issues.apache.org/jira/browse/PROTON-2792) - [cpp] Segmentation fault in container::impl::run_timer_jobs
 - [PROTON-2810](https://issues.apache.org/jira/browse/PROTON-2810) - C++ compile standard needs to be advanced to c++14 or later
 - [PROTON-2814](https://issues.apache.org/jira/browse/PROTON-2814) - [Python] Python tests incompatible with python 3.12
 - [PROTON-2816](https://issues.apache.org/jira/browse/PROTON-2816) - The current python pkg build can only build a package with a bundled proton core
 - [PROTON-2817](https://issues.apache.org/jira/browse/PROTON-2817) - [Python] Allow control of whether python build uses pip inside virtual environments
 - [PROTON-2818](https://issues.apache.org/jira/browse/PROTON-2818) - Move epoll proctor connection logic to a task thread
 - [PROTON-2820](https://issues.apache.org/jira/browse/PROTON-2820) - [Ruby] Test failure when using swig 4.2
 - [PROTON-2822](https://issues.apache.org/jira/browse/PROTON-2822) - Build fails without building the proactor library
 - [PROTON-2825](https://issues.apache.org/jira/browse/PROTON-2825) - C++ binding treats transaction coordinator termini incorrectly
 - [PROTON-2831](https://issues.apache.org/jira/browse/PROTON-2831) - Mistaken use of logical-or operator instead of bitwise-or operator
 - [PROTON-2832](https://issues.apache.org/jira/browse/PROTON-2832) - Use-after free tsan error in epoll.c::post_event
 - [PROTON-2835](https://issues.apache.org/jira/browse/PROTON-2835) - [Win TLS] Incorrect certificate checking - not checking time validity
 - [PROTON-2842](https://issues.apache.org/jira/browse/PROTON-2842) - Frame dump for custom descriptors is incorrect
 - [PROTON-2843](https://issues.apache.org/jira/browse/PROTON-2843) - [Go] Acknowledging a message on a closed receiver results in a segmentation fault
 - [PROTON-2853](https://issues.apache.org/jira/browse/PROTON-2853) - Undefined behaviour found by fuzzing transfer frame

## Tasks

 - [PROTON-2644](https://issues.apache.org/jira/browse/PROTON-2644) - Update various GH actions versions to resolve deprecation warnings
 - [PROTON-2860](https://issues.apache.org/jira/browse/PROTON-2860) - [cpp] Remove the unsettled API marker from the C++ reconnect API