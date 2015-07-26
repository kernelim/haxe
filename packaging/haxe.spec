Name:           haxe
Version:        PKG_VERSION
Release:        PKG_RELEASE%{?dist}
Summary:        The Cross-platform Toolkit
License:        GPLv2/LGPLv2/BSD
URL:            http://haxe.org
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-extra-%{version}.tar.gz
Source2:        %{name}-libs-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  zlib-devel

%description
Haxe is an open source toolkit based on a modern, high level,
strictly typed programming language, a cross-compiler, a complete
cross-platform standard library and ways to access each
platform\'s native capabilities.

%prep
%setup -q

tar -zxf $RPM_SOURCE_DIR/%{name}-extra-%{version}.tar.gz -C ..
tar -zxf $RPM_SOURCE_DIR/%{name}-libs-%{version}.tar.gz -C ..

%build
make \
    INSTALL_DIR=/%{_prefix} \
    INSTALL_BIN_DIR=/%{_bindir} \
    INSTALL_LIB_DIR=/%{_datadir}/haxe

%check

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
make \
    INSTALL_DIR=$RPM_BUILD_ROOT/%{_prefix} \
    INSTALL_BIN_DIR=$RPM_BUILD_ROOT/%{_bindir} \
    INSTALL_LIB_DIR=$RPM_BUILD_ROOT/%{_datadir}/haxe \
    RUNTIME_INSTALL_LIB_DIR=/%{_datadir}/haxe \
    install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/haxe
%{_bindir}/haxelib
%{_datadir}/haxe/*
