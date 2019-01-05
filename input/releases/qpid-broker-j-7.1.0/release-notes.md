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

# Qpid Broker-J 7.1.0 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-6933](https://issues.apache.org/jira/browse/QPID-6933) - [Broker-J][System Tests]Factor out a JMS client neutral messaging test suite from system tests
 - [QPID-7153](https://issues.apache.org/jira/browse/QPID-7153) - [Broker-J] Allow expired messages to be sent to DLQ
 - [QPID-7197](https://issues.apache.org/jira/browse/QPID-7197) - [Broker-J] Prevent deletion of objects that are in use
 - [QPID-7543](https://issues.apache.org/jira/browse/QPID-7543) - [Broker-J][WMC] Add UI for UserOrConnectionSpecific LogInclusionRule
 - [QPID-7567](https://issues.apache.org/jira/browse/QPID-7567) - [Broker-J] Select appropriate certificate for TLS based on SNIServerName
 - [QPID-7694](https://issues.apache.org/jira/browse/QPID-7694) - [Broker-J] Add 0-8..0-10 wire queue declare argument for holds on publish
 - [QPID-7873](https://issues.apache.org/jira/browse/QPID-7873) - [Broker-J] Delete store notion confused
 - [QPID-7885](https://issues.apache.org/jira/browse/QPID-7885) - [Broker-J] Support Java 9 and 11
 - [QPID-7925](https://issues.apache.org/jira/browse/QPID-7925) - [Broker-J] [WMC] Add ability to maintain rule-based access control provider for virtualhost
 - [QPID-8064](https://issues.apache.org/jira/browse/QPID-8064) - [Broker-J] FileKeyStore should validate java keystore content to make sure that private key is present
 - [QPID-8083](https://issues.apache.org/jira/browse/QPID-8083) - [Broker-J][REST] Refactor REST system test suite
 - [QPID-8085](https://issues.apache.org/jira/browse/QPID-8085) - [Broker-J][AMQP 1.0] Optimize the sending of flow performatives from broker sending link endpoint
 - [QPID-8088](https://issues.apache.org/jira/browse/QPID-8088) - [Broker-J]Pull-up bindingAdress attribute to Port
 - [QPID-8089](https://issues.apache.org/jira/browse/QPID-8089) - [Broker-J][HTTP Management] Activate dynamically added HTTP ports on creation 
 - [QPID-8091](https://issues.apache.org/jira/browse/QPID-8091) - [Broker-J] [AMQP 1.0] Store transaction timeout feature
 - [QPID-8101](https://issues.apache.org/jira/browse/QPID-8101) - [Broker-J] [Web Management Console] Add ability to close more than one connection at once
 - [QPID-8102](https://issues.apache.org/jira/browse/QPID-8102) - [Broker-J][Web Management Console] Add UI for virtual host node auto-creation policies
 - [QPID-8110](https://issues.apache.org/jira/browse/QPID-8110) - [Broker-J] Add ability to check ERRORED state of entire configured object hierarchy on broker startup
 - [QPID-8123](https://issues.apache.org/jira/browse/QPID-8123) - [Broker-J] [BDB Test] Remove compile time dependency on Qpid JMS Client AMQP 0-x
 - [QPID-8132](https://issues.apache.org/jira/browse/QPID-8132) - [Broker-J] Refresh Apache BCEL dependency to 6.2
 - [QPID-8133](https://issues.apache.org/jira/browse/QPID-8133) - [Broker-J] Refresh Commons-CLI dependency (1.4)
 - [QPID-8136](https://issues.apache.org/jira/browse/QPID-8136) - [Broker-J] Upgrade Jackson dependencies
 - [QPID-8143](https://issues.apache.org/jira/browse/QPID-8143) - [Broker-J] Properly validate @ManagedAttributeValueTypes, and allow for factory methods
 - [QPID-8147](https://issues.apache.org/jira/browse/QPID-8147) - [Broker-J] Report first 8 received bytes as part of operational log message for unsupported protocol header
 - [QPID-8150](https://issues.apache.org/jira/browse/QPID-8150) - [Broker-J] Prevent test failures due to slow initialisation of hostname resolution in HostnameAliasImpl
 - [QPID-8151](https://issues.apache.org/jira/browse/QPID-8151) - [Broker-J] Refresh mechanism that underpins unit tests
 - [QPID-8158](https://issues.apache.org/jira/browse/QPID-8158) - [Broker-J] [System Tests] Refactor BDB HA system tests
 - [QPID-8163](https://issues.apache.org/jira/browse/QPID-8163) - [Broker-J] [ACL] Owner ACL rules
 - [QPID-8166](https://issues.apache.org/jira/browse/QPID-8166) - [Broker-J] Remove use of ${QPID_HOME}/etc from default configuration
 - [QPID-8181](https://issues.apache.org/jira/browse/QPID-8181) - [Broker-J] Add statistics for a total number of connections established on AMQP port
 - [QPID-8193](https://issues.apache.org/jira/browse/QPID-8193) - [Broker-J] Updating maximum / minimum TTL on a queue does not affect messages already in the queue (until restart)
 - [QPID-8195](https://issues.apache.org/jira/browse/QPID-8195) - [Broker-J] Improve AmqpErrorException#toString
 - [QPID-8204](https://issues.apache.org/jira/browse/QPID-8204) - [Broker-J] Add statistics to report the maximum size of incoming messages
 - [QPID-8214](https://issues.apache.org/jira/browse/QPID-8214) - [Broker-J] Reduce the table names size in the JDBC configuration store to fit Oracle's 30 characters limitation
 - [QPID-8224](https://issues.apache.org/jira/browse/QPID-8224) - [Broker-J][WMC] Add UI to configure exchange unroutable message behaviour for AMQP 1.0
 - [QPID-8227](https://issues.apache.org/jira/browse/QPID-8227) - [Broker-J] Replace qpidbrokerversion.properties with jar metadata
 - [QPID-8232](https://issues.apache.org/jira/browse/QPID-8232) - [Broker-J] Disabling logging using  log level OFF is not respected by the logging framework
 - [QPID-8238](https://issues.apache.org/jira/browse/QPID-8238) - [Broker-J] Improve performance of asynchronous publishing of transient messages into topic exchange having queues bound using non-overlapping selectors 
 - [QPID-8240](https://issues.apache.org/jira/browse/QPID-8240) - [Broker-J] Detect idle connections
 - [QPID-8241](https://issues.apache.org/jira/browse/QPID-8241) - [Broker-J] Remove use of javax.xml.bind.DatatypeConverter
 - [QPID-8242](https://issues.apache.org/jira/browse/QPID-8242) - [Broker-J] JDBC store should remove message content/metadata asynchronously
 - [QPID-8243](https://issues.apache.org/jira/browse/QPID-8243) - [Broker-J] Optimize logback turbo filter implemented to provide a workaround for Logback1027
 - [QPID-8244](https://issues.apache.org/jira/browse/QPID-8244) - [Broker-J] Optimize fanout exchange routing functionality
 - [QPID-8245](https://issues.apache.org/jira/browse/QPID-8245) - [Broker-J] [AMQP 0-8..0-91] Decode FieldTable fields on demand
 - [QPID-8247](https://issues.apache.org/jira/browse/QPID-8247) - [Broker-J] Upgrade mockito to 2.x
 - [QPID-8256](https://issues.apache.org/jira/browse/QPID-8256) - [Broker-J] Update Guava to version 27.0
 - [QPID-8258](https://issues.apache.org/jira/browse/QPID-8258) - [Broker-J] Upgrade dojotoolkit to version 1.14
 - [QPID-8259](https://issues.apache.org/jira/browse/QPID-8259) - [Broker-J] Upgrade Jetty to version 9.4.12.v20180830
 - [QPID-8260](https://issues.apache.org/jira/browse/QPID-8260) - [Broker-J] Add support for provided preferences store into Derby and JDBC system configs
 - [QPID-8261](https://issues.apache.org/jira/browse/QPID-8261) - [Broker-J] Change broker model version to 7.1

## Bugs fixed

 - [QPID-7541](https://issues.apache.org/jira/browse/QPID-7541) - [Broker-J] Close Consumers when a Queue is deleted
 - [QPID-7642](https://issues.apache.org/jira/browse/QPID-7642) - [Broker-J] Create binding operations on exchanges should fail when invalid selector is provided as part of binding arguments
 - [QPID-7830](https://issues.apache.org/jira/browse/QPID-7830) - [Broker-J] Heap dominated by duplicates of common routing values / header values etc
 - [QPID-7948](https://issues.apache.org/jira/browse/QPID-7948) - [Broker-J] [AMQP0-9] [Publish Confirms] Client hangs if message sent to topic within no subscribers
 - [QPID-7996](https://issues.apache.org/jira/browse/QPID-7996) - [Broker-J] Make operations regarding link registry thread safe
 - [QPID-8014](https://issues.apache.org/jira/browse/QPID-8014) - [Broker-J][WMC] Loading of WMC fails on systems with high CPU usage
 - [QPID-8066](https://issues.apache.org/jira/browse/QPID-8066) - [Broker-J] Virtual host logger rules are left over in configuration store after deletion of virtual host logger on provided virtual host causing virtualhost restart failure
 - [QPID-8067](https://issues.apache.org/jira/browse/QPID-8067) - [Broker-J] Default queue filter for arrival time with non-zero replay period does not filter messages as documented
 - [QPID-8081](https://issues.apache.org/jira/browse/QPID-8081) - [Broker-J] FileLogger with "roll on restart" set to "true" does not roll log file on broker restart when "roll daily" is "true"
 - [QPID-8096](https://issues.apache.org/jira/browse/QPID-8096) - [Broker-J] PUTting a user preference to the BDB backed configuration store fails with NPE
 - [QPID-8098](https://issues.apache.org/jira/browse/QPID-8098) - [Broker-J] [AMQP 0-10] Queue browsers erroneously increment the delivery count
 - [QPID-8099](https://issues.apache.org/jira/browse/QPID-8099) - [Broker-J] [AMQP Management] Operation Queue#getMessageInfo response returned as serialised java object rather list of maps
 - [QPID-8100](https://issues.apache.org/jira/browse/QPID-8100) - [Broker-J] [AMQP 0-10] SESSION_BUSY sent on wrong channel leading to hung Messaging API based application
 - [QPID-8106](https://issues.apache.org/jira/browse/QPID-8106) - [Broker-J] [Alternate Binding] On virtualhost recovery, message "Gave up waiting for Queue 'xxxx' to attain state" written to the log and startup delayed 
 - [QPID-8114](https://issues.apache.org/jira/browse/QPID-8114) - [Broker-J] Attempting to use an unknown filter type incorrectly causes connection closure with a decode error
 - [QPID-8117](https://issues.apache.org/jira/browse/QPID-8117) - [Broker-J] Table prefix of JDBC Virtual Host Node is ignored by preferences store
 - [QPID-8137](https://issues.apache.org/jira/browse/QPID-8137) - [Broker-J] NPE is reported into broker logs on broker shutdown/restart when AMQP port is in ERRORED state due to port being bound by other process
 - [QPID-8140](https://issues.apache.org/jira/browse/QPID-8140) - [Broker-J][BDB HA] Removal of non existing group member can end up in broker crash due to uncaught MemberNotFoundException
 - [QPID-8156](https://issues.apache.org/jira/browse/QPID-8156) - [Broker-J] Heap memory is leaked on deletion of virtual host node
 - [QPID-8157](https://issues.apache.org/jira/browse/QPID-8157) - [Broker-J] Deletion of Virtual Host Node fails to clean-up properly all Virtual Host/Virtual Host Node resources
 - [QPID-8160](https://issues.apache.org/jira/browse/QPID-8160) - [Broker-J] [AMQP 1.0] AccessControlException when creating sending link reported as  amqp:internal-error rather than amqp:unauthorised-access
 - [QPID-8164](https://issues.apache.org/jira/browse/QPID-8164) - [Broker-J] [AMQP 1.0] [BINDMAP] Dynamic nodes created with the temporary-queue capability do not enforce connection exclusivity
 - [QPID-8165](https://issues.apache.org/jira/browse/QPID-8165) - [Broker-J][WMC] Validation of configured object names is too restrictive in Web Management Console
 - [QPID-8167](https://issues.apache.org/jira/browse/QPID-8167) - [Broker-J] Broker command line option '-mmqv/--management-mode-quiesce-virtualhosts' does not quiesce virtual hosts
 - [QPID-8171](https://issues.apache.org/jira/browse/QPID-8171) - [Broker-J] Failed to start broker under Windows when QPID_JAVA_GC is set 
 - [QPID-8172](https://issues.apache.org/jira/browse/QPID-8172) - [Broker-J] OAuth2 authentication provider should not mandate setting of client secret
 - [QPID-8182](https://issues.apache.org/jira/browse/QPID-8182) - [Broker-J] [Message Conversion] Message id fidelity lost when converting from AMQP 1.0 to 0-10 when message-id-string carries a ID: prefixed UUID
 - [QPID-8191](https://issues.apache.org/jira/browse/QPID-8191) - [Broker-J][WMC] Memory logger logs are not displayed in the log viewer UI
 - [QPID-8192](https://issues.apache.org/jira/browse/QPID-8192) - [Broker-J] Make bindingKey parameter mandatory in exchange bind/unbind operations
 - [QPID-8194](https://issues.apache.org/jira/browse/QPID-8194) - [Broker-J][Protocol Tests] [AMQP 1.0] TransferTests seen to fail on Windows
 - [QPID-8196](https://issues.apache.org/jira/browse/QPID-8196) - [Broker-J] [WMC] Edit form controls are not populated with current values
 - [QPID-8198](https://issues.apache.org/jira/browse/QPID-8198) - [Broker-J][Documentation] Account headers in formula for estimation of heap size
 - [QPID-8199](https://issues.apache.org/jira/browse/QPID-8199) - [Broker-J] Fix description for bind/unbind operations
 - [QPID-8201](https://issues.apache.org/jira/browse/QPID-8201) - [Broker-J] [AMQP1.0] Queue backing temporary subscription deleted twice during link close
 - [QPID-8202](https://issues.apache.org/jira/browse/QPID-8202) - [Broker-J][AMQP 0-8...0-91] Large flowed to disk message can be re-loaded from store for every content chunk sent to the client
 - [QPID-8203](https://issues.apache.org/jira/browse/QPID-8203) - [Broker-J][AMQP 0-8...0-91] [CVE-2018-8030] Denial of Service Vulnerability when AMQP 0-8...0-91 messages exceed maximum size limit
 - [QPID-8213](https://issues.apache.org/jira/browse/QPID-8213) - [Broker-J] InputStream is not closed in SSLUtil#readCertificates(URL) 
 - [QPID-8215](https://issues.apache.org/jira/browse/QPID-8215) - [Broker-J] The link-store fails to create its tables with Sybase
 - [QPID-8216](https://issues.apache.org/jira/browse/QPID-8216) - [Broker-J] Operational log message CHN-1011 about moving message to dead letter queue is not reported
 - [QPID-8219](https://issues.apache.org/jira/browse/QPID-8219) - [Broker-J] Authentication results are cached in SimpleLdap and OAUTH2 authentication providers per connection basis
 - [QPID-8223](https://issues.apache.org/jira/browse/QPID-8223) - [Broker-J] [AMQP 1.0] Broker can stop delivering messages when sending link delivery-count value exceeds Integer.MAX_VALUE, wraps around and turns negative
 - [QPID-8225](https://issues.apache.org/jira/browse/QPID-8225) - [Broker-J][AMQP 0-10] stops delivering queue/consumer messages after 4 GB data transfer
 - [QPID-8230](https://issues.apache.org/jira/browse/QPID-8230) - [Broker-J] Virtual Host children can be partially recovered and left in memory on failed Virtual Host startup
 - [QPID-8231](https://issues.apache.org/jira/browse/QPID-8231) - [Broker-J] [AMQP 0-8...0-9-1] Broker crashes on delivery of messages from queue having attribute 'messageGroupKeyOverride' set to an empty string
 - [QPID-8233](https://issues.apache.org/jira/browse/QPID-8233) - [Broker-J][AMQP 1.0] Failure on connecting to a virtual host which is not yet active should use connection-forced error
 - [QPID-8236](https://issues.apache.org/jira/browse/QPID-8236) - [Broker-J] [BDB HA] Changing of group name, address or node name in BDB HA virtual host node should be disallowed 
 - [QPID-8253](https://issues.apache.org/jira/browse/QPID-8253) - [Broker-J] NPE is thrown in QpidBestFitX509KeyManager when null is returned from SSLEngine.getSSLParameters().getServerNames()
 - [QPID-8254](https://issues.apache.org/jira/browse/QPID-8254) - [Broker-J] Illegal ascii characters are used in keystore passwords
 - [QPID-8257](https://issues.apache.org/jira/browse/QPID-8257) - [Broker-J] Sybase message store not supporting empty messages
 - [QPID-8264](https://issues.apache.org/jira/browse/QPID-8264) - [Broker-J] ClassCastException are thrown on creation and update of VirtualHostUserOrConnectionLogInclusionRule
