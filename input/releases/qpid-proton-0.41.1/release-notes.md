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

# Qpid Proton 0.41.1 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-1442](https://issues.apache.org/jira/browse/PROTON-1442) - [c++] Support for transactions
 - [PROTON-1646](https://issues.apache.org/jira/browse/PROTON-1646) - Proactor API needs a way to use an existing socket.
 - [PROTON-1779](https://issues.apache.org/jira/browse/PROTON-1779) - Completely omit default HEADER and PROPERTIES sections from message payload
 - [PROTON-2502](https://issues.apache.org/jira/browse/PROTON-2502) - Stop using deprecated (and insecure) SASL mechanisms based on MD5
 - [PROTON-2868](https://issues.apache.org/jira/browse/PROTON-2868) - Improve and simplify the scheme for wrapping C Proton objects in Python
 - [PROTON-2871](https://issues.apache.org/jira/browse/PROTON-2871) - Make the generated AMQP protocol constant names more explicit
 - [PROTON-2873](https://issues.apache.org/jira/browse/PROTON-2873) - Reorganize delivery disposition API and representation
 - [PROTON-2881](https://issues.apache.org/jira/browse/PROTON-2881) - Modernize python code
 - [PROTON-2888](https://issues.apache.org/jira/browse/PROTON-2888) - Add std::hash specializations to allow more proton types as keys in unordered datastructures
 - [PROTON-2889](https://issues.apache.org/jira/browse/PROTON-2889) - Improve C++ example broker
 - [PROTON-2890](https://issues.apache.org/jira/browse/PROTON-2890) - [Python examples] Improve python examples
 - [PROTON-2891](https://issues.apache.org/jira/browse/PROTON-2891) - Improve python type annotations
 - [PROTON-2892](https://issues.apache.org/jira/browse/PROTON-2892) - Model Endpoint state with builtin python IntFlag
 - [PROTON-2893](https://issues.apache.org/jira/browse/PROTON-2893) - Add on_delivery_updated callback to MessagingHandler
 - [PROTON-2898](https://issues.apache.org/jira/browse/PROTON-2898) - Introduce API to proton proactor that allows importing an already connected socket
 - [PROTON-2909](https://issues.apache.org/jira/browse/PROTON-2909) - [Test] SSL certificates used for testing are duplicated and scattered
 - [PROTON-2910](https://issues.apache.org/jira/browse/PROTON-2910) - Use better names for generated frame codec functions
 - [PROTON-2911](https://issues.apache.org/jira/browse/PROTON-2911) - [C++] Terminus capabilities which are single symbols incorrectly handled
 - [PROTON-2916](https://issues.apache.org/jira/browse/PROTON-2916) - C++ reconnect test takes a very long time
 - [PROTON-2921](https://issues.apache.org/jira/browse/PROTON-2921) - [C++ transactions] Better control of message settlement/disposition behaviour
 - [PROTON-2922](https://issues.apache.org/jira/browse/PROTON-2922) - [C++ transactions] Better CI testing of C++ transactions
 - [PROTON-2926](https://issues.apache.org/jira/browse/PROTON-2926) - Improve documentation and some behaviour when message ttl = 0
 - [PROTON-2932](https://issues.apache.org/jira/browse/PROTON-2932) - C++: Add std::hash specialized for transfers so they can be keys for unordered data structures
 - [PROTON-2936](https://issues.apache.org/jira/browse/PROTON-2936) - [C++] There is no way to detect when the proactor is idle
 - [PROTON-2946](https://issues.apache.org/jira/browse/PROTON-2946) - Interop round trip tests should use a semantic comparison
 - [PROTON-2958](https://issues.apache.org/jira/browse/PROTON-2958) - Implement small AMQP encodings for list/maps/arrays in pn_data_t encoder
 - [PROTON-2961](https://issues.apache.org/jira/browse/PROTON-2961) - Make CMake use of libuv align with the libuv conventions
 - [PROTON-2966](https://issues.apache.org/jira/browse/PROTON-2966) - pn_decoder_decode does not report why a decode failed
 - [PROTON-2967](https://issues.apache.org/jira/browse/PROTON-2967) - Decode AMQP values iteratively rather than recursively
 - [PROTON-2969](https://issues.apache.org/jira/browse/PROTON-2969) - Stop pn_value_dump from reading more input when the output is full
 - [PROTON-2979](https://issues.apache.org/jira/browse/PROTON-2979) - Omit optional fields on continuation transfers.
 - [PROTON-2981](https://issues.apache.org/jira/browse/PROTON-2981) - The windows API being used should be explicitly 6.1
 - [PROTON-2985](https://issues.apache.org/jira/browse/PROTON-2985) - Add random perturbation mode to threaderciser

## Bugs fixed

 - [PROTON-2296](https://issues.apache.org/jira/browse/PROTON-2296) - running ctest creates test sasl config artifacts in the source tree
 - [PROTON-2775](https://issues.apache.org/jira/browse/PROTON-2775) - pn_buffer_ensure crash due to overflow
 - [PROTON-2812](https://issues.apache.org/jira/browse/PROTON-2812) - Epoll proactor blocks thread during DNS lookups in getaddrinfo
 - [PROTON-2834](https://issues.apache.org/jira/browse/PROTON-2834) - Container stop delayed by canceled work_queue task.
 - [PROTON-2865](https://issues.apache.org/jira/browse/PROTON-2865) - Python doc build needs to run after executable build for no good reason
 - [PROTON-2872](https://issues.apache.org/jira/browse/PROTON-2872) - Ruby URI parser throws an error with ruby 3.4
 - [PROTON-2875](https://issues.apache.org/jira/browse/PROTON-2875) - Default Proton cpp fails to build with gcc 15
 - [PROTON-2879](https://issues.apache.org/jira/browse/PROTON-2879) - pn_unsettled_head/_next not available in Python bindings
 - [PROTON-2882](https://issues.apache.org/jira/browse/PROTON-2882) - Update the Coverage build to work with the latest tree and tools
 - [PROTON-2883](https://issues.apache.org/jira/browse/PROTON-2883) - Acking.release(delivered=True) should default to failed=True
 - [PROTON-2884](https://issues.apache.org/jira/browse/PROTON-2884) - CLONE - Acking.modified should default to failed=True
 - [PROTON-2895](https://issues.apache.org/jira/browse/PROTON-2895) - [Python] subclassing immutable classes shoudl be done using __new__ not __init__
 - [PROTON-2896](https://issues.apache.org/jira/browse/PROTON-2896) - [C++] When qpid is installed in a non default location libqpid-proton-cpp executables don't find libqpid-proton-core or proactor
 - [PROTON-2907](https://issues.apache.org/jira/browse/PROTON-2907) - Ruby Binding is broken for Ruby &lt; 3.4 and URI gem &gt;= 1
 - [PROTON-2908](https://issues.apache.org/jira/browse/PROTON-2908) - [Test] SSL certificates used for testing expired
 - [PROTON-2913](https://issues.apache.org/jira/browse/PROTON-2913) - pn_message_encode will create an illegal AMQP message if there is no message body
 - [PROTON-2928](https://issues.apache.org/jira/browse/PROTON-2928) - Certain network conditions cause proton container to hang during connect phase
 - [PROTON-2930](https://issues.apache.org/jira/browse/PROTON-2930) - Epoll proactor busy loop on socket error
 - [PROTON-2935](https://issues.apache.org/jira/browse/PROTON-2935) - Setting default logger sink context doesn't work correctly
 - [PROTON-2937](https://issues.apache.org/jira/browse/PROTON-2937) - Proton-c fails to build with OpenSSL 4
 - [PROTON-2938](https://issues.apache.org/jira/browse/PROTON-2938) - WIN: Heap Corruption Exiting Application 
 - [PROTON-2945](https://issues.apache.org/jira/browse/PROTON-2945) - SASL/AMQP performatives can be dispatched whether we are processing the AMQP or SASL sub protocols
 - [PROTON-2950](https://issues.apache.org/jira/browse/PROTON-2950) - pn_buffer can silently fail to allocate memory
 - [PROTON-2952](https://issues.apache.org/jira/browse/PROTON-2952) - Multi transfer message deliveries can consume indefinite memory
 - [PROTON-2954](https://issues.apache.org/jira/browse/PROTON-2954) - Decoding AMQP value into pn_data_t instances can use a lot of memory
 - [PROTON-2960](https://issues.apache.org/jira/browse/PROTON-2960) - pn_data_fill test passes uncast 0 into varargs for null pointer
 - [PROTON-2968](https://issues.apache.org/jira/browse/PROTON-2968) - pn_decoder_decode rejects compound counts too large for the node array
 - [PROTON-2970](https://issues.apache.org/jira/browse/PROTON-2970) - SASL frames are handled without checking the state of the protocol exchange
 - [PROTON-2972](https://issues.apache.org/jira/browse/PROTON-2972) - Recent versions of clang++ warn about Catch2 use of __COUNTER__
 - [PROTON-2973](https://issues.apache.org/jira/browse/PROTON-2973) - pn_ssl_domain_set_credentials will crash if either certificate_file or private_key_file are NULL
 - [PROTON-2974](https://issues.apache.org/jira/browse/PROTON-2974) - TLS peer hostname verification should proceed according to RFC9525
 - [PROTON-2976](https://issues.apache.org/jira/browse/PROTON-2976) - pn_ssl_domain_set_trusted_ca_db should override default system trusted ca roots
 - [PROTON-2978](https://issues.apache.org/jira/browse/PROTON-2978) - Improve validation of transfer performatives
 - [PROTON-2980](https://issues.apache.org/jira/browse/PROTON-2980) - Pkgconfig description files are incorrect on debian multiarch installations
 - [PROTON-2984](https://issues.apache.org/jira/browse/PROTON-2984) - Shutdown issues in libuv proactor
 - [PROTON-2986](https://issues.apache.org/jira/browse/PROTON-2986) - Libuv and win_iocp proactors crash if you close an unconnected listener
 - [PROTON-2987](https://issues.apache.org/jira/browse/PROTON-2987) - Fix mismatched mutex lock/unlock in libuv proactor work_start()