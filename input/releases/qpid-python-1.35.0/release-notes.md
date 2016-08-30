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

# Qpid Python 1.35.0 Release Notes

Qpid Python includes an AMQP messaging library and a suite of tests
for AMQP conformance.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-6475](https://issues.apache.org/jira/browse/QPID-6475) - 08..09 Send connection.close before closing socket
 - [QPID-6567](https://issues.apache.org/jira/browse/QPID-6567) - Support producer side flow control in the 0-8/9/9-1 Python client
 - [QPID-6839](https://issues.apache.org/jira/browse/QPID-6839) - When the Selector thread hits an unknown exception it should log the exception and traceback.
 - [QPID-7053](https://issues.apache.org/jira/browse/QPID-7053) - Exception Notifier Callback

## Bugs fixed

 - [QPID-6297](https://issues.apache.org/jira/browse/QPID-6297) - Python client (qpid.messaging) raises KeyError insead of reconnecting
 - [QPID-6326](https://issues.apache.org/jira/browse/QPID-6326) - [ACL] Python client demands unnecessary permission / performs unnecessary actions
 - [QPID-6405](https://issues.apache.org/jira/browse/QPID-6405) - Python client does not report version to peer
 - [QPID-6445](https://issues.apache.org/jira/browse/QPID-6445) - Qpid python client hangs when message with routing key longer than 255 is sent (mutual recursion)
 - [QPID-6473](https://issues.apache.org/jira/browse/QPID-6473) - Remove remaining Python &lt;= 2.5 raise syntax (i.e. raise "...") from connection08.py
 - [QPID-6474](https://issues.apache.org/jira/browse/QPID-6474) - 08..09 Python client connection leaks threads
 - [QPID-7064](https://issues.apache.org/jira/browse/QPID-7064) - Document Asynchronous Error Notification API on Connection, Session, Receiver, and Sender objects
 - [QPID-7222](https://issues.apache.org/jira/browse/QPID-7222) - Python test qpid_tests.broker_0_10.message.MessageTests.test_release_order fails sporadically against java broker
 - [QPID-7251](https://issues.apache.org/jira/browse/QPID-7251) - [Python Client for AMQP 0-8...0-91] Setting of SASL mechanism (other then PLAIN) explicitly does not work in python client for AMQP 0-8...0-91
 - [QPID-7258](https://issues.apache.org/jira/browse/QPID-7258) - [Python Client for AMQP 0-8...0-9-1] Perform hostname verification of ssl/tls connections
 - [QPID-7259](https://issues.apache.org/jira/browse/QPID-7259) - qpid_tests.broker_0_10.message.MessageTests.test_window_flow_messages occasionally fails against the Java Broker