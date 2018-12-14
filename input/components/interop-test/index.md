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

<div id="-left-column" markdown="1">

# Qpid Interop Test

<div class="feature" markdown="1">

A test suite that systematically tests [AMQP 1.0]({{site_url}}/amqp/index.html)
clients against each other to ensure that they are working correctly
with each other. The tests consist of matched client pairs to send and receive
messages through an AMQP server (or combination of connected servers). These tests
also check that the AMQP server is able to handle the clients and AMQP traffic.

</div>

## Features

<div class="two-column" markdown="1">

 - Tests all available clients against each other
 - Tests AMQP clients against any AMQP server
 - Tests AMQP types
 - Tests large messages
 - Tests JMS messages
 - Tests JMS headers and properties

</div>

## Supported servers

Any servers that can handle [AMQP 1.0]({{site_url}}/amqp/index.html)
will work. By default, the tests run against localhost using the default AMQP port (5672), but these can be
changed to any valid IP address and port.

## Supported clients

The following clients are currently supported:

 - [Qpid Proton C++]({{current_proton_release_url}}/proton/c/api/files.html)
 - [Qpid Proton Python]({{current_proton_release_url}}/proton/python/api/index.html)
 - [Qpid JMS]({{site_url}}/components/jms/index.html)
 - [Rhea Javascript](https://github.com/grs/rhea)
 - [AMQP .Net Lite](https://github.com/Azure/amqpnetlite)

## AMQP test coverage

<div class="scroll" markdown="1">

<table>
  <thead>
    <tr>
      <th>&nbsp;</th>
      <th colspan="4">Clients</th>
    </tr>
    <tr>
      <th>Test</th>
      <th>Qpid Proton C++</th>
      <th>Qpid Proton Python</th>
      <th>Rhea</th>
      <th>AMQP .Net Lite</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AMQP types</th>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
    </tr>
    <tr>
      <th>Large AMQP messages</th>
      <td>YES</td>
      <td>YES</td>
      <td></td>
      <td>YES</td>
    </tr>
  </tbody>
</table>

</div>

## JMS test coverage

<div class="scroll" markdown="1">

<table>
  <thead>
    <tr>
      <th>&nbsp;</th>
      <th colspan="5">Clients</th>
    </tr>
    <tr>
      <th>Test</th>
      <th>Qpid JMS</th>
      <th>Qpid Proton C++</th>
      <th>Qpid Proton Python</th>
      <th>Rhea</th>
      <th>AMQP .Net Lite</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>JMS messages</th>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>JMS headers & properties</th>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

</div>

## Documentation

<div class="two-column" markdown="1">

 - [Quickstart guide]({{current_interop_test_release_url}}/QUICKSTART.html)
 - [User guide]({{current_interop_test_release_url}}/users-guide.html)
 - [Developer overview](https://gitbox.apache.org/repos/asf?p=qpid-interop-test.git;a=blob_plain;f=docs/qpid-interop-test-devel-overview.txt;hb=0.1.0)
 - [Test HOWTO](https://gitbox.apache.org/repos/asf?p=qpid-interop-test.git;a=blob_plain;f=docs/Test_HOWTO.txt;hb=0.1.0)
 - [Shim HOWTO](https://gitbox.apache.org/repos/asf?p=qpid-interop-test.git;a=blob_plain;f=docs/Shim_HOWTO.txt;hb=0.1.0)

</div>

</div>

<div id="-right-column" class="right-column-adjusted" markdown="1">

## Releases

 - {{current_interop_test_release_link}} 
 - [Past releases]({{site_url}}/releases/index.html#past-releases)

## Issues

 - [Report a bug](https://issues.apache.org/jira/secure/CreateIssue.jspa?pid=12318621&issuetype=1&priority=3)
 - [Request an improvement](https://issues.apache.org/jira/secure/CreateIssue.jspa?pid=12318621&issuetype=4&priority=3)
 - <form id="-jira-goto-form">Go to issue <input name="jira" value="QPIDIT-"/></form>
 - [JIRA project page](https://issues.apache.org/jira/browse/QPIDIT)
 
## Source code

 - [Browse via GitHub](https://github.com/apache/qpid-interop-test)
 - [Git clone URL](https://gitbox.apache.org/repos/asf/qpid-interop-test.git)
 
</div>
