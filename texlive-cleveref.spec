# revision 21918
# category Package
# catalog-ctan /macros/latex/contrib/cleveref
# catalog-date 2011-04-02 11:34:17 +0200
# catalog-license lppl
# catalog-version 0.17.9
Name:		texlive-cleveref
Version:	0.17.9
Release:	1
Summary:	Intelligent cross-referencing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cleveref
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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
%{_texmfdistdir}/tex/latex/cleveref/cleveref.sty
%doc %{_texmfdistdir}/doc/latex/cleveref/README
%doc %{_texmfdistdir}/doc/latex/cleveref/cleveref.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cleveref/cleveref.dtx
%doc %{_texmfdistdir}/source/latex/cleveref/cleveref.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
