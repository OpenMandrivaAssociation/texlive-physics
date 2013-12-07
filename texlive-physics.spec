# revision 28590
# category Package
# catalog-ctan /macros/latex/contrib/physics
# catalog-date 2012-12-20 17:31:55 +0100
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-physics
Version:	1.30
Release:	5
Summary:	Macros supporting the Mathematics of Physics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/physics
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/physics.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/physics.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines simple and flexible macros for typesetting
equations in the languages of vector calculus and linear
algebra, using Dirac notation.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/physics/physics.sty
%doc %{_texmfdistdir}/doc/latex/physics/README
%doc %{_texmfdistdir}/doc/latex/physics/physics.pdf
%doc %{_texmfdistdir}/doc/latex/physics/physics.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
