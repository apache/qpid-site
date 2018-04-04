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

# Qpid Proton 0.22.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-1754](https://issues.apache.org/jira/browse/PROTON-1754) - Ensure that AMQP NULLs are emitted in every place in the protocol that they are permitted
 - [PROTON-1778](https://issues.apache.org/jira/browse/PROTON-1778) - [ruby] support for user threads communicating with proton threads
 - [PROTON-1781](https://issues.apache.org/jira/browse/PROTON-1781) - [c-proactor] fix mis-named netaddr functions 
 - [PROTON-1782](https://issues.apache.org/jira/browse/PROTON-1782) - [ruby] implement idle_timeout and heartbeats
 - [PROTON-1794](https://issues.apache.org/jira/browse/PROTON-1794) - Improve detection strategy for executable python modules
 - [PROTON-1803](https://issues.apache.org/jira/browse/PROTON-1803) - [ruby] Container support for scheduled tasks

## Bugs fixed

 - [PROTON-144](https://issues.apache.org/jira/browse/PROTON-144) - Reduce byte overhead for small payloads
 - [PROTON-1414](https://issues.apache.org/jira/browse/PROTON-1414) - heap-buffer-overflow in pni_decoder_decode_value when invoking pn_message_decode
 - [PROTON-1589](https://issues.apache.org/jira/browse/PROTON-1589) - [cpp] How can I handle invalid SASL PLAIN credentials error when reconnect is on?
 - [PROTON-1640](https://issues.apache.org/jira/browse/PROTON-1640) - ruby-data-spec test fails on Raspbian Stretch
 - [PROTON-1696](https://issues.apache.org/jira/browse/PROTON-1696) - Go test of SASL fails if it can't find saslpasswd2
 - [PROTON-1775](https://issues.apache.org/jira/browse/PROTON-1775) - rubygem doc is not multilib-clean for x86_64 vs i686
 - [PROTON-1784](https://issues.apache.org/jira/browse/PROTON-1784) - [ruby] Connection#each_sender each_receiver should take a block
 - [PROTON-1789](https://issues.apache.org/jira/browse/PROTON-1789) - [ruby] `pre_encode': undefined method `symbol_keys!' for Qpid::Proton::Types:Module (NoMethodError)
 - [PROTON-1790](https://issues.apache.org/jira/browse/PROTON-1790) - [ruby] Link name is not generated in open_sender when using hash as parameter
 - [PROTON-1791](https://issues.apache.org/jira/browse/PROTON-1791) - TCP sockets remain open in CLOSE_WAIT state
 - [PROTON-1804](https://issues.apache.org/jira/browse/PROTON-1804) - Memory leak reusing a pn_transport_t for multiple connections
 - [PROTON-1814](https://issues.apache.org/jira/browse/PROTON-1814) - core/terminus.rb:239:in `block in apply': undefined method[s ...] for #&lt;Qpid::Proton::Terminus: ...&gt; (NoMethodError)
 - [PROTON-1817](https://issues.apache.org/jira/browse/PROTON-1817) - Can't build C++ example broker as C++03 with C++11 built library

## Tasks

 - [PROTON-1799](https://issues.apache.org/jira/browse/PROTON-1799) - Remove deprecated bindings and APIs, obsolete code