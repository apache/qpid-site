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

# Qpid JMS AMQP 0-x 6.3.1 Release Notes

Qpid JMS AMQP 0-x is JMS 1.1 compatible client which can speak AMQP 0-8,0-9,0-9-1 and 0-10.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPID-8153](https://issues.apache.org/jira/browse/QPID-8153) - [JMS AMQP 0-x] JMS AMQP 0-x should be able to send SNI as part of TLS handshake
 - [QPID-8180](https://issues.apache.org/jira/browse/QPID-8180) - [JMS AMQP 0-8..0-91] Improve error message associated with the channel not found during frame dispatch

## Bugs fixed

 - [QPID-8044](https://issues.apache.org/jira/browse/QPID-8044) - [JMS AMQP 0-x] Address minor packaging issues raised during 6.3.0 vote
 - [QPID-8057](https://issues.apache.org/jira/browse/QPID-8057) - [JMS AMQP 0-x][AMQP 0-10] IoReceiver thread can block itself for 60 seconds after sending session close controls and waiting for broker responses
 - [QPID-8135](https://issues.apache.org/jira/browse/QPID-8135) - [JMS AMQP 0-x] Connection URL options for end-to-end encryption keystore/trustore passwords can be logged when log level for 'org.apache.qpid' loggers is lower than 'warn'
 - [QPID-8141](https://issues.apache.org/jira/browse/QPID-8141) - [JMS AMQP 0-x] Sending message to address based destinations that matches the address of a previously resolved address fails
 - [QPID-8185](https://issues.apache.org/jira/browse/QPID-8185) - [JMS AMQP 0-x][AMQP 0-8..0-91] Make sure that client closes TCP connection on failure with sending connection.close and avoid spurious NPEs whilst awaiting channel closure

## Tasks

 - [QPID-8074](https://issues.apache.org/jira/browse/QPID-8074) - [JMS AMQP 0-x] Build framework to run JMS client system tests