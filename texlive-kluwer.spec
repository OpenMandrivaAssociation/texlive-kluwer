Name:		texlive-kluwer
Version:	20111102
Release:	1
Summary:	TeXLive kluwer package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kluwer.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kluwer.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kluwer.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
TeXLive kluwer package.

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
%{_texmfdistdir}/bibtex/bst/kluwer/klunamed.bst
%{_texmfdistdir}/bibtex/bst/kluwer/klunum.bst
%{_texmfdistdir}/tex/latex/kluwer/klu10.clo
%{_texmfdistdir}/tex/latex/kluwer/klu105.clo
%{_texmfdistdir}/tex/latex/kluwer/klu11.clo
%{_texmfdistdir}/tex/latex/kluwer/klu12.clo
%{_texmfdistdir}/tex/latex/kluwer/klu9.clo
%{_texmfdistdir}/tex/latex/kluwer/klucite.sty
%{_texmfdistdir}/tex/latex/kluwer/kluedit.sty
%{_texmfdistdir}/tex/latex/kluwer/klufloa.sty
%{_texmfdistdir}/tex/latex/kluwer/klulist.sty
%{_texmfdistdir}/tex/latex/kluwer/klumac.sty
%{_texmfdistdir}/tex/latex/kluwer/klumath.sty
%{_texmfdistdir}/tex/latex/kluwer/klumono.sty
%{_texmfdistdir}/tex/latex/kluwer/klunote.sty
%{_texmfdistdir}/tex/latex/kluwer/kluopen.sty
%{_texmfdistdir}/tex/latex/kluwer/klups.sty
%{_texmfdistdir}/tex/latex/kluwer/kluref.sty
%{_texmfdistdir}/tex/latex/kluwer/klusec.sty
%{_texmfdistdir}/tex/latex/kluwer/klut10.clo
%{_texmfdistdir}/tex/latex/kluwer/klut11.clo
%{_texmfdistdir}/tex/latex/kluwer/klut12.clo
%{_texmfdistdir}/tex/latex/kluwer/klut9.clo
%{_texmfdistdir}/tex/latex/kluwer/klutab.sty
%{_texmfdistdir}/tex/latex/kluwer/kluwer.cls
%doc %{_texmfdistdir}/doc/latex/kluwer/00readme
%doc %{_texmfdistdir}/doc/latex/kluwer/mouse.eps
%doc %{_texmfdistdir}/doc/latex/kluwer/sampkluw.dvi
%doc %{_texmfdistdir}/doc/latex/kluwer/sampkluw.ent
%doc %{_texmfdistdir}/doc/latex/kluwer/sampkluw.tex
%doc %{_texmfdistdir}/doc/latex/kluwer/sampopen.dvi
%doc %{_texmfdistdir}/doc/latex/kluwer/sampopen.tex
%doc %{_texmfdistdir}/doc/latex/kluwer/usrman.dvi
%doc %{_texmfdistdir}/doc/latex/kluwer/usrman.ent
%doc %{_texmfdistdir}/doc/latex/kluwer/usrman.tex
#- source
%doc %{_texmfdistdir}/source/latex/kluwer/kluwer.dtx
%doc %{_texmfdistdir}/source/latex/kluwer/kluwer.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
