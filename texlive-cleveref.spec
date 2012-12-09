# revision 25979
# category Package
# catalog-ctan /macros/latex/contrib/cleveref
# catalog-date 2012-04-15 19:24:00 +0200
# catalog-license lppl
# catalog-version 0.18.5
Name:		texlive-cleveref
Version:	0.18.5
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


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.18.5-1
+ Revision: 804526
- Update to latest release.

* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.18.4-1
+ Revision: 779422
- Update to latest release.

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.18.3-1
+ Revision: 770135
- Update to latest upstream package

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.18.2-1
+ Revision: 762777
- Update to latest upstream package

* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.18.1-1
+ Revision: 758835
- texlive-cleveref

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.18-2
+ Revision: 750253
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.18-1
+ Revision: 745168
- texlive-cleveref

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.17.9-1
+ Revision: 718070
- texlive-cleveref
- texlive-cleveref
- texlive-cleveref
- texlive-cleveref
- texlive-cleveref

