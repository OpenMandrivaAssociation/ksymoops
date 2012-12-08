Summary:	Kernel oops and error message decoder
Name:		ksymoops
Version:	2.4.11
Release:	%mkrel 5
License:	GPL
Group:		System/Kernel and hardware
URL:		ftp://ftp.kernel.org/pub/linux/utils/kernel/ksymoops/v2.4/
Source0:	ftp://ftp.kernel.org/pub/linux/utils/kernel/ksymoops/v2.4/%{name}-%{version}.tar.gz
Source1:	ksymoops-gznm
Source2:	ksymoops-script
Source3:	README.mandriva
Patch1:		ksymoops-2.4.3-add_gz_modules_support
Patch2:		ksymoops_fix_link.patch
BuildRequires:	binutils-devel
Requires:	binutils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Linux kernel produces error messages that contain machine specific numbers
which are meaningless for debugging. ksymoops reads machine specific files and
the error log and converts the addresses to meaningful symbols and offsets.

%prep

%setup -q
%patch1 -p1
%patch2 -p1

cp %{SOURCE1} ksymoops-gznm
cp %{SOURCE2} ksymoops-script
cp %{SOURCE3} README.mandriva

%build
CFLAGS="%{optflags}" LDFLAGS="%{ldflags}" make DEF_MAP=\\\"/boot/System.map-*r\\\" all
 
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




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.4.11-4mdv2011.0
+ Revision: 666051
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4.11-3mdv2011.0
+ Revision: 606272
- rebuild

* Tue Feb 09 2010 Funda Wang <fwang@mandriva.org> 2.4.11-2mdv2010.1
+ Revision: 502594
- link against shared libs

* Sun Sep 27 2009 Olivier Blin <oblin@mandriva.com> 2.4.11-2mdv2010.0
+ Revision: 449843
- fix link by adding -lz for libbfd
  (from Arnaud Patard)

* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 2.4.11-1mdv2009.1
+ Revision: 316960
- 2.4.11
- use %%ldflags

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.4.9-5mdv2009.0
+ Revision: 222012
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.4.9-4mdv2008.1
+ Revision: 128239
- kill re-definition of %%buildroot on Pixel's request


* Fri Mar 16 2007 Oden Eriksson <oeriksson@mandriva.com> 2.4.9-4mdv2007.1
+ Revision: 145194
- Import ksymoops

* Fri Mar 16 2007 Oden Eriksson <oeriksson@mandrakesoft.com> 2.4.9-4mdv2007.1
- use the %%mkrel macro
- bunzip sources and patches

* Mon Jun 21 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.4.9-3mdk
- apply the mdk update fix (Geoffrey Lee)
- misc spec file fixes

