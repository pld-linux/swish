Summary:	Simple Web Indexing System for Humans 
Name:		swish
Version:	1.1
Release:	5
Source0:	http://web.eit.com/software/swish/src/%{name}.11.tar.Z
URL:		http://web.eit.com/software/swish/
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
License:	GPL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SWISH stands for Simple Web Indexing System for Humans. With it, you
can index directories of files and search the generated indexes.

%prep
%setup -q -n swish.11

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT%{_bindir}
install -m 755 swish $RPM_BUILD_ROOT%{_bindir}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES sample.swish swish.conf test.html
%doc docs
/usr/bin/swish
