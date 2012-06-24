Summary:	X Window Programming Environment
Summary(de):	X-Window-Programmierumgebung
Summary(es):	Ambiente de programaci�n X Window
Summary(fr):	Environnement de programmation X Window
Summary(pl):	�rodowisko programistyczne pod X Window
Summary(pt_BR):	Ambiente de programa��o X Window
Summary(ru):	����� ���������� ��� X Windows
Summary(tr):	X Window program geli�tirme ortam�
Summary(uk):	���������� �������� Ц� X Windows
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
Windows-�quivalent gesehnt haben, dann ist das hier die L�sung f�r
Sie! Ebenfalls eingeschlossen sind die Textmodus-�quivalente der
X-Programme, so da� Sie xwpe benutzen k�nnen, unabh�ngig davon, in
welcher Entwicklungsumgebung sie arbeiten.

%description -l es
XWPE es en realidad un paquete de 4 programas: we, wpe, xwe, y xwpe.
Son diferentes versiones del mismo ambiente de desarrollo y editor de
programaci�n. Si has usado alg�n de los ambientes de programaci�n del
Microsoft Windows y quieres algo equivalente en el X, acabas de
encontrar lo que buscabas. Tambi�n se incluyen las versiones en modo
texto de los programas, dejando que usen el xwpe no importando el tipo
de ambiente de desarrollo que tengas. Este paquete incluye las
bibliotecas b�sicas del xwpe y los programas en modo texto; los
programas para X est�n en el paquete 'xwpe-X11'.

%description -l fr
xwpe is un paquetage de quatre programmes : we, wpe, xwe et xwpe. Ce
sont des versions diff�rentes du m�me �diteur et environnement de
d�veloppement. Si vous avez d�j� utilis� les environnements de
programmation de Micro$oft Windows et que vous recherchiez un
�quivalent sous X, vous l'avez trouv� ! Il y a aussi les �quivalents
en mode texte des programmes X, ce qui vous permet d'utiliser xwpe
quel que soit votre environnement de d�veloppement.

%description -l pl
XWPE w�a�ciwie sk�ada si� z czterech program�w: we, wpe, xwe i xwpe.
S� to r�ne wersje tego samego podstawowego edytora programisty i
�rodowiska. Je�eli u�ywa�e� jakiego� zintegrowanego �rodowiska
programistycznego pod MS Windows i szukasz odpowiednika pod X Window,
to jest to! Za��czone s� tak�e tekstowe odpowiedniki program�w pod X,
pozwalaj�ce u�ywa� xwpe w ka�dym �rodowisku.

%description -l pt_BR
O XWPE � na verdade um pacote de 4 programas: we, wpe, xwe, e xwpe.
Eles s�o diferentes vers�es do mesmo ambiente de desenvolvimento e
editor de programa��o. Se voc� usou algum dos ambientes de programa��o
do Microsoft Windows e quer algo equivalente no X, voc� achou o que
estava procurando! Tamb�m est�o inclu�dos as vers�es em modo texto dos
programas, deixando voc�s usar o xwpe n�o importando o tipo de
ambiente de desenvolvimento que tenha. Este pacote inclui as
bibliotecas b�sicas do xwpe e os programas em modo texto; os programas
para X est�o no pacote 'xwpe-X11'.

%description -l ru
XWPE ������������ ����� ����� �� ������� ��������: we, wpe, xwe �
xwpe. ��� ������ ������ ������ � ���� �� ��������� � ����� ����������.
���� �� �������� � �����-���� ����� ���������� ��� Micro$oft Windows �
����� ���-�� ������� ��� X Windows, ���� ����� - ����� ���. �����
�������� ��������� ����������� �������� ��� X, �����������
������������ xwpe � ����� ���������.

%description -l tr
XWPE, Microsoft Windows'da bulunan benzerleri gibi, bir metin
d�zenleyici ve t�mle�ik bir geli�tirme ortam� sunan bir yaz�l�md�r. Bu
pakettekiler metin ekranda �al��an s�r�mleri bulundurmaktad�r.

%description -l uk
XWPE - �� ����� � �������� �������: we, wpe, xwe �� xwpe. �� Ҧ�Φ
���Ӧ� ������ � ���� � ��������� �� ���������� ��������. ���� ��
������ �� ������� ���������� �������� Ц� Micro$oft Windows � �������
���� ����� Ц� X Windows, �� ��� ����� - ���� ����. ����� ������Φ
������צ ��צ������� ������� ��� X, �� ���������� ��������������� xwpe
� ����-����� ��������ݦ.

%package X11
Summary:	X Window Programming Environment - X11 programs
Summary(es):	Ambiente de Programaci�n X Window - Programas X11
Summary(pl):	XWPE - programy pod X11
Summary(pt_BR):	Ambiente de Programa��o X Window - Programas X11
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
espec�ficos para X Window.

%description X11 -l pl
Pakiet zawiera programy xwpe i xwe ze �rodowiska xwpe - specyficzne
dla X Window System.

%description X11 -l pt_BR
Inclui os programas 'xwpe' e 'xwe' do pacote xwpe que s�o espec�ficos
para X Window.

%description X11 -l tr
X Window alt�nda �al��an t�mle�ik geli�tirme ortam� yaz�l�mlar�.

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
