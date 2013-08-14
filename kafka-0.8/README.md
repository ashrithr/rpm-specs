To build:

```bash
sudo yum -y install rpmdevtools && rpmdev-setuptree

curl https://raw.github.com/ashrithr/rpm-specs/master/kafka-0.8/kafka.spec -o ~/rpmbuild/SPECS/kafka.spec

curl https://dist.apache.org/repos/dist/release/kafka/kafka-0.8.0-beta1-src.tgz -o ~/rpmbuild/SOURCES/kafka-0.8.0-beta1-src.tgz

curl https://raw.github.com/ashrithr/rpm-specs/master/kafka-0.8/kafka -o ~/rpmbuild/SOURCES/kafka

curl https://raw.github.com/ashrithr/rpm-specs/master/kafka-0.8/kafka-server -o ~/rpmbuild/SOURCES/kafka-server

curl https://raw.github.com/ashrithr/rpm-specs/master/kafka-0.8/kafka.nofiles.conf -o ~/rpmbuild/SOURCES/kafka.nofiles.conf

rpmbuild -bb ~/rpmbuild/SPECS/kafka.spec
```