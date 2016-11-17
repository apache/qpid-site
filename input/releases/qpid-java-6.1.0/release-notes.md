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

# Qpid for Java 6.1.0 Release Notes

Qpid for Java 6.1 brings with it the following headline changes

* Support for consumer priorities
* Leverages the TLS cipher suite ordering abilities of JDK 1.8 to offer improved TLS performance
* New authentication/authorization features
 * Support for OAUTH2 authentication with out of the box support for many public OAUTH2 services (including Google, Github, and Facebook)
 * Support for the utilisation of group information from Directory Services (LDAP) for access control purposes
* Improvements to the Web Management Console
 * New Dashboard and Query UI features allow an operator to better understand a Broker's state
* Enhancements to the Management REST API
 * Support for Cross Origin Resource Sharing (CORS)
 * Support for message publishing via REST API
 * Query API allows developers and operators to better monitor the Broker
* Over 100 bug fixes and improvements

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-6703](https://issues.apache.org/jira/browse/QPID-6703) - Add optional mechanism to associate a temporary queue lifetime with that of it connection
 - [QPID-6764](https://issues.apache.org/jira/browse/QPID-6764) - Message age alerting is inappropriate on the enqueue path
 - [QPID-6805](https://issues.apache.org/jira/browse/QPID-6805) - Update Broker/Client documentation with changes made  for v6
 - [QPID-6852](https://issues.apache.org/jira/browse/QPID-6852) - Allow perftests to be conveniently run against Qpid JMS AMQP 1.0 client
 - [QPID-6866](https://issues.apache.org/jira/browse/QPID-6866) - Paginate connections table on virtualhost tab
 - [QPID-6915](https://issues.apache.org/jira/browse/QPID-6915) - Remove JMX support from Java Broker
 - [QPID-6916](https://issues.apache.org/jira/browse/QPID-6916) - Refactor system test suite to no longer assume exclusive use of port 15672 etc
 - [QPID-6917](https://issues.apache.org/jira/browse/QPID-6917) - Make web SASL pluggable in web management UI
 - [QPID-6927](https://issues.apache.org/jira/browse/QPID-6927) - Improve usability of Web Management Console when monitoring large deployments
 - [QPID-6932](https://issues.apache.org/jira/browse/QPID-6932) - Enhance model object to expose key JVM statistics such as heap memory, garbage collection
 - [QPID-6940](https://issues.apache.org/jira/browse/QPID-6940) - [Java Broker] [AMQP 1.0] The Delivery object does not need to retain a list of associated transfers
 - [QPID-6945](https://issues.apache.org/jira/browse/QPID-6945) - [Java Broker] Provide only one way to get content data from a Message
 - [QPID-6953](https://issues.apache.org/jira/browse/QPID-6953) - [Java Broker] Refactor AMQP 0-8/9/9-1 implementation to always use QpidByteBuffer for encoding output
 - [QPID-6954](https://issues.apache.org/jira/browse/QPID-6954) - [Java Broker] Add the ability to define "policies" for node auto-creation based on address
 - [QPID-6961](https://issues.apache.org/jira/browse/QPID-6961) - Use maven to generate Java Broker and (legacy) Java Client docbook
 - [QPID-6962](https://issues.apache.org/jira/browse/QPID-6962) - [Java Broker] Add ability to limit max message size on a per VirtualHost basis
 - [QPID-6965](https://issues.apache.org/jira/browse/QPID-6965) - Make preemptive HTTP authentication pluggable
 - [QPID-6967](https://issues.apache.org/jira/browse/QPID-6967) - [Java Broker] Add SCRAM-SHA1/256 sasl support to authentication managers which store the password in cleartext
 - [QPID-6969](https://issues.apache.org/jira/browse/QPID-6969) - [Java Broker] Provide SQL-like querying functionality through the HTTP Management API
 - [QPID-6971](https://issues.apache.org/jira/browse/QPID-6971) - [Java] [AMQP 0-8/9/9-1] Use QpidByteBuffer rather than MarkableDataInput for decoding
 - [QPID-6982](https://issues.apache.org/jira/browse/QPID-6982) - [Java Broker] Refactor VirtualHost to remove unnecessary methods
 - [QPID-6983](https://issues.apache.org/jira/browse/QPID-6983) - [Web Management Console] Add UI support for queries
 - [QPID-6984](https://issues.apache.org/jira/browse/QPID-6984) - [Web Management Console] Allow queries to be saved for later use
 - [QPID-6993](https://issues.apache.org/jira/browse/QPID-6993) - [Java Broker] Improve security of SCRAM-* authentication managers by not storing the salted passwords
 - [QPID-6995](https://issues.apache.org/jira/browse/QPID-6995) - [Java Broker] Keystores should warn of pending certificate expiration
 - [QPID-7006](https://issues.apache.org/jira/browse/QPID-7006) - Expose BDB JE cleanLog/checkpoint as an model operations of the BDBVH/BDBHAVHN
 - [QPID-7007](https://issues.apache.org/jira/browse/QPID-7007) - Add the ability to mutate JE configuration properties at runtime
 - [QPID-7009](https://issues.apache.org/jira/browse/QPID-7009) - BDD HA: DbPing call should have an independent timeout control
 - [QPID-7015](https://issues.apache.org/jira/browse/QPID-7015) - Add system test that ensure ability to login correctly with Scram-SHA based authentication providers
 - [QPID-7017](https://issues.apache.org/jira/browse/QPID-7017) - Include Queue UUID in QUE-1001/1002 operational log message
 - [QPID-7019](https://issues.apache.org/jira/browse/QPID-7019) - BDB JE turn on log file upgrade migration by default
 - [QPID-7027](https://issues.apache.org/jira/browse/QPID-7027) - [Java Broker] Make HTTP Management interactive login pluggable
 - [QPID-7028](https://issues.apache.org/jira/browse/QPID-7028) - [Java Broker] Add OAuth2 AuthenticationProvider
 - [QPID-7029](https://issues.apache.org/jira/browse/QPID-7029) - [Java Broker] Add OAuth2 PreemptiveAuthenticator
 - [QPID-7030](https://issues.apache.org/jira/browse/QPID-7030) - [Java Broker] Add OAuth2 HttpRequestInteractiveAuthenticator
 - [QPID-7031](https://issues.apache.org/jira/browse/QPID-7031) - [Java Broker] Add Pluggable OAuth2 AuthenticationProvider Backend for CloudFoundry
 - [QPID-7032](https://issues.apache.org/jira/browse/QPID-7032) - [Java Broker] Add information about the selected TLS protocol and cipher suite on Connection objects
 - [QPID-7035](https://issues.apache.org/jira/browse/QPID-7035) - [Java Broker] SCRAM implementation should make iteration count configurable
 - [QPID-7036](https://issues.apache.org/jira/browse/QPID-7036) - [Java Broker] Add ability to set the ClientCertRecorder trust store on the port in UI
 - [QPID-7037](https://issues.apache.org/jira/browse/QPID-7037) - [Java Broker] Add UI for exposing trust stores as message sources
 - [QPID-7038](https://issues.apache.org/jira/browse/QPID-7038) - [Java Perftests] Speedup Performance test execution
 - [QPID-7039](https://issues.apache.org/jira/browse/QPID-7039) - [Java Broker] Allow overriding of default initial configuration location via system property
 - [QPID-7041](https://issues.apache.org/jira/browse/QPID-7041) - Add system test for preemptive SSL client auth authentication against HTTP management
 - [QPID-7045](https://issues.apache.org/jira/browse/QPID-7045) - [Java Broker] Add OAuth2 SASL mechanism
 - [QPID-7046](https://issues.apache.org/jira/browse/QPID-7046) - Single-shot preemptively authenticated calls to the REST API should automatically expire the HTTP session
 - [QPID-7047](https://issues.apache.org/jira/browse/QPID-7047) - SaslServlet should invalidate the HTTP session in the event of authentication/authorisation failure
 - [QPID-7048](https://issues.apache.org/jira/browse/QPID-7048) - Log a warning if an AMQPPort does not have one or more virtual host aliases
 - [QPID-7049](https://issues.apache.org/jira/browse/QPID-7049) - [Java Broker] Provide a mechanism to inject attribute/statistic definitions into types at runtime
 - [QPID-7055](https://issues.apache.org/jira/browse/QPID-7055) - Improve GroupProvider API
 - [QPID-7056](https://issues.apache.org/jira/browse/QPID-7056) - [Java Broker/Client] Allow overriding of TLS cipher suites preferences
 - [QPID-7058](https://issues.apache.org/jira/browse/QPID-7058) - [Java Client] Log the current connection state when connection establishment times out
 - [QPID-7063](https://issues.apache.org/jira/browse/QPID-7063) - [Java Broker] SimpleLdap Authentication Provider should be able to override enabled cipher suites and TLS protocols from context variables for TLS connections to LDAP servers
 - [QPID-7066](https://issues.apache.org/jira/browse/QPID-7066) - [Java Broker] Add a validValuePattern attribute to ManagedAttribute
 - [QPID-7068](https://issues.apache.org/jira/browse/QPID-7068) - Drive AbstractConfiguredObject#validationChange from reflection rather than attribute metadata
 - [QPID-7069](https://issues.apache.org/jira/browse/QPID-7069) - [Java Broker] Add CloudFoundry specific GroupProvider
 - [QPID-7079](https://issues.apache.org/jira/browse/QPID-7079) - [Java Broker] Add connection state logging on idle timeout to 0-10 onnections
 - [QPID-7086](https://issues.apache.org/jira/browse/QPID-7086) - [Java Broker, Web Management Console] Add ability to set context variables
 - [QPID-7094](https://issues.apache.org/jira/browse/QPID-7094) - [Java Broker] Add tests for OAuth2
 - [QPID-7110](https://issues.apache.org/jira/browse/QPID-7110) - Create UI for virtual host alias
 - [QPID-7111](https://issues.apache.org/jira/browse/QPID-7111) - Create UI for the Oauth2 authentication provider
 - [QPID-7112](https://issues.apache.org/jira/browse/QPID-7112) - Create UI for the CloudFoundry Group Provider
 - [QPID-7113](https://issues.apache.org/jira/browse/QPID-7113) - [Java Broker] Add ability to select cipher suite during TLS negotiation based on Broker side cipher suite order
 - [QPID-7116](https://issues.apache.org/jira/browse/QPID-7116) - Ability to utilise group information from a LDAP compatible directory
 - [QPID-7118](https://issues.apache.org/jira/browse/QPID-7118) - Web Management Operator Dashboard
 - [QPID-7129](https://issues.apache.org/jira/browse/QPID-7129) - [Java Broker] BDB store should not attempt to load config from properties files
 - [QPID-7133](https://issues.apache.org/jira/browse/QPID-7133) - [Java Broker Documentation] Rename HA designated primary to match UI
 - [QPID-7135](https://issues.apache.org/jira/browse/QPID-7135) - [Java Broker] Add posibility to reload ACL files
 - [QPID-7151](https://issues.apache.org/jira/browse/QPID-7151) - [Java Broker] Improve error handling in OAuth2 AuthenticationProvider 
 - [QPID-7152](https://issues.apache.org/jira/browse/QPID-7152) - [Java Broker, Documentation] Add documentation for OAuth2 authentication
 - [QPID-7157](https://issues.apache.org/jira/browse/QPID-7157) - [Java Broker] Change metadata for management attributes having enum types to list all possible enum values in validValues property
 - [QPID-7158](https://issues.apache.org/jira/browse/QPID-7158) - [Java Broker] Change type of datetime management attributes from Long to java.util.Date
 - [QPID-7159](https://issues.apache.org/jira/browse/QPID-7159) - [Java Client] Disabling user ids in AMQP messages
 - [QPID-7162](https://issues.apache.org/jira/browse/QPID-7162) - Simple refactoring AbstractAMQPConnection &amp; sub-classes
 - [QPID-7165](https://issues.apache.org/jira/browse/QPID-7165) - Allow query results to be sorted and paginated
 - [QPID-7177](https://issues.apache.org/jira/browse/QPID-7177) - Add support for where clauses including time/date based functions such as now(), dateadd(), date()
 - [QPID-7188](https://issues.apache.org/jira/browse/QPID-7188) - [Java Broker] [AMQP1.0] Define a target capability to define how a target will respond when receiving a message it cannot route
 - [QPID-7198](https://issues.apache.org/jira/browse/QPID-7198) - LDAP and OAUTH2 Authentication Providers should cache authentication results for a short period
 - [QPID-7204](https://issues.apache.org/jira/browse/QPID-7204) - [Java systests] Add ability into system tests to override test, client and broker system properties from properties file
 - [QPID-7206](https://issues.apache.org/jira/browse/QPID-7206) - [Java Broker] Query API does not support conditions with fileds of enum type
 - [QPID-7209](https://issues.apache.org/jira/browse/QPID-7209) - [Java Broker, WMC] Enable HTTP compression by default
 - [QPID-7211](https://issues.apache.org/jira/browse/QPID-7211) - [Java Broker, WMC] Do not transfer inherited context variables
 - [QPID-7213](https://issues.apache.org/jira/browse/QPID-7213) - [Java Broker, WMC] Only transmit data for visible tab
 - [QPID-7214](https://issues.apache.org/jira/browse/QPID-7214) - [Java Broker, WMC] Do not use depth=2 in the REST request in Broker.js
 - [QPID-7215](https://issues.apache.org/jira/browse/QPID-7215) - [Java Broker, WMC] WMC should use query to retrieve connections
 - [QPID-7217](https://issues.apache.org/jira/browse/QPID-7217) - [Java Broker, WMC] Copyright footer should not be fixed at the bottom of the viewport
 - [QPID-7221](https://issues.apache.org/jira/browse/QPID-7221) - [Java Broker] On VirtualHost creation ManagedAttribute queue.deadLetterQueueEnabled should be initialised by context variable instead of referencing it
 - [QPID-7228](https://issues.apache.org/jira/browse/QPID-7228) - [Java Broker, Documentation] HA Backup documentation should mention that you cannot use a backup of one node to recover another
 - [QPID-7238](https://issues.apache.org/jira/browse/QPID-7238) - [Java Broker, WMC] Share data from structure service amongst UI elements
 - [QPID-7247](https://issues.apache.org/jira/browse/QPID-7247) - Implement preferences model and REST API
 - [QPID-7248](https://issues.apache.org/jira/browse/QPID-7248) - Extend the UI to allow queries to be saved, retrieved and re-run
 - [QPID-7249](https://issues.apache.org/jira/browse/QPID-7249) - [Java Tests] Handle failures in AMQQueueDeferredOrderingTest correctly 
 - [QPID-7255](https://issues.apache.org/jira/browse/QPID-7255) - Support delivery delay
 - [QPID-7274](https://issues.apache.org/jira/browse/QPID-7274) - [Java Client] Asynchronous client acknowledgements
 - [QPID-7276](https://issues.apache.org/jira/browse/QPID-7276) - [Java Broker] Message delay UI improvements
 - [QPID-7284](https://issues.apache.org/jira/browse/QPID-7284) - [Java Performance Tests] json_config_tool should recursively descend into configuration
 - [QPID-7291](https://issues.apache.org/jira/browse/QPID-7291) - [Java Broker] [Documentation] Add documentation for ManagedCertificateStore and SiteSpecificTrustStore
 - [QPID-7300](https://issues.apache.org/jira/browse/QPID-7300) - [Java Broker] The REST API should support Cross Origin Resource Sharing (CORS)
 - [QPID-7303](https://issues.apache.org/jira/browse/QPID-7303) - [Java Broker] Add operation returning the authenticated user principal and groups
 - [QPID-7305](https://issues.apache.org/jira/browse/QPID-7305) - [Java Broker] Queue operations copy/move/delete should take an optional JMS selector argument
 - [QPID-7308](https://issues.apache.org/jira/browse/QPID-7308) - [Java Broker] Improve Query UI functionality and look 
 - [QPID-7314](https://issues.apache.org/jira/browse/QPID-7314) - [Java Broker, Documentation] Apidocs should expose derivedAttributes
 - [QPID-7318](https://issues.apache.org/jira/browse/QPID-7318) - [Java Broker] Refactor existing ACL plugin code
 - [QPID-7323](https://issues.apache.org/jira/browse/QPID-7323) - [CVE-2016-4974] [Java Client] add whitelisting of trusted content for deserialization from ObjectMessage
 - [QPID-7330](https://issues.apache.org/jira/browse/QPID-7330) - [Java Broker] Preference Strore Integration
 - [QPID-7331](https://issues.apache.org/jira/browse/QPID-7331) - [Java Broker] Preference Store JSON backend
 - [QPID-7332](https://issues.apache.org/jira/browse/QPID-7332) - [Java Broker] Preference Store BDB backend
 - [QPID-7333](https://issues.apache.org/jira/browse/QPID-7333) - [Java Broker] Preference Store Recoverer
 - [QPID-7336](https://issues.apache.org/jira/browse/QPID-7336) - [Java Broker] Add createdDate to Preference object
 - [QPID-7337](https://issues.apache.org/jira/browse/QPID-7337) - [Java Broker] Preference Store JDBC/Derby backend
 - [QPID-7338](https://issues.apache.org/jira/browse/QPID-7338) - Use maven release plugin's tagNameFormat to avoid manual release step
 - [QPID-7340](https://issues.apache.org/jira/browse/QPID-7340) - Implement purge user managed operation
 - [QPID-7344](https://issues.apache.org/jira/browse/QPID-7344) - [Java Broker] Deprecate support for ACL checking based on the "immediate" flag
 - [QPID-7346](https://issues.apache.org/jira/browse/QPID-7346) - [Java Broker] Improve Principals to record their origin
 - [QPID-7352](https://issues.apache.org/jira/browse/QPID-7352) - [Java Broker] Principal serialisation
 - [QPID-7360](https://issues.apache.org/jira/browse/QPID-7360) - [Java Broker] [Web Management Console] Replace usages of the old preference system with the new one
 - [QPID-7362](https://issues.apache.org/jira/browse/QPID-7362) - [Java Broker] Remove old preferences API and UI
 - [QPID-7365](https://issues.apache.org/jira/browse/QPID-7365) - [Java Broker] Allow SystemConfig to be used for other models - not just Brokers
 - [QPID-7366](https://issues.apache.org/jira/browse/QPID-7366) - [Java Broker] Add Management operation to VirtualHost to allow publishing of messages through management
 - [QPID-7372](https://issues.apache.org/jira/browse/QPID-7372) - [Java Broker] Remove hard dependency on logback from broker-core
 - [QPID-7374](https://issues.apache.org/jira/browse/QPID-7374) - Reimplement producer transaction timeout feature to utilise an IO ticker
 - [QPID-7379](https://issues.apache.org/jira/browse/QPID-7379) - [Java Broker] Provide a mechanism to extract messages from a vhost message store and replay them into a new vhost
 - [QPID-7380](https://issues.apache.org/jira/browse/QPID-7380) - [Java Broker] Managed Operations returning potentially confidential information should not be permitted by default on insecure connections
 - [QPID-7381](https://issues.apache.org/jira/browse/QPID-7381) - [Java Broker] Support consumer priorities
 - [QPID-7409](https://issues.apache.org/jira/browse/QPID-7409) - Support preview of maps/list message content
 - [QPID-7411](https://issues.apache.org/jira/browse/QPID-7411) - Remove backup.sh from bdbstore module
 - [QPID-7422](https://issues.apache.org/jira/browse/QPID-7422) - [Java Tests] Make test timeouts configurable via system properties
 - [QPID-7426](https://issues.apache.org/jira/browse/QPID-7426) - [Java Client] Rename methods and variables in 0-8 Session and Consumer to better reflect their purpose
 - [QPID-7433](https://issues.apache.org/jira/browse/QPID-7433) - Add minimal maven module to invoke TCK
 - [QPID-7435](https://issues.apache.org/jira/browse/QPID-7435) - Avoid BDB fetching dummy single byte database entries during message instance recovery
 - [QPID-7437](https://issues.apache.org/jira/browse/QPID-7437) - [BDB] Avoid storing unnecessary single byte with message enqueue records
 - [QPID-7438](https://issues.apache.org/jira/browse/QPID-7438) - ACL provider and AutoGeneratedSelfSignedKeyStore modify configured state without using the configuration task executor
 - [QPID-7447](https://issues.apache.org/jira/browse/QPID-7447) - Java Broker tuning improvements for v6.1 release
 - [QPID-7448](https://issues.apache.org/jira/browse/QPID-7448) - [Java Client] Stop ClientDecoder from doing deep recursion
 - [QPID-7449](https://issues.apache.org/jira/browse/QPID-7449) - [Java Broker] Cache the ACL result for the system-user ACL provider
 - [QPID-7453](https://issues.apache.org/jira/browse/QPID-7453) - [Java Broker] Hand off selection task only if connection tasks need to be processed
 - [QPID-7454](https://issues.apache.org/jira/browse/QPID-7454) - [Java Broker] Queue Message Durability default (and others) should be overridable by context variables
 - [QPID-7460](https://issues.apache.org/jira/browse/QPID-7460) - [Java Broker] Improve performance of the Json Config store with large numbers of object
 - [QPID-7462](https://issues.apache.org/jira/browse/QPID-7462) - [Java Broker] Add experimental "pull" consumers to the broker
 - [QPID-7466](https://issues.apache.org/jira/browse/QPID-7466) - [Java Broker, Java Client for AMQP 0-8 to 0-10] Improve documentation for end-to-end encryption
 - [QPID-7471](https://issues.apache.org/jira/browse/QPID-7471) - [Java Broker] MessageConverter should respect mimeType
 - [QPID-7478](https://issues.apache.org/jira/browse/QPID-7478) - Add managed operation to reset statistics

## Bugs fixed

 - [QPID-5738](https://issues.apache.org/jira/browse/QPID-5738) - [Java Broker] AbstractConfigureObject#setAttribute() does not validate attributes
 - [QPID-5816](https://issues.apache.org/jira/browse/QPID-5816) - [Java Client 0-10] If a resolved destination is used to create a consumer on a new connection created after destination was resolved, the client does not try to create the destination on the broker
 - [QPID-6096](https://issues.apache.org/jira/browse/QPID-6096) - java broker doesn't indicate that port is already in use
 - [QPID-6377](https://issues.apache.org/jira/browse/QPID-6377) - Connection's taskpool not shutdown if Connection is closed from the broker side
 - [QPID-6753](https://issues.apache.org/jira/browse/QPID-6753) - Duplicate heartbeat reply
 - [QPID-6803](https://issues.apache.org/jira/browse/QPID-6803) - ByteBuffer slices/duplicates contribute significantly to garbage overhead in busy Brokers
 - [QPID-6817](https://issues.apache.org/jira/browse/QPID-6817) - [Java Broker] On abrupt connection close from client side when Broker is delivering messages to consumer the delivered messages might not be released as part of close in some unlucky circumstances
 - [QPID-6883](https://issues.apache.org/jira/browse/QPID-6883) - [Java Broker] In web management console Edit button is disabled for authentication providers: SCRAM-SHA-1, SCRAM-SHA-256, Plain, MD5
 - [QPID-6894](https://issues.apache.org/jira/browse/QPID-6894) - [Java Broker] VirtualHostNode of type REDIRECTOR cannot be stopped through web UI
 - [QPID-6901](https://issues.apache.org/jira/browse/QPID-6901) - Fix inconsistent channel log subject for 0-10 and 1.0
 - [QPID-6910](https://issues.apache.org/jira/browse/QPID-6910) - [Java Broker] Restore building of zip distribution bundle  for Qpid Java Broker
 - [QPID-6936](https://issues.apache.org/jira/browse/QPID-6936) - [Java Broker] Generation of Java Broker doc book in PDF format fails with exceptions
 - [QPID-6938](https://issues.apache.org/jira/browse/QPID-6938) - [Java Broker] [Java Client] Disable TLSv1 support by default
 - [QPID-6939](https://issues.apache.org/jira/browse/QPID-6939) - [Java Broker] [AMQP 1.0] Ensure all outstanding bytes get processed when received() is called on the connection
 - [QPID-6950](https://issues.apache.org/jira/browse/QPID-6950) - [Java Broker] Starting embedded broker with http-management plugin using Broker#startup(BrokerOptions)  requires Thread.UncaughtExceptionHandler to be set
 - [QPID-6951](https://issues.apache.org/jira/browse/QPID-6951) - [Java Client] AMQSession.deregisterConsumer() leaks Memory
 - [QPID-6957](https://issues.apache.org/jira/browse/QPID-6957) - [Java Tests] LastValueQueueTest sporadically fails on cpp profile
 - [QPID-6958](https://issues.apache.org/jira/browse/QPID-6958) - [Java Broker] A confusing exception is reported for Virtual Host type declared in the configuration store but with implementation not available in the classpath
 - [QPID-6959](https://issues.apache.org/jira/browse/QPID-6959) - [Java Broker] Cannot mutate BDB HA environment and modify such settings like priority, designating primary, etc when environment is in restarting state
 - [QPID-6968](https://issues.apache.org/jira/browse/QPID-6968) - [Java Broker] Decoding of pipelined AMQP 0-9.x frames can fail when multiple frames are received as part of the same byte buffer
 - [QPID-6972](https://issues.apache.org/jira/browse/QPID-6972) - BDB HA: Node may remain detached from group following loss of quorum
 - [QPID-6975](https://issues.apache.org/jira/browse/QPID-6975) - NonBlockingConnectionTLSDelegate won't read to stream end if SSLEngine is closed
 - [QPID-6979](https://issues.apache.org/jira/browse/QPID-6979) - AttributeValueConverter's Certificate handling code assumes unix line endings
 - [QPID-6994](https://issues.apache.org/jira/browse/QPID-6994) - [Java Broker] AMQP connection close might fail to delete temporary queue after close of VirtualHost
 - [QPID-6996](https://issues.apache.org/jira/browse/QPID-6996) - Can't make a node master twice (during a single Broker lifetime)
 - [QPID-6997](https://issues.apache.org/jira/browse/QPID-6997) - [Java Broker, BDBStore] HA JE Transaction commit might end up in NullPointerException when commit is invoked when majority is lost
 - [QPID-6999](https://issues.apache.org/jira/browse/QPID-6999) - [Java Broker, BDBStore, HA] In replicated environment JE transactions aborted on committing can cause Broker shutdown
 - [QPID-7001](https://issues.apache.org/jira/browse/QPID-7001) - [Java Broker] NullPointerException can be thrown from Port IO Thread
 - [QPID-7002](https://issues.apache.org/jira/browse/QPID-7002) - [Java Broker] REST API throws NullPointerException when requesting all consumers
 - [QPID-7008](https://issues.apache.org/jira/browse/QPID-7008) - [Java Broker] Add message user-id verification to 0-10 and 1-0 protocols
 - [QPID-7016](https://issues.apache.org/jira/browse/QPID-7016) - BDB JE cleaner can make no progress allowing for unbounded store growth
 - [QPID-7021](https://issues.apache.org/jira/browse/QPID-7021) - BDB hot backup (takeBackupNoLock) may fail with IOException
 - [QPID-7022](https://issues.apache.org/jira/browse/QPID-7022) - [Java Broker] Fix Web Management Console javascript issues
 - [QPID-7023](https://issues.apache.org/jira/browse/QPID-7023) - BDB HA: JE Cleaner warnings written to qpid log during apparently normal operation 
 - [QPID-7024](https://issues.apache.org/jira/browse/QPID-7024) - BDB HA - Group change thread-pool sized to availableProcessors +1
 - [QPID-7033](https://issues.apache.org/jira/browse/QPID-7033) - [Java Broker] Busy IO thread pools may cause client connections to be unfairly closed
 - [QPID-7050](https://issues.apache.org/jira/browse/QPID-7050) - [Java Broker] State change executor shutdown can delay closing of virtual host node when state change functionality is performed in parallel with replication environment facade close
 - [QPID-7052](https://issues.apache.org/jira/browse/QPID-7052) - [Java Performance Tests] In tests based on message number limit all consumed messages should be processed as normal reagrardless whether they arrive before or after StartDataCollectionCommand
 - [QPID-7057](https://issues.apache.org/jira/browse/QPID-7057) - [Java Client] The performance of the client connecting over TLS is significantly lower than before
 - [QPID-7060](https://issues.apache.org/jira/browse/QPID-7060) - [Java Broker] [0-10] Connection close disassociates virtualhost before closing sessions and connection model object
 - [QPID-7061](https://issues.apache.org/jira/browse/QPID-7061) - [Java Broker] Web management console help URL is set to wrong location
 - [QPID-7065](https://issues.apache.org/jira/browse/QPID-7065) - [Java Broker] Wrong RegEx prohibits HA VHNs with dash ("-") in host address
 - [QPID-7067](https://issues.apache.org/jira/browse/QPID-7067) - Scram SHA upgrader loses the original password
 - [QPID-7080](https://issues.apache.org/jira/browse/QPID-7080) - MultiNodeTest#testQuorumOverride may fail sporadically
 - [QPID-7081](https://issues.apache.org/jira/browse/QPID-7081) - [Java Broker] On broker startup with IBM JDK a log message "Cannot find com.sun.management.HotSpotDiagnosticMXBean MXBean" is repeated multiple times
 - [QPID-7082](https://issues.apache.org/jira/browse/QPID-7082) - [Java Broker] Created AccessControllerContext for SystemTasks should not reference current context
 - [QPID-7096](https://issues.apache.org/jira/browse/QPID-7096) - [Java Broker] Add minor release version to REST API version
 - [QPID-7097](https://issues.apache.org/jira/browse/QPID-7097) - [Java Broker, HA] Broker configuration thread is used to perform notifications about removal of BDB HA VirtualHost when VH is closed in response to environment state transition events
 - [QPID-7101](https://issues.apache.org/jira/browse/QPID-7101) - Guard CancelledKeyException to deal with the case where the Port is shutdown before the the connection has finally closed
 - [QPID-7108](https://issues.apache.org/jira/browse/QPID-7108) - [Java Broker] Test BDBHAVirtualHostNodeTest.testIntruderProtection is failing sporadically
 - [QPID-7114](https://issues.apache.org/jira/browse/QPID-7114) - [Java Broker] ConnectionBuilder should set protocol and cipher suites on all code paths
 - [QPID-7120](https://issues.apache.org/jira/browse/QPID-7120) - [Java Broker] Test AbruptClientDisconnectTest.testMessagingOnAbruptConnectivityLostWhilstConsuming fails sporadically
 - [QPID-7122](https://issues.apache.org/jira/browse/QPID-7122) - CloseOnNoRouteForMandatoryMessageTest.testNoRoute_brokerClosesConnection fails sporadically on slow CI
 - [QPID-7124](https://issues.apache.org/jira/browse/QPID-7124) - [Java Broker] IndexOutOfBoundsException when attempting to create an object through the REST API with no path
 - [QPID-7126](https://issues.apache.org/jira/browse/QPID-7126) - [Java Broker] A broker with multiple HTTP ports does not separate session attributes for requests on different ports
 - [QPID-7132](https://issues.apache.org/jira/browse/QPID-7132) - qpid-server does not properly quote dirname $0 argument
 - [QPID-7136](https://issues.apache.org/jira/browse/QPID-7136) - [Java Broker] [BDB HA] [AMQP 1.0] Connection to a replica throws an uncaught exception which closes the broker
 - [QPID-7154](https://issues.apache.org/jira/browse/QPID-7154) - Dead lettering of a message may timeout at store level, causing unexpected Broker shutdown
 - [QPID-7155](https://issues.apache.org/jira/browse/QPID-7155) - [Java Broker] Idle timeout ticker times out connection before heartbeating is negotiated
 - [QPID-7156](https://issues.apache.org/jira/browse/QPID-7156) - Possible Java Broker crash if connection is formed whilst virtualhost is stopping
 - [QPID-7160](https://issues.apache.org/jira/browse/QPID-7160) - No X509TrustManager implementation available when using truststore captured by SiteSpecificTrustStore
 - [QPID-7174](https://issues.apache.org/jira/browse/QPID-7174) - [JavaBroker] Broker fails to open ManagedPeerCertificateTrustStore containing certificates added via port
 - [QPID-7181](https://issues.apache.org/jira/browse/QPID-7181) - [AMQP 1.0] Selector parsing error causes Java Broker to shutdown
 - [QPID-7185](https://issues.apache.org/jira/browse/QPID-7185) - ReplicatedEnvironmentFacadeTest.testReplicationGroupListenerHearsNodeRemoved fails sporadically on Apache CI
 - [QPID-7186](https://issues.apache.org/jira/browse/QPID-7186) - CancelledKeyException from the accepting thread during Broker shutdown
 - [QPID-7189](https://issues.apache.org/jira/browse/QPID-7189) - [Java Client 0-8..0-10] Client fails to negotiate AMQP connection after downgrading from 0-10 to 0-91
 - [QPID-7195](https://issues.apache.org/jira/browse/QPID-7195) - Ensure socket is closed if Socket#connect times out or fails
 - [QPID-7196](https://issues.apache.org/jira/browse/QPID-7196) - [Java Broker] ConcurrentModificationException can occur on Broker startup when virtual host is activated
 - [QPID-7203](https://issues.apache.org/jira/browse/QPID-7203) - Model loses audit information 
 - [QPID-7208](https://issues.apache.org/jira/browse/QPID-7208) - Failure to add a certificate to a managed truststore not reported a second time in some browsers
 - [QPID-7223](https://issues.apache.org/jira/browse/QPID-7223) - [Java Broker] Broker does not decrement consumer statistics "unacknowledgedBytes" and "unacknowledgedMessages" after receiving message.release command for 0.10 AMQP protocol
 - [QPID-7224](https://issues.apache.org/jira/browse/QPID-7224) - Exposed truststores should exclude/include based on virtualhostnode rather than virtualhost
 - [QPID-7226](https://issues.apache.org/jira/browse/QPID-7226) - [Java Broker] [BDB HA] BDBHAVirtualHostNodeTest.testIntruderConnected test failed with ReplicaConsistencyException 
 - [QPID-7231](https://issues.apache.org/jira/browse/QPID-7231) - Example of REST call to invoke the Queue clear queue operation is incorrect
 - [QPID-7237](https://issues.apache.org/jira/browse/QPID-7237) - Excessive threads creation when suspending/resuming flow
 - [QPID-7253](https://issues.apache.org/jira/browse/QPID-7253) - [Java Client 0-10] Application allowed to create new JMS session whilst failover is in progress
 - [QPID-7257](https://issues.apache.org/jira/browse/QPID-7257) - [CVE-2016-4432] [Java Broker] Prevent possibility of by-passed authentication in AMQP 0-8..0-10 protocol implementations
 - [QPID-7267](https://issues.apache.org/jira/browse/QPID-7267) - [Java Broker] Content-Length header is set incorrectly when using compression
 - [QPID-7268](https://issues.apache.org/jira/browse/QPID-7268) - message sent over 0-10 can't be received over 1.0
 - [QPID-7269](https://issues.apache.org/jira/browse/QPID-7269) - broker issues disposition for delivery that is already settled
 - [QPID-7270](https://issues.apache.org/jira/browse/QPID-7270) - [Java Broker] Fix broker side TLS cipher suite order
 - [QPID-7271](https://issues.apache.org/jira/browse/QPID-7271) - [CVE-2016-3094] Prevent DoS within PlainSaslServer
 - [QPID-7273](https://issues.apache.org/jira/browse/QPID-7273) - The same JVM property names are used on client and broker sides for setting protocol and cipher suite white and black lists
 - [QPID-7278](https://issues.apache.org/jira/browse/QPID-7278) - [Java Broker] broker crashes when creating a JDBC VirtualHost with invalid JDBC Url
 - [QPID-7279](https://issues.apache.org/jira/browse/QPID-7279) - [Java Broker] with config encryption creating a JDBC VirtualHost fails
 - [QPID-7282](https://issues.apache.org/jira/browse/QPID-7282) - Java Broker should always send server-final message (if required) to the client on succesful SASL negotiation
 - [QPID-7287](https://issues.apache.org/jira/browse/QPID-7287) - Query parser fails silently with expression such as a + b
 - [QPID-7288](https://issues.apache.org/jira/browse/QPID-7288) - Dgrid flicker during refreshes
 - [QPID-7297](https://issues.apache.org/jira/browse/QPID-7297) - [Java Client] Using socket:// address to supply a preexisting existing socket to the client fails on the 0-10 path
 - [QPID-7298](https://issues.apache.org/jira/browse/QPID-7298) - [Java Broker] [0-8..0-91] Broker sends unsolicited ExchangeDeclareOk in response to declares of exchanges with reserved names 
 - [QPID-7299](https://issues.apache.org/jira/browse/QPID-7299) - [Web Management Console] Usabiity issues with new dgrid data tables
 - [QPID-7301](https://issues.apache.org/jira/browse/QPID-7301) - [Java Client] [Java Broker] JMS Selector parsing will not fail if a valid selector is followed by invalid text
 - [QPID-7313](https://issues.apache.org/jira/browse/QPID-7313) - [Java Broker] Connection close REST request can hang when client application does not reply with ConnectionCloseOk to broker ConnectionClose command
 - [QPID-7320](https://issues.apache.org/jira/browse/QPID-7320) - Management actor missing from operational logs
 - [QPID-7327](https://issues.apache.org/jira/browse/QPID-7327) - [Java Broker] Deleting Redirector VirtualHost results in IllegalStateException
 - [QPID-7328](https://issues.apache.org/jira/browse/QPID-7328) - [Java Broker, WMC] The Help Menu link in the WMC is broken
 - [QPID-7342](https://issues.apache.org/jira/browse/QPID-7342) - [Java Broker] ForbiddingAuthorisationFilter carelessly matches request paths
 - [QPID-7347](https://issues.apache.org/jira/browse/QPID-7347) - [Java Broker, WMC] Opening a BDBHA Replica VirtualHost tab results in a 404 error
 - [QPID-7363](https://issues.apache.org/jira/browse/QPID-7363) - [Java Broker] Unhandled 'Message store is not open exception' during Broker shutdown
 - [QPID-7368](https://issues.apache.org/jira/browse/QPID-7368) - CancelledKeyException from accepting socket during Broker shutdown
 - [QPID-7382](https://issues.apache.org/jira/browse/QPID-7382) - Message dialogue tries to inline the text of a text message content regardless of the its length
 - [QPID-7386](https://issues.apache.org/jira/browse/QPID-7386) - [Java Broker, WMC] Session Cookie should set the HttpOnly flag
 - [QPID-7387](https://issues.apache.org/jira/browse/QPID-7387) - [Java Broker, AMQP 0-8..0-91] Correct handling of consumer credit
 - [QPID-7394](https://issues.apache.org/jira/browse/QPID-7394) - [0-8..0-91] Prefetch accounting incorrect when session rolled back / recovered
 - [QPID-7398](https://issues.apache.org/jira/browse/QPID-7398) - [Java Broker] Initialise UserPreference object for new ConfiguredObjects
 - [QPID-7401](https://issues.apache.org/jira/browse/QPID-7401) - [Java Broker] Ensure getContextValue is only called after model has been resolved
 - [QPID-7408](https://issues.apache.org/jira/browse/QPID-7408) - REST API streams compressed message content without a Content-Encoding header
 - [QPID-7412](https://issues.apache.org/jira/browse/QPID-7412) - [Java Broker] Set default max message size to 100 MB
 - [QPID-7413](https://issues.apache.org/jira/browse/QPID-7413) - [Java Broker, WMC] Fix minor defects and usability issues in query and dashboard UI
 - [QPID-7414](https://issues.apache.org/jira/browse/QPID-7414) - [Java Broker] File based authentication providers PlainPasswordFile and Base64MD5PasswordFile should guard against colons in usernames and passwords
 - [QPID-7417](https://issues.apache.org/jira/browse/QPID-7417) - [Java Broker] Ensure message instance listeners only fire on state changes of the associated object
 - [QPID-7440](https://issues.apache.org/jira/browse/QPID-7440) - [Java Broker] Stop ProtocolOutputConverterImpl from leaking QpidByteBuffers
 - [QPID-7451](https://issues.apache.org/jira/browse/QPID-7451) - [Java Broker] MessageTransferMessage should cache message size
 - [QPID-7455](https://issues.apache.org/jira/browse/QPID-7455) - [Java Broker] Object references in configuration files should be able to use context variables
 - [QPID-7456](https://issues.apache.org/jira/browse/QPID-7456) - [Java Broker, WMC] Fix edit dialogue of BDB HA VHNs
 - [QPID-7465](https://issues.apache.org/jira/browse/QPID-7465) - [Java Broker] Stop ServerEncoder on AMQP 0-10 from unnecessarily allocating ByteBuffers
 - [QPID-7474](https://issues.apache.org/jira/browse/QPID-7474) - [Java Broker] Guard against NPE in StatisticsReportingTask
 - [QPID-7477](https://issues.apache.org/jira/browse/QPID-7477) - [Java Broker] Recovery of Broker preferences should happen without holding VirtualHostPrincipal
 - [QPID-7479](https://issues.apache.org/jira/browse/QPID-7479) - [Java Broker] Memory estimation formula fails to account for objects that comprise a persistent messages
 - [QPID-7480](https://issues.apache.org/jira/browse/QPID-7480) - Incorrect error message when editing "number of connection threads" of a virtual host
 - [QPID-7481](https://issues.apache.org/jira/browse/QPID-7481) - Statistics gathering screen label uses wrong unit
 - [QPID-7482](https://issues.apache.org/jira/browse/QPID-7482) - Heartbeat screen label uses wrong units
 - [QPID-7483](https://issues.apache.org/jira/browse/QPID-7483) - [Java Broker, WMC] Address minor UI issues
 - [QPID-7485](https://issues.apache.org/jira/browse/QPID-7485) - [Java Broker] Make the path attribute immutable on file based authentication/group providers
 - [QPID-7488](https://issues.apache.org/jira/browse/QPID-7488) - [Java Broker, WMC] Clicking on any of dashboard widget titlebar icons  (collapse pane, edit, goto, or close) triggers widget dragging in IE
 - [QPID-7489](https://issues.apache.org/jira/browse/QPID-7489) - [Java Broker] Only return false from AbstractQueue#attemptDelivery if remaining messages on queue can actually be consumed
 - [QPID-7490](https://issues.apache.org/jira/browse/QPID-7490) - [Java Broker] Stop CreditCreditManager from spuriously notifying subscribers of credit increases
 - [QPID-7503](https://issues.apache.org/jira/browse/QPID-7503) - [Java Broker, Web Management Console] Query widget ignores the selection of the same conditions which are already selected on another open Query widget

## Tasks

 - [QPID-6925](https://issues.apache.org/jira/browse/QPID-6925) - [Java] Generate source bundle on releasing a new version of java components
 - [QPID-7239](https://issues.apache.org/jira/browse/QPID-7239) - [Java Broker] Apply JavaScript code style to WMC
 - [QPID-7335](https://issues.apache.org/jira/browse/QPID-7335) - [Java Broker] Ensure thread correctness of UserPreferences and PreferenceStore
 - [QPID-7341](https://issues.apache.org/jira/browse/QPID-7341) - Names such as "Apache Qpid Java" cause trademark violations
 - [QPID-7356](https://issues.apache.org/jira/browse/QPID-7356) - Change default configuration provided by initial-config.json to model version 6.1
 - [QPID-7469](https://issues.apache.org/jira/browse/QPID-7469) - [Java Broker] Improve VirtualHost#publishMessage
 - [QPID-7470](https://issues.apache.org/jira/browse/QPID-7470) - [Java Broker] Address javax.xml.bind.DatatypeConverter shortcomings
 - [QPID-7502](https://issues.apache.org/jira/browse/QPID-7502) - [Java Broker] Add documentation for Query API
