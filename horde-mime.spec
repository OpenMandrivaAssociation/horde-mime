%define prj Horde_MIME

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-mime
Version:       0.0.2
Release:       61
Summary:       Horde Mime Library
License:       LGPL
Group:         Networking/Mail
Url:           https://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      php-pear-Text_Flowed
Requires:      horde-auth
Requires:      horde-util
Requires:      horde-compress
Requires:      horde-framework
Requires:      horde-icalendar
Requires:      horde-identity
Requires:      horde-sessionobjects
Requires:      horde-text-filter
Requires:      php-gettext
Requires:      php-imap
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
The Horde_MIME:: class provides methods for dealing with MIME standards.

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/MIME
%dir %{peardir}/Horde/MIME/Viewer
%dir %{peardir}/Horde/MIME/Viewer/ooo
%{peardir}/Horde/MIME.php
%{peardir}/Horde/MIME/Contents.php
%{peardir}/Horde/MIME/Headers.php
%{peardir}/Horde/MIME/MDN.php
%{peardir}/Horde/MIME/Magic.php
%{peardir}/Horde/MIME/Message.php
%{peardir}/Horde/MIME/Part.php
%{peardir}/Horde/MIME/Structure.php
%{peardir}/Horde/MIME/Viewer.php
%{peardir}/Horde/MIME/Viewer/css.php
%{peardir}/Horde/MIME/Viewer/deb.php
%{peardir}/Horde/MIME/Viewer/default.php
%{peardir}/Horde/MIME/Viewer/enriched.php
%{peardir}/Horde/MIME/Viewer/enscript.php
%{peardir}/Horde/MIME/Viewer/html.php
%{peardir}/Horde/MIME/Viewer/images.php
%{peardir}/Horde/MIME/Viewer/msexcel.php
%{peardir}/Horde/MIME/Viewer/mspowerpoint.php
%{peardir}/Horde/MIME/Viewer/msword.php
%{peardir}/Horde/MIME/Viewer/ooo.php
%{peardir}/Horde/MIME/Viewer/ooo/common.xsl
%{peardir}/Horde/MIME/Viewer/ooo/global_document.xsl
%{peardir}/Horde/MIME/Viewer/ooo/main_html.xsl
%{peardir}/Horde/MIME/Viewer/ooo/palm.xsl
%{peardir}/Horde/MIME/Viewer/ooo/style_header.xsl
%{peardir}/Horde/MIME/Viewer/ooo/style_inlined.xsl
%{peardir}/Horde/MIME/Viewer/ooo/style_mapping.xsl
%{peardir}/Horde/MIME/Viewer/ooo/table.xsl
%{peardir}/Horde/MIME/Viewer/ooo/table_cells.xsl
%{peardir}/Horde/MIME/Viewer/ooo/table_columns.xsl
%{peardir}/Horde/MIME/Viewer/ooo/table_rows.xsl
%{peardir}/Horde/MIME/Viewer/pdf.php
%{peardir}/Horde/MIME/Viewer/php.php
%{peardir}/Horde/MIME/Viewer/plain.php
%{peardir}/Horde/MIME/Viewer/rar.php
%{peardir}/Horde/MIME/Viewer/report.php
%{peardir}/Horde/MIME/Viewer/rfc822.php
%{peardir}/Horde/MIME/Viewer/richtext.php
%{peardir}/Horde/MIME/Viewer/rpm.php
%{peardir}/Horde/MIME/Viewer/security.php
%{peardir}/Horde/MIME/Viewer/simple.php
%{peardir}/Horde/MIME/Viewer/source.php
%{peardir}/Horde/MIME/Viewer/srchighlite.php
%{peardir}/Horde/MIME/Viewer/tgz.php
%{peardir}/Horde/MIME/Viewer/tnef.php
%{peardir}/Horde/MIME/Viewer/vcard.php
%{peardir}/Horde/MIME/Viewer/webcpp.php
%{peardir}/Horde/MIME/Viewer/zip.php
%{peardir}/Horde/MIME/mime.magic.php
%{peardir}/Horde/MIME/mime.mapping.php


%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-60mdv2011.0
+ Revision: 564076
- Increased release for rebuild

* Wed Mar 17 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-59mdv2010.1
+ Revision: 523066
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased release version

* Wed Mar 10 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-58mdv2010.1
+ Revision: 517274
- corrected version to 57 since 56 has already been used
- corrected release from 56 to 6
- correct spelling Requires: php-pear-Text_Flowed

* Mon Mar 08 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-5mdv2010.1
+ Revision: 515628
- added Requires: php-pear-Text_Flow
  bumped up release
- added Requires: php-pear-Text_Flow

* Mon Feb 22 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-4mdv2010.1
+ Revision: 509402
- replaced PreReq with Requires(pre)
- removed Buildrequires; horde-framework
- removed requires temorarily to biuld
- import horde-mime


