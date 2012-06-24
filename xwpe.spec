Summary:	X Windows Programming Environment
Summary(de):	X-Windows-Programmierumgebung
Summary(fr):	Environnement de programmation X Window
Summary(tr):	X Windows program geli�tirme ortam�
Name:		xwpe
Version:	1.5.26a
Release:	1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	http://www.identicalsoftware.com/xwpe/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.identicalsoftware.com/xwpe/
Buildrequires:	gpm-devel
Buildrequires:	ncurses-devel >= 5.1
Buildrequires:	XFree86-devel
Buildrequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XWPE is actually a package of four programs: we, wpe, xwe, and xwpe.
They are different versions of the same basic programmers editor and
development environment. If you have used some of the Microsoft
Windows programming IDE's and longed for an X Windows equivalent, this
is what you have been looking for! Also included are the text-mode
equivalents of the X programs, enabling you to use xwpe no matter what
your development environment may be.

%description -l de
XWPE sind eigentlich 4 Programme: we, wpe, xwe und xwpe. Dies sind
verschiedene Versionen desselben elementaren Programmeditors und
derselben Entwicklungsumgebung. Wenn Sie bereits mit manchen der
Micro$oft-Windows-Programmier-IDEs gearbeitet und sich nach einem X-
Windows-�quivalent gesehnt haben, dann ist das hier die L�sung f�r
Sie! Ebenfalls eingeschlossen sind die Textmodus-�quivalente der
X-Programme, so da� Sie xwpe benutzen k�nnen, unabh�ngig davon, in
welcher Entwicklungsumgebung sie arbeiten.

%description -l fr
xwpe is un paquetage de quatre programmes : we, wpe, xwe et xwpe. Ce
sont des versions diff�rentes du m�me �diteur et environnement de
d�veloppement. Si vous avez d�j� utilis� les environnements de
programmation de Micro$oft Windows et que vous recherchiez un
�quivalent sous X, vous l'avez trouv� ! Il y a aussi les �quivalents
en mode texte des programmes X, ce qui vous permet d'utiliser xwpe
quel que soit votre environnement de d�veloppement.

%description -l tr
XWPE, Micro$oft Windows'da bulunan benzerleri gibi, bir metin
d�zenleyici ve t�mle�ik bir geli�tirme ortam� sunan bir yaz�l�md�r. Bu
pakettekiler metin ekranda �al��an s�r�mleri bulundurmaktad�r.

%package X11
Summary:	X Windows Programming Environment - X11 programs
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Prereq:		xwpe

%description X11
Includes the 'xwpe' and 'xwe' programs from the xwpe package that are
specific to X Windows.

%description -l de X11
Beinhaltet die 'xwpe'- und 'xwe'-Programme aus dem xwpe-Paket, die
X-Windows-spezifisch sind.

%description -l tr X11
X Window alt�nda �al��an t�mle�ik geli�tirme ortam� yaz�l�mlar�.

%prep
%setup -q
%patch0 -p1

%build
autoconf
CFLAGS="-I%{_includedir}/ncurses %{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}" 
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Development

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Development

gzip -9nf README CHANGELOG

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/we
%attr(755,root,root) %{_bindir}/wpe
%dir %{_libdir}/xwpe
%{_libdir}/xwpe/help.key
%{_libdir}/xwpe/help.xwpe
%{_libdir}/xwpe/syntax_def
%attr(755,root,root) %{_libdir}/xwpe/libxwpe-term.so
%{_mandir}/man1/wpe.1*
%{_mandir}/man1/we.1*
%{_mandir}/man1/xwpe.1*
%{_mandir}/man1/xwe.1*
%lang(de) %{_mandir}/de/man1/xwpe.1*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xwe
%attr(755,root,root) %{_bindir}/xwpe
%attr(755,root,root) %{_libdir}/xwpe/libxwpe-x11.so
%{_applnkdir}/Development/*
