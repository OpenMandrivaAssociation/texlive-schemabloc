# revision 15878
# category Package
# catalog-ctan /graphics/pgf/contrib/schemabloc
# catalog-date 2009-01-23 11:09:06 +0100
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-schemabloc
Version:	1.5
Release:	11
Summary:	Draw block diagrams, using Tikz
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/schemabloc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schemabloc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schemabloc.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5-2
+ Revision: 755798
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.5-1
+ Revision: 719489
- texlive-schemabloc
- texlive-schemabloc
- texlive-schemabloc
- texlive-schemabloc

