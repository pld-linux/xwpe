Summary:	X Window Programming Environment
Summary(de.UTF-8):	X-Window-Programmierumgebung
Summary(es.UTF-8):	Ambiente de programación X Window
Summary(fr.UTF-8):	Environnement de programmation X Window
Summary(pl.UTF-8):	Środowisko programistyczne pod X Window
Summary(pt_BR.UTF-8):	Ambiente de programação X Window
Summary(ru.UTF-8):	Среда разработки под X Window
Summary(tr.UTF-8):	X Window program geliştirme ortamı
Summary(uk.UTF-8):	Середовище розробки під X Window
Name:		xwpe
Version:	1.5.30a
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.identicalsoftware.com/xwpe/%{name}-%{version}.tar.gz
# Source0-md5:	11ad41d636f9ff07820ee0869a177a5c
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-dynamic.patch
URL:		http://www.identicalsoftware.com/xwpe/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XWPE is actually a package of four programs: we, wpe, xwe, and xwpe.
They are different versions of the same basic programmers editor and
development environment. If you have used some of the Microsoft
Windows programming IDE's and longed for an X Window equivalent, this
is what you have been looking for! Also included are the text-mode
equivalents of the X programs, enabling you to use xwpe no matter what
your development environment may be.

%description -l de.UTF-8
XWPE sind eigentlich 4 Programme: we, wpe, xwe und xwpe. Dies sind
verschiedene Versionen desselben elementaren Programmeditors und
derselben Entwicklungsumgebung. Wenn Sie bereits mit manchen der
Micro$oft-Windows-Programmier-IDEs gearbeitet und sich nach einem X-
Window-Äquivalent gesehnt haben, dann ist das hier die Lösung für
Sie! Ebenfalls eingeschlossen sind die Textmodus-Äquivalente der
X-Programme, so daß Sie xwpe benutzen können, unabhängig davon, in
welcher Entwicklungsumgebung sie arbeiten.

%description -l es.UTF-8
XWPE es en realidad un paquete de 4 programas: we, wpe, xwe, y xwpe.
Son diferentes versiones del mismo ambiente de desarrollo y editor de
programación. Si has usado algún de los ambientes de programación del
Microsoft Windows y quieres algo equivalente en el X, acabas de
encontrar lo que buscabas. También se incluyen las versiones en modo
texto de los programas, dejando que usen el xwpe no importando el tipo
de ambiente de desarrollo que tengas. Este paquete incluye las
bibliotecas básicas del xwpe y los programas en modo texto; los
programas para X están en el paquete 'xwpe-X11'.

%description -l fr.UTF-8
xwpe is un paquetage de quatre programmes : we, wpe, xwe et xwpe. Ce
sont des versions différentes du même éditeur et environnement de
développement. Si vous avez déjà utilisé les environnements de
programmation de Micro$oft Windows et que vous recherchiez un
équivalent sous X, vous l'avez trouvé ! Il y a aussi les équivalents
en mode texte des programmes X, ce qui vous permet d'utiliser xwpe
quel que soit votre environnement de développement.

%description -l pl.UTF-8
XWPE właściwie składa się z czterech programów: we, wpe, xwe i xwpe.
Są to różne wersje tego samego podstawowego edytora programisty i
środowiska. Jeżeli używałeś jakiegoś zintegrowanego środowiska
programistycznego pod MS Windows i szukasz odpowiednika pod X Window,
to jest to! Załączone są także tekstowe odpowiedniki programów pod X,
pozwalające używać xwpe w każdym środowisku.

%description -l pt_BR.UTF-8
O XWPE é na verdade um pacote de 4 programas: we, wpe, xwe, e xwpe.
Eles são diferentes versões do mesmo ambiente de desenvolvimento e
editor de programação. Se você usou algum dos ambientes de programação
do Microsoft Windows e quer algo equivalente no X, você achou o que
estava procurando! Também estão incluídos as versões em modo texto dos
programas, deixando vocês usar o xwpe não importando o tipo de
ambiente de desenvolvimento que tenha. Este pacote inclui as
bibliotecas básicas do xwpe e os programas em modo texto; os programas
para X estão no pacote 'xwpe-X11'.

%description -l ru.UTF-8
XWPE представляет собой пакет из четырех программ: we, wpe, xwe и
xwpe. Это разные версии одного и того же редактора и среды разработки.
Если вы привыкли к какой-либо среде разработки под Micro$oft Windows и
ищете что-то похожее для X Window, этот пакет - самое оно. Также
включены текстовые эквиваленты программ для X, позволяющие
использовать xwpe в любом окружении.

%description -l tr.UTF-8
XWPE, Microsoft Windows'da bulunan benzerleri gibi, bir metin
düzenleyici ve tümleşik bir geliştirme ortamı sunan bir yazılımdır. Bu
pakettekiler metin ekranda çalışan sürümleri bulundurmaktadır.

%description -l uk.UTF-8
XWPE - це пакет з чотирьох програм: we, wpe, xwe та xwpe. Це різні
версії одного й того ж редактору та середовища розробки. Якщо ви
звикли до якогось середовища розробки під Micro$oft Windows і шукаєте
щось схоже під X Window, то цей пакет - саме воно. Також включені
текстові еквіваленти програм для X, що дозволяють використовувати xwpe
у будь-якому середовищі.

%package X11
Summary:	X Window Programming Environment - X11 programs
Summary(es.UTF-8):	Ambiente de Programación X Window - Programas X11
Summary(pl.UTF-8):	XWPE - programy pod X11
Summary(pt_BR.UTF-8):	Ambiente de Programação X Window - Programas X11
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description X11
Includes the 'xwpe' and 'xwe' programs from the xwpe package that are
specific to X Window System.

%description X11 -l de.UTF-8
Beinhaltet die 'xwpe'- und 'xwe'-Programme aus dem xwpe-Paket, die
X-Window-spezifisch sind.

%description X11 -l es.UTF-8
Incluye los programas 'xwpe' y 'xwe' del paquete xwpe que son
específicos para X Window.

%description X11 -l pl.UTF-8
Pakiet zawiera programy xwpe i xwe ze środowiska xwpe - specyficzne
dla X Window System.

%description X11 -l pt_BR.UTF-8
Inclui os programas 'xwpe' e 'xwe' do pacote xwpe que são específicos
para X Window.

%description X11 -l tr.UTF-8
X Window altında çalışan tümleşik geliştirme ortamı yazılımları.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
CFLAGS="-I/usr/include/ncurses %{rpmcflags}"
%configure
%{__make} xwpe libxwpe-x11.so libxwpe-term.so

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
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
%{_desktopdir}/xwpe.desktop
%{_pixmapsdir}/xwpe.png
