Name:           vulkan-tools
Version:        1.3.283.0
Release:        2%{?dist}
Summary:        Vulkan tools

License:        ASL 2.0
URL:            https://github.com/KhronosGroup/Vulkan-Tools
Source0:        %url/archive/vulkan-sdk-%{version}.tar.gz#/Vulkan-Tools-sdk-%{version}.tar.gz       

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  glslang
BuildRequires:  ninja-build
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  vulkan-loader-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xcb)

Provides:       vulkan-demos%{?_isa} = %{version}-%{release}
Obsoletes:      vulkan-demos < %{version}-%{release}

# vulkan-volk is required but not available in CentOS/RHEL 8
Source1:        https://github.com/zeux/volk/archive/vulkan-sdk-%{version}.tar.gz#/Vulkan-Volk-sdk-%{version}.tar.gz
BuildRequires:  vulkan-headers


%description
Vulkan tools

%prep
%autosetup -n Vulkan-Tools-vulkan-sdk-%{version} -p1

# Extract vulkan-volk in "volk"
mkdir -p volk
tar -xvf %{SOURCE1} -C volk --strip-components=1


%build
# vulkan-volk can't be compiled and linked because it contains .a libraries and
# check-buildroot would complain about debug symbols containing
# "/builddir/build/BUILDROOT" paths.
# Instead, add vulkan-volk as a subproject
echo "add_subdirectory(volk)" >> CMakeLists.txt

%cmake3 -GNinja -DCMAKE_BUILD_TYPE=Release -DGLSLANG_INSTALL_DIR=%{_prefix} \
        -DCMAKE_CXX_STANDARD_LIBRARIES="-lstdc++fs"
%cmake3_build


%install
%cmake3_install

%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md
%{_bindir}/*

%changelog
* Fri Sep 13 2024 José Expósito <jexposit@redhat.com> - 1.3.283.0-2
- Link stdc++fs
  Resolves: https://issues.redhat.com/browse/RHEL-54288

* Wed Sep 11 2024 José Expósito <jexposit@redhat.com> - 1.3.283.0-1
- Update to 1.3.283.0 SDK
  Resolves: https://issues.redhat.com/browse/RHEL-54288

* Wed Jul 12 2023 Dave Airlie <airlied@redhat.com> - 1.3.250.1-1
- Update to 1.3.250.1

* Tue Feb 14 2023 Dave Airlie <airlied@redhat.com> - 1.3.239.0-1
- Update to 1.3.239.0

* Wed Aug 24 2022 Dave Airlie <airlied@redhat.com> - 1.3.224.0-1
- Update to 1.3.224.0

* Mon Jun 20 2022 Dave Airlie <airlied@redhat.com> - 1.3.216.0-1
- Update to 1.3.216.0

* Tue Feb 22 2022 Dave Airlie <airlied@redhat.com> - 1.3.204.0-1
- Update to 1.3.204.0

* Mon Feb 01 2021 Dave Airlie <airlied@redhat.com> - 1.2.162.0-1
- Update to 1.2.162.0

* Wed Aug 05 2020 Dave Airlie <airlied@redhat.com> - 1.2.148.0-1
- Update to 1.2.148.0

* Wed Jan 29 2020 Dave Airlie <airlied@redhat.com> - 1.2.131.1-1
- Update for 8.2.0 for vulkan 1.2

* Sat Dec 07 2019 Dave Airlie <airlied@redhat.com> - 1.1.126.0-2
- Update for 8.2.0

* Tue Nov 12 2019 Dave Airlie <airlied@redhat.com> - 1.1.126.0-1
- Update to 1.1.126.0

* Mon Aug 05 2019 Dave Airlie <airlied@redhat.com> - 1.1.114.0-1
- Update to 1.1.114.0

* Thu Mar 07 2019 Dave Airlie <airlied@redhat.com> - 1.1.101.0-1
- Update to 1.1.101.0

* Tue Aug 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.82.0-1
- Update to 1.1.82.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.77.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.77.0-1
- Initial package
