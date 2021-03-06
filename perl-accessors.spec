#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
Summary:	accessors - create accessor methods in caller's package
Summary(pl.UTF-8):	accessors - tworzenie metod dostępu w pakiecie wywołującego
Name:		perl-accessors
Version:	1.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/SPURKIS/accessors-%{version}.tar.gz
# Source0-md5:	fc764c9cbfd03762c0d4f8ffaabaecb0
URL:		http://search.cpan.org/dist/accessors/
BuildRequires:	perl-Module-Build >= 0.20
%{?with_tests:BuildRequires:	perl-Test-Simple >= 0.01}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The accessors pragma lets you create simple accessors at compile-time.

This saves you from writing them by hand, which tends to result in
cut-n-paste errors and a mess of duplicated code. It can also help you
reduce the ammount of unwanted direct-variable access that may creep
into your codebase when you're feeling lazy. accessors was designed
with laziness in mind.

%description -l pl.UTF-8
Ten moduł pozwala na tworzenie prostych metod dostępowych w czasie
kompilacji. Oszczędza przed pisaniem ich ręcznie, co powodowałoby
błędy przy kopiowaniu i wklejaniu oraz bałagan w postaci powielonego
kodu. Może także zmniejszyć ilość niechcianych bezpośrednich dostępów
do zmiennych mogących się wkraść do kodu, kiedy programista jest
leniwy. accessors jest stworzony z myślą o lenistwie.

%prep
%setup -q -n accessors-%{version}

%build
perl Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/accessors.pm
%{perl_vendorlib}/accessors
%{_mandir}/man3/accessors*.3pm*
