Summary:	X Windows Programming Environment
Name:		xwpe
Version:	1.5.24a
Release:	1
License:	GPL
Group:		Development/Tools
URL:		http://www.identicalsoftware.com/xwpe
#Source:	ftp://ftp.rrzn.uni-hannover.de/pub/systems/unix/xwpe/%{name}-1.4.2.tar.Z
Source:		http://www.identicalsoftware.com/xwpe/%{name}-%{version}.tar.gz
Patch:		http://www.identicalsoftware.com/xwpe/xwpe-copyfix.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XWPE is actually a package of four programs: we, wpe, xwe, and xwpe. They
are different versions of the same basic programmers editor and development
environment. If you have used some of the Microsoft Windows programming
IDE's and longed for an X Windows equivalent, this is what you have been
looking for! Also included are the text-mode equivalents of the X programs,
enabling you to use xwpe no matter what your development environment may be.

This package includes the basic xwpe libraries and the text-mode programs;
the X Windows programs are contained in the 'xwpe-X11' package.

%package X11
Summary:	X Windows Programming Environment - X11 programs
Group:		X11/Applications/Development
Requires:	xwpe

%description X11
Includes the 'xwpe' and 'xwe' programs from the xwpe package that are
specific to X Windows.

%prep
%setup -q
%patch0 -p0

%build
patch -p1 <xwpe-%{version}-conf.patch
autoconf
./configure --prefix=/usr
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr

%{__make} prefix=$RPM_BUILD_ROOT/usr install
( cd $RPM_BUILD_ROOT/usr/bin
  strip we
)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
/usr/bin/we
/usr/bin/wpe
/usr/lib/xwpe/help.key
/usr/lib/xwpe/help.xwpe
/usr/lib/xwpe/syntax_def
/usr/lib/xwpe/libxwpe-term.so
/usr/man/man1/wpe.1
/usr/man/man1/we.1
/usr/man/man1/xwpe.1
/usr/man/man1/xwe.1

%files X11
%defattr(644,root,root,755)
/usr/bin/xwe
/usr/bin/xwpe
/usr/lib/xwpe/libxwpe-x11.so
