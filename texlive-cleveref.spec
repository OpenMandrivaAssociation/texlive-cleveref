Name:		texlive-cleveref
Version:	61719
Release:	2
Summary:	Intelligent cross-referencing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cleveref
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
