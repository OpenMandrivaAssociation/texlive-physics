%global tl_name physics
%global tl_revision 74247

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Macros supporting the Mathematics of Physics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/physics
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/physics.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/physics.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines simple and flexible macros for typesetting equations
in the languages of vector calculus and linear algebra, using Dirac
notation.

