Name:		texlive-schemabloc
Version:	58212
Release:	2
Summary:	Draw block diagrams, using Tikz
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/schemabloc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schemabloc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schemabloc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a set of macros for constructing block
diagrams, using TikZ.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/schemabloc/schemabloc.sty
%doc %{_texmfdistdir}/doc/latex/schemabloc/README
%doc %{_texmfdistdir}/doc/latex/schemabloc/schemabloc.pdf
%doc %{_texmfdistdir}/doc/latex/schemabloc/schemabloc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
