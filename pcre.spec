#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9766E084FB0F43D8 (ph10@cam.ac.uk)
#
Name     : pcre
Version  : 8.44
Release  : 53
URL      : https://ftp.pcre.org/pub/pcre/pcre-8.44.tar.gz
Source0  : https://ftp.pcre.org/pub/pcre/pcre-8.44.tar.gz
Source1  : https://ftp.pcre.org/pub/pcre/pcre-8.44.tar.gz.sig
Summary  : PCRE - Perl compatible regular expressions C library with 8 bit character support
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pcre-bin = %{version}-%{release}
Requires: pcre-lib = %{version}-%{release}
Requires: pcre-license = %{version}-%{release}
Requires: pcre-man = %{version}-%{release}
BuildRequires : bzip2-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev

%description
-----------------------------------------------------------------
NOTE: This set of files relates to PCRE releases that use the original API,
with library names libpcre, libpcre16, and libpcre32. January 2015 saw the
first release of a new API, known as PCRE2, with release numbers starting at
10.00 and library names libpcre2-8, libpcre2-16, and libpcre2-32. The old
libraries (now called PCRE1) are still being maintained for bug fixes, but
there will be no new development. New projects are advised to use the new PCRE2
libraries.

%package bin
Summary: bin components for the pcre package.
Group: Binaries
Requires: pcre-license = %{version}-%{release}

%description bin
bin components for the pcre package.


%package dev
Summary: dev components for the pcre package.
Group: Development
Requires: pcre-lib = %{version}-%{release}
Requires: pcre-bin = %{version}-%{release}
Provides: pcre-devel = %{version}-%{release}
Requires: pcre = %{version}-%{release}

%description dev
dev components for the pcre package.


%package dev32
Summary: dev32 components for the pcre package.
Group: Default
Requires: pcre-lib32 = %{version}-%{release}
Requires: pcre-bin = %{version}-%{release}
Requires: pcre-dev = %{version}-%{release}

%description dev32
dev32 components for the pcre package.


%package doc
Summary: doc components for the pcre package.
Group: Documentation
Requires: pcre-man = %{version}-%{release}

%description doc
doc components for the pcre package.


%package extras
Summary: extras components for the pcre package.
Group: Default

%description extras
extras components for the pcre package.


%package lib
Summary: lib components for the pcre package.
Group: Libraries
Requires: pcre-license = %{version}-%{release}

%description lib
lib components for the pcre package.


%package lib32
Summary: lib32 components for the pcre package.
Group: Default
Requires: pcre-license = %{version}-%{release}

%description lib32
lib32 components for the pcre package.


%package license
Summary: license components for the pcre package.
Group: Default

%description license
license components for the pcre package.


%package man
Summary: man components for the pcre package.
Group: Default

%description man
man components for the pcre package.


%prep
%setup -q -n pcre-8.44
cd %{_builddir}/pcre-8.44
pushd ..
cp -a pcre-8.44 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595270734
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --enable-jit --enable-utf  --enable-unicode-properties --enable-pcre16 --enable-pcre32
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --enable-jit --enable-utf  --enable-unicode-properties --enable-pcre16 --enable-pcre32   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1595270734
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pcre
cp %{_builddir}/pcre-8.44/LICENCE %{buildroot}/usr/share/package-licenses/pcre/11ff082389982b8168263850db69199065f2028d
cp %{_builddir}/pcre-8.44/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/pcre/ff3ed70db4739b3c6747c7f624fe2bad70802987
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pcre-config
/usr/bin/pcregrep
/usr/bin/pcretest

