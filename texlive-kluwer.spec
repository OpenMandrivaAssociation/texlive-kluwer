%global tl_name kluwer
%global tl_revision 54074

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Kluwer publication support
Group:		Publishing
URL:		https://www.ctan.org/pkg/kluwer
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kluwer.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kluwer.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kluwer.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Most likely long obsolete, unfortunately.

