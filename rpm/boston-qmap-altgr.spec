Name:       boston-qmap-altgr

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}

Summary:    boston.qmap fix
Version:    0.0.1
Release:    1
Group:      Qt/Qt
License:    LICENSE
URL:        https://github.com/kimmoli/
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch

%description
Just testing stuff

%prep
%setup -q -n %{name}-%{version}

%build

%qtc_qmake5 SPECVERSION=%{version}

%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}

%qmake5_install


%files
%defattr(644,root,root,755)
%config /usr/share/qt5/keymaps/boston.qmap
