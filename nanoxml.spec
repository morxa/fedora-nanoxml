Name:           nanoxml
Version:        2.2.1
Release:        1%{?dist}
Summary:        Small XML parser for Java

License:        zlib
URL:            http://nanoxml.sourceforge.net
Source0:        https://downloads.sourceforge.net/nanoxml/NanoXML-2.2.1.tar.gz
Patch0:         %{name}.compat.patch

BuildRequires:  java-devel
Requires:       java-headless

BuildArch:      noarch

%description
NanoXML is a small non-validating parser for Java.


%package        lite
Summary:        Extremely small XML parser
BuildArch:      noarch
Requires:       java-headless

%description    lite
NanoXML/Lite is the successor of NanoXML 1. It is still extremely small (only
6KB) and now features a much faster algorithm. It is recommended if you're
currently using NanoXML 1 and don't want to adapt your code for the new API or
if you're coding applications that have to be very small (like applets or
embedded code). Please note that NanoXML/Lite has only limited functionality
(no mixed content, DTD is ignored...).


%package        sax
Summary:        SAX adaptor for nanoxml and Java
BuildArch:      noarch
Requires:       java-headless

%description    sax
NanoXML/SAX is a SAX adapter for NanoXML/Java.

%prep
%autosetup -p1 -n NanoXML-%{version}


%build
./build.sh


%install
%__install -p -D -t %{buildroot}/%{_javadir} Output/{nanoxml,nanoxml-lite,nanoxml-sax}.jar

%files
%doc Documentation/NanoXML-Java/HTML/*
%{_javadir}/nanoxml.jar

%files lite
%doc Documentation/NanoXML-Lite/HTML/*
%{_javadir}/nanoxml-lite.jar

%files  sax
%{_javadir}/nanoxml-sax.jar



%changelog
* Mon Aug 13 2018 Till Hofmann <thofmann@fedoraproject.org> - 2.2.1-1
- Initial package
