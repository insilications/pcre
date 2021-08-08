#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : pcre
Version  : 8.45
Release  : 64
URL      : https://ftp.pcre.org/pub/pcre/pcre-8.45.tar.gz
Source0  : https://ftp.pcre.org/pub/pcre/pcre-8.45.tar.gz
Summary  : PCRE - Perl compatible regular expressions C library with 8 bit character support
Group    : Development/Tools
License  : GPL-2.0
Requires: pcre-bin = %{version}-%{release}
Requires: pcre-lib = %{version}-%{release}
Requires: pcre-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : bzip2-dev
BuildRequires : bzip2-dev32
BuildRequires : bzip2-staticdev
BuildRequires : findutils
BuildRequires : gcc
BuildRequires : gcc-abi
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : pkgconfig(32bzip2)
BuildRequires : pkgconfig(32zlib)
BuildRequires : pkgconfig(bzip2)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
BuildRequires : zlib-staticdev
BuildRequires : zlib-staticdev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
-----------------------------------------------------------------
NOTE: This set of files relates to PCRE releases that use the original API,
with library names libpcre, libpcre16, and libpcre32. January 2015 saw the
first release of a new API, known as PCRE2, with release numbers starting at
10.00 and library names libpcre2-8, libpcre2-16, and libpcre2-32. The old
libraries (now called PCRE1) are now at end of life, and 8.45 is the final
release. New projects are advised to use the new PCRE2 libraries.

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

%description lib
lib components for the pcre package.


%package lib32
Summary: lib32 components for the pcre package.
Group: Default

%description lib32
lib32 components for the pcre package.


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


%package staticdev32
Summary: staticdev32 components for the pcre package.
Group: Default
Requires: pcre-dev32 = %{version}-%{release}

%description staticdev32
staticdev32 components for the pcre package.


%prep
%setup -q -n pcre-8.45
cd %{_builddir}/pcre-8.45
pushd %{_builddir}
cp -a %{_builddir}/pcre-8.45 build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1628429481
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -Wl,--as-needed --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -Wp,-D_REENTRANT -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -Wl,-sort-common -fasynchronous-unwind-tables -static-libstdc++ -static-libgcc -fexceptions -Wl,--enable-new-dtags -lgcov $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -Wl,--as-needed --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -Wp,-D_REENTRANT -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -Wl,-sort-common -fasynchronous-unwind-tables -fexceptions -Wl,--enable-new-dtags -lgcov $PGO_GEN"
export FFLAGS_GENERATE="-O3 -Wl,--as-needed --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -Wp,-D_REENTRANT -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -Wl,-sort-common -fasynchronous-unwind-tables -fexceptions -Wl,--enable-new-dtags -lgcov $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -Wl,--as-needed --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -Wp,-D_REENTRANT -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -Wl,-sort-common -fasynchronous-unwind-tables -fexceptions -Wl,--enable-new-dtags -lgcov $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -Wl,--as-needed --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -Wp,-D_REENTRANT -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -Wl,-sort-common -fasynchronous-unwind-tables -Wl,--enable-new-dtags -static-libstdc++ -static-libgcc -lgcov $PGO_GEN"
## pgo use
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize
## -Ofast -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
## -Wl,-Bsymbolic-functions
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=0
export __GL_SYNC_DISPLAY_DEVICE=DFP-1
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-1
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
## altflags_pgo end
if [ ! -f statuspgo ]; then
echo PGO Phase 1
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%configure --enable-shared --enable-static  --enable-jit --enable-utf --enable-unicode-properties --enable-pcre16 --enable-pcre32
make  %{?_smp_mflags}  V=1 VERBOSE=1  V=1 VERBOSE=1

make -j1 VERBOSE=1 V=1 check || :
make clean || :
echo USED > statuspgo
fi
if [ -f statuspgo ]; then
echo PGO Phase 2
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%configure --enable-shared --enable-static  --enable-jit --enable-utf --enable-unicode-properties --enable-pcre16 --enable-pcre32
make  %{?_smp_mflags}  V=1 VERBOSE=1  V=1 VERBOSE=1
fi

pushd ../build32/
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
unset FCFLAGS
unset FFLAGS
unset CFFLAGS
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --enable-shared --enable-static  --enable-jit --enable-utf --enable-unicode-properties --enable-pcre16 --enable-pcre32  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}  V=1 VERBOSE=1  V=1 VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1628429481
rm -rf %{buildroot}
pushd ../build32/
%make_install32 V=1 VERBOSE=1
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
    pushd %{buildroot}/usr/lib32/pkgconfig
    for i in *.pc ; do ln -s $i 32$i ; done
    popd
fi
popd
%make_install V=1 VERBOSE=1
## install_append content
install -dm 0755 %{buildroot}/usr/lib64/haswell/ || :
cp --archive %{buildroot}/usr/lib64/libpcre* %{buildroot}/usr/lib64/haswell/ || :
## install_append end

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
/usr/lib64/haswell/libpcre.so
/usr/lib64/haswell/libpcre16.so
/usr/lib64/haswell/libpcre32.so
/usr/lib64/haswell/libpcrecpp.so
/usr/lib64/haswell/libpcreposix.so
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
/usr/lib64/libpcre32.so.0
/usr/lib64/libpcrecpp.so.0
/usr/lib64/libpcrecpp.so.0.0.2
/usr/lib64/libpcreposix.so.0
/usr/lib64/libpcreposix.so.0.0.7

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libpcre.so.1
/usr/lib64/haswell/libpcre.so.1.2.13
/usr/lib64/haswell/libpcre16.so.0
/usr/lib64/haswell/libpcre16.so.0.2.13
/usr/lib64/haswell/libpcre32.so.0
/usr/lib64/haswell/libpcre32.so.0.0.13
/usr/lib64/haswell/libpcrecpp.so.0
/usr/lib64/haswell/libpcrecpp.so.0.0.2
/usr/lib64/haswell/libpcreposix.so.0
/usr/lib64/haswell/libpcreposix.so.0.0.7
/usr/lib64/libpcre.so.1
/usr/lib64/libpcre.so.1.2.13
/usr/lib64/libpcre16.so.0.2.13
/usr/lib64/libpcre32.so.0.0.13

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpcre.so.1
/usr/lib32/libpcre.so.1.2.13
/usr/lib32/libpcre16.so.0
/usr/lib32/libpcre16.so.0.2.13
/usr/lib32/libpcre32.so.0
/usr/lib32/libpcre32.so.0.0.13
/usr/lib32/libpcrecpp.so.0
/usr/lib32/libpcrecpp.so.0.0.2
/usr/lib32/libpcreposix.so.0
/usr/lib32/libpcreposix.so.0.0.7

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pcre-config.1
/usr/share/man/man1/pcregrep.1
/usr/share/man/man1/pcretest.1
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

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/haswell/libpcre.a
/usr/lib64/haswell/libpcre16.a
/usr/lib64/haswell/libpcre32.a
/usr/lib64/haswell/libpcrecpp.a
/usr/lib64/haswell/libpcreposix.a
/usr/lib64/libpcre.a
/usr/lib64/libpcre16.a
/usr/lib64/libpcre32.a
/usr/lib64/libpcrecpp.a
/usr/lib64/libpcreposix.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libpcre.a
/usr/lib32/libpcre16.a
/usr/lib32/libpcre32.a
/usr/lib32/libpcrecpp.a
/usr/lib32/libpcreposix.a
