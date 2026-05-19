Name:           vulkan-tools
Version:        1.4.328.1
Release:        1%{?dist}
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
BuildRequires:  vulkan-volk-devel
BuildRequires:  vulkan-volk-static
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
%autosetup -n Vulkan-Tools-vulkan-sdk-%{version} -p1


%build
%cmake3 -GNinja -DCMAKE_BUILD_TYPE=Release -DGLSLANG_INSTALL_DIR=%{_prefix}
%cmake3_build


%install
%cmake3_install

%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md
%{_bindir}/*

%changelog
* Thu 08 2026 José Expósito <jexposit@redhat.com> - 1.4.328.1-1
- Update to 1.4.328.1 SDK

* Thu Jun 26 2025 Anusha Srivatsa <asrivats@redhat.com> - 1.4.313.0-1
- Update to 1.4.313.0 SDK

* Mon Jan 20 2025 José Expósito <jexposit@redhat.com> - 1.4.304.0-1
- Update to 1.4.304.0 SDK

* Tue May 28 2024 José Expósito <jexposit@redhat.com> - 1.3.283.0-1
- Update to 1.3.283.0 SDK

* Wed Jan 17 2024 José Expósito <jexposit@redhat.com> - 1.3.268.0-1
- Update to 1.3.268.0 SDK

* Fri Jul 07 2023 Dave Airlie <airlied@redhat.com> - 1.3.250.1-1
- Update to 1.3.250.1

* Wed Feb 15 2023 Dave Airlie <airlied@redhat.com> - 1.3.239.0-1
- Update to 1.3.239.0

* Fri Aug 26 2022 Dave Airlie <airlied@redhat.com> - 1.3.224.0-1
- Update to 1.3.224.0

* Wed Jun 22 2022 Dave Airlie <airlied@redhat.com> - 1.3.216.0-1
- Update to 1.3.216.0

* Fri Feb 25 2022 Dave Airlie <airlied@redhat.com> - 1.3.204.0-1
- Update to 1.3.204.0

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.2.182.0-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Jul 30 2021 Dave Airlie <airlied@redhat.com> - 1.2.182.0-1
- Update to 1.2.182.0 sdk

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.2.162.0-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Fri Jan 29 2021 Dave Airlie <airlied@redhat.com> - 1.2.162.0-1
- Update to 1.2.162.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.154.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 04 2020 Dave Airlie <airlied@redhat.com> - 1.2.154.0-1
- Update to 1.2.154.0

* Wed Aug 05 2020 Dave Airlie <airlied@redhat.com> - 1.2.148.0-1
- Update to 1.2.148.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.135.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Dave Airlie <airlied@redhat.com> - 1.2.135.0-1
- Update to 1.2.135.0

* Wed Jan 29 2020 Dave Airlie <airlied@redhat.com> - 1.2.131.1-1
- Update to 1.2.131.1

* Thu Nov 14 2019 Dave Airlie <airlied@redhat.com> - 1.1.126.0-1
- Update to 1.1.126.0

* Wed Jul 31 2019 Dave Airlie <airlied@redhat.com> - 1.1.114.0-1
- Update to 1.1.114.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.108.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Dave Airlie <airlied@redhat.com> - 1.1.108.0-1
- Update to 1.1.108.0

* Thu Mar 07 2019 Dave Airlie <airlied@redhat.com> - 1.1.101.0-1
- Update to 1.1.101.0

* Wed Feb 13 2019 Dave Airlie <airlied@redhat.com> - 1.1.97.0-1
- Update to 1.1.97.0

* Tue Feb 12 2019 Dave Airlie <airlied@redhat.com> - 1.1.92.0-1
- Update to 1.1.92.0
- don't rename anymore, upstream changed cube app name

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.82.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.82.0-1
- Update to 1.1.82.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.77.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.77.0-1
- Initial package
