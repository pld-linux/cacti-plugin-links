%define		namesrc	links
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Links
Summary(pl.UTF-8):	Wtyczka do Cacti - Links
Name:		cacti-plugin-links
Version:	0.3
Release:	1
License:	GPL v2
Group:		Applications/WWW
#!!!!problem with version
Source0:	http://wotsit.thingy.com/haj/cacti/%{namesrc}-%{version}.zip
# Source0-md5:	cf90133193311a3e3d63d11d3528e7ba
Patch0:		%{name}-config.patch
URL:		http://wotsit.thingy.com/haj/cacti/links-plugin.html
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}
%define		webcactipluginconf %{_sysconfdir}/cacti

%description
This is a very simple plugin for the Cacti Plugin Architecture created
by Jimmy Smith for Cacti 0.8.x (0.9.0 is slated to have a new plugin
system from the start). It's just about the smallest plugin you can
have - it lets you have a page of arbitrary HTML content behind one of
the tabs at the top of the page. You could use this to integrate other
tools into Cacti - say you want to have links to Smokeping, or Request
Tracker, or Nagios...

%description -l pl.UTF-8
To jest bardzo prosta wtyczka dla architektury wtyczek Cacti
stworzonej przez Jimmy'ego Smitha dla Cacti 0.8.x (0.9.0 ma mieć nowy
system wtyczek). Jest to zapewne najmniejsza wtyczka jaką można mieć -
pozwala umieścić dowolną treść HTML pod jedną z zakładek na górnej
stronie. Można użyć jej do zintegrowania innych narzędzi z Cacti - np.
odnośników do Smokepinga, Request Trackera lub Nagiosa...

%prep
%setup -q -n %{namesrc}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{webcactipluginroot},%{webcactipluginconf}}
install editme.php $RPM_BUILD_ROOT%{webcactipluginconf}/plugin-links.php
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{webcactipluginconf}/plugin-links.php
%{webcactipluginroot}
