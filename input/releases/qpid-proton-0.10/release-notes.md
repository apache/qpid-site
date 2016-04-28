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

# Qpid Proton 0.10 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-490](https://issues.apache.org/jira/browse/PROTON-490) - [proton-c] Python binding fails to link with Python 3 libraries
 - [PROTON-518](https://issues.apache.org/jira/browse/PROTON-518) - Add SASL hostname getter/setter
 - [PROTON-781](https://issues.apache.org/jira/browse/PROTON-781) - Implement the Reactive APIs in Ruby
 - [PROTON-799](https://issues.apache.org/jira/browse/PROTON-799) - Provide the engine APIs in Ruby
 - [PROTON-857](https://issues.apache.org/jira/browse/PROTON-857) - reduce memory usage for the TransportSession link handle tracking
 - [PROTON-873](https://issues.apache.org/jira/browse/PROTON-873) - Convert use of Object.send to Object.__send__ for Ruby bindings
 - [PROTON-880](https://issues.apache.org/jira/browse/PROTON-880) - make Array iterable
 - [PROTON-881](https://issues.apache.org/jira/browse/PROTON-881) - Proton-j reactor implementation
 - [PROTON-882](https://issues.apache.org/jira/browse/PROTON-882) - it should be possible to override logging from python
 - [PROTON-883](https://issues.apache.org/jira/browse/PROTON-883) - Return the raw bytes from a transport buffer in Ruby.
 - [PROTON-885](https://issues.apache.org/jira/browse/PROTON-885) - Allow setup.py to bundle qpid-proton
 - [PROTON-897](https://issues.apache.org/jira/browse/PROTON-897) - Enhance the Ruby examples
 - [PROTON-903](https://issues.apache.org/jira/browse/PROTON-903) - UUID version should be in sixth octet
 - [PROTON-906](https://issues.apache.org/jira/browse/PROTON-906) - Would be nice to make durable subscriptions simpler
 - [PROTON-919](https://issues.apache.org/jira/browse/PROTON-919) - make C impl behave like java wrt channel_max error
 - [PROTON-932](https://issues.apache.org/jira/browse/PROTON-932) - Document platform-specific usage of certificates and trust stores.
 - [PROTON-944](https://issues.apache.org/jira/browse/PROTON-944) - add ability to set a default state for settling received deliveries
 - [PROTON-956](https://issues.apache.org/jira/browse/PROTON-956) - [proton-j] avoid some overhead when sending frames if the trace logging isnt enabled and there is no frame tracer
 - [PROTON-957](https://issues.apache.org/jira/browse/PROTON-957) - [proton-j] make trace logging of transfer frames more useful

## Bugs fixed

 - [PROTON-109](https://issues.apache.org/jira/browse/PROTON-109) - Proton should handle inbound max-frame size violations.
 - [PROTON-707](https://issues.apache.org/jira/browse/PROTON-707) - Valgrind 'invalid read' errors in proton_tests.message.LoadSaveTest tests
 - [PROTON-842](https://issues.apache.org/jira/browse/PROTON-842) - proton-c should honor channel_max
 - [PROTON-843](https://issues.apache.org/jira/browse/PROTON-843) - proton-j: Transport advertises idle timeout as-is whereas proton-c halves it before
 - [PROTON-844](https://issues.apache.org/jira/browse/PROTON-844) - proton-j: ArrayIndexOutOfBounds exception if remote peer sends a handle &gt;1024
 - [PROTON-845](https://issues.apache.org/jira/browse/PROTON-845) - Proton-J: Potential NPE in proton-jms outbound native transformer
 - [PROTON-848](https://issues.apache.org/jira/browse/PROTON-848) - [proton-j] TransportSession state is never discarded
 - [PROTON-849](https://issues.apache.org/jira/browse/PROTON-849) - [proton-j] TransportLink state is never discarded
 - [PROTON-850](https://issues.apache.org/jira/browse/PROTON-850) - inconsistent state when reusing link name
 - [PROTON-853](https://issues.apache.org/jira/browse/PROTON-853) - [proton-j] the transport emitted a new attach frame for a link in the process of being closed
 - [PROTON-854](https://issues.apache.org/jira/browse/PROTON-854) - [proton-j] ConnectionImpl retains all created Sessions until the Connection is freed
 - [PROTON-858](https://issues.apache.org/jira/browse/PROTON-858) - unbalanced maps can get corrupted
 - [PROTON-859](https://issues.apache.org/jira/browse/PROTON-859) - cyrus sasl not compatible with pre 2.1.24 versions
 - [PROTON-861](https://issues.apache.org/jira/browse/PROTON-861) - need to get at aspect of the client certificate when for authenticated clients
 - [PROTON-864](https://issues.apache.org/jira/browse/PROTON-864) - don't crash when channel number goes high
 - [PROTON-868](https://issues.apache.org/jira/browse/PROTON-868) - Make Pipelined ANONYMOUS authentication work with fallback SASL implementation
 - [PROTON-874](https://issues.apache.org/jira/browse/PROTON-874) - PN_VERSION only supports major and minor versions
 - [PROTON-877](https://issues.apache.org/jira/browse/PROTON-877) - proton-c sasl client hangs on server pipeline
 - [PROTON-878](https://issues.apache.org/jira/browse/PROTON-878) - Python wrapper mixes up 'user' and 'password' configuration API
 - [PROTON-879](https://issues.apache.org/jira/browse/PROTON-879) - null initial response makes cyrus challenge when it probably shouldn't
 - [PROTON-887](https://issues.apache.org/jira/browse/PROTON-887) - Windows SSL implementation needs working version of pn_ssl_get_remote_subject()
 - [PROTON-895](https://issues.apache.org/jira/browse/PROTON-895) - Rely on python to build the downloaded tarball
 - [PROTON-898](https://issues.apache.org/jira/browse/PROTON-898) - Ruby Messenger using pn_selectable_fd and not pn_selectable_get_fd
 - [PROTON-899](https://issues.apache.org/jira/browse/PROTON-899) - Unnecessary relative path in include
 - [PROTON-901](https://issues.apache.org/jira/browse/PROTON-901) - No constants defined for Terminus.expiry_policy
 - [PROTON-904](https://issues.apache.org/jira/browse/PROTON-904) - Remove dependency on libuuid
 - [PROTON-907](https://issues.apache.org/jira/browse/PROTON-907) - Qpid Proton Point to Point Hang on CentOS 6 pn_messenger_send
 - [PROTON-908](https://issues.apache.org/jira/browse/PROTON-908) - Use swig as a build dependency when possible
 - [PROTON-913](https://issues.apache.org/jira/browse/PROTON-913) - Calling allow_unsecured_client() on SSLDomain.MODE_CLIENT causes client segfault
 - [PROTON-914](https://issues.apache.org/jira/browse/PROTON-914) - SSL.peer_hostname does not return the proper value.
 - [PROTON-915](https://issues.apache.org/jira/browse/PROTON-915) - Incompatible protocol header handled incorrectly
 - [PROTON-916](https://issues.apache.org/jira/browse/PROTON-916) - [SASL] pn_sasl_config_name - name gets overwritten in python binding
 - [PROTON-917](https://issues.apache.org/jira/browse/PROTON-917) - [SASL] buffer underrun if no mechs specified by peer
 - [PROTON-920](https://issues.apache.org/jira/browse/PROTON-920) - frames on invalid channel crash proton
 - [PROTON-922](https://issues.apache.org/jira/browse/PROTON-922) - [python] setup.py fails to build bindings if qpid-proton-c-devel installed
 - [PROTON-923](https://issues.apache.org/jira/browse/PROTON-923) - [SASL] PN_TRANSPORT_ERROR event not raised
 - [PROTON-925](https://issues.apache.org/jira/browse/PROTON-925) - proton-c seems to treat unspecified channel-max as implying 0
 - [PROTON-929](https://issues.apache.org/jira/browse/PROTON-929) - [SASL] If both client and server specify ANONYMOUS mech connection setup does not complete
 - [PROTON-931](https://issues.apache.org/jira/browse/PROTON-931) - proton-j: unable to determine if LINK_REMOTE_DETACH happened in response to a local detach
 - [PROTON-933](https://issues.apache.org/jira/browse/PROTON-933) - Cyrus SASL GSSAPI plugin can error if sent long buffers.
 - [PROTON-934](https://issues.apache.org/jira/browse/PROTON-934) - Build tests fail if Java is not available
 - [PROTON-935](https://issues.apache.org/jira/browse/PROTON-935) - drop Java 6 support and move to targetting Java 7
 - [PROTON-936](https://issues.apache.org/jira/browse/PROTON-936) - update session outgoing window handling
 - [PROTON-939](https://issues.apache.org/jira/browse/PROTON-939) - [SSL] Regression: binding a transport erases the configured peer name
 - [PROTON-940](https://issues.apache.org/jira/browse/PROTON-940) - provide the session initial incoming window via Begin rather than sending a separate Flow
 - [PROTON-947](https://issues.apache.org/jira/browse/PROTON-947) - deprecate stale methods on the Message
 - [PROTON-950](https://issues.apache.org/jira/browse/PROTON-950) - SASL PLAIN over cleartext should be supported
 - [PROTON-954](https://issues.apache.org/jira/browse/PROTON-954) - miscelaneous cleanup
 - [PROTON-955](https://issues.apache.org/jira/browse/PROTON-955) - [proton-j] only the payload for the current frame, and not the entire remainder for the delivery, should be handed to the trace logging / frame tracer
 - [PROTON-958](https://issues.apache.org/jira/browse/PROTON-958) - [python] pip installed binding fails to find correct libqpid-proton.so
 - [PROTON-959](https://issues.apache.org/jira/browse/PROTON-959) - On error Proton can send an open and a close frame before sending the AMQP header
 - [PROTON-960](https://issues.apache.org/jira/browse/PROTON-960) - On error Proton can send an open and a close frame during the SASL negotiation (before sending the AMQP header)
 - [PROTON-961](https://issues.apache.org/jira/browse/PROTON-961) - messenger doesn't handle received multi-frame transfers
 - [PROTON-962](https://issues.apache.org/jira/browse/PROTON-962) - heartbeat/empty frame trace has spurious newline
 - [PROTON-963](https://issues.apache.org/jira/browse/PROTON-963) - [SASL] Raise PN_TRANSPORT_ERROR events with correct condition for authentication failure
 - [PROTON-965](https://issues.apache.org/jira/browse/PROTON-965) - [proton-j] freed receiver link may cause a removal from the wrong collection in the session
 - [PROTON-966](https://issues.apache.org/jira/browse/PROTON-966) - [proton-j] empty frames are logged/traced when sent but not when received
 - [PROTON-967](https://issues.apache.org/jira/browse/PROTON-967) - [proton-j] make empty frame logging actually mention that it is an empty frame.
 - [PROTON-975](https://issues.apache.org/jira/browse/PROTON-975) - connecting with DIGEST-MD5 fails if buffer containing outcome and first encrypted frame is received
 - [PROTON-976](https://issues.apache.org/jira/browse/PROTON-976) - pn_read_frame does not validate frame offset
 - [PROTON-978](https://issues.apache.org/jira/browse/PROTON-978) - Framing errors after SASL exchange when max-frame-size is configured

## Tasks

 - [PROTON-943](https://issues.apache.org/jira/browse/PROTON-943) - Bump library (.so) major version for proton-c libraries