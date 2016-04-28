# Overview

The Dispatch router is an AMQP router that provides advanced interconnect for AMQP.
It is *not* a broker.  It will never assume ownership of a message.  It will,
however, propagate settlement and disposition across a network such that delivery
guarantees are met.

The router is meant to be deployed in topologies of multiple routers, preferably with
redundant paths.  It uses link-state routing protocols and algorithms (similar to OSPF
or IS-IS from the networking world) to calculate the best path from every point to
every other point and to recover quickly from failures.  It does not need to use
clustering for high availability; rather, it relies on redundant paths to provide
continued connectivity in the face of system or network failure.

A messaging client can make a single AMQP connection into a messaging bus built of
Dispatch routers and, over that connection, exchange messages with one or more message
brokers, and at the same time exchange messages directly with other endpoints without
involving a broker at all.

## Benefits

### Simplifies connectivity

- An endpoint can do all of its messaging through a single transport connection
- Avoid opening holes in firewalls for incoming connections

### Simplifies reliability

- Reliability and availability are provided using redundant topology, not server clustering
- Reliable end-to-end messaging without persistent stores
- Use a message broker only when you need store-and-forward semantics
