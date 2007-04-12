Summary:	Kernel oops and error message decoder
Name:		ksymoops
Version:	2.4.9
Release:	%mkrel 4
License:	GPL
Group:		System/Kernel and hardware
URL:		ftp://ftp.kernel.org/pub/linux/utils/kernel/ksymoops/v2.4/
Source0:	%{name}-%{version}.tar.bz2
Source1:	ksymoops-gznm
Source2:	ksymoops-script
Source3:	README.mandriva
Patch1:		ksymoops-2.4.3-add_gz_modules_support
BuildRequires:	binutils-devel
Requires:	binutils
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
The Linux kernel produces error messages that contain machine specific numbers
which are meaningless for debugging. ksymoops reads machine specific files and
the error log and converts the addresses to meaningful symbols and offsets.

%prep

%setup -q
%patch1 -p1

cp %{SOURCE1} ksymoops-gznm
cp %{SOURCE2} ksymoops-script
cp %{SOURCE3} README.mandriva

%build
CFLAGS="%{optflags}" make DEF_MAP=\\\"/boot/System.map-*r\\\" all
 
%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

make INSTALL_PREFIX=%{buildroot}%{_prefix} INSTALL_MANDIR=%{buildroot}%{_mandir}/ install

mv %{buildroot}/usr/bin/ksymoops %{buildroot}%{_bindir}/ksymoops.real

install -m0755 ksymoops-gznm %{buildroot}%{_bindir}/
install -m0755 ksymoops-script %{buildroot}%{_bindir}/ksymoops

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README INSTALL Changelog README.mandriva
%{_bindir}/ksymoops
%{_bindir}/ksymoops-gznm
%{_bindir}/ksymoops.real
%{_mandir}/man8/ksymoops.8*


