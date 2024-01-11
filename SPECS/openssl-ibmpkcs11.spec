%global enginesdir %(pkg-config --variable=enginesdir libcrypto)

Name:           openssl-ibmpkcs11
Version:        1.0.2
Release:        1%{?dist}
Summary:        IBM OpenSSL PKCS#11 engine

License:        OpenSSL
URL:            https://github.com/opencryptoki/openssl-ibmpkcs11
Source0:        https://github.com/opencryptoki/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  automake autoconf libtool
BuildRequires:  openssl-devel
Requires:       opencryptoki-libs%{?_isa}


%description
This package contains a shared object OpenSSL dynamic engine for the use
with a PKCS#11 implementation such as openCryptoki.

%prep
%autosetup -p1

./bootstrap.sh


%build
%configure --libdir=%{enginesdir}
%make_build


%install
%make_install
mv openssl.cnf.sample openssl.cnf.sample.%{_arch}
rm -f $RPM_BUILD_ROOT%{enginesdir}/*.la


%files
%license LICENSE
%doc README openssl.cnf.sample.%{_arch}
%{enginesdir}/ibmpkcs11.so


%changelog
* Fri Feb 23 2018 Dan Horák <dan@danny.cz> - 1.0.2-1
- updated to 1.0.2

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Dan Horák <dan@danny.cz> - 1.0.1-2
- apply fix for autotools
- don't hard-code %%enginesdir

* Fri Jan 19 2018 Dan Horák <dan@danny.cz> - 1.0.1-1
- initial Fedora version
