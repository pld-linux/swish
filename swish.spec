Summary: Simple Web Indexing System for Humans 
Name: swish
Version: 1.1
Release: 5
Source: http://web.eit.com/software/swish/src/swish.11.tar.Z
URL: http://web.eit.com/software/swish/
Group: Utilities/Text
Copyright: GPL
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
mkdir -p  $RPM_BUILD_ROOT/usr/bin
install -m 755 swish $RPM_BUILD_ROOT/usr/bin

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES sample.swish swish.conf test.html
%doc docs
/usr/bin/swish

%changelog
* Wed Mar 24 1999 Peter Hanecak <hanecak@megaloman.sk>
- changes to allow non-root users to build too

* Mon Oct 12 1998 Michael Maher <mike@redhat.com>
- good enough spec file.

* Tue May 19 1998 Michael Maher <mike@redhat.com>
- checked package and rebuilt it.  
- added buildroot

* Mon Feb 16 1998 Otto Hammersmith <otto@redhat.com>
- tweaked description

* Fri Jan 23 1998 Otto Hammersmith <otto@redhat.com>
- built the package
