Name:           vulkan-tools
Version:        1.3.250.1
Release:        1%{?dist}
Summary:        Vulkan tools

License:        ASL 2.0
URL:            https://github.com/KhronosGroup/Vulkan-Tools
Source0:        %url/archive/sdk-%{version}.tar.gz#/Vulkan-Tools-sdk-%{version}.tar.gz       

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
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

%description
Vulkan tools

%prep
%autosetup -n Vulkan-Tools-sdk-%{version}


%build
%cmake -GNinja -DCMAKE_BUILD_TYPE=Release -DGLSLANG_INSTALL_DIR=%{_prefix} .
%ninja_build


%install
%ninja_install

%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md
%{_bindir}/*

%changelog
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
