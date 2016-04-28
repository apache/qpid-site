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

# Qpid Dispatch 0.3 Release Notes

Dispatch is a lightweight AMQP message router library. More about
[Qpid Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-1](https://issues.apache.org/jira/browse/DISPATCH-1) - Use Target Address from the link if there is no To field in a message from a producer
 - [DISPATCH-2](https://issues.apache.org/jira/browse/DISPATCH-2) - Adhere to the AMQP Management Specification for remote management
 - [DISPATCH-12](https://issues.apache.org/jira/browse/DISPATCH-12) - Exercise qdstat in the tests
 - [DISPATCH-16](https://issues.apache.org/jira/browse/DISPATCH-16) - Improve logging for dispatch
 - [DISPATCH-26](https://issues.apache.org/jira/browse/DISPATCH-26) - Documentation updates for 0.3
 - [DISPATCH-33](https://issues.apache.org/jira/browse/DISPATCH-33) - Use session flow control to protect the router's memory
 - [DISPATCH-34](https://issues.apache.org/jira/browse/DISPATCH-34) - Multi-Leg Addressing for Broker Integration
 - [DISPATCH-36](https://issues.apache.org/jira/browse/DISPATCH-36) - Make max-frame-size configurable per-connector/listener
 - [DISPATCH-38](https://issues.apache.org/jira/browse/DISPATCH-38) - Interpret unqualified $management as _local/$management
 - [DISPATCH-39](https://issues.apache.org/jira/browse/DISPATCH-39) - Use studlyCaps for standard management property names
 - [DISPATCH-41](https://issues.apache.org/jira/browse/DISPATCH-41) - Port the container to Proton Engine's new event API
 - [DISPATCH-49](https://issues.apache.org/jira/browse/DISPATCH-49) - Hush doxygen output
 - [DISPATCH-50](https://issues.apache.org/jira/browse/DISPATCH-50) - Allow configurable setting of logging levels.
 - [DISPATCH-54](https://issues.apache.org/jira/browse/DISPATCH-54) - Move message metadata from delivery-annotations to message-annotations
 - [DISPATCH-63](https://issues.apache.org/jira/browse/DISPATCH-63) - Daemon operation is needed for SysV-style service execution
 - [DISPATCH-67](https://issues.apache.org/jira/browse/DISPATCH-67) - Add listener configuration for allow-no-sasl
 - [DISPATCH-69](https://issues.apache.org/jira/browse/DISPATCH-69) - Router container should offer ANONYMOUS-RELAY capability
 - [DISPATCH-74](https://issues.apache.org/jira/browse/DISPATCH-74) - Allow changes to logging configuration of a running router.
 - [DISPATCH-80](https://issues.apache.org/jira/browse/DISPATCH-80) - Management schema: implement annotations and entity inheritance as per AMQP management WD 09
 - [DISPATCH-81](https://issues.apache.org/jira/browse/DISPATCH-81) - Remove old management code.
 - [DISPATCH-92](https://issues.apache.org/jira/browse/DISPATCH-92) - Make dispatch logging configuration more flexible and qpid-like
 - [DISPATCH-94](https://issues.apache.org/jira/browse/DISPATCH-94) - Router documentation to Qpid web site for 0.3 release.

## Bugs fixed

 - [DISPATCH-31](https://issues.apache.org/jira/browse/DISPATCH-31) - Valgrind reports memory leaks due to stubbed destructors
 - [DISPATCH-37](https://issues.apache.org/jira/browse/DISPATCH-37) - Various memory leaks
 - [DISPATCH-40](https://issues.apache.org/jira/browse/DISPATCH-40) - Qdrouterd segfaults while connecting to neighbour router
 - [DISPATCH-46](https://issues.apache.org/jira/browse/DISPATCH-46) - dispatch crash when proton gets bad socket
 - [DISPATCH-51](https://issues.apache.org/jira/browse/DISPATCH-51) - address semantics don't propagate from one router to another
 - [DISPATCH-59](https://issues.apache.org/jira/browse/DISPATCH-59) - Inconsistency on router reconnection
 - [DISPATCH-61](https://issues.apache.org/jira/browse/DISPATCH-61) - Inconsistent service names for the router
 - [DISPATCH-66](https://issues.apache.org/jira/browse/DISPATCH-66) - NULL header fields are interpreted as present
 - [DISPATCH-72](https://issues.apache.org/jira/browse/DISPATCH-72) - Sporadic core dumps in dispatch tests
 - [DISPATCH-73](https://issues.apache.org/jira/browse/DISPATCH-73) - Disallow inter-router listeners and connectors if role = standalone.
 - [DISPATCH-75](https://issues.apache.org/jira/browse/DISPATCH-75) - Remove reference to qdstat.conf from qdstat manpage
 - [DISPATCH-76](https://issues.apache.org/jira/browse/DISPATCH-76) - qd_log should not evaluate its arguments if log statement is not enabled.
 - [DISPATCH-77](https://issues.apache.org/jira/browse/DISPATCH-77) - Error decoding an integer message body
 - [DISPATCH-78](https://issues.apache.org/jira/browse/DISPATCH-78) - Driver runs at 100% CPU after an unclean disconnect
 - [DISPATCH-79](https://issues.apache.org/jira/browse/DISPATCH-79) - Management agent errors after restarting a second router.
 - [DISPATCH-82](https://issues.apache.org/jira/browse/DISPATCH-82) - Poor error handling by qdmanage and qdstat tools.
 - [DISPATCH-83](https://issues.apache.org/jira/browse/DISPATCH-83) - Error messages are not displayed if an error occurs when starting in deamon mode 
 - [DISPATCH-85](https://issues.apache.org/jira/browse/DISPATCH-85) - Remove all direct printing to stdout and stderr.
 - [DISPATCH-86](https://issues.apache.org/jira/browse/DISPATCH-86) - Management agent should enforce format of identifiers.
 - [DISPATCH-87](https://issues.apache.org/jira/browse/DISPATCH-87) - Double load of libqpid-dispatch.so
 - [DISPATCH-88](https://issues.apache.org/jira/browse/DISPATCH-88) - Python functions invoked without the Python lock being held causes crash
 - [DISPATCH-91](https://issues.apache.org/jira/browse/DISPATCH-91) - Configured log levels don't work with Python-based sources
 - [DISPATCH-93](https://issues.apache.org/jira/browse/DISPATCH-93) - Multiple log entries in config file prevent qdrouterd from starting
 - [DISPATCH-95](https://issues.apache.org/jira/browse/DISPATCH-95) - Connector and listener  identity does not show address and port.

## Tasks

 - [DISPATCH-65](https://issues.apache.org/jira/browse/DISPATCH-65) - Packages are needed for Ubuntu Precise (12 LTS)