%files dev
%defattr(-,root,root,-)
/usr/include/pcre.h
/usr/include/pcre_scanner.h
/usr/include/pcre_stringpiece.h
/usr/include/pcrecpp.h
/usr/include/pcrecpparg.h
/usr/include/pcreposix.h
/usr/lib64/libpcre.so
/usr/lib64/libpcre16.so
/usr/lib64/libpcre32.so
/usr/lib64/libpcrecpp.so
/usr/lib64/libpcreposix.so
/usr/lib64/pkgconfig/libpcre.pc
/usr/lib64/pkgconfig/libpcre16.pc
/usr/lib64/pkgconfig/libpcre32.pc
/usr/lib64/pkgconfig/libpcrecpp.pc
/usr/lib64/pkgconfig/libpcreposix.pc
/usr/share/man/man3/pcre.3
/usr/share/man/man3/pcre16.3
/usr/share/man/man3/pcre16_assign_jit_stack.3
/usr/share/man/man3/pcre16_compile.3
/usr/share/man/man3/pcre16_compile2.3
/usr/share/man/man3/pcre16_config.3
/usr/share/man/man3/pcre16_copy_named_substring.3
/usr/share/man/man3/pcre16_copy_substring.3
/usr/share/man/man3/pcre16_dfa_exec.3
/usr/share/man/man3/pcre16_exec.3
/usr/share/man/man3/pcre16_free_study.3
/usr/share/man/man3/pcre16_free_substring.3
/usr/share/man/man3/pcre16_free_substring_list.3
/usr/share/man/man3/pcre16_fullinfo.3
/usr/share/man/man3/pcre16_get_named_substring.3
/usr/share/man/man3/pcre16_get_stringnumber.3
/usr/share/man/man3/pcre16_get_stringtable_entries.3
/usr/share/man/man3/pcre16_get_substring.3
/usr/share/man/man3/pcre16_get_substring_list.3
/usr/share/man/man3/pcre16_jit_exec.3
/usr/share/man/man3/pcre16_jit_stack_alloc.3
/usr/share/man/man3/pcre16_jit_stack_free.3
/usr/share/man/man3/pcre16_maketables.3
/usr/share/man/man3/pcre16_pattern_to_host_byte_order.3
/usr/share/man/man3/pcre16_refcount.3
/usr/share/man/man3/pcre16_study.3
/usr/share/man/man3/pcre16_utf16_to_host_byte_order.3
/usr/share/man/man3/pcre16_version.3
/usr/share/man/man3/pcre32.3
/usr/share/man/man3/pcre32_assign_jit_stack.3
/usr/share/man/man3/pcre32_compile.3
/usr/share/man/man3/pcre32_compile2.3
/usr/share/man/man3/pcre32_config.3
/usr/share/man/man3/pcre32_copy_named_substring.3
/usr/share/man/man3/pcre32_copy_substring.3
/usr/share/man/man3/pcre32_dfa_exec.3
/usr/share/man/man3/pcre32_exec.3
/usr/share/man/man3/pcre32_free_study.3
/usr/share/man/man3/pcre32_free_substring.3
/usr/share/man/man3/pcre32_free_substring_list.3
/usr/share/man/man3/pcre32_fullinfo.3
/usr/share/man/man3/pcre32_get_named_substring.3
/usr/share/man/man3/pcre32_get_stringnumber.3
/usr/share/man/man3/pcre32_get_stringtable_entries.3
/usr/share/man/man3/pcre32_get_substring.3
/usr/share/man/man3/pcre32_get_substring_list.3
/usr/share/man/man3/pcre32_jit_exec.3
/usr/share/man/man3/pcre32_jit_stack_alloc.3
/usr/share/man/man3/pcre32_jit_stack_free.3
/usr/share/man/man3/pcre32_maketables.3
/usr/share/man/man3/pcre32_pattern_to_host_byte_order.3
/usr/share/man/man3/pcre32_refcount.3
/usr/share/man/man3/pcre32_study.3
/usr/share/man/man3/pcre32_utf32_to_host_byte_order.3
/usr/share/man/man3/pcre32_version.3
/usr/share/man/man3/pcre_assign_jit_stack.3
/usr/share/man/man3/pcre_compile.3
/usr/share/man/man3/pcre_compile2.3
/usr/share/man/man3/pcre_config.3
/usr/share/man/man3/pcre_copy_named_substring.3
/usr/share/man/man3/pcre_copy_substring.3
/usr/share/man/man3/pcre_dfa_exec.3
/usr/share/man/man3/pcre_exec.3
/usr/share/man/man3/pcre_free_study.3
/usr/share/man/man3/pcre_free_substring.3
/usr/share/man/man3/pcre_free_substring_list.3
/usr/share/man/man3/pcre_fullinfo.3
/usr/share/man/man3/pcre_get_named_substring.3
/usr/share/man/man3/pcre_get_stringnumber.3
/usr/share/man/man3/pcre_get_stringtable_entries.3
/usr/share/man/man3/pcre_get_substring.3
/usr/share/man/man3/pcre_get_substring_list.3
/usr/share/man/man3/pcre_jit_exec.3
/usr/share/man/man3/pcre_jit_stack_alloc.3
/usr/share/man/man3/pcre_jit_stack_free.3
/usr/share/man/man3/pcre_maketables.3
/usr/share/man/man3/pcre_pattern_to_host_byte_order.3
/usr/share/man/man3/pcre_refcount.3
/usr/share/man/man3/pcre_study.3
/usr/share/man/man3/pcre_utf16_to_host_byte_order.3
/usr/share/man/man3/pcre_utf32_to_host_byte_order.3
/usr/share/man/man3/pcre_version.3
/usr/share/man/man3/pcreapi.3
/usr/share/man/man3/pcrebuild.3
/usr/share/man/man3/pcrecallout.3
/usr/share/man/man3/pcrecompat.3
/usr/share/man/man3/pcrecpp.3
/usr/share/man/man3/pcredemo.3
/usr/share/man/man3/pcrejit.3
/usr/share/man/man3/pcrelimits.3
/usr/share/man/man3/pcrematching.3
/usr/share/man/man3/pcrepartial.3
/usr/share/man/man3/pcrepattern.3
/usr/share/man/man3/pcreperform.3
/usr/share/man/man3/pcreposix.3
/usr/share/man/man3/pcreprecompile.3
/usr/share/man/man3/pcresample.3
/usr/share/man/man3/pcrestack.3
/usr/share/man/man3/pcresyntax.3
/usr/share/man/man3/pcreunicode.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libpcre.so
/usr/lib32/libpcre16.so
/usr/lib32/libpcre32.so
/usr/lib32/libpcrecpp.so
/usr/lib32/libpcreposix.so
/usr/lib32/pkgconfig/32libpcre.pc
/usr/lib32/pkgconfig/32libpcre16.pc
/usr/lib32/pkgconfig/32libpcre32.pc
/usr/lib32/pkgconfig/32libpcrecpp.pc
/usr/lib32/pkgconfig/32libpcreposix.pc
/usr/lib32/pkgconfig/libpcre.pc
/usr/lib32/pkgconfig/libpcre16.pc
/usr/lib32/pkgconfig/libpcre32.pc
/usr/lib32/pkgconfig/libpcrecpp.pc
/usr/lib32/pkgconfig/libpcreposix.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/pcre/*

%files extras
%defattr(-,root,root,-)
/usr/lib64/libpcre16.so.0
/usr/lib64/libpcre16.so.0.2.12
/usr/lib64/libpcre32.so.0
/usr/lib64/libpcre32.so.0.0.12
/usr/lib64/libpcrecpp.so.0
/usr/lib64/libpcrecpp.so.0.0.2
/usr/lib64/libpcreposix.so.0
/usr/lib64/libpcreposix.so.0.0.7

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpcre.so.1
/usr/lib64/libpcre.so.1.2.12

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpcre.so.1
/usr/lib32/libpcre.so.1.2.12
/usr/lib32/libpcre16.so.0
/usr/lib32/libpcre16.so.0.2.12
/usr/lib32/libpcre32.so.0
/usr/lib32/libpcre32.so.0.0.12
/usr/lib32/libpcrecpp.so.0
/usr/lib32/libpcrecpp.so.0.0.2
/usr/lib32/libpcreposix.so.0
/usr/lib32/libpcreposix.so.0.0.7

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pcre/11ff082389982b8168263850db69199065f2028d
/usr/share/package-licenses/pcre/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pcre-config.1
/usr/share/man/man1/pcregrep.1
/usr/share/man/man1/pcretest.1
