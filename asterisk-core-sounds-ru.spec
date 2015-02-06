%undefine __find_provides
%undefine __find_requires

Summary:	Russian sound files for the Asterisk PBX and telephony application and toolkit
Name:		asterisk-core-sounds-ru
Version:	1.4.22
Release:	2
License:	Public Domain
Group:		System/Servers
URL:		http://www.asterisk.org/
#for FMT in alaw g722 g729 gsm sln16 ulaw wav siren7 siren14; do wget -P SOURCES/ -c http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-${FMT}-1.4.17.tar.gz ; done
Source0:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-alaw-%{version}.tar.gz
Source1:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-g722-%{version}.tar.gz
Source2:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-g729-%{version}.tar.gz
Source3:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-gsm-%{version}.tar.gz
Source4:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-siren7-%{version}.tar.gz
Source5:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-siren14-%{version}.tar.gz
Source6:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-sln16-%{version}.tar.gz
Source7:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-ulaw-%{version}.tar.gz
Source8:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-wav-%{version}.tar.gz
Requires:	asterisk
Provides:	asterisk-core-sounds = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Asterisk is an Open Source PBX and telephony development platform that can both
replace a conventional PBX and act as a platform for developing custom
telephony applications for delivering dynamic content over a telephone
similarly to how one can deliver dynamic content through a web browser using
CGI and a web server.
 
Asterisk talks to a variety of telephony hardware including BRI, PRI, POTS, and
IP telephony clients using the Inter-Asterisk eXchange protocol (e.g. gnophone
or miniphone).

This package contains freely usable recorded sounds that were meant to be used
with Asterisk in the following formats: a-Law, G.722, G.729, GSM, Siren7, 
Siren14, sln16, mu-Law, WAV

%prep

%setup -q -c -T -n asterisk-core-sounds-%{version} -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8

# fix dir perms
find . -type d | xargs chmod 755
    
# fix file perms
find . -type f | xargs chmod 644

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}/var/lib/asterisk/sounds/en

cp -aRf * %{buildroot}/var/lib/asterisk/sounds/en

# cleanup
#rm -f %{buildroot}%{_datadir}/asterisk/sounds/*-asterisk-core-*-%{version}

# make a file list
find %{buildroot}/var/lib/asterisk/sounds/en -type f | sed -e "s|%{buildroot}||" | sed -e 's/^/%attr(0644,root,root) /' >> %{name}.filelist

%clean
rm -rf %{buildroot}

%files -f %{name}.filelist
%defattr(-,root, root)
%doc *-asterisk-core-*-%{version}


%changelog
* Thu Jul 19 2012 Lonyai Gergely <aleph@mandriva.org> 1.4.22-1mdv2012.0
+ Revision: 810201
- 1.4.22

* Fri Jun 03 2011 Lonyai Gergely <aleph@mandriva.org> 1.4.21-1
+ Revision: 682581
- initial release
  1.4.21
- create asterisk-core-sounds-ru

