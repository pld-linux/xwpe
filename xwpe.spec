Summary:	X Window Programming Environment
Summary(de):	X-Window-Programmierumgebung
Summary(es):	Ambiente de programaciСn X Window
Summary(fr):	Environnement de programmation X Window
Summary(pl):	╕rodowisko programistyczne pod X Window
Summary(pt_BR):	Ambiente de programaГЦo X Window
Summary(ru):	Среда разработки под X Windows
Summary(tr):	X Window program geliЧtirme ortamЩ
Summary(uk):	Середовище розробки п╕д X Windows
Name:		xwpe
Version:	1.5.29a
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://www.identicalsoftware.com/xwpe/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.identicalsoftware.com/xwpe/
BuildRequires:	autoconf
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
Windows-дquivalent gesehnt haben, dann ist das hier die LЖsung fЭr
Sie! Ebenfalls eingeschlossen sind die Textmodus-дquivalente der
X-Programme, so daъ Sie xwpe benutzen kЖnnen, unabhДngig davon, in
welcher Entwicklungsumgebung sie arbeiten.

%description -l es
XWPE es en realidad un paquete de 4 programas: we, wpe, xwe, y xwpe.
Son diferentes versiones del mismo ambiente de desarrollo y editor de
programaciСn. Si has usado algЗn de los ambientes de programaciСn del
Microsoft Windows y quieres algo equivalente en el X, acabas de
encontrar lo que buscabas. TambiИn se incluyen las versiones en modo
texto de los programas, dejando que usen el xwpe no importando el tipo
de ambiente de desarrollo que tengas. Este paquete incluye las
bibliotecas bАsicas del xwpe y los programas en modo texto; los
programas para X estАn en el paquete 'xwpe-X11'.

%description -l fr
xwpe is un paquetage de quatre programmes : we, wpe, xwe et xwpe. Ce
sont des versions diffИrentes du mЙme Иditeur et environnement de
dИveloppement. Si vous avez dИjЮ utilisИ les environnements de
programmation de Micro$oft Windows et que vous recherchiez un
Иquivalent sous X, vous l'avez trouvИ ! Il y a aussi les Иquivalents
en mode texte des programmes X, ce qui vous permet d'utiliser xwpe
quel que soit votre environnement de dИveloppement.

%description -l pl
XWPE wЁa╤ciwie skЁada siЙ z czterech programСw: we, wpe, xwe i xwpe.
S╠ to rС©ne wersje tego samego podstawowego edytora programisty i
╤rodowiska. Je©eli u©ywaЁe╤ jakiego╤ zintegrowanego ╤rodowiska
programistycznego pod MS Windows i szukasz odpowiednika pod X Window,
to jest to! ZaЁ╠czone s╠ tak©e tekstowe odpowiedniki programСw pod X,
pozwalaj╠ce u©ywaФ xwpe w ka©dym ╤rodowisku.

%description -l pt_BR
O XWPE И na verdade um pacote de 4 programas: we, wpe, xwe, e xwpe.
Eles sЦo diferentes versУes do mesmo ambiente de desenvolvimento e
editor de programaГЦo. Se vocЙ usou algum dos ambientes de programaГЦo
do Microsoft Windows e quer algo equivalente no X, vocЙ achou o que
estava procurando! TambИm estЦo incluМdos as versУes em modo texto dos
programas, deixando vocЙs usar o xwpe nЦo importando o tipo de
ambiente de desenvolvimento que tenha. Este pacote inclui as
bibliotecas bАsicas do xwpe e os programas em modo texto; os programas
para X estЦo no pacote 'xwpe-X11'.

%description -l ru
XWPE представляет собой пакет из четырех программ: we, wpe, xwe и
xwpe. Это разные версии одного и того же редактора и среды разработки.
Если вы привыкли к какой-либо среде разработки под Micro$oft Windows и
ищете что-то похожее для X Windows, этот пакет - самое оно. Также
включены текстовые эквиваленты программ для X, позволяющие
использовать xwpe в любом окружении.

%description -l tr
XWPE, Microsoft Windows'da bulunan benzerleri gibi, bir metin
dЭzenleyici ve tЭmleЧik bir geliЧtirme ortamЩ sunan bir yazЩlЩmdЩr. Bu
pakettekiler metin ekranda ГalЩЧan sЭrЭmleri bulundurmaktadЩr.

%description -l uk
XWPE - це пакет з чотирьох програм: we, wpe, xwe та xwpe. Це р╕зн╕
верс╕╖ одного й того ж редактору та середовища розробки. Якщо ви
звикли до якогось середовища розробки п╕д Micro$oft Windows ╕ шука╓те
щось схоже п╕д X Windows, то цей пакет - саме воно. Також включен╕
текстов╕ екв╕валенти програм для X, що дозволяють використовувати xwpe
у будь-якому середовищ╕.

%package X11
Summary:	X Window Programming Environment - X11 programs
Summary(es):	Ambiente de ProgramaciСn X Window - Programas X11
Summary(pl):	XWPE - programy pod X11
Summary(pt_BR):	Ambiente de ProgramaГЦo X Window - Programas X11
Group:		X11/Applications
Prereq:		xwpe

%description X11
Includes the 'xwpe' and 'xwe' programs from the xwpe package that are
specific to X Window System.

%description X11 -l de
Beinhaltet die 'xwpe'- und 'xwe'-Programme aus dem xwpe-Paket, die
X-Window-spezifisch sind.

%description X11 -l es
Incluye los programas 'xwpe' y 'xwe' del paquete xwpe que son
especМficos para X Window.

%description X11 -l pl
Pakiet zawiera programy xwpe i xwe ze ╤rodowiska xwpe - specyficzne
dla X Window System.

%description X11 -l pt_BR
Inclui os programas 'xwpe' e 'xwe' do pacote xwpe que sЦo especМficos
para X Window.

%description X11 -l tr
X Window altЩnda ГalЩЧan tЭmleЧik geliЧtirme ortamЩ yazЩlЩmlarЩ.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
CFLAGS="-I/usr/include/ncurses %{rpmcflags}"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Development,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Development
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
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
%{_pixmapsdir}/*.png
