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

# Qpid Dispatch 0.6.0 Release Notes

Dispatch is a lightweight AMQP message router library. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-10](https://issues.apache.org/jira/browse/DISPATCH-10) - Add link-cost for route computation
 - [DISPATCH-57](https://issues.apache.org/jira/browse/DISPATCH-57) - Balance deliveries adaptively across all competing consumers in the network
 - [DISPATCH-144](https://issues.apache.org/jira/browse/DISPATCH-144) - Configurable heartbeats for listeners and connectors
 - [DISPATCH-148](https://issues.apache.org/jira/browse/DISPATCH-148) - Strip qpid-dispatch-specific message annotations on ingress/egress
 - [DISPATCH-159](https://issues.apache.org/jira/browse/DISPATCH-159) - Enhance the address prefix used for link routing to support different patterns
 - [DISPATCH-163](https://issues.apache.org/jira/browse/DISPATCH-163) - Add username and password for authentication of connectors
 - [DISPATCH-164](https://issues.apache.org/jira/browse/DISPATCH-164) - Remove connector state-machine from the server module
 - [DISPATCH-165](https://issues.apache.org/jira/browse/DISPATCH-165) - Discriminate between sending and receiving links when matching link-route patterns
 - [DISPATCH-166](https://issues.apache.org/jira/browse/DISPATCH-166) - Use test-controlled SASL configuration for system tests
 - [DISPATCH-170](https://issues.apache.org/jira/browse/DISPATCH-170) - qdrouterd should not require a restart after the destination broker restarts
 - [DISPATCH-178](https://issues.apache.org/jira/browse/DISPATCH-178) - Route proton trace messages to the dispatch router log file instead of console
 - [DISPATCH-179](https://issues.apache.org/jira/browse/DISPATCH-179) - Refactor Router Core
 - [DISPATCH-180](https://issues.apache.org/jira/browse/DISPATCH-180) - Add a system test to test the 'linkRoutePattern' attribute of qdrouterd.conf
 - [DISPATCH-188](https://issues.apache.org/jira/browse/DISPATCH-188) - Dispatch needs a policy mechanism to limit user connections and activity
 - [DISPATCH-190](https://issues.apache.org/jira/browse/DISPATCH-190) - Expose the Protocol Family for the configuration of listeners and connectors
 - [DISPATCH-193](https://issues.apache.org/jira/browse/DISPATCH-193) - Updates to the Container API
 - [DISPATCH-194](https://issues.apache.org/jira/browse/DISPATCH-194) - Move libqpid-dispatch.so out of /lib
 - [DISPATCH-197](https://issues.apache.org/jira/browse/DISPATCH-197) - Provide list of current link routing
 - [DISPATCH-199](https://issues.apache.org/jira/browse/DISPATCH-199) - Add Dockerfiles that launches the dispatch router inside a container for RHEL and Debian based systems
 - [DISPATCH-200](https://issues.apache.org/jira/browse/DISPATCH-200) - Flexible mapping from x.509 certificates to an identity
 - [DISPATCH-203](https://issues.apache.org/jira/browse/DISPATCH-203) - Improve loop-prevention to drop messages before they are improperly forwarded
 - [DISPATCH-217](https://issues.apache.org/jira/browse/DISPATCH-217) - Make the UI more consistant with other hawtio plugins 
 - [DISPATCH-228](https://issues.apache.org/jira/browse/DISPATCH-228) - In ctools, add a variant of DEQ_* to allow membership in multiple lists
 - [DISPATCH-230](https://issues.apache.org/jira/browse/DISPATCH-230) - New connection role: route-container
 - [DISPATCH-232](https://issues.apache.org/jira/browse/DISPATCH-232) - Add capability to delete listeners and connectors via the qdmanage DELETE operation
 - [DISPATCH-242](https://issues.apache.org/jira/browse/DISPATCH-242) - Add options to qdstat to display autoLinks and linkRoutes
 - [DISPATCH-253](https://issues.apache.org/jira/browse/DISPATCH-253) - Configurable link-capacity
 - [DISPATCH-256](https://issues.apache.org/jira/browse/DISPATCH-256) - Documentation Updates for 0.6
 - [DISPATCH-265](https://issues.apache.org/jira/browse/DISPATCH-265) - Improvements to Detecting Routers with Duplicate IDs
 - [DISPATCH-277](https://issues.apache.org/jira/browse/DISPATCH-277) - Improve defaults for router configuration
 - [DISPATCH-286](https://issues.apache.org/jira/browse/DISPATCH-286) - Prefix delimiters:  allow slashes as well as periods
 - [DISPATCH-300](https://issues.apache.org/jira/browse/DISPATCH-300) - Deprecate the ContainerEntity and move its attributes to RouterEntity
 - [DISPATCH-303](https://issues.apache.org/jira/browse/DISPATCH-303) - Block all remote access to the "console" entity
 - [DISPATCH-305](https://issues.apache.org/jira/browse/DISPATCH-305) - Don't tie inter-router flow credit to unsettled deliveries
 - [DISPATCH-306](https://issues.apache.org/jira/browse/DISPATCH-306) - Deprecate addr and routerId attributes in qdrouter schema and replace them with host and id respectively
 - [DISPATCH-331](https://issues.apache.org/jira/browse/DISPATCH-331) - Allow for a default policy to apply when open.hostname doesn't match an existing policy

## Bugs fixed

 - [DISPATCH-32](https://issues.apache.org/jira/browse/DISPATCH-32) - Undeliverable messages should get released.
 - [DISPATCH-43](https://issues.apache.org/jira/browse/DISPATCH-43) - Router control messages delayed by inter-router message traffic
 - [DISPATCH-47](https://issues.apache.org/jira/browse/DISPATCH-47) - qdrouterd doesn't know where its libraries are
 - [DISPATCH-53](https://issues.apache.org/jira/browse/DISPATCH-53) - waypoints are not robust if targets not set up in advance.
 - [DISPATCH-58](https://issues.apache.org/jira/browse/DISPATCH-58) - Router/Broker interaction - Unroutable/released messages are continually resent
 - [DISPATCH-111](https://issues.apache.org/jira/browse/DISPATCH-111) - helloworld example hangs when run against a broker via link-routing
 - [DISPATCH-126](https://issues.apache.org/jira/browse/DISPATCH-126) - Link-route behavior doesn't honor the semantics assigned to the address prefix
 - [DISPATCH-127](https://issues.apache.org/jira/browse/DISPATCH-127) - Messages from waypoints to remote routers are not delivered
 - [DISPATCH-155](https://issues.apache.org/jira/browse/DISPATCH-155) - Allow multiple connectors to the same broker
 - [DISPATCH-168](https://issues.apache.org/jira/browse/DISPATCH-168) - A message sent to $management without a reply-to field causes a crash
 - [DISPATCH-171](https://issues.apache.org/jira/browse/DISPATCH-171) - SSL Domain objects are leaked.
 - [DISPATCH-172](https://issues.apache.org/jira/browse/DISPATCH-172) - QDStat system test never tests SASL EXTERNAL
 - [DISPATCH-173](https://issues.apache.org/jira/browse/DISPATCH-173) - Half-closed connections spin on "writable" until they close
 - [DISPATCH-174](https://issues.apache.org/jira/browse/DISPATCH-174) - Improper use of ref-counted object references in container
 - [DISPATCH-175](https://issues.apache.org/jira/browse/DISPATCH-175) - Router continues to forward messages to the broker even when the broker is not available
 - [DISPATCH-176](https://issues.apache.org/jira/browse/DISPATCH-176) - Messages sent got lost when one of the brokers went down 
 - [DISPATCH-183](https://issues.apache.org/jira/browse/DISPATCH-183) - plaintext sasl password being written to the dispatch router log
 - [DISPATCH-191](https://issues.apache.org/jira/browse/DISPATCH-191) - router not replying to detach frame
 - [DISPATCH-196](https://issues.apache.org/jira/browse/DISPATCH-196) - Remove endpoint mode from router documentation
 - [DISPATCH-198](https://issues.apache.org/jira/browse/DISPATCH-198) - Message module doesn't parse AMQP-Value bodies that are strings or symbols
 - [DISPATCH-207](https://issues.apache.org/jira/browse/DISPATCH-207) - When a message body of [ ] is sent from rhea it is rejected as an invalid body 
 - [DISPATCH-208](https://issues.apache.org/jira/browse/DISPATCH-208) - Closest semantics forwards improperly in multi-router network
 - [DISPATCH-215](https://issues.apache.org/jira/browse/DISPATCH-215) - The topology diagram initially draws off the bottom of the visible page.
 - [DISPATCH-218](https://issues.apache.org/jira/browse/DISPATCH-218) - Dispatch system tests run very slowly if connected to a VPN
 - [DISPATCH-219](https://issues.apache.org/jira/browse/DISPATCH-219) - System test security configuration for installed/built tests.
 - [DISPATCH-222](https://issues.apache.org/jira/browse/DISPATCH-222) - For Dispatch 0.6 release move up the minimum required version of qpid proton to 0.12.0
 - [DISPATCH-223](https://issues.apache.org/jira/browse/DISPATCH-223) - Unknown connector name is not properly printed in error messages
 - [DISPATCH-225](https://issues.apache.org/jira/browse/DISPATCH-225) - Sending UPDATE log request with relative path crashes router
 - [DISPATCH-226](https://issues.apache.org/jira/browse/DISPATCH-226) - The default role is not applied when creating a connector
 - [DISPATCH-231](https://issues.apache.org/jira/browse/DISPATCH-231) - Router should not issue credit for unavailable targets
 - [DISPATCH-234](https://issues.apache.org/jira/browse/DISPATCH-234) - undeliverable-here set to true for messages from waypoints if there is no receiver
 - [DISPATCH-237](https://issues.apache.org/jira/browse/DISPATCH-237) - Dispatch Router overwrites delivery tag for link-routed deliveries
 - [DISPATCH-238](https://issues.apache.org/jira/browse/DISPATCH-238) - Need more documentation for qdstat output
 - [DISPATCH-240](https://issues.apache.org/jira/browse/DISPATCH-240) - qdstat : leading "/" character effects a wrong showed address
 - [DISPATCH-241](https://issues.apache.org/jira/browse/DISPATCH-241) - Bias "spread" config with leading "/" on address has a "multicast" behavior
 - [DISPATCH-245](https://issues.apache.org/jira/browse/DISPATCH-245) - Various Bugs found by Coverity
 - [DISPATCH-247](https://issues.apache.org/jira/browse/DISPATCH-247) - Policy gets username from transport
 - [DISPATCH-248](https://issues.apache.org/jira/browse/DISPATCH-248) - Policy self test uses python features not supported by RHEL 6 (python 2.6)
 - [DISPATCH-250](https://issues.apache.org/jira/browse/DISPATCH-250) - Router crash when deleting connector
 - [DISPATCH-254](https://issues.apache.org/jira/browse/DISPATCH-254) - Router crash after several management requests
 - [DISPATCH-259](https://issues.apache.org/jira/browse/DISPATCH-259) - qdstat man-page doc is no good
 - [DISPATCH-261](https://issues.apache.org/jira/browse/DISPATCH-261) - Bind error on one port causes bind error on other ports
 - [DISPATCH-262](https://issues.apache.org/jira/browse/DISPATCH-262) - oslo.messaging RPC fanout crashes qdrouterd
 - [DISPATCH-263](https://issues.apache.org/jira/browse/DISPATCH-263) - Router crash when requesting log
 - [DISPATCH-264](https://issues.apache.org/jira/browse/DISPATCH-264) - printf formats for 64-bit quantities need to be 64/32-bit safe
 - [DISPATCH-267](https://issues.apache.org/jira/browse/DISPATCH-267) - Policy does not increment denial statistics
 - [DISPATCH-268](https://issues.apache.org/jira/browse/DISPATCH-268) - Delivery from waypoint queue can stall when messages are released
 - [DISPATCH-269](https://issues.apache.org/jira/browse/DISPATCH-269) - Policy denial logs at wrong level
 - [DISPATCH-271](https://issues.apache.org/jira/browse/DISPATCH-271) - Handle single router
 - [DISPATCH-272](https://issues.apache.org/jira/browse/DISPATCH-272) - Re-enable the connection cross-section popup
 - [DISPATCH-273](https://issues.apache.org/jira/browse/DISPATCH-273) - The entity view is missing information for some entities
 - [DISPATCH-275](https://issues.apache.org/jira/browse/DISPATCH-275) - Prevent javascript alert errors when navigating to console from a bookmark 
 - [DISPATCH-278](https://issues.apache.org/jira/browse/DISPATCH-278) - Deleting amqp listener using qdmanage crashes the router
 - [DISPATCH-279](https://issues.apache.org/jira/browse/DISPATCH-279) - Policy crash when application name is null
 - [DISPATCH-281](https://issues.apache.org/jira/browse/DISPATCH-281) - Hostname not sent in open frame on connectors
 - [DISPATCH-282](https://issues.apache.org/jira/browse/DISPATCH-282) - Prevent topology updates when adding a new router node
 - [DISPATCH-283](https://issues.apache.org/jira/browse/DISPATCH-283) - Start the overview page with the Router tree node expanded
 - [DISPATCH-284](https://issues.apache.org/jira/browse/DISPATCH-284) - The management schema no longer exposes a way to associate links with their connections
 - [DISPATCH-285](https://issues.apache.org/jira/browse/DISPATCH-285) - qdmanage returns an empty list when you QUERY for certain entities
 - [DISPATCH-287](https://issues.apache.org/jira/browse/DISPATCH-287) - Policy does not allow configuration for unspecified Open hostname
 - [DISPATCH-288](https://issues.apache.org/jira/browse/DISPATCH-288) - Driver - Wakeup pipe was seen to block on read, deadlocking the driver.
 - [DISPATCH-289](https://issues.apache.org/jira/browse/DISPATCH-289) - Unit tests failing on Solaris
 - [DISPATCH-290](https://issues.apache.org/jira/browse/DISPATCH-290) - Adapt CMakeLists.txt and code so that qpid-dispatch can be compiled on Solaris
 - [DISPATCH-292](https://issues.apache.org/jira/browse/DISPATCH-292) - some router.link attributes should be graphable
 - [DISPATCH-293](https://issues.apache.org/jira/browse/DISPATCH-293) - The $ character can't be used inside a prefix for linkRoute
 - [DISPATCH-294](https://issues.apache.org/jira/browse/DISPATCH-294) - Crash in the core-thread due to an address referencing a link on a closed connection
 - [DISPATCH-295](https://issues.apache.org/jira/browse/DISPATCH-295) - Router aborted on assertion failed after socker closing by client
 - [DISPATCH-298](https://issues.apache.org/jira/browse/DISPATCH-298) - router spinning on shutdown (in qdr_del_connection_ref)
 - [DISPATCH-299](https://issues.apache.org/jira/browse/DISPATCH-299) - After policy rejects a connection queued Begin causes a crash
 - [DISPATCH-304](https://issues.apache.org/jira/browse/DISPATCH-304) - Console PNG images not showing up in documentation
 - [DISPATCH-309](https://issues.apache.org/jira/browse/DISPATCH-309) - Mobile addresses get the wrong distribution when mapped to remote routers
 - [DISPATCH-310](https://issues.apache.org/jira/browse/DISPATCH-310) - Use router.id instead of container.containerName
 - [DISPATCH-312](https://issues.apache.org/jira/browse/DISPATCH-312) - Closest distribution fails to react to loss of a remote destination
 - [DISPATCH-319](https://issues.apache.org/jira/browse/DISPATCH-319) - Discrepancy between origin router's path and other routers' valid-origins
 - [DISPATCH-320](https://issues.apache.org/jira/browse/DISPATCH-320) - SSL enabled connector does not do hostname verification
 - [DISPATCH-321](https://issues.apache.org/jira/browse/DISPATCH-321) - Dispatch does not send out SASL-OUTCOME frame on sasl failure
 - [DISPATCH-334](https://issues.apache.org/jira/browse/DISPATCH-334) - Proton sequence error during backpressure with balanced distribution
 - [DISPATCH-335](https://issues.apache.org/jira/browse/DISPATCH-335) - link routes aren't balanced over remote routers
 - [DISPATCH-338](https://issues.apache.org/jira/browse/DISPATCH-338) - Incorrect default distribution for addresses
 - [DISPATCH-339](https://issues.apache.org/jira/browse/DISPATCH-339) - The change from 'routerId' to 'id' and 'addr' to 'host' configuration option is not backwards compatible
 - [DISPATCH-340](https://issues.apache.org/jira/browse/DISPATCH-340) - Test inter_router_plain_over_ssl fails to find SSL connection
 - [DISPATCH-342](https://issues.apache.org/jira/browse/DISPATCH-342) - qdrouterd.conf doc calls out router.config.{address,linkRoute,autoLink}
 - [DISPATCH-343](https://issues.apache.org/jira/browse/DISPATCH-343) - Router stops accepting connections after load from parallel senders
 - [DISPATCH-356](https://issues.apache.org/jira/browse/DISPATCH-356) - Creating and deleting a listener on already listening port causes router to crash
 - [DISPATCH-368](https://issues.apache.org/jira/browse/DISPATCH-368) - Router in bad state in two inter-connected routers

## Tasks

 - [DISPATCH-307](https://issues.apache.org/jira/browse/DISPATCH-307) - misc fixups for console plugin build
 - [DISPATCH-308](https://issues.apache.org/jira/browse/DISPATCH-308) - console documentation needs updated