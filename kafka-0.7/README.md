To build:

sudo yum -y install rpmdevtools && rpmdev-setuptree

wget https://raw.github.com/nmilford/rpm-kafka/master/kafka.spec -O ~/rpmbuild/SPECS/kafka.spec

wget http://mirror.symnds.com/software/Apache/incubator/kafka/kafka-0.7.2-incubating/kafka-0.7.2-incubating-src.tgz -O ~/rpmbuild/SOURCES/kafka-0.7.2-incubating-src.tgz

wget https://raw.github.com/nmilford/rpm-kafka/master/kafka -O ~/rpmbuild/SOURCES/kafka

wget https://raw.github.com/nmilford/rpm-kafka/master/kafka-server -O ~/rpmbuild/SOURCES/kafka-server

wget https://raw.github.com/nmilford/rpm-kafka/master/kafka.nofiles.conf -O ~/rpmbuild/SOURCES/kafka.nofiles.conf

rpmbuild -bb ~/rpmbuild/SPECS/kafka.spec