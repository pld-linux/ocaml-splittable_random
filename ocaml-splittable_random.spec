#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	PRNG that can be split into independent streams
Summary(pl.UTF-8):	PRNG pozwalający na dzielenie na niezależne strumienie
Name:		ocaml-splittable_random
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/splittable_random/tags
Source0:	https://github.com/janestreet/splittable_random/archive/v%{version}/splittable_random-%{version}.tar.gz
# Source0-md5:	5e557d49f4a14230e18d86aef98379a0
URL:		https://github.com/janestreet/splittable_random
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_assert-devel >= 0.14
BuildRequires:	ocaml-ppx_assert-devel < 0.15
BuildRequires:	ocaml-ppx_bench-devel >= 0.14
BuildRequires:	ocaml-ppx_bench-devel < 0.15
BuildRequires:	ocaml-ppx_inline_test-devel >= 0.14
BuildRequires:	ocaml-ppx_inline_test-devel < 0.15
BuildRequires:	ocaml-ppx_sexp_message-devel >= 0.14
BuildRequires:	ocaml-ppx_sexp_message-devel < 0.15
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
A splittable pseudo-random number generator (SPRNG) functions like a
PRNG in that it can be used as a stream of random values; it can also
be "split" to produce a second, independent stream of random values.

This library implements a splittable pseudo-random number generator
that sacrifices cryptographic-quality randomness in favour of
performance.

This package contains files needed to run bytecode executables using
splittable_random library.

%description -l pl.UTF-8
SPRNG (Splittable Pseudo-Random Number Generator) funkcjonuje tak, jak
generator liczb pseudolosowych, który można używać jako strumień
wartości losowych; można go także "rozdzielić" aby utworzyć drugi,
niezależny strumień wartości losowych.

Ta biblioteka implementuje podzielny generator liczb pseudolosowych
poświęcający losowość kryptograficznej jakości na rzecz wydajności.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki splittable_random.

%package devel
Summary:	PRNG that can be split into independent streams - development part
Summary(pl.UTF-8):	PRNG pozwalający na dzielenie na niezależne strumienie - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppx_assert-devel >= 0.14
Requires:	ocaml-ppx_bench-devel >= 0.14
Requires:	ocaml-ppx_inline_test-devel >= 0.14
Requires:	ocaml-ppx_sexp_message-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
splittable_random library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki splittable_random.

%prep
%setup -q -n splittable_random-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/splittable_random/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/splittable_random

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/splittable_random
%{_libdir}/ocaml/splittable_random/META
%{_libdir}/ocaml/splittable_random/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/splittable_random/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/splittable_random/*.cmi
%{_libdir}/ocaml/splittable_random/*.cmt
%{_libdir}/ocaml/splittable_random/*.cmti
%{_libdir}/ocaml/splittable_random/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/splittable_random/splittable_random.a
%{_libdir}/ocaml/splittable_random/*.cmx
%{_libdir}/ocaml/splittable_random/*.cmxa
%endif
%{_libdir}/ocaml/splittable_random/dune-package
%{_libdir}/ocaml/splittable_random/opam
