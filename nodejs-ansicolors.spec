%{?scl:%scl_package nodejs-ansicolors}
%{!?scl:%global pkg_name %{name}}

%global npm_name ansicolors
 
%{?nodejs_find_provides_and_requires}


Name:           %{?scl_prefix}nodejs-ansicolors
Version:        0.3.2
Release:        1%{?dist}
Summary:        Functions that surround a string with ansicolor codes so it prints in color.
Url:            https://github.com/thlorenz/ansicolors
Source0:        http://registry.npmjs.org/ansicolors/-/ansicolors-0.3.2.tgz
License:        MIT

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  %{?scl_prefix}nodejs-devel

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

%description
Functions that surround a string with ansicolor codes so it prints in color.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{nodejs_sitelib}/ansicolors
cp -pr ansicolors.js package.json %{buildroot}%{nodejs_sitelib}/ansicolors
%nodejs_symlink_deps

%clean
rm -rf %buildroot


%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/ansicolors
%doc README.md LICENSE

%changelog
* Wed Jan 29 2014 Tomas Hrcka <thrcka@redhat.com> - 0.3.2-1
- initial build 

