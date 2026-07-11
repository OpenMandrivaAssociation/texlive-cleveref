%global tl_name cleveref
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.21.4
Release:	%{tl_revision}.1
Summary:	Intelligent cross-referencing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cleveref
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enhances LaTeX's cross-referencing features, allowing the
format of references to be determined automatically according to the
type of reference. The formats used may be customised in the preamble of
a document; babel support is available (though the choice of languages
remains limited: currently Danish, Dutch, English, French, German,
Italian, Norwegian, Russian, Spanish and Ukrainian). The package also
offers a means of referencing a list of references, each formatted
according to its type. In such lists, it can collapse sequences of
numerically-consecutive labels to a reference range.

