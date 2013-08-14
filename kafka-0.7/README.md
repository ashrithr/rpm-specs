To build:

```bash
sudo yum -y install rpmdevtools && rpmdev-setuptree

curl https://raw.github.com/ashrithr/rpm-specs/master/kafka-0.7/kafka.spec -o ~/rpmbuild/SPECS/kafka.spec

curl http://mirror.symnds.com/software/Apache/incubator/kafka/kafka-0.7.2-incubating/kafka-0.7.2-incubating-src.tgz -o ~/rpmbuild/SOURCES/kafka-0.7.2-incubating-src.tgz

curl https://raw.github.com/ashrithr/rpm-specs/master/kafka-0.7/kafka -o ~/rpmbuild/SOURCES/kafka

curl https://raw.github.com/ashrithr/rpm-specs/master/kafka-0.7/kafka-server -o ~/rpmbuild/SOURCES/kafka-server

curl https://raw.github.com/ashrithr/rpm-specs/master/kafka-0.7/kafka.nofiles.conf -o ~/rpmbuild/SOURCES/kafka.nofiles.conf

rpmbuild -bb ~/rpmbuild/SPECS/kafka.spec
```