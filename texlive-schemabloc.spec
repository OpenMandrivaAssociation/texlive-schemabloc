%global tl_name schemabloc
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9
Release:	%{tl_revision}.1
Summary:	Draw block diagrams, using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/schemabloc
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/schemabloc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/schemabloc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a set of macros for constructing block diagrams,
using TikZ. (The blox package is an "English translation" of this
package.)

