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

# Qpid Proton 0.6 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-273](https://issues.apache.org/jira/browse/PROTON-273) - Fix disabled ruby test "can have nil content"
 - [PROTON-287](https://issues.apache.org/jira/browse/PROTON-287) - Fix Qpid Proton-C build with MinGW on Fedora
 - [PROTON-290](https://issues.apache.org/jira/browse/PROTON-290) - Allow querying of unsent messages by tracker
 - [PROTON-343](https://issues.apache.org/jira/browse/PROTON-343) - Add a pluggable Proton logging layer
 - [PROTON-382](https://issues.apache.org/jira/browse/PROTON-382) - Perl Message class should expose a Properties attribute
 - [PROTON-383](https://issues.apache.org/jira/browse/PROTON-383) - Perl Message class should expose an Annotations property.
 - [PROTON-384](https://issues.apache.org/jira/browse/PROTON-384) - Perl Message class should expose an Instructions property.
 - [PROTON-385](https://issues.apache.org/jira/browse/PROTON-385) - Perl Message class should expose an Body property.
 - [PROTON-386](https://issues.apache.org/jira/browse/PROTON-386) - Provide Perl client and server examples
 - [PROTON-414](https://issues.apache.org/jira/browse/PROTON-414) - Perl Messenger does not return a tracker on put
 - [PROTON-415](https://issues.apache.org/jira/browse/PROTON-415) - Perl Messenger does not return a tracker on get
 - [PROTON-426](https://issues.apache.org/jira/browse/PROTON-426) - [Messenger] messenger has no ability to dynamically create queues/topics on qpidd
 - [PROTON-439](https://issues.apache.org/jira/browse/PROTON-439) - Support for dynamic reply-to address in Messenger
 - [PROTON-443](https://issues.apache.org/jira/browse/PROTON-443) - update hawt-dispatch dependency version
 - [PROTON-444](https://issues.apache.org/jira/browse/PROTON-444) - Java Messenger needs internal store.
 - [PROTON-450](https://issues.apache.org/jira/browse/PROTON-450) - Rspec tests should NOT use the default port for listening
 - [PROTON-457](https://issues.apache.org/jira/browse/PROTON-457) - Expose the Messenger interrupt method in Perl
 - [PROTON-458](https://issues.apache.org/jira/browse/PROTON-458) - Perl should die on negative return values
 - [PROTON-459](https://issues.apache.org/jira/browse/PROTON-459) - Perl binding omits pn_messenger_route interface
 - [PROTON-460](https://issues.apache.org/jira/browse/PROTON-460) - Perl interface omits pn_messenger_rewrite()
 - [PROTON-463](https://issues.apache.org/jira/browse/PROTON-463) - Perl should provide incoming and outgoing trackers
 - [PROTON-464](https://issues.apache.org/jira/browse/PROTON-464) - Interpolate CMAKE_INSTALL_PREFIX into Ruby install directory.
 - [PROTON-472](https://issues.apache.org/jira/browse/PROTON-472) - Expose the Messenger route and pattern function in the Perl bindings
 - [PROTON-476](https://issues.apache.org/jira/browse/PROTON-476) - Support a user-context for SASL and SSL objects.
 - [PROTON-479](https://issues.apache.org/jira/browse/PROTON-479) - Expose Settled status in Ruby bindings.
 - [PROTON-480](https://issues.apache.org/jira/browse/PROTON-480) - Expose Settled status in Perl bindings.

## Bugs fixed

 - [PROTON-200](https://issues.apache.org/jira/browse/PROTON-200) - Credit distribution by messenger is not balanced across all links
 - [PROTON-278](https://issues.apache.org/jira/browse/PROTON-278) - Messenger - allow the application to control the use of the message reply-to field.
 - [PROTON-302](https://issues.apache.org/jira/browse/PROTON-302) - Messenger does not verify the hostname in the peer's SSL certificate.
 - [PROTON-323](https://issues.apache.org/jira/browse/PROTON-323) - Regression: Messenger sends "null" in disposition state after accept
 - [PROTON-401](https://issues.apache.org/jira/browse/PROTON-401) - Ordering issue prevents credit drain from working properly
 - [PROTON-412](https://issues.apache.org/jira/browse/PROTON-412) - pkg-config has wrong configuration
 - [PROTON-413](https://issues.apache.org/jira/browse/PROTON-413) - [proton-c] Cmake install does not produce package files that work on windows
 - [PROTON-417](https://issues.apache.org/jira/browse/PROTON-417) - Remove/optionalize bouncycastle dependency
 - [PROTON-418](https://issues.apache.org/jira/browse/PROTON-418) - data error interface should match other error APIs (probably should review all error accessors)
 - [PROTON-424](https://issues.apache.org/jira/browse/PROTON-424) - Memory Leak in Proton Messenger Send / Recv
 - [PROTON-425](https://issues.apache.org/jira/browse/PROTON-425) - [Messenger] messenger can only browse qpidd's queues
 - [PROTON-427](https://issues.apache.org/jira/browse/PROTON-427) - settle does not match accept/reject for ruby
 - [PROTON-428](https://issues.apache.org/jira/browse/PROTON-428) - proton-hawtdispatch drops data when more than 512 bytes are read from the socket
 - [PROTON-430](https://issues.apache.org/jira/browse/PROTON-430) - cmake install package files created at wrong time and place
 - [PROTON-431](https://issues.apache.org/jira/browse/PROTON-431) - Ruby integration test have incorrect failure messages
 - [PROTON-432](https://issues.apache.org/jira/browse/PROTON-432) - seg fault when handling error
 - [PROTON-433](https://issues.apache.org/jira/browse/PROTON-433) - seg fault when handling error
 - [PROTON-434](https://issues.apache.org/jira/browse/PROTON-434) - seg fault when handling error
 - [PROTON-435](https://issues.apache.org/jira/browse/PROTON-435) - seg fault when handling error
 - [PROTON-440](https://issues.apache.org/jira/browse/PROTON-440) - MessengerImpl tests fail on OSX
 - [PROTON-445](https://issues.apache.org/jira/browse/PROTON-445) - Binding installation ignores prefix
 - [PROTON-446](https://issues.apache.org/jira/browse/PROTON-446) - [SSL] when certificate validation fails, the connection is not cleanly closed.
 - [PROTON-449](https://issues.apache.org/jira/browse/PROTON-449) - Unit tests fail if proton is built without OpenSSL.
 - [PROTON-453](https://issues.apache.org/jira/browse/PROTON-453) - OpenSSL libraries are not Valgrind clean
 - [PROTON-454](https://issues.apache.org/jira/browse/PROTON-454) - ruby binding omits pn_messenger_route interface
 - [PROTON-455](https://issues.apache.org/jira/browse/PROTON-455) - Ruby interface omits pn_messenger_rewrite()
 - [PROTON-456](https://issues.apache.org/jira/browse/PROTON-456) - Ruby binding does not implement password attr
 - [PROTON-462](https://issues.apache.org/jira/browse/PROTON-462) - Documentation: Add doxygen overview file for Proton C API
 - [PROTON-466](https://issues.apache.org/jira/browse/PROTON-466) - Driver - Optimization causes hangs in cleanly closed connections
 - [PROTON-473](https://issues.apache.org/jira/browse/PROTON-473) - Windows driver.c matching fixes
 - [PROTON-474](https://issues.apache.org/jira/browse/PROTON-474) - Incorrect mapping of TTL to JMSExpiration in JMS InboundTransformer
 - [PROTON-475](https://issues.apache.org/jira/browse/PROTON-475) - [python] Proton wrapper API's use of time values is inconsistent
 - [PROTON-477](https://issues.apache.org/jira/browse/PROTON-477) - [python] Proton wrapper API does not enforce SASL or SSL singleton pattern
 - [PROTON-481](https://issues.apache.org/jira/browse/PROTON-481) - [python] link name is not available
 - [PROTON-482](https://issues.apache.org/jira/browse/PROTON-482) - Ruby bindings install to vendorarchdir rather than vendorlibdir

## Tasks

<div class="none">None</div>
