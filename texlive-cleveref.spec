# revision 29503
# category Package
# catalog-ctan /macros/latex/contrib/cleveref
# catalog-date 2013-03-24 16:33:18 +0100
# catalog-license lppl
# catalog-version 0.18.9
Name:		texlive-cleveref
Version:	0.18.9
Release:	3
Summary:	Intelligent cross-referencing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cleveref
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enhances LaTeX's cross-referencing features,
allowing the format of references to be determined
automatically according to the type of reference. The formats
used may be customised in the preamble of a document; babel
support is available (though the choice of languages remains
limited: currently Danish, Dutch, English, French, German,
Italian, Norwegian, Russian, Spanish and Ukranian). The package
also offers a means of referencing a list of references, each
formatted according to its type. In such lists, it can collapse
sequences of numerically-consecutive labels to a reference
range.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cleveref/cleveref.sty
%doc %{_texmfdistdir}/doc/latex/cleveref/README
%doc %{_texmfdistdir}/doc/latex/cleveref/cleveref.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cleveref/cleveref.dtx
%doc %{_texmfdistdir}/source/latex/cleveref/cleveref.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
