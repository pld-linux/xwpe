Summary: X Windows Programming Environment
Name: xwpe
%define	version	1.5.21a
Version: %{version}
Release: 1
Copyright: GPL
Url: http://www.identicalsoftware.com/xwpe
Group: Development/Tools
#
#Source: ftp://ftp.rrzn.uni-hannover.de/pub/systems/unix/xwpe/xwpe-1.4.2.tar.Z
Source: http://www.identicalsoftware.com/xwpe/xwpe-%{version}.tar.gz
Prefix: /usr
BuildRoot: /var/tmp/xwpe-root

%description
XWPE is actually a package of four programs: we, wpe, xwe, and xwpe.
They are different versions of the same basic programmers editor and
development environment. If you have used some of the Microsoft
Windows programming IDE's and longed for an X Windows equivalent, this
is what you have been looking for! Also included are the text-mode
equivalents of the X programs, enabling you to use xwpe no matter what
your development environment may be.

This package includes the basic xwpe libraries and the text-mode programs;
the X Windows programs are contained in the 'xwpe-X11' package.

%package X11
Summary: X Windows Programming Environment - X11 programs
Group: X11/Applications/Development
Requires: xwpe

%description X11

Includes the 'xwpe' and 'xwe' programs from the xwpe package that are
specific to X Windows.

%prep
%setup -q

%build
patch -p1 <xwpe-%{version}-conf.patch
autoconf
./configure --prefix=/usr
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr

make prefix=$RPM_BUILD_ROOT/usr install
( cd $RPM_BUILD_ROOT/usr/bin
  strip we
)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
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
%defattr(-,root,root)
/usr/bin/xwe
/usr/bin/xwpe
/usr/lib/xwpe/libxwpe-x11.so

%changelog
* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.5.12a.

* Thu Aug 20 1998 Jeff Johnson <jbj!redhat.com>
- update to 1.5.11a.

* Sun Jul 26 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.5.10a.

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.5.9a.

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed source and patch urls
- added URL tag

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
