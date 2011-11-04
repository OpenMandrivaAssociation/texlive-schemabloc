# revision 15878
# category Package
# catalog-ctan /graphics/pgf/contrib/schemabloc
# catalog-date 2009-01-23 11:09:06 +0100
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-schemabloc
Version:	1.5
Release:	1
Summary:	Draw block diagrams, using Tikz
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/schemabloc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schemabloc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schemabloc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides a set of macros for constructing block
diagrams, using TikZ.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/schemabloc/schemabloc.sty
%doc %{_texmfdistdir}/doc/latex/schemabloc/README
%doc %{_texmfdistdir}/doc/latex/schemabloc/schemabloc.pdf
%doc %{_texmfdistdir}/doc/latex/schemabloc/schemabloc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
