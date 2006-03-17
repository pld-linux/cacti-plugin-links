%define		namesrc	links
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Links
Summary(pl):	Wtyczka do Cacti - Links
Name:		cacti-plugin-links
Version:	0.3
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
#!!!!problem with version
Source0:	http://wotsit.thingy.com/haj/cacti/%{namesrc}-%{version}.zip
# Source0-md5:	cf90133193311a3e3d63d11d3528e7ba
URL:		http://wotsit.thingy.com/haj/cacti/links-plugin.html
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti -This is a very simple plugin for the Cacti Plugin
Architecture created by Jimmy Smith for Cacti 0.8.x (0.9.0 is slated to
have a new plugin system from the start). It's just about the smallest
plugin you can have - it lets you have a page of arbitrary HTML content
behind one of the tabs at the top of the page. You could use this to
integrate other tools into Cacti - say you want to have links to
Smokeping, or Request Tracker, or Nagios...

%description -l pl
Wtyczka do Cacti - 

%prep
%setup -q -n %{namesrc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc LICENSE README 
%{webcactipluginroot}
