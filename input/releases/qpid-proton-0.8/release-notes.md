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

# Qpid Proton 0.8 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-287](https://issues.apache.org/jira/browse/PROTON-287) - Fix Qpid Proton-C build with MinGW on Fedora
 - [PROTON-429](https://issues.apache.org/jira/browse/PROTON-429) - pn_bytes(size_t size, char *start) needs a const on the 'start' argument
 - [PROTON-465](https://issues.apache.org/jira/browse/PROTON-465) - FindPerlLibs.cmake module in Proton behaves differently to Qpid's Perl detection
 - [PROTON-476](https://issues.apache.org/jira/browse/PROTON-476) - Support a user-context for SASL and SSL objects.
 - [PROTON-558](https://issues.apache.org/jira/browse/PROTON-558) - Make friendly protocol field logging optional for low-memory devices
 - [PROTON-581](https://issues.apache.org/jira/browse/PROTON-581) - SSL/TLS support for Proton-c on Windows
 - [PROTON-583](https://issues.apache.org/jira/browse/PROTON-583) - Can move a bunch of things from .data to .rodata by adding const
 - [PROTON-585](https://issues.apache.org/jira/browse/PROTON-585) - Can improve memory use by rearranging structs to eliminate padding
 - [PROTON-591](https://issues.apache.org/jira/browse/PROTON-591) - There are two large, mostly empty tables used for dispatching incoming frames
 - [PROTON-597](https://issues.apache.org/jira/browse/PROTON-597) - Improve the memory footprint of TrasportImpl
 - [PROTON-613](https://issues.apache.org/jira/browse/PROTON-613) - update java messenger 'send' example behaviour to be more in line with the other language examples
 - [PROTON-620](https://issues.apache.org/jira/browse/PROTON-620) - Remove unnecessary wrapped types from proton low level bindings
 - [PROTON-628](https://issues.apache.org/jira/browse/PROTON-628) - split out usage of the buffer in MessageImpl#decode() to its own method
 - [PROTON-630](https://issues.apache.org/jira/browse/PROTON-630) - [python] Add a setup.py for installing the python bindings via PyPi
 - [PROTON-640](https://issues.apache.org/jira/browse/PROTON-640) - IO completion port Windows IO for Proton
 - [PROTON-642](https://issues.apache.org/jira/browse/PROTON-642) - SASL Servers need to be able to optionally handle clients that don't use SASL
 - [PROTON-647](https://issues.apache.org/jira/browse/PROTON-647) - Implement an Event.copy or clone method
 - [PROTON-650](https://issues.apache.org/jira/browse/PROTON-650) - proton-dump should include a man page
 - [PROTON-651](https://issues.apache.org/jira/browse/PROTON-651) - Export the proton version numbers via the bindings.
 - [PROTON-653](https://issues.apache.org/jira/browse/PROTON-653) - Expose the version and build details for Proton in the Perl bindings.
 - [PROTON-657](https://issues.apache.org/jira/browse/PROTON-657) - OSX: build proton with homebrew openssl
 - [PROTON-664](https://issues.apache.org/jira/browse/PROTON-664) - add pom profile to allow creating souces jar during non-release builds.
 - [PROTON-668](https://issues.apache.org/jira/browse/PROTON-668) - Document Proton-c IO restrictions for 0.8 release
 - [PROTON-693](https://issues.apache.org/jira/browse/PROTON-693) - Python Url class to wrap C function pni_parse_url
 - [PROTON-705](https://issues.apache.org/jira/browse/PROTON-705) - Windows: Allow C based tests to run directly from ctest/Visual Studio without having to set up environment
 - [PROTON-711](https://issues.apache.org/jira/browse/PROTON-711) - [contrib/proton-jms] add support to message transformers for more efficient destination type annotation value

## Bugs fixed

 - [PROTON-436](https://issues.apache.org/jira/browse/PROTON-436) - pn_data_dump is broken for complex types
 - [PROTON-462](https://issues.apache.org/jira/browse/PROTON-462) - Documentation: Add doxygen overview file for Proton C API
 - [PROTON-474](https://issues.apache.org/jira/browse/PROTON-474) - Incorrect mapping of TTL to JMSExpiration in JMS InboundTransformer
 - [PROTON-509](https://issues.apache.org/jira/browse/PROTON-509) - Proton build fails on OS X 10.9
 - [PROTON-516](https://issues.apache.org/jira/browse/PROTON-516) - [proton-c] Dispatcher frame buffer set to peer's max frame size.
 - [PROTON-543](https://issues.apache.org/jira/browse/PROTON-543) - Frame Parser error if input stream is read before SASL is initialized in the transport
 - [PROTON-548](https://issues.apache.org/jira/browse/PROTON-548) - Proton-C driver and URL Parsers don't support AF_INET6 (IPv6)
 - [PROTON-576](https://issues.apache.org/jira/browse/PROTON-576) - proton-j: codec support for UTF-8 encoding and decoding appears broken?
 - [PROTON-582](https://issues.apache.org/jira/browse/PROTON-582) - Perl language bindings do not properly identify integers from strings when encoding
 - [PROTON-587](https://issues.apache.org/jira/browse/PROTON-587) - Proton 0.7 fails to compile with Visual Studio 2008
 - [PROTON-590](https://issues.apache.org/jira/browse/PROTON-590) - If Proton receives a frame with an unexpected performative number it will SEGV
 - [PROTON-592](https://issues.apache.org/jira/browse/PROTON-592) - Python test function common _ready() fails on windows
 - [PROTON-593](https://issues.apache.org/jira/browse/PROTON-593) - Scripts for running java examples contain old paths
 - [PROTON-595](https://issues.apache.org/jira/browse/PROTON-595) - Python test function MessengerApp.start fails on Windows
 - [PROTON-596](https://issues.apache.org/jira/browse/PROTON-596) - There is no equivalent to 'config.sh' for windows
 - [PROTON-602](https://issues.apache.org/jira/browse/PROTON-602) - Syntax error in perl bindings Data.pm for perl 10.5.1
 - [PROTON-603](https://issues.apache.org/jira/browse/PROTON-603) - Python testReclaimCredit fails on Windows
 - [PROTON-604](https://issues.apache.org/jira/browse/PROTON-604) - Unable to display usage information for perl example send.pl
 - [PROTON-606](https://issues.apache.org/jira/browse/PROTON-606) - Python testReclaimCredit exposes test server messenger hang on windows
 - [PROTON-607](https://issues.apache.org/jira/browse/PROTON-607) - Perl recv.pl shows error if a message has no subject
 - [PROTON-608](https://issues.apache.org/jira/browse/PROTON-608) - seg fault if attach is sent before open and begin
 - [PROTON-610](https://issues.apache.org/jira/browse/PROTON-610) - proton-c: messenger doesn't honour an advertised remote idle timeout
 - [PROTON-611](https://issues.apache.org/jira/browse/PROTON-611) - [proton-c] transport buffer increased to peer's max frame size if initial output_size is not enough
 - [PROTON-615](https://issues.apache.org/jira/browse/PROTON-615) - Cmake binding dependencies wrong (building python binding always; no dependency for include/proton/cproton.i)
 - [PROTON-616](https://issues.apache.org/jira/browse/PROTON-616) - Use Symbol keys in message annotations
 - [PROTON-617](https://issues.apache.org/jira/browse/PROTON-617) - Proton map/hash entries can disappear
 - [PROTON-618](https://issues.apache.org/jira/browse/PROTON-618) - [proton-j] some of the .java source files have crlf line endings, most dont
 - [PROTON-619](https://issues.apache.org/jira/browse/PROTON-619) - The heuristics in config.sh don't work for all build directory locations
 - [PROTON-624](https://issues.apache.org/jira/browse/PROTON-624) - Corrupted payload with redelivered messages when transformer is jms
 - [PROTON-625](https://issues.apache.org/jira/browse/PROTON-625) - prevert looping when map-&gt;load_factor exactly equals load
 - [PROTON-627](https://issues.apache.org/jira/browse/PROTON-627) - Use Symbol keys in delivery annotations
 - [PROTON-631](https://issues.apache.org/jira/browse/PROTON-631) - Potential null pointer exception if 'x-opt-jms-type' annotation is present but has a null value.
 - [PROTON-635](https://issues.apache.org/jira/browse/PROTON-635) - PN_TRANSPORT events not generated in enough places
 - [PROTON-636](https://issues.apache.org/jira/browse/PROTON-636) - setting a 1MB frame size results in an undesirably small session window
 - [PROTON-641](https://issues.apache.org/jira/browse/PROTON-641) - pn_connection_t leaked when links not closed
 - [PROTON-646](https://issues.apache.org/jira/browse/PROTON-646) - Perl message does not have the correct type when the body is a boolean with a FALSE value
 - [PROTON-648](https://issues.apache.org/jira/browse/PROTON-648) - Memory leaks on aborted connections.
 - [PROTON-655](https://issues.apache.org/jira/browse/PROTON-655) - URL parser fails to parse ActiveMQ dynamically generated address
 - [PROTON-656](https://issues.apache.org/jira/browse/PROTON-656) - pn_transport_close_{head, tail} no longer return an error code on framing error.
 - [PROTON-658](https://issues.apache.org/jira/browse/PROTON-658) - driver.c implemented with selectors and selectables
 - [PROTON-660](https://issues.apache.org/jira/browse/PROTON-660) - Fix openssl.c build on windows
 - [PROTON-661](https://issues.apache.org/jira/browse/PROTON-661) - pn_message_save_* do not return correct message size when PN_OVERFLOW
 - [PROTON-666](https://issues.apache.org/jira/browse/PROTON-666) - TransactionalState applied to indicate the txn-id before sending has no effect on the outgoing transfer frames
 - [PROTON-669](https://issues.apache.org/jira/browse/PROTON-669) - proton-c: Messenger abstracts away connections, but it would be useful to fail fast for auth errors etc.
 - [PROTON-670](https://issues.apache.org/jira/browse/PROTON-670) - proton-c: Messenger doesn't provide accessors for the links it is using
 - [PROTON-671](https://issues.apache.org/jira/browse/PROTON-671) - proton-c: Messenger doesn't provide a way to set the link settlement modes it uses 
 - [PROTON-672](https://issues.apache.org/jira/browse/PROTON-672) - proton-c: Messenger doesn't support setting the transport tracer
 - [PROTON-673](https://issues.apache.org/jira/browse/PROTON-673) - proton-c: Messenger doesn't provide a way to obtain the remote idle timeout
 - [PROTON-674](https://issues.apache.org/jira/browse/PROTON-674) - proton-c: Messenger doesn't provide a way of setting the TTL on a subscription
 - [PROTON-675](https://issues.apache.org/jira/browse/PROTON-675) - proton-c: Messenger doesn't provide a way of setting the SSL peer authentication mode
 - [PROTON-676](https://issues.apache.org/jira/browse/PROTON-676) - proton-c: transport layer SSL failures not propagated back to Messenger in pni_connection_readable
 - [PROTON-677](https://issues.apache.org/jira/browse/PROTON-677) - proton-c: transport incorrectly detaches all links with closed=true by default
 - [PROTON-679](https://issues.apache.org/jira/browse/PROTON-679) - proton-c: add a "manual" link credit mode to Messenger
 - [PROTON-680](https://issues.apache.org/jira/browse/PROTON-680) - proton-c: Messenger doesn't provide a way of obtaining link or delivery information
 - [PROTON-684](https://issues.apache.org/jira/browse/PROTON-684) - Restrict IOCP enlistment to pn_selector_t usage scenarios in Windows
 - [PROTON-685](https://issues.apache.org/jira/browse/PROTON-685) - calling free() on session with multiple Sender or Receiver links leads to ConcurrentModificationException
 - [PROTON-686](https://issues.apache.org/jira/browse/PROTON-686) - va_copy is C99 (not C89) and is not supported by the Microsoft Visual Studio C compiler before VS 2013
 - [PROTON-687](https://issues.apache.org/jira/browse/PROTON-687) - Memory corruption in proton-test
 - [PROTON-688](https://issues.apache.org/jira/browse/PROTON-688) - pn_transport_unbind() doesn't reset all relevant trasnport state
 - [PROTON-689](https://issues.apache.org/jira/browse/PROTON-689) - Python binding does not expose transport error details
 - [PROTON-690](https://issues.apache.org/jira/browse/PROTON-690) - Fix Windows components for new Proton object/class refcounting mechanisms
 - [PROTON-694](https://issues.apache.org/jira/browse/PROTON-694) - splitting contrib/JMSMappingOutboundTransformer's encoding and transformation
 - [PROTON-695](https://issues.apache.org/jira/browse/PROTON-695) - New URL code causing invalid reads/writes according to valgrind
 - [PROTON-698](https://issues.apache.org/jira/browse/PROTON-698) - ClassCastException occurs when testing equality of Binary instance against a different type of Object
 - [PROTON-699](https://issues.apache.org/jira/browse/PROTON-699) - Messenger installed examples send,recv do not compile
 - [PROTON-701](https://issues.apache.org/jira/browse/PROTON-701) - Windows ctest fixes for proton-c
 - [PROTON-702](https://issues.apache.org/jira/browse/PROTON-702) - Windows proton-c selector can forget timer events
 - [PROTON-704](https://issues.apache.org/jira/browse/PROTON-704) - delivery-count is set incorrectly during outbound transformation
 - [PROTON-706](https://issues.apache.org/jira/browse/PROTON-706) - CMake fails - get_filename_component unknown component DIRECTORY
 - [PROTON-707](https://issues.apache.org/jira/browse/PROTON-707) - Valgrind 'invalid read' errors in proton_tests.message.LoadSaveTest tests
 - [PROTON-708](https://issues.apache.org/jira/browse/PROTON-708) - C proton driver needs a getter function to access the pn_error so it can be cleared
 - [PROTON-709](https://issues.apache.org/jira/browse/PROTON-709) - [proton-c] Windows 64-bit transport issue
 - [PROTON-712](https://issues.apache.org/jira/browse/PROTON-712) - Seg fault due to missing NULL return value check of getprotobyname
 - [PROTON-714](https://issues.apache.org/jira/browse/PROTON-714) - SSL buffer overflow with large frames
 - [PROTON-715](https://issues.apache.org/jira/browse/PROTON-715) - [contrib/proton-jms] delivery-count is set incorrectly during Native outbound transformation
 - [PROTON-716](https://issues.apache.org/jira/browse/PROTON-716) - Reject SSL clients that attempt to use SSLv3
 - [PROTON-717](https://issues.apache.org/jira/browse/PROTON-717) - Disable SSL compression
 - [PROTON-718](https://issues.apache.org/jira/browse/PROTON-718) - disable SSL v3 for proton-j
 - [PROTON-719](https://issues.apache.org/jira/browse/PROTON-719) - Disable SSL v3 for Windows SChannel
 - [PROTON-720](https://issues.apache.org/jira/browse/PROTON-720) - [Windows IO] Prints warning string as %d
 - [PROTON-724](https://issues.apache.org/jira/browse/PROTON-724) - pn_transport_close_head doesn't generate the expected PN_TRANSPORT_HEAD_CLOSED event
 - [PROTON-725](https://issues.apache.org/jira/browse/PROTON-725) - pni_parse_url does not properly handle Base64 in URL
 - [PROTON-728](https://issues.apache.org/jira/browse/PROTON-728) - transport aborts when delivery ids are out of sequence

## Tasks

 - [PROTON-634](https://issues.apache.org/jira/browse/PROTON-634) - Packages are needed for Ubuntu Precise (12 LTS)
