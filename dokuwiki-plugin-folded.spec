%define		plugin		folded
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	DokuWiki folded plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	20130207
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/dokufreaks/plugin-%{plugin}/tarball/master/%{plugin}-%{version}.tgz
# Source0-md5:	343fdef474f78cbfdac0c2a0b4902f7c
URL:		http://www.dokuwiki.org/plugin:folded
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20070626
Requires:	php-common >= 4:%{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
Foldable page sections for DokuWiki.

%prep
%setup -qc
mv *-%{plugin}-*/* .

version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force js/css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.css
%{plugindir}/*.gif
%{plugindir}/*.js
%{plugindir}/*.txt
%{plugindir}/*.php
%{plugindir}/conf
%{plugindir}/syntax
