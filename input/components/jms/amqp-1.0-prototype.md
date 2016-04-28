# Earlier AMQP 1.0 JMS Client

Before the new [Qpid JMS](index.html) AMQP 1.0 client became available, the Qpid
project offered an earlier AMQP 1.0 JMS client based on some initial prototyping work.
Its details are preserved here to support existing users during transition to the newer
client. If you are using this earlier client or just starting out, we encourage you to
look at the newer [Qpid JMS](index.html) AMQP 1.0 client.

## Download

The earlier AMQP 1.0 JMS client is released as part of {{current_release_link}}.

<div class="two-column" markdown="1">

 - [Java binary](http://archive.apache.org/dist/qpid/{{current_release}}/binaries/qpid-amqp-1-0-client-jms-{{current_release}}-bin.tar.gz)
 - [PGP signature](http://archive.apache.org/dist/qpid/{{current_release}}/binaries/qpid-amqp-1-0-client-jms-{{current_release}}-bin.tar.gz.asc)
 - [MD5 checksum](http://archive.apache.org/dist/qpid/{{current_release}}/binaries/qpid-amqp-1-0-client-jms-{{current_release}}-bin.tar.gz.md5)
 - [SHA1 checksum](http://archive.apache.org/dist/qpid/{{current_release}}/binaries/qpid-amqp-1-0-client-jms-{{current_release}}-bin.tar.gz.sha1)

</div>

## Documentation

 - [Examples](http://svn.apache.org/repos/asf/qpid/branches/{{current_release}}/qpid/java/amqp-1-0-client-jms/example)

## Maven

The earlier AMQP 1.0 JMS client is also available via Maven. Use the following depencencies:

<div class="highlight"><pre>
<span class="nt">&lt;dependency&gt;</span>
  <span class="nt">&lt;groupId&gt;</span>org.apache.qpid<span class="nt">&lt;/groupId&gt;</span>
  <span class="nt">&lt;artifactId&gt;</span>qpid-amqp-1-0-client-jms<span class="nt">&lt;/artifactId&gt;</span>
  <span class="nt">&lt;version&gt;</span>{{current_release}}<span class="nt">&lt;/version&gt;</span>
<span class="nt">&lt;/dependency&gt;</span>
<span class="nt">&lt;dependency&gt;</span>
  <span class="nt">&lt;groupId&gt;</span>org.apache.geronimo.specs<span class="nt">&lt;/groupId&gt;</span>
  <span class="nt">&lt;artifactId&gt;</span>geronimo-jms_1.1_spec<span class="nt">&lt;/artifactId&gt;</span>
  <span class="nt">&lt;version&gt;</span>1.0<span class="nt">&lt;/version&gt;</span>
<span class="nt">&lt;/dependency&gt;</span>
</pre></div>
