Summary:	Simple Web Indexing System for Humans
Summary(pl):	Prosty system indeksowania stron WWW
Name:		swish
Version:	1.1
Release:	5
License:	GPL
Group:		Applications/Text
Source0:	http://web.eit.com/software/swish/src/%{name}.11.tar.Z
URL:		http://web.eit.com/software/swish/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SWISH stands for Simple Web Indexing System for Humans. With it, you
can index directories of files and search the generated indexes.

%description -l pl
SWISH (Simple Web Indexing System for Humans) to prosty system
indeksowania stron WWW. Pozwala indeksowaæ katalogi plików i
przeszukiwaæ wygenerowane indeksy.

%prep
%setup -q -n swish.11

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install swish $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README CHANGES

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz CHANGES.gz sample.swish swish.conf test.html docs
%attr(755,root,root) %{_bindir}/swish
