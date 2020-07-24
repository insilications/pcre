#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9766E084FB0F43D8 (ph10@cam.ac.uk)
#
%define keepstatic 1
Name     : pcre
Version  : 8.44
Release  : 58
URL      : https://ftp.pcre.org/pub/pcre/pcre-8.44.tar.gz
Source0  : https://ftp.pcre.org/pub/pcre/pcre-8.44.tar.gz
Source1  : https://ftp.pcre.org/pub/pcre/pcre-8.44.tar.gz.sig
Summary  : PCRE - Perl compatible regular expressions C library with 8 bit character support
Group    : Development/Tools
License  : FTL GPL-2.0+ MIT Zlib
Requires: pcre-bin = %{version}-%{release}
Requires: pcre-lib = %{version}-%{release}
Requires: pcre-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : bzip2-dev
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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

%description lib
lib components for the pcre package.


%package man
Summary: man components for the pcre package.
Group: Default

%description man
man components for the pcre package.


%package staticdev
Summary: staticdev components for the pcre package.
Group: Default
Requires: pcre-dev = %{version}-%{release}

%description staticdev
staticdev components for the pcre package.


%prep
%setup -q -n pcre-8.44
cd %{_builddir}/pcre-8.44

%build
## build_prepend content
find . -type f -name 'configure' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595605615
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-common -Wno-error -Wp,-D_REENTRANT
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%configure  --enable-shared --enable-static  --enable-jit --enable-utf --enable-unicode-properties --enable-pcre16 --enable-pcre32
## make_prepend content
find . -type f -name 'Makefile' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#
find . -type f -name 'libtool' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1

make VERBOSE=1 V=1 %{?_smp_mflags} check || :
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%configure  --enable-shared --enable-static  --enable-jit --enable-utf --enable-unicode-properties --enable-pcre16 --enable-pcre32
## make_prepend content
find . -type f -name 'Makefile' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#
find . -type f -name 'libtool' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1595605615
rm -rf %{buildroot}
%make_install V=1 VERBOSE=1

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

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pcre-config.1
/usr/share/man/man1/pcregrep.1
/usr/share/man/man1/pcretest.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libpcre.a
/usr/lib64/libpcre16.a
/usr/lib64/libpcre32.a
/usr/lib64/libpcrecpp.a
/usr/lib64/libpcreposix.a
