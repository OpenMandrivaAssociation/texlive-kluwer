Name:		texlive-kluwer
Version:	20180303
Release:	2
Summary:	TeXLive kluwer package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kluwer.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kluwer.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kluwer.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive kluwer package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/kluwer
%{_texmfdistdir}/tex/latex/kluwer
%doc %{_texmfdistdir}/doc/latex/kluwer
#- source
%doc %{_texmfdistdir}/source/latex/kluwer

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
