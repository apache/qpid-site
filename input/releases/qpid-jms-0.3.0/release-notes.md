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

# Qpid JMS 0.3.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 1.1 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-53](https://issues.apache.org/jira/browse/QPIDJMS-53) - treat messages with a Data section and common textual content-type values as TextMessage
 - [QPIDJMS-55](https://issues.apache.org/jira/browse/QPIDJMS-55) - Add support for using standard AMQP ports if the URI fails to provide one
 - [QPIDJMS-61](https://issues.apache.org/jira/browse/QPIDJMS-61) - add support for setting the sasl / open frame 'hostname'
 - [QPIDJMS-64](https://issues.apache.org/jira/browse/QPIDJMS-64) - Throw a JMSException with a more consistent error message when connection attempts fail
 - [QPIDJMS-70](https://issues.apache.org/jira/browse/QPIDJMS-70) - Add a redelivery policy to control when the client should reject new deliveries based on the delivery count.

## Bugs fixed

 - [QPIDJMS-48](https://issues.apache.org/jira/browse/QPIDJMS-48) - inconsistent handling of property names in Message methods
 - [QPIDJMS-49](https://issues.apache.org/jira/browse/QPIDJMS-49) - handle messages with an unknown content-type
 - [QPIDJMS-52](https://issues.apache.org/jira/browse/QPIDJMS-52) - support charset parameter in content-type value
 - [QPIDJMS-54](https://issues.apache.org/jira/browse/QPIDJMS-54) - remove extraneous indirection around selector verification
 - [QPIDJMS-56](https://issues.apache.org/jira/browse/QPIDJMS-56) - throw InvalidClientIDException rather than JMSException when hint present that container-id was the problem field
 - [QPIDJMS-57](https://issues.apache.org/jira/browse/QPIDJMS-57) - ErrorCondition 'info' field lookups should use Symbol keys
 - [QPIDJMS-58](https://issues.apache.org/jira/browse/QPIDJMS-58) - when a connection redirect error is received, the original connection details will be used first
 - [QPIDJMS-59](https://issues.apache.org/jira/browse/QPIDJMS-59) - uri pool object is not thread safe but is accessed by multiple threads
 - [QPIDJMS-60](https://issues.apache.org/jira/browse/QPIDJMS-60) - using 'nested options' causes issues when adding/removing a URI from the pool object
 - [QPIDJMS-62](https://issues.apache.org/jira/browse/QPIDJMS-62) - ensure that a body section is always sent when using ObjectMessage
 - [QPIDJMS-63](https://issues.apache.org/jira/browse/QPIDJMS-63) - SASL ANONYMOUS doesn't seem to work against the C++ broker
 - [QPIDJMS-65](https://issues.apache.org/jira/browse/QPIDJMS-65) - updated SASL mechanism selection to consider available credentials
 - [QPIDJMS-66](https://issues.apache.org/jira/browse/QPIDJMS-66) - fix documentation of URI option for ClientID
 - [QPIDJMS-67](https://issues.apache.org/jira/browse/QPIDJMS-67) - AMQP header and Open+Close frames are sent after a SASL failure
 - [QPIDJMS-71](https://issues.apache.org/jira/browse/QPIDJMS-71) - calling receive(0) on a consumer always returns null
 - [QPIDJMS-72](https://issues.apache.org/jira/browse/QPIDJMS-72) - update discovery uri syntax for consistency and add some basic documentation