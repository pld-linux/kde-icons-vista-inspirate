#$Revision: 1.2 $, $Date: 2006-01-26 10:52:57 $

%define		_name Vista-Inspirate

Summary:	KDE icons - %{_name}
Summary(pl):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	1.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://nuovext.pwsp.net/vista-inspirate/files/%{_name}_%{version}-kde.tar.gz
# Source0-md5:	6b1f4b81c69196b6cb40bf8f961f0535
URL:		http://www.kde-look.org/content/show.php?content=31585
Requires:	kdelibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vista-Inspirate is an icon theme based on the theme nuoveXT and
Windows Vista. It is strongly recommended to have NuoveXT (1.5)
installed to use this theme, simply because it inherits it (all
mimetypes for instance).

%description -l pl
Vista-Inspirate jest motywem ikon opartym na motywie nuoveXT oraz na
Windows Vista. Zalecane jest, aby posiadaæ zainstalowany równie¿ motyw
NuoveXT (1.5), poniewa¿ motyw Vista-Inspirate czê¶ciowo wykorzystuje
ikony tam zawarte (np. dla typów mime).

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xfz %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/*
