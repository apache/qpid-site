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

The downloads on this page are from our [current releases]({{site_url}}/releases/index.html#current-releases), produced as part of our community release process.
*In addition to the source artefacts below, Qpid is available via [packages](packages.html) and [Maven](maven.html).*

It is important to [verify the integrity](#verify-what-you-download) of the files you download.

## Messaging APIs

| Content | Version | Download  | More |
| ------- | ------- | --------  | ---- |
| [Qpid Proton]({{site_url}}/proton/index.html) | {{current_proton_release}} | [Source](https://www.apache.org/dyn/closer.lua?filename=qpid/proton/{{current_proton_release}}/qpid-proton-{{current_proton_release}}.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/proton/{{current_proton_release}}/qpid-proton-{{current_proton_release}}.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/proton/{{current_proton_release}}/qpid-proton-{{current_proton_release}}.tar.gz.sha512)) | [Release Page]({{current_proton_release_url}}/index.html) |
| [Qpid Proton-J]({{site_url}}/proton/index.html) | {{current_proton_j_release}} | [Source](https://www.apache.org/dyn/closer.lua?filename=qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-src.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-src.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-src.tar.gz.sha512)),  [Binary](https://www.apache.org/dyn/closer.lua?filename=qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-bin.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-bin.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-bin.tar.gz.sha512)) | [Release Page]({{current_proton_j_release_url}}/index.html), [Maven](maven.html) |
| [Qpid ProtonJ2]({{site_url}}/proton/index.html) | {{current_protonj2_release}} | [Source](https://www.apache.org/dyn/closer.lua?filename=qpid/protonj2/{{current_protonj2_release}}/apache-qpid-protonj2-{{current_protonj2_release}}-src.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/protonj2/{{current_protonj2_release}}/apache-qpid-protonj2-{{current_protonj2_release}}-src.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/protonj2/{{current_protonj2_release}}/apache-qpid-protonj2-{{current_protonj2_release}}-src.tar.gz.sha512)),  [Binary](https://www.apache.org/dyn/closer.lua?filename=qpid/protonj2/{{current_protonj2_release}}/apache-qpid-protonj2-{{current_protonj2_release}}-bin.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/protonj2/{{current_protonj2_release}}/apache-qpid-protonj2-{{current_protonj2_release}}-bin.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/protonj2/{{current_protonj2_release}}/apache-qpid-protonj2-{{current_protonj2_release}}-bin.tar.gz.sha512)) | [Release Page]({{current_protonj2_release_url}}/index.html), [Maven](maven.html) |
| [Qpid JMS]({{site_url}}/components/jms/index.html) (AMQP 1.0) | {{current_jms_release}} | [Source](https://www.apache.org/dyn/closer.lua?filename=qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-src.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-src.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-src.tar.gz.sha512)),  [Binary](https://www.apache.org/dyn/closer.lua?filename=qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-bin.tar.gz&action=download)  ([ASC](https://downloads.apache.org/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-bin.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-bin.tar.gz.sha512)) | [Release Page]({{current_jms_release_url}}/index.html), [Maven](maven.html)|
| &#160;                                                        | {{other_jms_release}} | [Source](https://www.apache.org/dyn/closer.lua?filename=qpid/jms/{{other_jms_release}}/apache-qpid-jms-{{other_jms_release}}-src.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/jms/{{other_jms_release}}/apache-qpid-jms-{{other_jms_release}}-src.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/jms/{{other_jms_release}}/apache-qpid-jms-{{other_jms_release}}-src.tar.gz.sha512)),  [Binary](https://www.apache.org/dyn/closer.lua?filename=qpid/jms/{{other_jms_release}}/apache-qpid-jms-{{other_jms_release}}-bin.tar.gz&action=download)  ([ASC](https://downloads.apache.org/qpid/jms/{{other_jms_release}}/apache-qpid-jms-{{other_jms_release}}-bin.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/jms/{{other_jms_release}}/apache-qpid-jms-{{other_jms_release}}-bin.tar.gz.sha512)) | [Release Page]({{site_url}}/releases/qpid-jms-{{other_jms_release}}/index.html), [Maven](maven.html)|
| [Qpid JMS AMQP 0-x]({{site_url}}/components/jms/amqp-0-x.html) | {{current_jms_amqp_0_x_release}} | [Source](https://www.apache.org/dyn/closer.lua?filename=qpid/jms-amqp-0-x/{{current_jms_amqp_0_x_release}}/apache-qpid-jms-amqp-0-x-{{current_jms_amqp_0_x_release}}-src.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/jms-amqp-0-x/{{current_jms_amqp_0_x_release}}/apache-qpid-jms-amqp-0-x-{{current_jms_amqp_0_x_release}}-src.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/jms-amqp-0-x/{{current_jms_amqp_0_x_release}}/apache-qpid-jms-amqp-0-x-{{current_jms_amqp_0_x_release}}-src.tar.gz.sha512)),  [Binary](https://www.apache.org/dyn/closer.lua?filename=qpid/jms-amqp-0-x/{{current_jms_amqp_0_x_release}}/binaries/apache-qpid-jms-amqp-0-x-{{current_jms_amqp_0_x_release}}-bin.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/jms-amqp-0-x/{{current_jms_amqp_0_x_release}}/binaries/apache-qpid-jms-amqp-0-x-{{current_jms_amqp_0_x_release}}-bin.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/jms-amqp-0-x/{{current_jms_amqp_0_x_release}}/binaries/apache-qpid-jms-amqp-0-x-{{current_jms_amqp_0_x_release}}-bin.tar.gz.sha512)) | [Release Page]({{current_jms_amqp_0_x_release_url}}/index.html), [Maven](maven.html) |
| [Qpid Messaging API]({{site_url}}/components/messaging-api/index.html) C++ | {{current_cpp_release}} | [Source](https://www.apache.org/dyn/closer.lua?filename=qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz&action=download)  ([ASC](https://downloads.apache.org/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.sha512)) | [Release Page]({{current_cpp_release_url}}/index.html) |
| [Qpid Messaging API]({{site_url}}/components/messaging-api/index.html) Python 2* | {{current_python_release}} | [Source](https://www.apache.org/dyn/closer.lua?filename=qpid/python/{{current_python_release}}/qpid-python-{{current_python_release}}.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/python/{{current_python_release}}/qpid-python-{{current_python_release}}.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/python/{{current_python_release}}/qpid-python-{{current_python_release}}.tar.gz.sha512)) | [Release Page]({{current_python_release_url}}/index.html) |

\* Look to the newer [Qpid Proton](http://qpid.apache.org/proton) for Python 3 and AMQP 1.0 support.

## Messaging servers

| Content | Version | Download | More |
| ------- | ------- | -------- | ---- |
| [Broker-J]({{site_url}}/components/broker-j/index.html) | {{current_broker_j_release}} | [Source](https://www.apache.org/dyn/closer.lua?filename=qpid/broker-j/{{current_broker_j_release}}/apache-qpid-broker-j-{{current_broker_j_release}}-src.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/broker-j/{{current_broker_j_release}}/apache-qpid-broker-j-{{current_broker_j_release}}-src.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/broker-j/{{current_broker_j_release}}/apache-qpid-broker-j-{{current_broker_j_release}}-src.tar.gz.sha512)),  [Binary](https://www.apache.org/dyn/closer.lua?filename=qpid/broker-j/{{current_broker_j_release}}/binaries/apache-qpid-broker-j-{{current_broker_j_release}}-bin.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/broker-j/{{current_broker_j_release}}/binaries/apache-qpid-broker-j-{{current_broker_j_release}}-bin.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/broker-j/{{current_broker_j_release}}/binaries/apache-qpid-broker-j-{{current_broker_j_release}}-bin.tar.gz.sha512)) | [Release Page]({{current_broker_j_release_url}}/index.html) |
| &#160;                                                 | {{other_broker_j_release}} | [Source](https://www.apache.org/dyn/closer.lua?filename=qpid/broker-j/{{other_broker_j_release}}/apache-qpid-broker-j-{{other_broker_j_release}}-src.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/broker-j/{{other_broker_j_release}}/apache-qpid-broker-j-{{other_broker_j_release}}-src.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/broker-j/{{other_broker_j_release}}/apache-qpid-broker-j-{{other_broker_j_release}}-src.tar.gz.sha512)),  [Binary](https://www.apache.org/dyn/closer.lua?filename=qpid/broker-j/{{other_broker_j_release}}/binaries/apache-qpid-broker-j-{{other_broker_j_release}}-bin.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/broker-j/{{other_broker_j_release}}/binaries/apache-qpid-broker-j-{{other_broker_j_release}}-bin.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/broker-j/{{other_broker_j_release}}/binaries/apache-qpid-broker-j-{{other_broker_j_release}}-bin.tar.gz.sha512)) | [Release Page]({{site_url}}/releases/qpid-broker-j-{{other_broker_j_release}}/index.html) |
| [C++ broker]({{site_url}}/components/cpp-broker/index.html) | {{current_cpp_release}} | [Source](https://www.apache.org/dyn/closer.lua?filename=qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.sha512)) | [Release Page]({{current_cpp_release_url}}/index.html) |
| [Dispatch router]({{site_url}}/components/dispatch-router/index.html) | {{current_dispatch_release}} | [Source](https://www.apache.org/dyn/closer.lua?filename=qpid/dispatch/{{current_dispatch_release}}/qpid-dispatch-{{current_dispatch_release}}.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/dispatch/{{current_dispatch_release}}/qpid-dispatch-{{current_dispatch_release}}.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/dispatch/{{current_dispatch_release}}/qpid-dispatch-{{current_dispatch_release}}.tar.gz.sha512)) | [Release Page]({{current_dispatch_release_url}}/index.html) |

## Messaging tools

| Content | Version | Download | More |
| ------- | ------- | -------- | ---- |
|[Qpid Interop Test]({{site_url}}/components/interop-test/index.html) | {{current_interop_test_release}} | [Source](https://www.apache.org/dyn/closer.lua?filename=qpid/interop-test/{{current_interop_test_release}}/qpid-interop-test-{{current_interop_test_release}}.tar.gz&action=download) ([ASC](https://downloads.apache.org/qpid/interop-test/{{current_interop_test_release}}/qpid-interop-test-{{current_interop_test_release}}.tar.gz.asc), [SHA512](https://downloads.apache.org/qpid/interop-test/{{current_interop_test_release}}/qpid-interop-test-{{current_interop_test_release}}.tar.gz.sha512)) |  [Release Page]({{current_interop_test_release_url}}/index.html) |

## Verify what you download

It is essential that you verify the integrity of the downloaded files
using the ASC signatures or SHA checksums.

The signatures can be verified using PGP or GPG. First download
the [`KEYS`](https://downloads.apache.org/qpid/KEYS) file as well as the
`.asc` signature file for the relevant artefact. Then verify the signatures
using one of the following sets of commands.

    % gpg --import KEYS
    % gpg --verify <artifact-name>.asc <artifact-name>

    % pgpk -a KEYS
    % pgpv <artifact-name>.asc

    % pgp -ka KEYS
    % pgp <artifact-name>.asc

Alternatively, you can verify the SHA checksums of the
files. Unix programs called `sha1sum` and `sha512sum` (or `sha1` and
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
