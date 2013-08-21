To build:

```bash
sudo yum -y install rpmdevtools && rpmdev-setuptree

curl https://raw.github.com/ashrithr/rpm-specs/master/storm-0.8/storm.spec -o ~/rpmbuild/SPECS/storm.spec

curl https://dl.dropbox.com/u/133901206/storm-0.8.2.zip -o ~/rpmbuild/SOURCES/storm-0.8.2.zip

curl https://raw.github.com/ashrithr/rpm-specs/master/storm-0.8/storm -o ~/rpmbuild/SOURCES/storm

curl https://raw.github.com/ashrithr/rpm-specs/master/storm-0.8/storm-niumbus -o ~/rpmbuild/SOURCES/storm-nimbus

curl https://raw.github.com/ashrithr/rpm-specs/master/storm-0.8/storm-ui -o ~/rpmbuild/SOURCES/storm-ui

curl https://raw.github.com/ashrithr/rpm-specs/master/storm-0.8/storm-supervisor -o ~/rpmbuild/SOURCES/storm-supervisor

curl https://raw.github.com/ashrithr/rpm-specs/master/storm-0.8/storm.nofiles.conf -o ~/rpmbuild/SOURCES/storm.nofiles.conf

rpmbuild -bb ~/rpmbuild/SPECS/storm.spec
```