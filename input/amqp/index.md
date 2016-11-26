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

# AMQP

The Advanced Message Queueing Protocol is at the heart of everything
we do at Qpid. It is an open standard designed to support reliable,
high-performance messaging over the internet. AMQP can be used for any
distributed application and supports common messaging patterns such as
point-to-point, fan-out, publish-subscribe, and request-response.

## AMQP 1.0

The AMQP working group released the 1.0 specification in the final
quarter of 2011. Future evolution of the protocol is now driven by the
member section and technical committees at OASIS.

In October 2012 AMQP 1.0 became an [OASIS Standard][oasis].  In May
2014 AMQP was approved as an
[ISO and IEC International Standard][iso].

[oasis]: http://www.amqp.org/node/102
[iso]: https://www.oasis-open.org/news/pr/iso-and-iec-approve-oasis-amqp-advanced-message-queuing-protocol

AMQP 1.0 is fully symmetric (peer-to-peer) as opposed to its
asymmetric (client-server) predecessors. This means it can be used
with or without intermediaries such as brokers and offers new
possibilities for messaging applications.

Qpid offers AMQP 1.0 support in the following components:

<div class="two-column" markdown="1">

 - [C++ broker]({{site_url}}/components/cpp-broker/index.html)
 - [Dispatch router]({{site_url}}/components/dispatch-router/index.html)
 - [Broker for Java]({{site_url}}/components/java-broker/index.html)
 - [Qpid JMS]({{site_url}}/components/jms/index.html)
 - [Qpid Messaging API]({{site_url}}/components/messaging-api/index.html)
 - [Qpid Proton]({{site_url}}/proton/index.html)

</div>

## AMQP and your app

We offer a library, [Qpid Proton]({{site_url}}/proton/index.html),
whose aim is to help you make your application speak AMQP.

## More information

 - [AMQP website](http://www.amqp.org/)
 - [AMQP presentation](http://www.amqp.org/sites/amqp.org/files/2014.05.01%20ISO%2019464%20AMQP-ORG_0.pdf)
 - [AMQP 1.0 specification](http://docs.oasis-open.org/amqp/core/v1.0/os/amqp-core-overview-v1.0-os.html)
 - [AMQP 1.0 interactive type reference](type-reference.html)
 - [OASIS AMQP technical committee](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=amqp)
 - [ISO 19464](http://www.iso.org/iso/home/store/catalogue_tc/catalogue_detail.htm?csnumber=64955)
 - [AMQP on Wikipedia](http://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol)
 - [Awesome AMQP links](https://github.com/xinchen10/awesome-amqp)
