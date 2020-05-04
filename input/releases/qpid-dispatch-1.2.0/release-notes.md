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

# Qpid Dispatch 1.2.0 Release Notes

Dispatch is a lightweight AMQP 1.0 message router. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-965](https://issues.apache.org/jira/browse/DISPATCH-965) - Python 3 compatibiliy
 - [DISPATCH-980](https://issues.apache.org/jira/browse/DISPATCH-980) - Allow address translation on link routes
 - [DISPATCH-982](https://issues.apache.org/jira/browse/DISPATCH-982) - Handle small form-factor screens
 - [DISPATCH-1013](https://issues.apache.org/jira/browse/DISPATCH-1013) - Enable vhost policies to be used in the router config file (not just through separate JSON files)
 - [DISPATCH-1014](https://issues.apache.org/jira/browse/DISPATCH-1014) - Visualize link congestion on topology page
 - [DISPATCH-1015](https://issues.apache.org/jira/browse/DISPATCH-1015) - Improve visualization of connection and link info on console's topology page. 
 - [DISPATCH-1016](https://issues.apache.org/jira/browse/DISPATCH-1016) - Consolidate console style sheets to improve load time
 - [DISPATCH-1020](https://issues.apache.org/jira/browse/DISPATCH-1020) - Detach expiring links with closed=true when peer connectivity lost
 - [DISPATCH-1024](https://issues.apache.org/jira/browse/DISPATCH-1024) - Latest version of qpid-proton is causing build issues on Travis, to system tests using incorrect url with user and password
 - [DISPATCH-1049](https://issues.apache.org/jira/browse/DISPATCH-1049) - Add console tests
 - [DISPATCH-1053](https://issues.apache.org/jira/browse/DISPATCH-1053) - Allow deliveries to be constrained to router-control links by address state

## Bugs fixed

 - [DISPATCH-969](https://issues.apache.org/jira/browse/DISPATCH-969) - Dropdown menu doesn't work when browser is narrow
 - [DISPATCH-976](https://issues.apache.org/jira/browse/DISPATCH-976) - Allow policy for sources and targets to handle multiple wildcards
 - [DISPATCH-979](https://issues.apache.org/jira/browse/DISPATCH-979) - self test mock policy manager does not forward policy warnings
 - [DISPATCH-984](https://issues.apache.org/jira/browse/DISPATCH-984) - Json config file processing clobbers files with '#' character in strings
 - [DISPATCH-985](https://issues.apache.org/jira/browse/DISPATCH-985) - Policy username substitution token is documented incorrectly
 - [DISPATCH-988](https://issues.apache.org/jira/browse/DISPATCH-988) - Documentation of policy default vhost is wrong
 - [DISPATCH-990](https://issues.apache.org/jira/browse/DISPATCH-990) - Use patterns for policy vhost hostnames
 - [DISPATCH-998](https://issues.apache.org/jira/browse/DISPATCH-998) - Parse tree does not have remove function that takes a string pattern
 - [DISPATCH-1003](https://issues.apache.org/jira/browse/DISPATCH-1003) - Enable console support for connecting to listener configured with saslMechanisms other than ANONYMOUS
 - [DISPATCH-1008](https://issues.apache.org/jira/browse/DISPATCH-1008) - Router should preserve original connection information when attempting to make failover connections
 - [DISPATCH-1011](https://issues.apache.org/jira/browse/DISPATCH-1011) - Policy username substitution fails to match certain user names
 - [DISPATCH-1025](https://issues.apache.org/jira/browse/DISPATCH-1025) - User token not being replaced properly on a vhost policy when defined in the prefix or suffix
 - [DISPATCH-1026](https://issues.apache.org/jira/browse/DISPATCH-1026) - Router crashing when using sourcePattern/targetPattern with multiple patterns and one of them being user token when trying to open an unauthorized address
 - [DISPATCH-1029](https://issues.apache.org/jira/browse/DISPATCH-1029) - State is not retained on Entities tree for console
 - [DISPATCH-1030](https://issues.apache.org/jira/browse/DISPATCH-1030) - Empty table on Entities page of console
 - [DISPATCH-1031](https://issues.apache.org/jira/browse/DISPATCH-1031) - Remove the links associated with a console from the console's overview page
 - [DISPATCH-1033](https://issues.apache.org/jira/browse/DISPATCH-1033) - Incorrect location for legend on Message flow page in console
 - [DISPATCH-1034](https://issues.apache.org/jira/browse/DISPATCH-1034) - saslPlugin option does not work with http option in listener
 - [DISPATCH-1036](https://issues.apache.org/jira/browse/DISPATCH-1036) - Dropdown lists on the Entity page are the wrong color
 - [DISPATCH-1037](https://issues.apache.org/jira/browse/DISPATCH-1037) - Listeners with http enabled are not being shutdown after they are deleted
 - [DISPATCH-1041](https://issues.apache.org/jira/browse/DISPATCH-1041) - Add new test to validate global delivery counts provided by the router
 - [DISPATCH-1043](https://issues.apache.org/jira/browse/DISPATCH-1043) - In a two router network, qdstat -g is showing non-zero values for "Ingress Count" even when no messages are sent
 - [DISPATCH-1044](https://issues.apache.org/jira/browse/DISPATCH-1044) - Link routed deliveries not included in the global transit and egress counts
 - [DISPATCH-1045](https://issues.apache.org/jira/browse/DISPATCH-1045) - Sometimes close connetion after releasing partial multi-frame messsage
 - [DISPATCH-1046](https://issues.apache.org/jira/browse/DISPATCH-1046) - system_tests_policy fail in python3 environment
 - [DISPATCH-1047](https://issues.apache.org/jira/browse/DISPATCH-1047) - system_tests_ssl fail when running under python3 environment
 - [DISPATCH-1048](https://issues.apache.org/jira/browse/DISPATCH-1048) - system_tests_http fail when run under python3 environment
 - [DISPATCH-1050](https://issues.apache.org/jira/browse/DISPATCH-1050) - sasl delegation plugin should set SNI to match auth address
 - [DISPATCH-1051](https://issues.apache.org/jira/browse/DISPATCH-1051) - Python memory leak via PyLong_FromLong
 - [DISPATCH-1052](https://issues.apache.org/jira/browse/DISPATCH-1052) - minor lock leak in policy code
 - [DISPATCH-1056](https://issues.apache.org/jira/browse/DISPATCH-1056) - Build fails making docs on python-3-only fedora 28
 - [DISPATCH-1057](https://issues.apache.org/jira/browse/DISPATCH-1057) - system_tests_console failing 
 - [DISPATCH-1058](https://issues.apache.org/jira/browse/DISPATCH-1058) - Fix leaks/other code issues found by Coverity 

## Tasks

 - [DISPATCH-1001](https://issues.apache.org/jira/browse/DISPATCH-1001) - Deprecate the tools under the console directory and move them to a separate npm repistory.