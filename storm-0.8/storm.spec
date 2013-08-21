%define storm_name storm
%define storm_branch 0.8
%define storm_version 0.8.2
%define release_version 1
%define storm_home /opt/%{storm_name}-%{storm_version}
%define etc_storm /etc/%{name}
%define config_storm %{etc_storm}/conf
%define storm_user storm
%define strom_group storm

Name: %{storm_name}
Version: %{storm_version}
Release: %{release_version}
Summary: Storm Complex Real Time Event Processing.
License: EPLv1
URL: http://storm-project.net
Group: Development/Libraries
Source0: %{storm_name}-%{storm_version}.zip
Source1: storm-nimbus
Source2: storm-ui
Source3: storm-supervisor
Source4: storm
Source5: storm.nofiles.conf
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Provides: storm
Packager: Ankus <ankus@cloudwick.com>
BuildArch: noarch

%description
Storm is a distributed realtime computation system.
Similar to how Hadoop provides a set of general primitives for doing batch processing,
Storm provides a set of general primitives for doing realtime computation. Storm is simple,
can be used with any programming language, is used by many companies, and is a lot of fun to use!

The Rationale page on the wiki explains what Storm is and why it was built.
This presentation is also a good introduction to the project.

Storm has a website at storm-project.net.

%package nimbus
Summary: The Storm Nimbus node manages the Storm cluster.
Group: System/Daemons
Requires: %{name} = %{version}-%{release}, jzmq
BuildArch: noarch
%description nimbus
Nimbus is responsible for distributing code around the Storm cluster, assigning
tasks to machines, and monitoring for failures.

%package ui
Summary: The Storm UI exposes metrics for the Storm cluster.
Group: System/Daemons
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description ui
The Storm UI exposes metrics on a web interface on port 8080 to give you
a high level view of the cluster.

%package supervisor
Summary: The Storm Supervisor is a worker process of the Storm cluster.
Group: System/Daemons
Requires: %{name} = %{version}-%{release}, jzmq
BuildArch: noarch
%description supervisor
The Supervisor listens for work assigned to its machine and starts and stops
worker processes as necessary based on what Nimbus has assigned to it.

%prep
%setup -n %{storm_name}-%{storm_version}

%build
echo 'log4j.rootLogger=INFO, R
log4j.appender.R=org.apache.log4j.RollingFileAppender
log4j.appender.R.File=${storm.home}/logs/${logfile.name}
log4j.appender.R.MaxFileSize=50MB
log4j.appender.R.MaxBackupIndex=10
log4j.appender.R.layout=org.apache.log4j.PatternLayout
log4j.appender.R.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} %c{1} [%p] %m%n' ./conf/storm.log.properties

%clean
rm -rf %{buildroot}

%install
pwd
mkdir -p %{buildroot}/%{storm_home}/
mkdir -p %{buildroot}/%{storm_home}/conf/
mkdir -p %{buildroot}/%{storm_home}/lib/
mkdir -p %{buildroot}/%{storm_home}/log4j/
mkdir -p %{buildroot}/%{storm_home}/bin/
mkdir -p %{buildroot}/%{storm_home}/logs/
mkdir -p %{buildroot}/%{storm_home}/public/
mkdir -p %{buildroot}/%{_initrddir}
mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig/
mkdir -p %{buildroot}/%{_sysconfdir}/security/limits.d/
mkdir -p %{buildroot}/var/log/
mkdir -p %{buildroot}/%{etc_storm}
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/var/run/storm/
mkdir -p %{buildroot}/%{storm_home}/local/

cp -r %{_builddir}/%{storm_name}-%{storm_version}/*.jar        %{buildroot}/%{storm_home}/
cp -r %{_builddir}/%{storm_name}-%{storm_version}/bin          %{buildroot}/%{storm_home}/
cp -r %{_builddir}/%{storm_name}-%{storm_version}/conf         %{buildroot}/%{storm_home}/
cp -r %{_builddir}/%{storm_name}-%{storm_version}/lib          %{buildroot}/%{storm_home}/
cp -r %{_builddir}/%{storm_name}-%{storm_version}/log4j        %{buildroot}/%{storm_home}/
cp -r %{_builddir}/%{storm_name}-%{storm_version}/public       %{buildroot}/%{storm_home}/
cp -r %{_builddir}/%{storm_name}-%{storm_version}/project      %{buildroot}/%{storm_home}/
cp %{_builddir}/%{storm_name}-%{storm_version}-beta1-src/sbt   %{buildroot}/%{storm_home}/

cd %{buildroot}/opt/
ln -s %{storm_name}-%{storm_version} %{storm_name}
cd -

cd %{buildroot}/%{etc_storm}
ln -s %{storm_home}/conf conf
cd -

cp %_sourcedir/storm-numbus       %{buildroot}/%{_initrddir}/storm-nimbus
cp %_sourcedir/storm-ui           %{buildroot}/%{_initrddir}/storm-ui
cp %_sourcedir/storm-supervisor   %{buildroot}/%{_initrddir}/storm-supervisor
cp %_sourcedir/storm              %{buildroot}/%{_sysconfdir}/sysconfig/storm
cp %_sourcedir/storm.nofiles.conf %{buildroot}/%{_sysconfdir}/security/limits.d/storm.nofiles.conf

cd %{buildroot}/usr/bin
ln -s %{storm_home}/bin/%{storm_name} %{storm_name}
cd -

cd %{buildroot}/var/log/
ln -s %{storm_home}/logs %{storm_name}
cd -

echo 'storm.local.dir: "/opt/storm/local/"' >> %{buildroot}/%{storm_home}/conf/storm.yaml.example

%pre
getent group %{storm_group} >/dev/null || groupadd -r %{storm_group}
getent passwd %{storm_user} >/dev/null || /usr/sbin/useradd --comment "Storm Daemon User" --shell /bin/bash -M -r -g %{storm_group} --home %{storm_home} %{storm_user}

%files
%defattr(-,%{storm_user},%{storm_group})
/opt/%{storm_name}
%{storm_home}
%{storm_home}/*
%{storm_home}/bin/*.properties
%attr(755,%{storm_user},%{storm_group}) %{storm_home}/bin/*
/etc/storm/
/var/log/*
/var/run/storm/
/usr/bin/storm
/etc/sysconfig/storm
/etc/security/limits.d/storm.nofiles.conf

%post
chkconfig --add %{storm_name}-nimbus
chkconfig --add %{storm_name}-ui
chkconfig --add %{storm_name}-supervisor
%preun
service %{storm_name}-nimbus stop > /dev/null 2>&1
service %{storm_name}-ui stop > /dev/null 2>&1
service %{storm_name}-supervisor stop > /dev/null 2>&1
chkconfig --del %{storm_name}-nimbus
chkconfig --del %{storm_name}-ui
chkconfig --del %{storm_name}-supervisor
%postun
service %{storm_name}-nimbus condrestart >/dev/null 2>&1
service %{storm_name}-ui condrestart >/dev/null 2>&1
service %{storm_name}-supervisor condrestart >/dev/null 2>&1

%changelog
* Sun Jun 03 2012 Ankus <ankus@cloudwick.com> [0.8.2-1]
- Initial Build Release 0.8.2.