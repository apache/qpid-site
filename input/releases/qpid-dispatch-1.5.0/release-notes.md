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

# Qpid Dispatch 1.5.0 Release Notes

Dispatch is a lightweight AMQP message router library. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-1141](https://issues.apache.org/jira/browse/DISPATCH-1141) - Add an event API in the router core to more cleanly support module interactions
 - [DISPATCH-1142](https://issues.apache.org/jira/browse/DISPATCH-1142) - Edge Router Module - Connection manager to select the active uplink
 - [DISPATCH-1143](https://issues.apache.org/jira/browse/DISPATCH-1143) - Connection-scoped link routes
 - [DISPATCH-1145](https://issues.apache.org/jira/browse/DISPATCH-1145) - Edge Router - Implement address proxy component
 - [DISPATCH-1150](https://issues.apache.org/jira/browse/DISPATCH-1150) - A request/response message client API for core
 - [DISPATCH-1152](https://issues.apache.org/jira/browse/DISPATCH-1152) - Improvements to the core-endpoint API
 - [DISPATCH-1154](https://issues.apache.org/jira/browse/DISPATCH-1154) - Synchronize routed link configurations on edge router with interior router
 - [DISPATCH-1156](https://issues.apache.org/jira/browse/DISPATCH-1156) - Delivery echo-prevention for edge routers
 - [DISPATCH-1158](https://issues.apache.org/jira/browse/DISPATCH-1158) - Add background map to console's topology page
 - [DISPATCH-1159](https://issues.apache.org/jira/browse/DISPATCH-1159) - Remove the term "uplink" from the edge router - It's confusing
 - [DISPATCH-1160](https://issues.apache.org/jira/browse/DISPATCH-1160) - Add edge address tracking module to interior routers which will inform edges of mobile address receiver changes
 - [DISPATCH-1161](https://issues.apache.org/jira/browse/DISPATCH-1161) - Handle edge routers in the console
 - [DISPATCH-1162](https://issues.apache.org/jira/browse/DISPATCH-1162) - Documentation updates related to Edge Router
 - [DISPATCH-1165](https://issues.apache.org/jira/browse/DISPATCH-1165) - Generate egress-link histograms for more kinds of connections
 - [DISPATCH-1166](https://issues.apache.org/jira/browse/DISPATCH-1166) - Expand the mouseover area for connections on the console's topology page 
 - [DISPATCH-1168](https://issues.apache.org/jira/browse/DISPATCH-1168) - Display additional detail for end-point connections, and edge-routers on the console's topology page
 - [DISPATCH-1178](https://issues.apache.org/jira/browse/DISPATCH-1178) - Allow unspecified router-id in configuration - select a random ID
 - [DISPATCH-1191](https://issues.apache.org/jira/browse/DISPATCH-1191) - Log files could use some analysis and summary tools
 - [DISPATCH-1193](https://issues.apache.org/jira/browse/DISPATCH-1193) - Smoothly transition colors on console's traffic congestion view
 - [DISPATCH-1194](https://issues.apache.org/jira/browse/DISPATCH-1194) - Asynchronous address lookup on attach for Edge to determine if there are link-route destinations
 - [DISPATCH-1195](https://issues.apache.org/jira/browse/DISPATCH-1195) - Continually update detail info on conole topology page
 - [DISPATCH-1199](https://issues.apache.org/jira/browse/DISPATCH-1199) - [tools] Log scraper tool should be moved to tools directory
 - [DISPATCH-1200](https://issues.apache.org/jira/browse/DISPATCH-1200) - [Test] system_tests_edge_router must import 're'
 - [DISPATCH-1201](https://issues.apache.org/jira/browse/DISPATCH-1201) - [tools] Scraper is mishandling transfers with no AMQP properties
 - [DISPATCH-1202](https://issues.apache.org/jira/browse/DISPATCH-1202) - [tools] Scraper README is stale
 - [DISPATCH-1204](https://issues.apache.org/jira/browse/DISPATCH-1204) - Add console tests for edge router
 - [DISPATCH-1205](https://issues.apache.org/jira/browse/DISPATCH-1205) - Allow signed int values &gt;= 0 be parsed as unsigned int
 - [DISPATCH-1206](https://issues.apache.org/jira/browse/DISPATCH-1206) - Consolidate similar HTML templates into an angularjs directive
 - [DISPATCH-1207](https://issues.apache.org/jira/browse/DISPATCH-1207) - [tools] Scraper does not handle session recreation over same connection
 - [DISPATCH-1208](https://issues.apache.org/jira/browse/DISPATCH-1208) - [tools] Scraper is slow with large number of links
 - [DISPATCH-1209](https://issues.apache.org/jira/browse/DISPATCH-1209) - Add and enabling gate to control the initialization of core modules
 - [DISPATCH-1210](https://issues.apache.org/jira/browse/DISPATCH-1210) - [tools] Scraper could find and show unsettled transfers
 - [DISPATCH-1211](https://issues.apache.org/jira/browse/DISPATCH-1211) - Show rate of acceptedDeliveries in console detail for edge routers
 - [DISPATCH-1216](https://issues.apache.org/jira/browse/DISPATCH-1216) - [tools] Scraper should sort links by source/target address
 - [DISPATCH-1224](https://issues.apache.org/jira/browse/DISPATCH-1224) - Waypoints may be attached by external containers without using auto-links
 - [DISPATCH-1227](https://issues.apache.org/jira/browse/DISPATCH-1227) - Add a policy setting to allow or forbid dynamic link routes
 - [DISPATCH-1238](https://issues.apache.org/jira/browse/DISPATCH-1238) - [tools] Scraper does not roll up error counts for convienient viewing

## Bugs fixed

 - [DISPATCH-1146](https://issues.apache.org/jira/browse/DISPATCH-1146) - Core-endpoint can't receive deliveries on core-initiated links
 - [DISPATCH-1153](https://issues.apache.org/jira/browse/DISPATCH-1153) - Router crash when a detach arrives on a link that is processing deliveries
 - [DISPATCH-1155](https://issues.apache.org/jira/browse/DISPATCH-1155) - dueling httpRootDirs
 - [DISPATCH-1163](https://issues.apache.org/jira/browse/DISPATCH-1163) - Coverity issues on master branch 
 - [DISPATCH-1164](https://issues.apache.org/jira/browse/DISPATCH-1164) - Failing to compile the router when only python3 is installed
 - [DISPATCH-1169](https://issues.apache.org/jira/browse/DISPATCH-1169) - Remove stranded link info popup on console's topology page
 - [DISPATCH-1170](https://issues.apache.org/jira/browse/DISPATCH-1170) - System tests failing when executed on a python3 only machine
 - [DISPATCH-1171](https://issues.apache.org/jira/browse/DISPATCH-1171) - Interior router crash when edge receiver disconnects
 - [DISPATCH-1174](https://issues.apache.org/jira/browse/DISPATCH-1174) - Update console's address class logic for edge routers
 - [DISPATCH-1176](https://issues.apache.org/jira/browse/DISPATCH-1176) - Router crash when connected to network that has &gt; 400 edge routers
 - [DISPATCH-1180](https://issues.apache.org/jira/browse/DISPATCH-1180) - Console's traffic animation incorrectly shows traffic from an edge router
 - [DISPATCH-1181](https://issues.apache.org/jira/browse/DISPATCH-1181) - handling MAU when local address is not yet defined can result in wrong treatment
 - [DISPATCH-1182](https://issues.apache.org/jira/browse/DISPATCH-1182) - Fix various drawing glitches with console
 - [DISPATCH-1184](https://issues.apache.org/jira/browse/DISPATCH-1184) - Deal with router ids that differ only by spaces in the id
 - [DISPATCH-1185](https://issues.apache.org/jira/browse/DISPATCH-1185) - Update .gitignore for a few generated files
 - [DISPATCH-1187](https://issues.apache.org/jira/browse/DISPATCH-1187) - Allow router to be configured to log in UTC time
 - [DISPATCH-1189](https://issues.apache.org/jira/browse/DISPATCH-1189) - "log" configuration is missing "module" attribute
 - [DISPATCH-1190](https://issues.apache.org/jira/browse/DISPATCH-1190) - Fix console topology page not recognizing edge router connected to multiple routers
 - [DISPATCH-1192](https://issues.apache.org/jira/browse/DISPATCH-1192) - Use black for idle (no traffic) color on console's topology page
 - [DISPATCH-1196](https://issues.apache.org/jira/browse/DISPATCH-1196) - Delivery reference count assertion can fail with released multiframe messages
 - [DISPATCH-1197](https://issues.apache.org/jira/browse/DISPATCH-1197) - Released multi-frame deliveries can cause stalling of inbound links
 - [DISPATCH-1198](https://issues.apache.org/jira/browse/DISPATCH-1198) - An early query of 'org.apache.qpid.dispatch.router.node' can crash the router
 - [DISPATCH-1203](https://issues.apache.org/jira/browse/DISPATCH-1203) - Console tests are skipped
 - [DISPATCH-1212](https://issues.apache.org/jira/browse/DISPATCH-1212) - Incorrect "Dropped Presettled Count " in output of qdstat -g when receiver drops off 
 - [DISPATCH-1213](https://issues.apache.org/jira/browse/DISPATCH-1213) - Sender  link  sending  pre-settled multi-frame deliveries can stall if receiver drops  
 - [DISPATCH-1217](https://issues.apache.org/jira/browse/DISPATCH-1217) - Dragging a new node doesn't freeze its position on console topology page
 - [DISPATCH-1219](https://issues.apache.org/jira/browse/DISPATCH-1219) - [tools] Scraper fails to parse AMQP error with no description
 - [DISPATCH-1220](https://issues.apache.org/jira/browse/DISPATCH-1220) - Valgrid errors when running system_tests_edge_router
 - [DISPATCH-1221](https://issues.apache.org/jira/browse/DISPATCH-1221) - Syncing a new router to an existing network can fail
 - [DISPATCH-1222](https://issues.apache.org/jira/browse/DISPATCH-1222) - coverity static analysis reports several issues
 - [DISPATCH-1223](https://issues.apache.org/jira/browse/DISPATCH-1223) - [tools] Scraper miscounts transfers with 'more' set as unsettled
 - [DISPATCH-1228](https://issues.apache.org/jira/browse/DISPATCH-1228) - qdstat -a fails with "KeyError: priority" against 1.4 version of router
 - [DISPATCH-1229](https://issues.apache.org/jira/browse/DISPATCH-1229) - System tests failing when executed with python3.7
 - [DISPATCH-1231](https://issues.apache.org/jira/browse/DISPATCH-1231) - Edge router fails to sync link routes due to credit stall
 - [DISPATCH-1232](https://issues.apache.org/jira/browse/DISPATCH-1232) - Edge router test failing on RHEL6
 - [DISPATCH-1233](https://issues.apache.org/jira/browse/DISPATCH-1233) - system_tests_global_delivery_counts fails intermittently
 - [DISPATCH-1234](https://issues.apache.org/jira/browse/DISPATCH-1234) - Router crash when edge tracking address handler tries to access freed endpoint
 - [DISPATCH-1235](https://issues.apache.org/jira/browse/DISPATCH-1235) - peer deliveries for multicast are incorrectly unlinked
 - [DISPATCH-1237](https://issues.apache.org/jira/browse/DISPATCH-1237) - large frame multicast can stall receivers if one receiver closes its connection
 - [DISPATCH-1239](https://issues.apache.org/jira/browse/DISPATCH-1239) - System tests failing when executed with python 2.6
 - [DISPATCH-1240](https://issues.apache.org/jira/browse/DISPATCH-1240) - core client api generates non-unique correlation id's on 32 bit systems

## Tasks

 - [DISPATCH-1175](https://issues.apache.org/jira/browse/DISPATCH-1175) - Update console to use the latest rhea.js library