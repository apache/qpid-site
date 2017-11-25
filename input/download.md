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

# Download

*In addition to the source artefacts below, we offer
[Qpid packages](packages.html) and [Qpid via Maven](maven.html).*

Qpid's source artefacts are produced as part of our community release
process. The downloads on this page are from our
[current releases]({{site_url}}/releases/index.html#current-releases).

It is important to [verify the integrity](#verify-what-you-download) of the files you download.

## Messaging APIs

| Content | Download | Verify |
| ------- | -------- | ------ |
| [Qpid Proton]({{site_url}}/proton/index.html) | [qpid-proton-{{current_proton_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/proton/{{current_proton_release}}/qpid-proton-{{current_proton_release}}.tar.gz) | [ASC](http://www.apache.org/dist/qpid/proton/{{current_proton_release}}/qpid-proton-{{current_proton_release}}.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/proton/{{current_proton_release}}/qpid-proton-{{current_proton_release}}.tar.gz.md5), [SHA512](http://www.apache.org/dist/qpid/proton/{{current_proton_release}}/qpid-proton-{{current_proton_release}}.tar.gz.sha512) |
| [Qpid Proton-J]({{site_url}}/proton/index.html) | [apache-qpid-proton-j-{{current_proton_j_release}}-bin.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-bin.tar.gz)\* | [ASC](http://www.apache.org/dist/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-bin.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-bin.tar.gz.md5), [SHA512](http://www.apache.org/dist/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-bin.tar.gz.sha512) |
| [Qpid JMS]({{site_url}}/components/jms/index.html) (AMQP 1.0) | [apache-qpid-jms-{{current_jms_release}}-bin.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-bin.tar.gz)\* | [ASC](http://www.apache.org/dist/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-bin.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-bin.tar.gz.md5), [SHA512](http://www.apache.org/dist/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-bin.tar.gz.sha512) |
| [Qpid JMS AMQP 0-x]({{site_url}}/components/jms/amqp-0-x.html) | [apache-qpid-jms-amqp-0-x-{{current_jms_amqp_0_x_release}}-bin.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/jms-amqp-0-x/{{current_jms_amqp_0_x_release}}/binaries/apache-qpid-jms-amqp-0-x-{{current_jms_amqp_0_x_release}}-bin.tar.gz)\* | [ASC](http://www.apache.org/dist/qpid/jms-amqp-0-x/{{current_jms_amqp_0_x_release}}/binaries/apache-qpid-jms-amqp-0-x-{{current_jms_amqp_0_x_release}}-bin.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/jms-amqp-0-x/{{current_jms_amqp_0_x_release}}/binaries/apache-qpid-jms-amqp-0-x-{{current_jms_amqp_0_x_release}}-bin.tar.gz.md5), [SHA512](http://www.apache.org/dist/qpid/jms-amqp-0-x/{{current_jms_amqp_0_x_release}}/binaries/apache-qpid-jms-amqp-0-x-{{current_jms_amqp_0_x_release}}-bin.tar.gz.sha512) |
| [Qpid Messaging API]({{site_url}}/components/messaging-api/index.html) (C++, bindings) | [qpid-cpp-{{current_cpp_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz) | [ASC](http://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.md5), [SHA512](http://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.sha512) |
| [Qpid Messaging API]({{site_url}}/components/messaging-api/index.html) (Python) | [qpid-python-{{current_python_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/python/{{current_python_release}}/qpid-python-{{current_python_release}}.tar.gz) | [ASC](http://www.apache.org/dist/qpid/python/{{current_python_release}}/qpid-python-{{current_python_release}}.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/python/{{current_python_release}}/qpid-python-{{current_python_release}}.tar.gz.md5), [SHA512](http://www.apache.org/dist/qpid/python/{{current_python_release}}/qpid-python-{{current_python_release}}.tar.gz.sha) |

## Messaging servers

| Content | Download | Verify |
| ------- | -------- | ------ |
| [Broker-J]({{site_url}}/components/broker-j/index.html) | [apache-qpid-broker-j-{{current_broker_j_release}}-bin.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/broker-j/{{current_broker_j_release}}/binaries/apache-qpid-broker-j-{{current_broker_j_release}}-bin.tar.gz)\* | [ASC](http://www.apache.org/dist/qpid/broker-j/{{current_broker_j_release}}/binaries/apache-qpid-broker-j-{{current_broker_j_release}}-bin.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/broker-j/{{current_broker_j_release}}/binaries/apache-qpid-broker-j-{{current_broker_j_release}}-bin.tar.gz.md5), [SHA512](http://www.apache.org/dist/qpid/broker-j/{{current_broker_j_release}}/binaries/apache-qpid-broker-j-{{current_broker_j_release}}-bin.tar.gz.sha512) |
| [C++ broker]({{site_url}}/components/cpp-broker/index.html) | [qpid-cpp-{{current_cpp_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz) | [ASC](http://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.md5), [SHA512](http://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.sha512) |
| [Dispatch router]({{site_url}}/components/dispatch-router/index.html) | [qpid-dispatch-{{current_dispatch_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/dispatch/{{current_dispatch_release}}/qpid-dispatch-{{current_dispatch_release}}.tar.gz) | [ASC](http://www.apache.org/dist/qpid/dispatch/{{current_dispatch_release}}/qpid-dispatch-{{current_dispatch_release}}.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/dispatch/{{current_dispatch_release}}/qpid-dispatch-{{current_dispatch_release}}.tar.gz.md5), [SHA512](http://www.apache.org/dist/qpid/dispatch/{{current_dispatch_release}}/qpid-dispatch-{{current_dispatch_release}}.tar.gz.sha512) |

\*These Java artefacts are presented as compiled bytecode.  We also
offer the source as part of our
[Qpid Proton-J source release](http://www.apache.org/dyn/closer.lua/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-src.tar.gz)
\[[ASC](http://www.apache.org/dist/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-src.tar.gz.asc),
[MD5](http://www.apache.org/dist/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-src.tar.gz.md5),
[SHA512](http://www.apache.org/dist/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-src.tar.gz.sha512)\]
and
[Qpid JMS source release](http://www.apache.org/dyn/closer.lua/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-src.tar.gz)
\[[ASC](http://www.apache.org/dist/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-src.tar.gz.asc),
[MD5](http://www.apache.org/dist/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-src.tar.gz.md5),
[SHA512](http://www.apache.org/dist/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-src.tar.gz.sha512)\]
and
[Qpid JMS AMQP 0-x source release](http://www.apache.org/dyn/closer.lua/qpid/jms-amqp-0-x/{{current_jms_amqp_0_x_release}}/apache-qpid-jms-amqp-0-x-{{current_jms_amqp_0_x_release}}-src.tar.gz)
\[[ASC](http://www.apache.org/dist/qpid/jms-amqp-0-x/{{current_jms_amqp_0_x_release}}/apache-qpid-jms-amqp-0-x-{{current_jms_amqp_0_x_release}}-src.tar.gz.asc),
[MD5](http://www.apache.org/dist/qpid/jms-amqp-0-x/{{current_jms_amqp_0_x_release}}/apache-qpid-jms-amqp-0-x-{{current_jms_amqp_0_x_release}}-src.tar.gz.md5),
[SHA512](http://www.apache.org/dist/qpid/jms-amqp-0-x/{{current_jms_amqp_0_x_release}}/apache-qpid-jms-amqp-0-x-{{current_jms_amqp_0_x_release}}-src.tar.gz.sha512)\]
and
[Qpid Broker-J source release](http://www.apache.org/dyn/closer.lua/qpid/broker-j/{{current_broker_j_release}}/apache-qpid-broker-j-{{current_broker_j_release}}-src.tar.gz)
\[[ASC](http://www.apache.org/dist/qpid/broker-j/{{current_broker_j_release}}/apache-qpid-broker-j-{{current_broker_j_release}}-src.tar.gz.asc),
[MD5](http://www.apache.org/dist/qpid/broker-j/{{current_broker_j_release}}/apache-qpid-broker-j-{{current_broker_j_release}}-src.tar.gz.md5),
[SHA512](http://www.apache.org/dist/qpid/broker-j/{{current_broker_j_release}}/apache-qpid-broker-j-{{current_broker_j_release}}-src.tar.gz.sha512)\]
and
[Qpid for Java source release](http://www.apache.org/dyn/closer.lua/qpid/java/{{current_java_release}}/qpid-java-{{current_java_release}}.tar.gz)
\[[ASC](http://www.apache.org/dist/qpid/java/{{current_java_release}}/qpid-java-{{current_java_release}}.tar.gz.asc),
[MD5](http://www.apache.org/dist/qpid/java/{{current_java_release}}/qpid-java-{{current_java_release}}.tar.gz.md5),
[SHA512](http://www.apache.org/dist/qpid/java/{{current_java_release}}/qpid-java-{{current_java_release}}.tar.gz.sha)\].

;; ## Other components
;;
;; | Content | Download | Verify |
;; | ------- | -------- | ------ |
;; | [Interop Test]({{site_url}}/components/interop-test/index.html) | [qpid-interop-test-{{current_interop_test_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/interop-test/{{current_interop_test_release}}/qpid-interop-test-{{current_interop_test_release}}.tar.gz) | [ASC](http://www.apache.org/dist/qpid/interop-test/{{current_interop_test_release}}/qpid-interop-test-{{current_interop_test_release}}.tar.gz.asc), [SHA](http://www.apache.org/dist/qpid/interop-test/{{current_interop_test_release}}/qpid-interop-test-{{current_interop_test_release}}.tar.gz.sha) |

## Verify what you download

It is essential that you verify the integrity of the downloaded files
using the ASC signatures, MD5 checksums, or SHA checksums.

The signatures can be verified using PGP or GPG. First download
the [`KEYS`](http://www.apache.org/dist/qpid/KEYS) file as well as the
`.asc` signature file for the relevant artefact. Then verify the signatures
using one of the following sets of commands.

    % gpg --import KEYS
    % gpg --verify <artifact-name>.asc

    % pgpk -a KEYS
    % pgpv <artifact-name>.asc

    % pgp -ka KEYS
    % pgp <artifact-name>.asc

Alternatively, you can verify the MD5 or SHA checksums of the
files. Unix programs called `md5sum`, `sha1sum` and `sha512sum` (or `md5`, `sha1` and
`sha512`) are included in many unix distributions.  They are also
available as part of
[GNU Coreutils](http://www.gnu.org/software/coreutils/). For
Windows users, [FSUM](http://www.slavasoft.com/fsum/) supports this.
Ensure your generated checksum string matches the string
published in the checksum file included with each release artefact.

## More information

 - [Components]({{site_url}}/components/index.html)
 - [Releases]({{site_url}}/releases/index.html)
 - [Packages](packages.html)
 - [Qpid via Maven](maven.html)
