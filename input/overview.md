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

# Overview

## The challenge

Modern large-scale applications are rarely built as monoliths.
Instead, they are built as distributed network applications, with
parts of the application in distinct processes and distinct parts of
the world.

All the same, the parts need to work together to behave as one
reliable application. They need a way to communicate, and they must
be able to tolerate failures.

## Messaging is a better way

Modern messaging systems aren't the only way to get processes talking.
Your application's parts can share a view into a database, or you can
use HTTP and REST to expose information.  But these approaches have
some serious drawbacks.  A database is reliable, but it isn't designed
to intermediate communication.  Its focus is storing data, not moving
it between processes.  REST helps you communicate efficiently, but it
offers no reliability.  If the party you're talking to is unavailable,
the transmission is dropped.

A store-and-forward messaging system gives you efficient, reliable
communication.  Message brokers take responsibility for ensuring
messages reach their destination, even if the destination is
temporarily out of reach.  Messaging APIs manage acknowledgments so
that no messages are dropped in transit.

## Proprietary messaging solutions

For decades, the messaging approach to application integration was
available only from proprietary vendors.  Each vendor had its own
messaging API and its own wire protocol, and without going to trouble,
they wouldn't interoperate.  Imagine each web server vendor using its
own protocol.  That would seem intolerable, but that's precisely the
situation messaging was in.

With the introduction of the
[Java Message Service](http://en.wikipedia.org/wiki/Java_Message_Service)
API, things got a little better.  Now we had a standard messaging API.
But JMS doesn't define a standard wire protocol, and it doesn't help
you if you're not using Java.

## Qpid and AMQP

[AMQP]({{site_url}}/amqp/index.html) is the first open standard wire
protocol for messaging.  AMQP is foremost about the choices it gives
you.  You can choose any AMQP solution you prefer, and if the one you
chose doesn't work out, you can switch.  Your application will still
work.

The Qpid project aims to spur the growth of the AMQP ecosystem.  We
offer messaging APIs and message brokers for use in your application,
and core libraries for making AMQP part of your own messaging product.

 - *Open source* - We do our work in the community, and you can gain
   from our contributions just as we can gain from yours.

 - *Many languages, many platforms* - We want AMQP to be available
   everywhere.  That's why we have focused on supporting a wide range
   of programming languages and computing environments.

 - *Application development* - Messaging is essential to reliable
   distributed applications, and we offer the tools you need to build
   one.  Check out our
   [messaging APIs]({{site_url}}/components/index.html#messaging-apis).

 - *Messaging infrastructure* - You can design and deploy an AMQP
   network that integrates with other services in your organization.
   See our
   [messaging servers]({{site_url}}/components/index.html#messaging-servers).

 - *Your messaging product* - We know that there are many established
   messaging systems, and we want to make it easy for them to speak
   AMQP.  Consider using [Qpid Proton]({{site_url}}/proton/index.html)
   instead of developing your own protocol support.

;; - *Language-native communication frameworks* - Java, .NET, Python,
;;   and others have their own generic communication frameworks, and
;;   Qpid integrates with many of them.
   
## The future of messaging is bigger still

Traditional messaging has focused on the back office, with just one
logical broker at the center of things.  The AMQP 1.0 standard makes
messaging possible in a new, larger dimension.  The next incarnation
of messaging will provide a diverse network of messaging
intermediaries.  It will leverage redundancy in the network to route
around failures, just as TCP and routers do, and it will allow
messaging applications to operate at unprecedented scale.

The Qpid community is building the foundations for these new
technologies.

;; XXX add link to roadmap once we have a reasonable one

## More information

 - [How to get involved](get-involved.html)
 - [Qpid is a top-level project at Apache](http://www.apache.org/foundation/press/pr_2009_03_03.html)
