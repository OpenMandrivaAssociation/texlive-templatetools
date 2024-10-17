Name:		texlive-templatetools
Version:	67201
Release:	1
Summary:	Commands useful in LaTeX templates
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/templatetools
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/templatetools.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/templatetools.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/templatetools.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a collection of tools, which are helpful
for the creation of a LaTeX template if conditional paths for
code execution are required. All the commands work both in the
preamble and in the document.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/templatetools
%{_texmfdistdir}/tex/latex/templatetools
%doc %{_texmfdistdir}/doc/latex/templatetools

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
