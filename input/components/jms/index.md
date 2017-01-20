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

# Qpid JMS

<div class="feature" markdown="1">

## JMS with the strength of AMQP

Qpid JMS is an AMQP 1.0 [Java Message Service][jms] 2.0 client built
using [Qpid Proton]({{site_url}}/proton/index.html).

Qpid also provides an alternate JMS client supporting
[earlier AMQP versions](amqp-0-x.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service

</div>

## Features

 - [JMS 2.0](https://jcp.org/aboutJava/communityprocess/mrel/jsr343/index.html)
   API
 - Secure communication via SSL and SASL 
 - Producer flow control
 - Failover
 - Pure-Java implementation

## Documentation

<div class="two-column" markdown="1">

 - [API reference](http://docs.oracle.com/javaee/7/api/javax/jms/package-summary.html)
 - [Examples](https://github.com/apache/qpid-jms/tree/{{current_jms_release}}/qpid-jms-examples)
 - [Configuration]({{current_jms_release_url}}/docs/index.html)
 - [Building Qpid JMS]({{current_jms_release_url}}/building.html)

</div>

For details about the AMQP 0-x JMS client, look [here](amqp-0-x.html).

</div>

<div id="-right-column" class="right-column-adjusted" markdown="1">

## Releases

 - {{current_jms_release_link}}
 - [Past releases]({{site_url}}/releases/index.html#past-releases)

## Issues

 - [Report a bug](https://issues.apache.org/jira/secure/CreateIssue.jspa?pid=12314524&issuetype=1&priority=3&summary=[Enter%20a%20brief%20description])
 - [Request an improvement](https://issues.apache.org/jira/secure/CreateIssue.jspa?pid=12314524&issuetype=4&priority=3)
 - <form id="-jira-goto-form">Go to issue <input name="jira" value="QPIDJMS-"/></form>
 - [JIRA project page](https://issues.apache.org/jira/browse/QPIDJMS)

## Source code

 - [Browse via GitHub](https://github.com/apache/qpid-jms)
 - [Git clone URL](https://git-wip-us.apache.org/repos/asf/qpid-jms.git)

## Resources

 - [AMQP 0-x JMS Client](amqp-0-x.html)

</div>
