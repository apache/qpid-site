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

# Qpid Dispatch 0.7.0 Release Notes

Dispatch is a lightweight AMQP message router library. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-204](https://issues.apache.org/jira/browse/DISPATCH-204) - Identity mapping from X.509 certificate data to a descriptive nickname
 - [DISPATCH-211](https://issues.apache.org/jira/browse/DISPATCH-211) - Expose connection properties in management response
 - [DISPATCH-233](https://issues.apache.org/jira/browse/DISPATCH-233) - Allow client side saslMechanisms to be specified for qdstat and qdmanage
 - [DISPATCH-311](https://issues.apache.org/jira/browse/DISPATCH-311) - [Policy] schema object names could be improved
 - [DISPATCH-348](https://issues.apache.org/jira/browse/DISPATCH-348) - Don't show deprecated entities and attributes
 - [DISPATCH-349](https://issues.apache.org/jira/browse/DISPATCH-349) - Modify the client icon on the topology page to indicate when there are multiple clients.
 - [DISPATCH-350](https://issues.apache.org/jira/browse/DISPATCH-350) - Display list of links for client connections. Allow acquiesce of links
 - [DISPATCH-388](https://issues.apache.org/jira/browse/DISPATCH-388) - Add deprecated flag to schema entities and attributes
 - [DISPATCH-395](https://issues.apache.org/jira/browse/DISPATCH-395) - Add Links to overview page
 - [DISPATCH-399](https://issues.apache.org/jira/browse/DISPATCH-399) - Convert documentation to asciidoc format
 - [DISPATCH-400](https://issues.apache.org/jira/browse/DISPATCH-400) - Remember last entity expanded on overview page
 - [DISPATCH-407](https://issues.apache.org/jira/browse/DISPATCH-407) - Tweeks to Links on overview page
 - [DISPATCH-412](https://issues.apache.org/jira/browse/DISPATCH-412) - Support 'stdout' as log destination as well as 'stderr'
 - [DISPATCH-427](https://issues.apache.org/jira/browse/DISPATCH-427) - Implement expand/collapse all to the Overview and Entities tabs
 - [DISPATCH-428](https://issues.apache.org/jira/browse/DISPATCH-428) - Connecting the dispatch-console to wrong port throws JS exception and freezes console
 - [DISPATCH-434](https://issues.apache.org/jira/browse/DISPATCH-434) - Remember all entities expanded on overview and entities pages
 - [DISPATCH-440](https://issues.apache.org/jira/browse/DISPATCH-440) - Use the placeholder HTML attribute to communicate default values in the Connect form
 - [DISPATCH-446](https://issues.apache.org/jira/browse/DISPATCH-446) - Make sslProfile an entity and remove all annotations
 - [DISPATCH-447](https://issues.apache.org/jira/browse/DISPATCH-447) - Modify cmake to optionally Install stand-alone and hawtio console
 - [DISPATCH-464](https://issues.apache.org/jira/browse/DISPATCH-464) - Change plugin name from dispatch-plugin to dispatch-hawtio-console to match the artifact name
 - [DISPATCH-468](https://issues.apache.org/jira/browse/DISPATCH-468) - Display-name for identity in x.509 certificates
 - [DISPATCH-471](https://issues.apache.org/jira/browse/DISPATCH-471) - server.c needs refactoring around qd_connection_t allocation
 - [DISPATCH-477](https://issues.apache.org/jira/browse/DISPATCH-477) - Drop pre-settled under congestion
 - [DISPATCH-483](https://issues.apache.org/jira/browse/DISPATCH-483) - Display links per address and connection on overview page
 - [DISPATCH-511](https://issues.apache.org/jira/browse/DISPATCH-511) - Remove performance problems from locks and memory allocation
 - [DISPATCH-513](https://issues.apache.org/jira/browse/DISPATCH-513) - Add a typed iterator to parsed field (qd_parsed_field_t) 
 - [DISPATCH-514](https://issues.apache.org/jira/browse/DISPATCH-514) - Add link statistics for different dispositions
 - [DISPATCH-515](https://issues.apache.org/jira/browse/DISPATCH-515) - Add example config file for auto starting webbroxy
 - [DISPATCH-517](https://issues.apache.org/jira/browse/DISPATCH-517) - Expose new link statistics on overview page
 - [DISPATCH-518](https://issues.apache.org/jira/browse/DISPATCH-518) - Use eventfd instead of a pipe for poll wakeup.
 - [DISPATCH-520](https://issues.apache.org/jira/browse/DISPATCH-520) - Remove qpidd references from dispatch system_test.py
 - [DISPATCH-521](https://issues.apache.org/jira/browse/DISPATCH-521) - Switch to verify qdrouterd installation
 - [DISPATCH-522](https://issues.apache.org/jira/browse/DISPATCH-522) - Performance: Defer activation and driver-awakening

## Bugs fixed

 - [DISPATCH-8](https://issues.apache.org/jira/browse/DISPATCH-8) - Message:user-id must be authenticated on ingress
 - [DISPATCH-160](https://issues.apache.org/jira/browse/DISPATCH-160) - Dispatch router does not propagate custom message annotations
 - [DISPATCH-224](https://issues.apache.org/jira/browse/DISPATCH-224) - Tools fail with no useful error in some SASL configurations
 - [DISPATCH-280](https://issues.apache.org/jira/browse/DISPATCH-280) - Management tools do not send AMQP Open.hostname with new proton
 - [DISPATCH-313](https://issues.apache.org/jira/browse/DISPATCH-313) - Tree on left side of entity page scrolls back to top after data is updated 
 - [DISPATCH-316](https://issues.apache.org/jira/browse/DISPATCH-316) - Refector javascript so the common code between hawtio and standalone is not duplicated
 - [DISPATCH-317](https://issues.apache.org/jira/browse/DISPATCH-317) - Show tooltip for long values on left panel on topology page
 - [DISPATCH-318](https://issues.apache.org/jira/browse/DISPATCH-318) - Don't allow router nodes to be moved off of the screen on topology page
 - [DISPATCH-336](https://issues.apache.org/jira/browse/DISPATCH-336) - Very high latency for fire-and-forget sender
 - [DISPATCH-345](https://issues.apache.org/jira/browse/DISPATCH-345) - Initialize current node on entity page when logged into a different router network 
 - [DISPATCH-346](https://issues.apache.org/jira/browse/DISPATCH-346) - Don't attempt to load non-existant css file when hawtio plugin loads
 - [DISPATCH-353](https://issues.apache.org/jira/browse/DISPATCH-353) - segfault in qd_entity_refresh_connection
 - [DISPATCH-354](https://issues.apache.org/jira/browse/DISPATCH-354) - qdstat general statistics broken
 - [DISPATCH-362](https://issues.apache.org/jira/browse/DISPATCH-362) - Handwritten paragraphs of man qdrouterd.conf are out of sync with autogenerated parts
 - [DISPATCH-363](https://issues.apache.org/jira/browse/DISPATCH-363) - Autogenerated part of man page qdrouterd.conf and output of `qdmanage print-json-schema` leave out the `name:` attribute in annotation sections
 - [DISPATCH-370](https://issues.apache.org/jira/browse/DISPATCH-370) - qdmanage tool hangs if --type option is "linkRoute" or "address"
 - [DISPATCH-373](https://issues.apache.org/jira/browse/DISPATCH-373) - qdmanage : no clear error message when "read" type linkRoute, address and autoLink
 - [DISPATCH-375](https://issues.apache.org/jira/browse/DISPATCH-375) - Console instalation instructions do not work
 - [DISPATCH-379](https://issues.apache.org/jira/browse/DISPATCH-379) - Missing default route indication on topology page
 - [DISPATCH-381](https://issues.apache.org/jira/browse/DISPATCH-381) - qdstat -g causes segfault
 - [DISPATCH-384](https://issues.apache.org/jira/browse/DISPATCH-384) - qdrouter.conf manual : saslMechanisms as "Space separated list ..."
 - [DISPATCH-389](https://issues.apache.org/jira/browse/DISPATCH-389) - Removing CONFIG and DISPATCH as modules for logging
 - [DISPATCH-391](https://issues.apache.org/jira/browse/DISPATCH-391) - Attributes missing for listener and connector and trustedCerts still there
 - [DISPATCH-392](https://issues.apache.org/jira/browse/DISPATCH-392) - "attributeName is undefined error" when showing "address", "linkRoute" and "autoLink"
 - [DISPATCH-393](https://issues.apache.org/jira/browse/DISPATCH-393) - Download router configuration doesn't work
 - [DISPATCH-394](https://issues.apache.org/jira/browse/DISPATCH-394) - Chart just added isn't shown in the dashboard
 - [DISPATCH-396](https://issues.apache.org/jira/browse/DISPATCH-396) - The "console" entity attributes aren't shown in the qdrouterd.conf
 - [DISPATCH-397](https://issues.apache.org/jira/browse/DISPATCH-397) - Error creating a new connector on a router with same name but on another router
 - [DISPATCH-398](https://issues.apache.org/jira/browse/DISPATCH-398) - For Dispatch 0.7 release move up the minimum required version of qpid proton to 0.13.0
 - [DISPATCH-401](https://issues.apache.org/jira/browse/DISPATCH-401) - qdstat and qdmanage client tools do not verify host name when using SSL
 - [DISPATCH-402](https://issues.apache.org/jira/browse/DISPATCH-402) - Remove deprecated hyphen-separated config and entity names
 - [DISPATCH-405](https://issues.apache.org/jira/browse/DISPATCH-405) - Chart data should be cleared when the console disconnects
 - [DISPATCH-406](https://issues.apache.org/jira/browse/DISPATCH-406) - Area charts only show the top line in Firefox.
 - [DISPATCH-414](https://issues.apache.org/jira/browse/DISPATCH-414) - Deleting a ProxyListener from dispatch-console segfaults the router
 - [DISPATCH-416](https://issues.apache.org/jira/browse/DISPATCH-416) - Connecting the dispatch-console to wrong host displays incomplete error message
 - [DISPATCH-417](https://issues.apache.org/jira/browse/DISPATCH-417) - "There are no policyStatss" in dispatch-console
 - [DISPATCH-418](https://issues.apache.org/jira/browse/DISPATCH-418) - Deleting an address in the dispatch-console does not work
 - [DISPATCH-425](https://issues.apache.org/jira/browse/DISPATCH-425) - Tree on the left side gets rerendered when navigating in dispatch-console preferences
 - [DISPATCH-426](https://issues.apache.org/jira/browse/DISPATCH-426) - The left tree view in Overview tab allows opening multiple branches at once. Tree view in Entities tab behives like accordeon.
 - [DISPATCH-431](https://issues.apache.org/jira/browse/DISPATCH-431) - Do not link to http://127.0.0.1:8080/dispatch-plugin
 - [DISPATCH-435](https://issues.apache.org/jira/browse/DISPATCH-435) - Dragging a node to a corner on the topology screen leads to a visual disconnect between the node and its link
 - [DISPATCH-436](https://issues.apache.org/jira/browse/DISPATCH-436) - Releasing the mouse button outside of the Topology SVG when dragging a node causes the node follow the mouse even if the mouse button is not pressed
 - [DISPATCH-439](https://issues.apache.org/jira/browse/DISPATCH-439) - Connect form cannot be submitted using only keyboard
 - [DISPATCH-442](https://issues.apache.org/jira/browse/DISPATCH-442) - system_tests_sasl_plain and system_tests_deprecated failing on Ubuntu
 - [DISPATCH-444](https://issues.apache.org/jira/browse/DISPATCH-444) - Add full entity type to schema
 - [DISPATCH-445](https://issues.apache.org/jira/browse/DISPATCH-445) - Use fullyQualifiedType from the schema when calling methods
 - [DISPATCH-449](https://issues.apache.org/jira/browse/DISPATCH-449) - Link-leak for attach-routed links
 - [DISPATCH-452](https://issues.apache.org/jira/browse/DISPATCH-452) - Prevent javascript alerts on Entities and Topology pages when new routers join network 
 - [DISPATCH-453](https://issues.apache.org/jira/browse/DISPATCH-453) - Reserve the right column on the topology page for the legend 
 - [DISPATCH-454](https://issues.apache.org/jira/browse/DISPATCH-454) - Legend on topology page is too tall
 - [DISPATCH-455](https://issues.apache.org/jira/browse/DISPATCH-455) - When autostart is checked and there is no router listening, FF generates a stream of error popups
 - [DISPATCH-456](https://issues.apache.org/jira/browse/DISPATCH-456) - Redirect back to connect page as soon as connection is dropped
 - [DISPATCH-457](https://issues.apache.org/jira/browse/DISPATCH-457) - Overview page does not update after router is added/removed from network
 - [DISPATCH-458](https://issues.apache.org/jira/browse/DISPATCH-458) - Batching of settlement can cause credit to be not issued to senders
 - [DISPATCH-461](https://issues.apache.org/jira/browse/DISPATCH-461) - [Policy] policyStats object missed being renamed to vhostStats
 - [DISPATCH-462](https://issues.apache.org/jira/browse/DISPATCH-462) - [Policy] Policy and vhost objects not named correctly by agent
 - [DISPATCH-463](https://issues.apache.org/jira/browse/DISPATCH-463) - [Policy] Remove wildcard user name description from policy doc
 - [DISPATCH-473](https://issues.apache.org/jira/browse/DISPATCH-473) - Deleting an SSL Profile used by a listener sometimes causes the router to crash
 - [DISPATCH-479](https://issues.apache.org/jira/browse/DISPATCH-479) - Use atomic operations for ref counts
 - [DISPATCH-482](https://issues.apache.org/jira/browse/DISPATCH-482) - trace level log messages are printing out as null
 - [DISPATCH-484](https://issues.apache.org/jira/browse/DISPATCH-484) - Update tree icons on overview and entities pages
 - [DISPATCH-485](https://issues.apache.org/jira/browse/DISPATCH-485) - All routers table on overview page is missing data
 - [DISPATCH-486](https://issues.apache.org/jira/browse/DISPATCH-486) - Data table on entities page has no left margin
 - [DISPATCH-487](https://issues.apache.org/jira/browse/DISPATCH-487) - Missing header on Quiesce button column
 - [DISPATCH-488](https://issues.apache.org/jira/browse/DISPATCH-488) - Provide a notification system for stand-alone console
 - [DISPATCH-489](https://issues.apache.org/jira/browse/DISPATCH-489) - Fetching logs entries on Entities page no longer works
 - [DISPATCH-491](https://issues.apache.org/jira/browse/DISPATCH-491) - Frequent skipped HELLO message from route engine
 - [DISPATCH-494](https://issues.apache.org/jira/browse/DISPATCH-494) - Policy objects do not support management update and delete directives
 - [DISPATCH-495](https://issues.apache.org/jira/browse/DISPATCH-495) - Autolinks to non-existent nodes cause problems in the router
 - [DISPATCH-496](https://issues.apache.org/jira/browse/DISPATCH-496) - Activation of an autolink does not result in issuing credit to a blocked sender
 - [DISPATCH-498](https://issues.apache.org/jira/browse/DISPATCH-498) - memory leak in _configure_ssl_profile error path
 - [DISPATCH-499](https://issues.apache.org/jira/browse/DISPATCH-499) - in propagating link detach the info field is dropped
 - [DISPATCH-500](https://issues.apache.org/jira/browse/DISPATCH-500) - name in conf file is not sent in response to management query
 - [DISPATCH-501](https://issues.apache.org/jira/browse/DISPATCH-501) - router segfaults if you sent a management query with an empty body
 - [DISPATCH-502](https://issues.apache.org/jira/browse/DISPATCH-502) - Seeing unexpected values in management query response
 - [DISPATCH-505](https://issues.apache.org/jira/browse/DISPATCH-505) - Eventual loss of credit on inter-router control links when the topology changes
 - [DISPATCH-507](https://issues.apache.org/jira/browse/DISPATCH-507) - Switching between hawtio console and stand-alone causes problems
 - [DISPATCH-508](https://issues.apache.org/jira/browse/DISPATCH-508) - Self tests use deprecated configuration objects
 - [DISPATCH-523](https://issues.apache.org/jira/browse/DISPATCH-523) - Topology changes can cause in-flight deliveries to be stuck in the ingress router
 - [DISPATCH-524](https://issues.apache.org/jira/browse/DISPATCH-524) - Unfair handling of multiple connections to the router
 - [DISPATCH-532](https://issues.apache.org/jira/browse/DISPATCH-532) - man pages installed in wrong directory (man.X)
 - [DISPATCH-533](https://issues.apache.org/jira/browse/DISPATCH-533) - Router crash in the 6-node example
 - [DISPATCH-535](https://issues.apache.org/jira/browse/DISPATCH-535) - Use correct lifecycle management for Proton objects
 - [DISPATCH-550](https://issues.apache.org/jira/browse/DISPATCH-550) - Assertion failure in router in larger scale networks
 - [DISPATCH-558](https://issues.apache.org/jira/browse/DISPATCH-558) - Remove assertions in the core agent that fail due to malformed requests