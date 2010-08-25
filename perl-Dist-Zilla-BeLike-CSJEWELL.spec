%define upstream_name    Dist-Zilla-BeLike-CSJEWELL
%define upstream_version 0.901

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Upload tarball to my own site
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Dist::Zilla)
BuildRequires: perl(Dist::Zilla::Plugin::Mercurial)
BuildRequires: perl(Dist::Zilla::Plugin::Twitter)
BuildRequires: perl(Email::Address)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Moose)
BuildRequires: perl(Net::FTP)
BuildRequires: perl(Net::Netrc)
BuildRequires: perl(PPIx::Regexp)
BuildRequires: perl(PPIx::Utilities::Statement)
BuildRequires: perl(Parse::CPAN::Meta)
BuildRequires: perl(Perl::Critic)
BuildRequires: perl(Perl::Critic::More)
BuildRequires: perl(Perl::Critic::Utils::Constants)
BuildRequires: perl(Perl::MinimumVersion)
BuildRequires: perl(Perl::Tidy)
BuildRequires: perl(Pod::Coverage)
BuildRequires: perl(Pod::Coverage::Moose)
BuildRequires: perl(Pod::Readme)
BuildRequires: perl(Pod::Simple)
BuildRequires: perl(Pod::Spell::CommonMistakes)
BuildRequires: perl(Software::License)
BuildRequires: perl(Test::CPAN::Meta)
BuildRequires: perl(Test::CheckChanges)
BuildRequires: perl(Test::DistManifest)
BuildRequires: perl(Test::Fixme)
BuildRequires: perl(Test::HasVersion)
BuildRequires: perl(Test::MinimumVersion)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Perl::Critic)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::Pod::Spelling::CommonMistakes)
BuildRequires: perl(Test::Portability::Files)
BuildRequires: perl(Test::Prereq::Build)
BuildRequires: perl(Test::UseAllModules)
BuildRequires: perl(autodie)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*

