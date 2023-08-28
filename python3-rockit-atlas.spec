Name:           python3-rockit-atlas
Version:        %{_version}
Release:        1
License:        GPL3
Summary:        Common backend code for FLI Atlas focuser daemon
Url:            https://github.com/rockit-astro/atlasd
BuildArch:      noarch
BuildRequires:  python3-devel

%description

%prep
rsync -av --exclude=build --exclude=.git --exclude=.github .. .

%generate_buildrequires
%pyproject_buildrequires -R

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files rockit

%files -f %{pyproject_files}
